(audio-engine)=

# The audio engine

`a3-engine` is the program that does A³ Core's audio: channel strips, the 3D
encoding, the effects, main, booth, phones and rec. It replaces REAPER as the thing that makes sound; the IEM code it uses
(encoder, decoders, DualDelay) is compiled into it from source. Core still
routes the OSC: the engine receives Core's words on `engine.osc` and says
`/engine/hello` to Core on `core.osc` ({doc}`ports <../ressources/ports>`).
Source: [a3-engine](https://github.com/a3-audio/a3-engine).

## Engine or REAPER

There is **no switch to flip**. At boot the system asks one question:

- **Is `a3-engine` installed, and does `a3-engine --check-config` pass?** Then
  the engine runs and REAPER does not start.
- **Otherwise** REAPER starts, set up exactly as before. Core's status says
  why (not installed, or what the config check said).

The question is asked by a small internal helper, `a3-engine-runs`, which both
units call; you never run it yourself. The units are described in
{ref}`A³ Core services <core-engine-units>`.

REAPER is **frozen**: it keeps working as it is, but it gets no new features.
Everything below is about the engine.

```{note}
The engine is decided at start. After installing it, or after fixing a broken
config, run `systemctl --user restart a3-main`.
```

## The window

The engine shows a window (hidden when it runs as a service and you close
it). One page per job, a **Save** bar below:

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

In engine mode the **I/O map** decides what is connected to what; the engine
makes those JACK links itself and removes only links it made. The QjackCtl
patchbay ({doc}`Patchbay <../ressources/patchbay>`) stays for REAPER mode and
is built so that it cannot fight the engine (no socket is exclusive, none
names the engine). The page shows, per engine port, its JACK peers (editable)
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
- **Two decks need engine mode.** REAPER mode keeps the old two-deck StemDeck
  as it was.

## Starting it by hand

```sh
a3-engine [--config FILE] [--spatial DIR] [--truth FILE]
          [--no-connect] [--no-window] [--service] [--timing] [--check-config]
```

| Flag | What it does |
| :--- | :--- |
| `--check-config` | prints `ok` or `<file>: <reason>`, exit 0 or 1, opens nothing; this is what the boot question uses |
| `--config FILE` | else `~/.config/a3/engine/engine.json`, else the installed default. Save writes to the file the app started with |
| `--spatial DIR` | the speaker layouts |
| `--truth FILE` | the OSC truth (default `/usr/share/a3/a3-osc.json`) |
| `--no-window` | no window, for a unit without a screen |
| `--service` | closing the window only hides it |
| `--no-connect` | the engine makes no JACK link; see below |
| `--timing` | prints the backend's load and xruns at exit |

**`--no-connect`** is for a hand test next to REAPER only. The engine refuses
to connect at all while a JACK client named REAPER exists. Never run the
engine and REAPER on the rig at the same time.
