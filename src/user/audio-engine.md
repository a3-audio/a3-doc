(audio-engine)=

# The audio engine

The engine is the part of the `a3-core` program that does A³ Core's audio:
channel strips, the 3D encoding, the effects, main, booth, phones and rec. It
is `a3-core --role engine`, a process of its own, run by `a3-engine.service`.
It replaces REAPER as the thing that makes sound; the IEM code it uses
(encoder, decoders, DualDelay) is compiled into it from source. Core still
routes the OSC: the engine receives Core's words on `engine.osc` and says
`/engine/hello` to Core on `core.osc` ({doc}`ports <../ressources/ports>`).
Source: [a3-engine](https://github.com/a3-audio/a3-engine).

## The engine always runs

There is **no switch and no fallback**. `a3-engine.service` has no
`Conflicts=` and no start condition: when `a3-main` starts, the engine starts.
If it cannot open its sound device it restarts five times in a minute and then
stops, visibly (`systemctl --user status a3-engine`), rather than looping.

**REAPER is frozen and never started.** Its files stay on the machine, but
`a3-reaper.service` and the old two-deck `stemdeck.service` are kept off by
drop-ins from the a3-core package, which ask a small helper,
`a3-engine-runs --reaper`; it always answers "no". You never run the helper
yourself.

```{note}
After installing a new engine, restart it: `systemctl --user restart a3-engine`.
```

## The window

The window is the `a3-core` program run without a role (on the rig, on the
screen's ENGINE workspace). It reaches the engine over its local control port
(`engine.control`), so closing it never stops the sound. One page per job, a
**Save** bar below:

| Page | What it is for |
| :--- | :--- |
| **AUDIO** | the sound device. On JACK the rate and quantum are read-only: the server owns them |
| **STATUS** | what runs now: mode, Core's last word, the gate, load, xruns, missing peers, the meters. Says **NO ENGINE RUNNING** when nothing could be opened |
| **CHANNELS** | how many channels (1–128), with the load beside it |
| **ZONES** | which speaker layout (spatial data) is used. There is no layout editor |
| **I/O** | where each engine port connects, see below |
| **CALIBRATION** | the trim of each output zone |
| **FILTER** | the DJ filter type, SVF or Ladder |

Changes are **pending** until you press **Save** ("not saved" shows while the
edit differs from what runs). Save checks the file the way a start would and
refuses a bad one, leaving the old file in place. Then it writes
`~/.config/a3/engine/engine.json` and **restarts the engine session**: a new
engine, which says hello to Core, which replays what it knows. That holds for
every change, and the old setting is opened again if the new one does not open.

The FILTER page is the one exception: it acts at once and needs no Save.

### I/O replaces the patchbay

The **I/O map** decides what is connected to what; the engine
makes those JACK links itself and removes only links it made. The QjackCtl
patchbay ({doc}`Patchbay <../ressources/patchbay>`) is built so that it cannot
fight the engine (no socket is exclusive, none names the engine). Its
`beat-analyzer:vu_*` sockets are dead: the analyzer has no meter ports any
more, the engine measures the meters itself. The page shows, per engine port, its JACK peers (editable)
and the live peers the map does not name ("foreign": shown, never edited).

## Calibration and the gate

- **Trim** per zone, -90 to +6 dB. A slider only *proposes*: a dialog names
  the old and the new value before anything changes. A zone without a trim
  stays closed.
- **The gate.** Main, booth and phones are **closed** (exact silence) from the
  start of the engine until Core has replayed the evening and sends
  `/engine/open 1`. Then each output ramps up to its trim over **1 s**.
  Closing takes 10 ms. **Rec is never gated**, so the beat analyzer always
  has its input.
- **Silence is silence.** Every gain control at its minimum (3D, VOLUME,
  TRIM/GAIN, MASTER, BOOTH, RETURN, PHONES, the sends) is exactly zero, not a
  very quiet signal.

Switches are smoothed over 10 ms (source, filter on/off and kind, send
weights), so nothing clicks.

## Decks

In engine mode {ref}`StemDeck <stemdeck-at-a-glance>`'s decks arrive as
**16-channel B-format**, straight into Core: StemDeck does the encoding and
the engine does not encode the deck again. Deck k listens on
`stemdeck.osc` + (k − 1), so deck B uses 7781. The decks are separate
StemDeck instances, started by the installer, not by `a3-engine`.

- **A channel takes analog or a deck**, never both. Analog ↔ deck crossfades
  over 10 ms; deck ↔ deck dips out and in.
- **Decks are numbered 1…D on the wire and lettered A, B on screen**; slot k is
  StemDeck's instance with letter k.
- On the A³ Mixer the source ring shows **AN | A | B** in engine mode.
- On a deck channel, **A³ Motion shows "deck A" or "deck B"** and sends no
  positions, 3D, FREQ or Q for it. The desk's 3D of the channel that holds deck k
  is relayed by Core to that StemDeck (`/stemdeck/{deck}/3d`); the engine applies
  no 3D to a deck channel. Echoes keep the stems' positions: the deck's
  AUX send takes all 16 channels.
- **Stem cue.** Each deck's cue pair goes into the phones, weighted by the
  CUE↔MIX knob alone, whether or not the deck is on a channel, so you can
  pre-listen before you bring a deck in.
- The return can be the analog return pair or a deck's AUX pair.
- **The decks are StemDeck's B-format instances** (`stemdeck@A`, and one per
  further deck); the old two-deck StemDeck unit is kept off.

## Starting it by hand

On the rig the units start everything. By hand, the same program plays every
role:

```sh
a3-core                       # the window (starts what is missing on a laptop)
a3-core --headless            # Core and the engine as children, no window
a3-core --role core           # just Core
a3-core --role engine [--config FILE] [--spatial DIR] [--truth FILE]
                      [--no-connect] [--timing] [--check-config]
```

| Flag (engine role) | What it does |
| :--- | :--- |
| `--check-config` | prints `ok` or `<file>: <reason>`, exit 0 or 1, opens nothing |
| `--config FILE` | else `~/.config/a3/engine/engine.json`, else the installed default. Save writes to the file the app started with |
| `--spatial DIR` | the speaker layouts |
| `--truth FILE` | the OSC truth (default `/usr/share/a3/a3-osc.json`) |
| `--no-connect` | the engine makes no JACK link; see below |
| `--timing` | prints the backend's load and xruns at exit |

Each role takes only its own flags; a flag of another role, an unknown one or a
missing value prints the usage and exits with 2. `a3-core --truth host NAME`
and `a3-core --truth port PROGRAM ROLE` print one fact from the OSC truth for a
script; `a3-core --render-truth user|network-file|network` is what the installer
uses to write the files programs read the truth from.

**`--no-connect`** is for a hand test only, on a machine whose JACK graph you
share with something else. Never start a second engine next to the rig's.
