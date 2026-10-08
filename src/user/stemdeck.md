# StemDeck

(stemdeck-at-a-glance)=

## At a glance

![StemDeck on the Core's screen: both decks loaded, deck A playing](pics_user/stemdeck-main.png)

A stem player for DJs: **two decks, each playing a track split into four
stems**, and a mixer that sends every stem to its own output. Where a CDJ gives
A³ Core a stereo mix, StemDeck gives it the parts.

- Four stem buses go to A³ Core's channels 1–4, the aux bus to its Return.
  Pre-listening is the desk's cue; StemDeck has no headphone bus.
- The A³ Mixer [remote-controls it](#stemdeck-remote) through the Core.
- On the Core it always runs, on workspace **STEMDECK** (2);
  see [Always running on the Core](#stemdeck-on-the-core).
- With no CDJs it can be [the tempo master](#stemdeck-master).
- It [splits stereo tracks into stems](#stemdeck-stem-creator) itself.
- Linux, JUCE, JACK. Source: [stemdeck](https://github.com/rafjagger/stemdeck)
  (outside the `a3-audio` organisation, carried by a3-system).

```{tip}
**Best with A³ Motion**: each stem travels the room on its own path, in time
with StemDeck's beat. See [StemDeck × A³ Motion](stemdeck-with-motion.md).
```

(stemdeck-stem-sets)=

## Stem sets

A **set** is exactly four audio files in one folder, the same name with a
different ending after the last space, `-` or `_`:

```text
Artist - Title-001.wav  …  Artist - Title-004.wav
Artist - Title - DUB.wav, … - KICK.wav, … - PADS.wav, … - PERC.wav
```

Endings sort naturally (`01` before `10`, words alphabetically) into stems 1–4.
Three or five files are not a set. Formats: WAV, AIFF, FLAC, Ogg Vorbis; WAV
and AIFF stream from disk, so jumps and loops are instant.

### Artist, album, set

```text
stems/
├── Burial/
│   └── Untrue/
│       └── Archangel - 01.wav … Archangel - 04.wav
└── Aphex Twin/
    └── Drukqs/
        └── CD1/
            └── Avril 14th - 1.wav … Avril 14th - 4.wav
```

First folder: **artist**; second: **album**; deeper folders join the album
(`Drukqs / CD1`). The library scans its folder recursively; it starts in
`stems/` next to where StemDeck started and remembers the last folder.

(stemdeck-screen)=

## The screen

Top: both decks' scrolling waveforms (drag to move, wheel to zoom). Middle:
deck A, mixer, deck B. Bottom: the library. The top bar holds **REC** (24-bit
FLAC of the `rec_L/R` inputs into `recordings/`), **AUTO DJ**, the **SYNC**
source, **Audio** (grey under JACK), **Settings**, the workspace switch, and,
where there is room, the audio status.

![StemDeck's top bar](pics_user/stemdeck-topbar.png)

(stemdeck-workspaces)=

### Over to A³ Motion, and back

**MOTION** shows A³ Motion, whose **STEMDECK** key sits in the same place.
**▾** lists the workspaces. See {ref}`A³ Core's screen <core-workspaces>`.

(stemdeck-settings)=

### Settings

![Settings: the stem library folder](pics_user/stemdeck-settings.png)

The **stem library** folder, picked with **Choose…** (the touch screen has no
keyboard).

(stemdeck-decks)=

### Decks

![Deck A playing: title, time, overview, BPM with the original tempo, CUE and PLAY, and at the foot the tempo fader with the loop, sync and grid keys](pics_user/stemdeck-deck.png)

Like a CDJ without the platter; the [SCS.3d](#stemdeck-scs3d) is the jog.

| Control | What it does |
| :--- | :--- |
| **CUE** | playing: back to the cue point and stop. Stopped: set the cue point, or on it, play while held |
| **PLAY** | start / pause |
| overview | one lane per stem. Click: jump; drag: loop |
| **LOOP OFF** | clears the loop |
| **REPEAT** | restarts at the end |
| **VINYL** | the controller's platter scratches |
| tempo fader | range button: ±8 / ±16 / ±50 % |
| **BPM** | current tempo; **Original** below |
| **SYNC** | follow a leader; see [Sync](#stemdeck-sync) |
| **MASTER** | Pro DJ Link tempo master; see [MASTER](#stemdeck-master) |
| **GRID** | fix the beat grid; see [GRID](#stemdeck-grid) |

The tempo is analysed once per set in the background, over all four stems,
assuming a constant tempo.

(stemdeck-mixer)=

### Mixer

![The mixer: per stem a knob, M and the bus switches; channel faders and the output meters](pics_user/stemdeck-mixer.png)

| Per stem | What it does |
| :--- | :--- |
| gain knob | −60 to +6 dB; double-click: 0 dB |
| **M** | mute |
| **1 2 3 / 4 A** | buses 1–4 and AUX. A stem plays on every lit bus; none: silent |

Below: the channel fader (every bus is post-fader). Between the strips: meters
for buses 1–4 and AUX, each with a clip lamp that holds for a second. The desk
sets the switches through Core and StemDeck reports back, so both agree.

(stemdeck-start-buses)=

**Where the stems start:** on **AUX only**. A stem on bus 1–4 silences that
desk channel's analog input, so a fresh StemDeck takes no channel. Loading a
set keeps the switches; a session restores its own.

**Every bus is trimmed 6 dB**, before its meter: two full tracks on AUX would
otherwise clip, and the channels match it.

(stemdeck-library)=

### Library

![The library: search box, Load to A and Load to B, the library folder with its set count, Create stems… and Rescan, and the sets by artist and album](pics_user/stemdeck-library.png)

Columns **Artist | Album | Set | BPM | Stems | Length**; click a header to
sort. Search matches name, artist or album. Load with **Load to A/B**, a
double-click or Return (first deck not playing), or drag onto a deck.
**Rescan** reads the folder again.

(stemdeck-grid)=

### GRID: correcting the beat grid

Grid Adjust, as on a CDJ-3000:

| Control | What it does |
| :--- | :--- |
| jog | moves the grid; a turn is 100 ms |
| **‹1/2** / **1/2›** | half a beat |
| **SNAP** | downbeat to the cue point |
| **SET 1** | downbeat to the playhead |
| **SHIFT** | takes a beat aligned by ear with the jog ring |
| **RESET** | the analysed grid again |

Corrections are kept in `analysis.xml`.

(stemdeck-autodj)=

### AUTO DJ

Plays the sets the search shows, at random, each once:

- Nothing playing: loads a set on deck A and plays it.
- 30 s before the mix: loads the next set on the other deck, fader down.
- The mix starts on a downbeat 16 bars before the end, SYNC on, equal-power
  crossfade over those 16 bars; then the old deck stops and SYNC goes off.
- No beat grid: a 10 s unsynced crossfade.
- Never mixes out of a loop or loads onto a looping deck.

(stemdeck-keys)=

### Keys

| | Deck A | Deck B |
| :--- | :---: | :---: |
| Play / pause | `D` | `L` |
| Cue (hold to preview) | `S` | `K` |
| Mute stem 1–4 | `1` `2` `3` `4` | `7` `8` `9` `0` |

(stemdeck-scs3d)=

### The Stanton SCS.3d

Up to two, one per deck, taken as plugged in (first = deck A;
`<VALUE name="scs3dSwap" val="1"/>` in `~/.config/StemDeck/StemDeck.settings`
swaps them). Mapping follows Mixxx's.

| SCS.3d | StemDeck |
| :--- | :--- |
| **FX EQ LOOP TRIG** | mute stem 1–4 |
| **VINYL** | loop in; again: loop out |
| **DECK** | loop off, and on again from its start |
| circle top left / right | previous / next set |
| circle centre tap | load the selected set (not onto a playing deck) |
| **GAIN** / **PITCH** | channel fader / tempo (relative) |
| ring | scratch: touch holds, turning scratches |
| **PLAY CUE SYNC TAP** | play, cue, SYNC, MASTER |

(stemdeck-stem-creator)=

## Making stems from a stereo track

<!-- IMAGE: the "Create stems" question with its Target folder field, and the strip under the library bar showing a running job, e.g. "Stems: Title  42 %  +2 waiting". Not taken: both need files dropped on the rig's running StemDeck. -->

### Starting

1. Drop stereo files or a folder onto the library, or press **Create stems…**
   (FLAC, WAV, MP3, AIFF, OGG, M4A, Opus).
2. Set the **Target folder**, relative to the library (typed, **Browse…**, or
   empty). It is preset from the source path (`Artist/Album`). The whole batch
   goes there.
3. **Create**.

### What you get

```text
stems/Artist/Album/
├── Title - 1 - drums.flac
├── Title - 2 - bass.flac
├── Title - 3 - other.flac
├── Title - 4 - vocals.flac
└── originals/Title.flac
```

- Stems 1–4: drums, bass, other, vocals. `originals/` holds a copy and is not
  scanned.
- Format: FLAC, WAV, AIFF at 24 bit; Ogg at quality 8; MP3, M4A and Opus
  become FLAC.
- A name already in the album becomes `Title (2)`. When done, the library
  rescans and selects the set.

### While it works

[Demucs](https://github.com/adefossez/demucs) (`htdemucs`, 44.1 kHz) runs in
the background, one track at a time, **while the decks play**: the audio
thread owns CPU 1, the separator gets the other cores at idle CPU and disk
priority, at most 6 GB. Fewer cores: `<VALUE name="separatorCores" val="1"/>`
in `StemDeck.settings` (CPU 0 only: about 1.2 × the track's length).

The strip under the library bar shows progress and the queue (`+2 waiting`), or
`Stems: failed: …`. **Cancel** stops the track and leaves nothing behind.

(stemdeck-stem-creator-setup)=

### Setting it up, once

About 1 GB per machine, from the StemDeck checkout:

```sh
sudo apt install ffmpeg python3-venv
tools/setup-separator.sh
```

It installs Demucs and CPU PyTorch into `~/.local/share/StemDeck/separator`
and fetches the model. Without it the strip says `separator not installed`.

(stemdeck-remote)=

### Remote control from the desk

With A³ Core running, the A³ Mixer chooses what is on its channels: turn a
channel's encoder to a stem and push; a push on the channel's **A** (its
analog input) takes it off. How the desk does it, and the rules for
it, are on the {ref}`desk's input selectors <a3mix-displays>`. From
StemDeck's side:

- **StemDeck keeps the truth.** Core only relays the desk's request to switch a
  bus and asks StemDeck for all switches when it hears StemDeck for the first
  time. A click on a bus switch here also shows on the desk.
- **One stem per channel.** A channel plays at most one stem, and a stem
  plays on one channel at most. If a session shows several stems on one bus,
  Core keeps the lowest and switches the others off, about 0.3 s after your
  reports settle.
- **AUX follows the return's mode.** In stem mode every stem no channel plays
  has its **A** lit, and Core switches a free stem's A back on if you click it
  off. In analog mode no stem is on AUX, and the return plays the analog
  inputs 11/12 instead of the AUX bus. A stem pushed onto a channel loses
  its A.
- **The C switches are yours.** A stem's **C** puts it on StemDeck's CUE bus,
  for pre-listening here, e.g. a stem no channel plays yet. Core does not set
  them: a desk channel's cue goes through the channel itself (see
  {ref}`the cue <a3mix-cue>`).
- **StemDeck says hello to Core every 30 seconds**, and Core learns its
  address from that. StemDeck listens on `stemdeck.osc` (see
  {doc}`../ressources/ports`).
- **It starts on AUX only**, on no desk channel — see
  [Where the stems start](#stemdeck-start-buses).
- **Stem meters.** StemDeck sends one meter per stem to the desk only
  (deck A stems 1–4 are `/vu/41`–`/vu/44`, deck B `/vu/45`–`/vu/48`), 25 times
  a second. Each is measured after the stem's knob and mute, before the fader
  and the buses.
- **AUX bus meter.** StemDeck also meters its AUX bus as a stereo pair,
  `/vu/49` (L) and `/vu/50` (R), at the same rate: peak and rms of each side
  after the bus and its 6 dB trim, i.e. what goes to the aux return. The desk shows it as STEM
  beside the analog return, ANALOG.

(stemdeck-audio)=

## Audio out

A JACK client, `StemDeck`: ten outputs (`deck1_L` … `aux_R`) and the `rec_L/R`
inputs. Ports and where they land in Core: {doc}`Patchbay <../ressources/patchbay>`.
`deck1` … `deck4` are the **buses**, not the decks; bus N is A³ channel N, aux
is Core's Return.

- **Nothing connects by itself.** On the Core the package's patchbay does;
  elsewhere see [StemDeck on another machine](#stemdeck-with-motion-remote-machine).
- It **never starts a JACK server**: it uses JACK, PipeWire's JACK, or ALSA
  (**Audio**). With fewer than ten outputs, buses are summed down.
- It takes the graph's rate and buffer and resamples itself; changing a
  running graph would throw out zita. Set the rate before starting, e.g.
  `pw-metadata -n settings 0 clock.force-rate 44100`.

<!-- NOTE: audio I/O (ports, REAPER inputs, zita channels) is documented once, on the Patchbay page (src/ressources/patchbay.md). The REAPER template routes the zita-n2j track: pairs 1-2 .. 7-8 -> 1-input .. 4-input, 9-10 -> Return, 11-12 unused. -->

(stemdeck-sync)=

## Sync

<!-- IMAGE: the top bar under SYNC: PIO, with the PIO status readout (e.g. "PIO 128.0 · CDJ 2") and the player box. Not taken: switching SYNC on the rig's running StemDeck turns off every SYNC that was on. The top bar as it is, under SYNC: DECK, is under "The screen" above. -->

**SYNC** on a deck follows a leader, chosen in the top bar: **DECK** (the other
deck) or **PIO** (the Pro DJ Link tempo master). Switching it turns all SYNC
off.

- **Tempo:** the leader's × ½, 1 or 2, whichever is the smallest change, chosen
  when SYNC goes on; the fader range widens if needed.
- **Phase:** only while both play and nobody scratches. Over 50 ms off: jump;
  closer: nudge, at most 2 %.

### DECK: one deck follows the other

SYNC on A follows B; SYNC on B hands over. At ×1 it also lines up **bars**.

(stemdeck-pio)=

### PIO: following the Pro DJ Link tempo master

Follows the master's tempo (pitch included) and beat; both decks may follow.

- StemDeck is **player 6**; it reads the Pro DJ Link ports (`prolink.*`) from
  `a3-osc.json` ({ref}`Where addresses live <osc-truth>`). On the Core it
  follows Core's file and restarts its window once (about 5 s) when it changes
  ({ref}`Following Core <osc-follow>`). No file: `PIO: no a3-osc.json`.
- It shares the ports with the beat-analyzer (player 7) on one machine;
  retries every 2 s while the network is down.
- No status packets for 2 s: **no master**; it follows the player picked in the
  box (default: the first heard).
- Master silent: tempo **held**, phase left alone.
- It aligns the **beat, not the bar**; set the downbeat with the jog.
- Player number: `pioDevice` in `~/.config/StemDeck/StemDeck.settings`.

Ask the venue before joining their Pro DJ Link network.

(stemdeck-master)=

## MASTER: StemDeck as the tempo master

With no CDJs, **MASTER** on a deck makes StemDeck the Pro DJ Link tempo master;
the beat-analyzer (mode 2) and A³ Motion on **PIO** follow. Whole chain:
{ref}`Playing without CDJs <beat-analyzer-without-cdjs>`.

- Press MASTER to take it, on the other deck to hand over, again to drop it.
  MASTER off and SYNC not on PIO: StemDeck leaves the network.
- No master chosen: the only playing deck becomes master — not under SYNC: PIO
  (two masters would fight), and not after you turned it off.
- Sends, as player 6, a **beat packet per beat** (BPM × fader, beat counted from
  the grid's first beat) and a **status packet every 200 ms**.
- A master that stops while the other deck plays hands over (like a CDJ-3000).
- Nothing goes out until the deck's tempo is analysed.
- **Broadcast** on the first non-loopback interface that can, so a listener on
  the same machine hears it.
- Beats are timed to about 1 ms on their own thread: none lost, none doubled,
  no burst after a jump.
- Top bar: `PIO master: A` (or B).

Packets follow [prolink-connect](https://github.com/EvanPurkhiser/prolink-connect)'s
reading. Independent implementation; not affiliated with AlphaTheta or
Pioneer — see {doc}`../ressources/trademarks`.

(stemdeck-build)=

## Build and start

Needs CMake ≥ 3.22, a C++17 compiler, pkg-config, **JUCE** ({ref}`the A³
version <build-juce>`, found under `~/local/juce` unless `CMAKE_PREFIX_PATH`
says otherwise), and:

```sh
apt install libjack-jackd2-dev libflac-dev libvorbis-dev libogg-dev
```

GoogleTest (`libgtest-dev`) only for {ref}`the tests <build-commands>`. Then:

```sh
./start.sh
```

It configures a Release build in `build/` once, rebuilds what changed and
starts StemDeck via JACK, `pw-jack` or ALSA. Binary:
`build/StemDeck_artefacts/Release/StemDeck`.

Settings live in `~/.config/StemDeck/`, with `analysis.xml` (tempo analyses and
grids, per file, size and date). Delete it, with StemDeck closed, to analyse
everything again.

(stemdeck-session)=

### Session

`~/.config/StemDeck/session.xml` is written every 2 s while anything changes and
on quit. Next start restores decks, mixer and bus switches, library and stem
jobs; a playing deck plays on.

(stemdeck-on-the-core)=

### Always running on the Core

A user service on i3 workspace `2:STEMDECK`. The package's i3 config tiles the
main window borderless (i3 full screen would make every dialog full screen);
all other windows float. The {doc}`installer <../configuration/install>` (role
StemDeck) sets it up; by hand:

```sh
cp .config/systemd/user/stemdeck.service ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now stemdeck
```

It runs the build in `build-make/`; `systemctl --user restart stemdeck` picks up
a rebuild. `tools/rig-keep-the-screen.sh` gives the screen back to the
workspace that showed before the start.

```{warning}
**Do not restart StemDeck mid-set.** Its JACK client leaving and joining
causes xruns: clicks on everything the Core plays.
```

(stemdeck-troubleshooting)=

## Troubleshooting

| Symptom | What to do |
| :--- | :--- |
| A set is missing | Exactly four files, one name, different endings. **Rescan**. Right folder? [Settings](#stemdeck-settings) |
| `separator not installed` | [Set it up once](#stemdeck-stem-creator-setup) |
| Stems are slow to make | Idle priority on the free cores; see `separatorCores` |
| Nothing to hear | Ports are never connected automatically; patch them |
| `JACK-Server wurde beendet` | JACK went away. Restart StemDeck after JACK |
| A stem does not move | Its channel's **3d** up, clip playing; a stem only on **A** is on the Return. See [StemDeck × A³ Motion](#stemdeck-with-motion-troubleshooting) |
| A³ Motion ignores MASTER | Wait for the BPM; deck playing? Motion on **PIO**? |
| Downbeat on the wrong beat | CUE on the real first beat of a bar, **GRID**, **SNAP** |
| `PIO: no a3-osc.json` | No truth found: `$A3_OSC_TRUTH`, `~/.cache/a3/a3-osc.json` (filled by Core's announcement) or `/usr/share/a3/a3-osc.json` (from a3-core) |
| SYNC: PIO says **no master** | Status packets don't arrive; it follows the player in the box |
