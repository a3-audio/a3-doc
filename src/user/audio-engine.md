(audio-engine)=

# The audio engine

The engine is the part of the `a3-core` program that does A³ Core's audio:
channel strips, the 3D encoding, the effects, main, booth, phones and rec. It
is `a3-core --role engine`, a process of its own, run by `a3-engine.service`.
It is the thing that makes sound (REAPER did before it, and is gone); the IEM
code it uses (encoder, decoders, DualDelay) is compiled into it from source. Core still
routes the OSC: the engine receives Core's words on `engine.osc` and says
`/engine/hello` to Core on `core.osc` ({doc}`ports <../ressources/ports>`).
Source: [a3-core](https://github.com/a3-audio/a3-core), the same repository and
the same package as the Core (its `PROGRAM.md`, {doc}`development page <../development/core>`). The
repository `a3-engine` it grew in is archived; the name lives on as the engine
**role**, its unit `a3-engine.service` and its JACK client `a3-engine`.

## The engine always runs

There is **no switch and no fallback**. `a3-engine.service` has no
`Conflicts=` and no start condition: when `a3-main` starts, the engine starts.
If it cannot open its sound device it restarts five times in a minute and then
stops, visibly (`systemctl --user status a3-engine`), rather than looping.

**REAPER is gone**, and so are its patchbay and QjackCtl: the package ships
none of them. On a machine that ran REAPER the upgrade moves the retired units
and the patchbay aside (named in the install output); REAPER's own files in
`~/.config/REAPER` and `~/.local/opt/REAPER` are never touched, deleting them is
yours. The old two-deck `stemdeck.service` stays off by a drop-in of the
package (`stemdeck.service.d/two-deck-off.conf`); the decks are the
`stemdeck@A` instances.

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
| **STATUS** | what runs now: mode, Core's last word, the gate, load, xruns, missing peers, the meters. Says **NO ENGINE RUNNING** when nothing could be opened. Missing peers are grouped by client ("AES67 deck B (41), system (1)"), not listed one by one |
| **CHANNELS** | how many channels (1–128), with the load beside it |
| **ZONES** | which speaker layout (spatial data) is used. There is no layout editor. Also **PHONES HEADPHONE EQ**: off, or the correction of one headphone model, applied to the phones only (rec has none) |
| **I/O** | where each engine port connects, and for each deck its source, see below |
| **CALIBRATION** | the trim of each output zone |
| **FILTER** | the DJ filter type, SVF or Ladder |

Changes are **pending** until you press **Save** ("not saved" shows while the
edit differs from what runs). Save checks the file the way a start would and
refuses a bad one, leaving the old file in place. Then it writes
`~/.config/a3/engine/engine.json` and **restarts the engine session**: a new
engine, which says hello to Core, which replays what it knows. That holds for
every change, and the old setting is opened again if the new one does not open.

The FILTER page is the one exception: it acts at once and needs no Save.

(audio-engine-io)=

### The I/O map: the engine does the patching

The **I/O map** decides what is connected to what; the engine
makes those JACK links itself and removes only links it made. There is no
patchbay and no QjackCtl on the Core. The beat-analyzer has no meter ports any
more, the engine measures the meters itself. The page shows, per engine port,
its JACK peers (editable) and the live peers the map does not name ("foreign":
shown, never edited).

The shipped map (`/usr/share/a3-engine/engine.json`, `io.jack`). The audio
interface is the JACK client `system` (PipeWire, 44.1 kHz, quantum 128):

| Engine port | Connected to |
| :--- | :--- |
| `analog_1` … `analog_8` | `system:capture_1` … `capture_8`: the A³ Mixer's four channels, stereo |
| `analog_11`, `analog_12` | `system:capture_11`, `capture_12`: the aux return's analog input |
| `main_sub`, `main_top_1` … `main_top_4` | `system:playback_1` … `playback_5` |
| `phones_L`, `phones_R` | `system:playback_9`, `playback_10` |
| `booth_sub`, `booth_top_1` … `booth_top_4` | `system:playback_11` … `playback_15` |
| `rec_L` | `StemDeck-A:rec_L`, the Core's AES67 channel 1 and `beat-analyzer:bpm_1` (the beat-analyzer's tempo input in clock mode EXT, the first channel of the pair only) |
| `rec_R` | `StemDeck-A:rec_R` and the Core's AES67 channel 2 |
| `deckA_1` … `deckA_16`, `deckA_aux_1` … `16`, `deckA_cue_1` … `9` | `StemDeck-A:bformat_1` … `16`, `aux_1` … `16`, `cue_1` … `9` |
| `deckB_…` | the same 41 ports, from the AES67 stream of deck B: `AES67 deck B:receive_MAIN1` … `receive_CUE9` |

