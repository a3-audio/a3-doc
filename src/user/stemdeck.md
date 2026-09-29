# StemDeck

(stemdeck-at-a-glance)=

## At a glance

StemDeck is a stem player for DJs: **two decks, each playing a track split
into four stems**, and a mixer that sends every stem to its own output. Where a
CDJ gives A³ Core a finished stereo mix, StemDeck gives it the parts — so the
drums can stay put while the pads fly round the room.

It runs on Linux, as a program with its own window, and plays into the JACK
graph. Its four stem buses and its aux bus go to A³ Core; a stem you send to
**aux** can be put onto a movement there and moved through the room by A³
Motion.

It can also be **the tempo master** of the whole system when there are no
CDJs in the booth: its master deck's beat goes out on Pro DJ Link, the
[beat-analyzer](beat-analyzer.md) follows it, and A³ Motion follows the
beat-analyzer.

- [StemDeck repository](https://github.com/rafjagger/stemdeck) — not under the
  `a3-audio` organisation, but carried by the a3-system repository along with
  the rest
- Built with JUCE

<!-- IMAGE: the whole main window with a set loaded on both decks, one of them playing -->

(stemdeck-stem-sets)=

## Stem sets

A **set** is exactly four audio files in one folder that share a name and
differ only in the part after the last space, `-` or `_`:

```text
Artist - Title-001.wav  …  Artist - Title-004.wav
Artist - Title - 01.wav …  Artist - Title - 04.wav
Artist - Title - DUB.wav, … - KICK.wav, … - PADS.wav, … - PERC.wav
```

The endings are sorted naturally — `01` before `10`, words alphabetically —
and stem N goes to bus N. A group of three or five files is not a set and
does not show up.

StemDeck reads WAV, AIFF, FLAC and Ogg Vorbis. WAV and AIFF are read straight
from disk as they are needed, which makes jumping and looping instant: for a
set you will loop, prefer those.

### Artist, album, set

Sort your stems into folders by artist and album — the library reads its
columns from them:

```text
stems/
├── Burial/
│   └── Untrue/
│       ├── Archangel - 01.wav … Archangel - 04.wav
│       └── Etched Headplate - Drums.flac … Etched Headplate - Vox.flac
└── Aphex Twin/
    └── Drukqs/
        └── CD1/
            └── Avril 14th - 1.wav … Avril 14th - 4.wav
```

The first folder under the library folder is the **artist**, the second the
**album**. Deeper folders are added to the album (`Drukqs / CD1`) — handy for
a double album. A set lying straight in the library folder has neither, one
level down only an artist. Inside a folder the rule above holds: four files
with the same beginning are one set, their endings sorted naturally
(`1 2 3 10`, `01 … 04`) or alphabetically.

The library looks through its folder and every folder below it. It starts in
`stems/`, next to where StemDeck was started, and remembers the last folder
you picked.

(stemdeck-screen)=

## The screen

Across the top, the scrolling waveforms of both decks. In the middle, deck A,
the mixer and deck B. At the bottom, the library. The top bar shows the audio
status — JACK client, sample rate, buffer, connected ports, xruns — and the
SYNC source.

Some labels on the screen are still German; this page gives them as the
screen shows them.

(stemdeck-decks)=

### Decks

<!-- IMAGE: one deck close-up: title, overview waveform with a loop set, CUE/PLAY, jog wheel, BPM readout with "Original", SYNC, MASTER, range button, tempo fader -->

Laid out like a CDJ:

| Control | What it does |
| :--- | :--- |
| **CUE** | as on a CDJ. While playing: back to the cue point, and stop. While stopped: sets the cue point here — or, if you are already on it, plays for as long as you hold it |
| **PLAY** | starts and pauses |
| **overview waveform** | the whole track, one lane per stem. Click to jump; drag to set a loop |
| **LOOP AUS** | clears the loop |
| **REPEAT** | starts the track over when it ends |
| **jog wheel** | with **VINYL** on, the platter scratches, forwards and backwards. The outer ring bends the pitch while playing and searches while stopped. The mouse wheel nudges, or searches finely |
| **tempo fader** | with its range button beside it, which steps ±8 / ±16 / ±50 % |
| **BPM** | the tempo as it plays now; below it, **Original**, the track's own tempo |
| **SYNC** | follows a leader — see [Sync](#stemdeck-sync) |
| **MASTER** | makes this deck the Pro DJ Link tempo master — see [StemDeck as the tempo master](#stemdeck-master) |

The tempo comes from an analysis that runs in the background when a set is
loaded. It sums the four stems and assumes the tempo does not change during
the track. The result is kept, so each set is analysed only once.

The scrolling waveforms at the top run past a fixed playhead: drag to move
through the track, turn the mouse wheel to zoom.

(stemdeck-mixer)=

### Mixer

<!-- IMAGE: the mixer between the decks: both channel strips with stem knobs, M and AUX buttons (one AUX lit), channel faders, and the output meters 1-4 / AUX -->

One channel strip per deck, and per stem:

| Control | What it does |
| :--- | :--- |
| **gain knob** | −60 to +6 dB. Double-click for 0 dB |
| **M** | mutes the stem |
| **AUX** | takes the stem off its bus and sends it to the aux bus instead, after the channel fader |

Below the stems, the channel fader. Between the two strips, the output meters
for buses 1–4 and AUX.

(stemdeck-library)=

### Library

<!-- IMAGE: the library with a few sets listed, BPM column filled, the search box and the "Laden in A / Laden in B" buttons -->

One row per set: **Artist | Album | Set | BPM | Stems | Länge** — artist and
album from the folders, BPM once analysed. It starts sorted artist → album →
set; click a header to sort by that column (artist and album keep their sets
together and in order). The search box finds sets by name, artist or album as
you type.

To load a set:

- **Laden in A** / **Laden in B**, or
- double-click the row, or press Return — it goes to the first deck that is
  not playing, or
- drag the row onto a deck or its waveform.

**Ordner...** picks the folder, **Neu scannen** looks through it again.

(stemdeck-keys)=

### Keys

| | Deck A | Deck B |
| :--- | :---: | :---: |
| Play / pause | `D` | `L` |
| Cue (hold to preview) | `S` | `K` |
| Mute stem 1–4 | `1` `2` `3` `4` | `7` `8` `9` `0` |

(stemdeck-audio)=

## Audio out

StemDeck is a JACK client named `StemDeck` with ten outputs, five stereo
pairs:

| Ports | What is on them |
| :--- | :--- |
| `deck1_L`, `deck1_R` | bus 1: stem 1 of deck A plus stem 1 of deck B |
| `deck2_L`, `deck2_R` | bus 2: the two stems 2 |
| `deck3_L`, `deck3_R` | bus 3: the two stems 3 |
| `deck4_L`, `deck4_R` | bus 4: the two stems 4 |
| `aux_L`, `aux_R` | every stem switched to **AUX**, from either deck |

Despite the names, `deck1` … `deck4` are the **buses**, one per stem
position, not the decks.

- **Nothing is connected automatically.** Patch the ports yourself, in
  qjackctl or any other patchbay.
- **Aux is how a stem gets a movement.** In A³ Core a sound is moved by
  arriving on one of the four channels A³ Motion moves. Patch `aux_L` and
  `aux_R` there, switch a stem to AUX, and that channel's clip on A³ Motion
  flies it round the room — while the rest of the track stays where it is.
- StemDeck **never starts a JACK server**. It uses the one that is running,
  or PipeWire's JACK interface; with neither, it falls back to a plain audio
  device (ALSA), chosen with **Audio-Einstellungen**. With fewer than ten
  outputs there, the buses are summed down onto the ones there are.
- It takes the graph's sample rate and buffer size as they are, and resamples
  the stems itself. It asks for nothing on purpose: changing a running graph
  throws out other clients (zita-j2n, for one). If the rate matters, set it
  before starting — for PipeWire, until its next restart:

  ```sh
  pw-metadata -n settings 0 clock.force-rate 44100
  ```

<!-- QUESTION (maintainer): which Core inputs should StemDeck's buses and aux land on in the A³ setup? Core's patchbay (a3-patchbay.xml) has no StemDeck socket yet, so the page only says "one of the four channels A³ Motion moves". -->

(stemdeck-sync)=

## Sync

<!-- IMAGE: the top bar, right side: the PIO status readout (e.g. "PIO 128.0 · CDJ 2"), the player box, the "SYNC: PIO" button and "Audio-Einstellungen" -->

**SYNC** on a deck makes it follow a leader. The **SYNC: DECK | PIO** button
in the top bar chooses which leader: the other deck, or the CDJs. Switching it
turns off every SYNC that was on.

Both follow by the same rules:

- **Tempo:** the leader's tempo times a half, one or two — whichever needs the
  smallest change, chosen once when SYNC goes on. The tempo fader's range
  widens if it has to.
- **Phase:** corrected only while both play and nobody is scratching. More
  than 50 ms off, the deck jumps into phase; closer, it is nudged, by at most
  2 %.

### DECK: one deck follows the other

SYNC on deck A makes A follow B. Pressing SYNC on B hands the role over: B
follows A.

(stemdeck-pio)=

### PIO: following the CDJs

SYNC follows the **Pro DJ Link tempo master**: its tempo, pitch included, and
its beat. Both decks may follow at once, each with its own half/one/two.

- StemDeck joins the link as **virtual CDJ 6** and listens on UDP ports
  50000–50002. It shares those ports, so it can run on the same machine as the
  beat-analyzer (virtual CDJ 7), and both get the beats. If the network is not
  up yet, it tries again every two seconds.
- It learns who is master from the players' status packets. Some of those are
  sent to one address only, so on a machine it shares with the beat-analyzer
  they may not arrive. After two seconds without them the readout says **no
  master**, and StemDeck follows the player chosen in the box beside it — by
  default the first one it heard.
- If the master falls silent, the tempo is held (the readout says **held**)
  and the phase is left alone until beats come back.
- It lines up the **beat, not the bar**: the track's grid knows beats, not
  where the one is. Put the downbeat right with the jog, as on a CDJ.

The player number is the setting `pioDevice` in
`~/.config/StemDeck/StemDeck.settings`.

(stemdeck-master)=

## MASTER: StemDeck as the tempo master

No CDJs on the link? Then StemDeck is the CDJ. Each deck has a **MASTER**
button, as a CDJ has: the master deck's beat goes out on the Pro DJ Link
network, and whatever follows the link's tempo master follows StemDeck. In the
A³ system that is the beat-analyzer in clock mode 2, and through it A³ Motion
on **PIO**. The whole chain is on the beat-analyzer's page:
{ref}`Playing without CDJs <beat-analyzer-without-cdjs>`.

- **Press MASTER** on a deck to make it master; on the other deck, to hand
  over; on the master, to turn MASTER off. With MASTER off and SYNC not on
  PIO, StemDeck leaves the network.
- **With no master chosen, the only playing deck becomes master by itself** —
  except under SYNC: PIO, where a real CDJ may hold master and two masters
  would pull every listener back and forth, and except after you turned
  MASTER off by hand.
- **What goes out**, as virtual CDJ 6: a **beat packet on every beat** of the
  master deck — tempo is the track's BPM times the tempo fader, the beat in
  the bar counted from the first beat of the grid — and a **status packet
  every 200 ms**: master, playing or not, tempo, beat.
- **A stopped master stays master** and simply sends no beats.
- **Nothing goes out while the master deck has no tempo yet** — its analysis
  is still running.
- Everything goes out as **broadcast**, on the first network interface that
  is up, can broadcast and is not the loopback. So a listener on the same
  machine gets it, whichever program started first.
- The beats are timed to about a millisecond, on a thread of their own, not
  by the screen. A beat is not lost to a late wake-up, a cue on a beat sends
  that beat when you press PLAY, a jump does not send a burst of the beats
  skipped, and a handover never sends a beat twice.
- The top bar reads `PIO master: A` (or B) while StemDeck sends.

The packets are laid out the way
[prolink-connect](https://github.com/EvanPurkhiser/prolink-connect) reads
them, so tools built on it see StemDeck as a CDJ.

(stemdeck-build)=

## Build and start

StemDeck is built from source, on Linux. It needs:

- CMake 3.22 or newer, a C++17 compiler, pkg-config
- **JUCE 9**, installed so that CMake finds it, plus JUCE's own Linux build
  dependencies. `start.sh` looks for it under `~/local/juce` unless
  `CMAKE_PREFIX_PATH` says otherwise
- JACK, FLAC, Vorbis and Ogg development files. On Debian:

  ```sh
  apt install libjack-jackd2-dev libflac-dev libvorbis-dev libogg-dev
  ```

- GoogleTest (`libgtest-dev`), only for the tests

Then, in the StemDeck checkout:

```sh
./start.sh
```

The first run configures a Release build in `build/`; every run after that
rebuilds what changed and starts StemDeck — through a running JACK server,
through PipeWire's `pw-jack` if there is no JACK server but PipeWire runs, or
on ALSA. The program itself is `build/StemDeck_artefacts/Release/StemDeck`.

The settings — the library folder, the SYNC source, the audio device, the
player number — live in `~/.config/StemDeck/`, next to `analysis.xml`, the
kept tempo analyses. An analysis is kept per file, size and date, so a stem
file that changes is analysed again; to analyse everything anew, delete
`analysis.xml` while StemDeck is closed.

<!-- QUESTION (maintainer): is StemDeck meant to be started by hand with ./start.sh on the Core machine, or should the a3-core package get a user service for it like beat-analyzer's? -->

(stemdeck-troubleshooting)=

## Troubleshooting

| Symptom | What to do |
| :--- | :--- |
| A set is missing from the library | It needs exactly four files with one name and different endings. **Neu scannen** after adding files |
| Nothing to hear | The ports are never connected automatically. Patch them in qjackctl |
| The top bar says `JACK-Server wurde beendet` | JACK went away under StemDeck. Restart StemDeck once JACK is back |
| A stem on AUX does not move | The aux ports have to reach one of the channels A³ Motion moves, and that channel's **3d** has to be up |
| MASTER is on, but A³ Motion does not follow | Wait for the deck's BPM: nothing goes out before its analysis is done. Is the deck playing? Is A³ Motion on **PIO**? |
| The downbeat on A³ Motion is on the wrong beat | StemDeck counts the bar from the grid's first beat. Move the track with the jog |
| SYNC: PIO says **no master** | The status packets don't reach StemDeck. It follows the player chosen in the box beside the readout instead |