The **REC bus is the only recording source**: it feeds the deck recorders
(StemDeck's `rec_L/R`) and AES67 channels 1 and 2, which a deck on another
machine records from. Nothing else is linked to a recorder.

**Deck A is local, deck B comes over the network** by default: a StemDeck on
another machine reaches the Core as one AES67 stream per deck, 41 channels
({ref}`network audio <ports-audio-network>`). On the **I/O** page each deck has
a **source** chooser, *Local StemDeck* or *AES67 stream*; it rewrites that
deck's 41 links in the map, and **Save** applies it. A deck whose links are
only partly one or the other shows neither. The map stays plain text, so hand
edits remain possible. The engine never picks a source by itself.

The Core's map names the Core's own AES67 sender (`AES67 <hostname> out`), so
another host copies the file to `~/.config/a3/engine/engine.json` and edits the
host name.

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

In engine mode {ref}`StemDeck <stemdeck-one-deck>`'s decks arrive as
**41 channels each**: 16 main (B-format, third order), 16 aux (B-format) and 9
cue (B-format, second order). StemDeck does the encoding and the engine does
not encode a deck again. Deck k listens on `stemdeck.osc` + (k − 1), so deck B
uses 7781. The decks are separate StemDeck instances, started by the
installer, not by `a3-engine`.

- **A channel takes analog or a deck**, never both. Analog ↔ deck crossfades
  over 10 ms; deck ↔ deck dips out and in.
- **Decks are numbered 1…D on the wire and lettered A, B on screen**; slot k is
  StemDeck's instance with letter k.
- On the A³ Mixer the source ring shows **AN | A | B** in engine mode.
- On a deck channel, **A³ Motion shows "deck A" or "deck B"** and sends no
  positions, 3D, FREQ or Q for it. The desk's 3D of the channel that holds deck k
  is relayed by Core to that StemDeck (`/stemdeck/{deck}/3d`); the engine applies
  no 3D to a deck channel.
- **Aux is per stem.** Only the stems you send in StemDeck (their AUX knobs)
  are on the deck's aux bus, at their positions. The bus goes through the
  channel's own TRIM, EQ, filter and VOLUME and then the desk's **AUX pot**,
  which scales the whole deck aux, into the delay. The deck's main 16 channels
  never reach the delay. A deck on no channel feeds no delay.
- **Stem cue.** Each deck's 9 cue channels go into the phones before the
  phones decoder, weighted by the CUE↔MIX knob alone, whether or not the deck is
  on a channel, so you can pre-listen before you bring a deck in. The cue
  shares the decoder, the headphone EQ and PHONES with the desk's cue; StemDeck
  has no decoder of its own on the rig. The cue is second order, so it is spatially as sharp as second order.
- **The return is analog or the delay.** Source **ANALOG** is the analog
  pair 11/12, with the delay at unity as before. Source **DELAY** plays the
  delay's output instead, scaled by RETURN, wherever the return goes (main,
  booth, rec, phones), and shuts the analog pair. The change between them
  takes 10 ms. The return's CUE key does not touch the delay. The desk shows
  DELAY where it showed STEM.
- **A deck that is missing** (stream gone, StemDeck not running) is silent and
  listed on STATUS. The engine tells Core within about 2 s; Core then marks the
  deck absent on the desk and Motion, and the channel stays on the deck. When
  the stream returns the engine links it again by itself.
- **The decks are StemDeck's B-format instances** (`stemdeck@A`, and one per
  further deck); the old two-deck StemDeck unit is kept off.
- **An old `engine.json`** may still hold the retired links `deck<X>_cue_L/R`
  and `deck<X>_aux_L/R`. They are dropped on load, one line each on STATUS, and
  never make the file invalid. The new aux and cue links are not guessed: the
  deck shows them missing until its source is chosen on the I/O page.

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
