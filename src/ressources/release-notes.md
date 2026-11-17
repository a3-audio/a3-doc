# Release notes

One version is one tag, set on every repository at once: the devices are built and played
together, so they are released together. Each section lists what changed, grouped by device,
newest version first. Each group names the repository the changes live in. To put a version
on a machine, use {doc}`install <../configuration/install>` (`install --update VERSION`).

For how the system got here, the reasoning and the wrong turns included, see
[History](history.md).

## Unreleased

On `main` since `v03.3`, not tagged yet.

## v03.3 (2026-11-17)

v03.3 retires the legacy 12-channel AES67 stream `AES67 <host> out`. The Core now sends four
streams, named by role: `AES67 Core MAIN`, `AES67 Core BOOTH`, `AES67 Core REC` and
`AES67 Core PHONES`, and a deck host records from `AES67 Core REC`. Every Core stream has its
own SAP session id. **a3-core and StemDeck have to be updated together:** without the new
a3-core there is no `AES67 Core REC`, and the deck hosts' recorder has no source. Beside this,
a **stereo deck** plays through its channel's analog strip and is moved by A³ Motion like an
analog channel, StemDeck plays **NI Stems** straight from the library, its events (scripted
moves) can be prepared from the stems' content and edited at the playhead, and the audio path
runs faster: Block 64, FFTW and a 4 ms deck buffer.

### The whole system

- **The legacy AES67 stream is gone.** The streams are listed in a stream table in
  `a3-osc.json`; the Core sends exactly its own rows (MAIN, BOOTH, REC, PHONES) and re-announces
  them when a layout is saved. The stream reference in a3-doc is rendered from that table.
- **A stereo deck** is a channel's analog input: StemDeck's *Output Stereo* mode sends one
  master pair, a3-core plays it through the channel's analog strip, and A³ Motion moves the
  channel like an analog one.
- **Lower latency:** Block 64 shipped, the headphone decoders and the delay at 2nd order, JUCE's
  FFT on FFTW, and the deck receive buffer at 4 ms (2 and 3 ms gave artifacts at Block 64).
- The hardware repositories carry one folder per board revision under `hardware/pcb/`, and the
  housings are revision v03.2.

### a3-core (`a3-core`)

- **Core streams by role:** `AES67 Core MAIN`, `BOOTH`, `REC` and `PHONES`, each with its own
  SAP session id (`c4ac82c4`); the stream table is validated, a bad row or a stream above the
  packet limit is refused alone and said, and the REC bus reaches `AES67 Core REC`.
- **The legacy stream is retired** from the truth and from the receive rule; an unknown AES67
  source is refused.
- **Stereo decks:** each deck slot has its own stereo inputs, told by its links and passed to
  Core with the hello; the deck runs through the channel's analog strip and is controlled as an
  analog channel. The engine crossfades between analog, stereo deck and B-format in 10 ms.
- **A deck always moves fully;** the channel's pot is its AUX-Send, not its 3D.
- **Screencast** can carry the REC bus, with a picture delay and a wait for the push route;
  `A3_SCREENCAST_PUSH` sends the picture to a target instead of listening.
- **Latency:** shipped Block 64, JUCE FFT on FFTW without allocation in the audio callback,
  headphone decoders and delay at 2nd order. A live block change forces its value. The
  configure step refuses a JUCE without the FFT patch.
- **Clock and links:** the clock brakes in time far from the lock instead of a limit cycle;
  a peer that pipewire-jack renamed to `<client>-<id>` is linked, and of a name and its
  renames the newest port is linked.
- Every A³ app opens full screen, StemDeck's decks too; the Core's DNS is the uplink router.
- **STATUS:** the AES67 row says it is the calculated deck-to-Core delay.
- **ABOUT:** `pcb` is a node with one row per board revision folder; only named third parties
  are listed, with versions from REUSE.

### a3-stemdeck (`a3-stemdeck`)

- **Records from `AES67 Core REC`**, not the legacy stream (`0962fef`); deck hosts take their
  sender from the stream table, and a malformed deck entry falls back instead of crashing.
- **NI Stems:** a `.stem.mp4` plays straight from the library (tracks 1–4 on slots 1–4),
  decoded natively with FFmpeg's libraries, no cache. StemDeck builds against them.
- **Output Stereo / B-Format** for a one-deck instance, set in Settings (a change restarts the
  unit); the stereo stream goes out as a 2-channel deck sender.
- **Events:** a set's events (one-shot moves) load, save and record per track and fire in the
  audio path. The **event strip** sits under the rolling waveform, markers show on the overview,
  and pads place an event at the playhead (3D REC) also while the deck stands. A DJ's edit makes
  a prepared event a hand one. Events are edited at the playhead in the one-deck clip settings
  and the two-deck stem popup.
- **`stemdeck-prepare-events`** writes event files for the library from the stems' content:
  grooves, breaks, builds, solos, drum gaps, hats-alone passages; v3 is the default rule set,
  `--explain` and a dry run report what it did, files with events are kept unless `--replace`.
  `compare-events` sets two event files side by side.
- **Motion shapes:** ORBIT is reversible, shown as `>` and `<`; a swipe on a shape pad sets
  direction (sideways) or tempo (up and down); PING jumps as a cross between the speakers and
  reads CROSS; RISE narrows the width as it climbs; one-shots can be a quarter bar long, with a
  beat-related tempo step per stem.
- **QUANTIZE** switch for playhead, cue and loop; a quantized cue takes the playhead with it,
  and a restored cue and loop never move.
- **One-deck screen:** on-screen keyboard (KEYS), space is PLAY, the deck title wraps at the
  playhead in the running waveform.
- A deck host's PipeWire runs 64 samples and its sender asks for 1 ms.

### a3-mixer (`a3-mixer`)

- Hardware: every board revision has a folder of its own under `hardware/pcb/`; the built
  mainboard is rev v0.2, as printed on it (KiCad holds the V03 draft), the shared parts come
  from the `a3-kicad-lib` submodule, and the housing is revision v03.2, unchanged and compatible.

### a3-motion (`a3-motion`)

- Hardware: `pcbs/` is now `pcb/`, one folder per board revision: `v1` (the first boards) and
  `v3_1` (the current board); the old boards are restored from history. Shared parts come from
  `a3-kicad-lib`; the housing is revision v03.2, unchanged and compatible.

### a3-motion-ui (`a3-motion-ui`)

- A channel on a stereo deck is moved like an analog one.

### a3-stem-separator (`a3-stem-separator`)

- No change beyond the README's picture of the A³ setup.

### a3-system (`a3-system`)

- StemDeck's packages build against FFmpeg's libraries (NI Stems), and the packages are built
  with JUCE's FFT patched for FFTW.
- The archive build files arch-all packages per suite and creates the shared pool before
  scanning it.
- The README shows every repository, part and third-party work in one aligned tree, `pcb` as a
  node with one row per board revision.

### a3-doc (`a3-doc`)

- **The AES67 reference** is generated from the truth: the Core's streams by role, who sees
  them, a zone without a sub; the ports table is rendered without the retired stream.
- **The audio signal flow in nine diagrams** (Mermaid in the Sphinx build).
- The stereo deck, StemDeck's Stereo output and how it patches onto `analog_N`, screencast with
  the REC bus.
- StemDeck: prepared events, QUANTIZE, the event file, cue and REC.
- Assembly pages by board revision, the A³ Assembly tree, **Playing A³: DJ knowledge** (from
  a3-pro-dj), Stem Separator, Beat Analyzer and Speaker Setup pages, current pictures of the
  a3-core window.
- Open points settled, the retired return stereo row removed, the booth stream described as a
  possibility, not a home setup.

## v03.2 (2026-10-31)

v03.2 gives the system its final shape and its face. Every repository sits under the one it
belongs to, under its own a3-audio name; the a3-core window opens on **ABOUT**, the project's
own page: the A³ logo, and PUBLISHED — every repository and part with its version and licence,
and every third-party work A³ is built on, with the version and licence its authors set. The
Debian packages of a release are now attached to the release page, and the first piece of the
rig updater is in: the `a3-update` package with a signed, checked install path.

### The whole system


- **Each repository sits under the one it belongs to, at its own name.** The virtual desk is
  its own repository, [a3-mixer-ui](https://github.com/a3-audio/a3-mixer-ui), a submodule of
  a3-mixer as a3-motion-ui is of a3-motion (whose `ui` is now `a3-motion-ui`);
  a3-beat-analyzer is a3-core's submodule, a3-stem-separator a3-stemdeck's and part of the
  release, and a3-prodj joins the umbrella. beat-analyzer, stemdeck and stemseparator moved to
  the `a3-audio` organisation as a3-beat-analyzer, a3-stemdeck and a3-stem-separator; the
  packages keep their names. A checkout follows with `git submodule sync --recursive` and
  `git submodule update --init --recursive`.
- The hardware parts carry their revision (`REVISION`: a board the revision printed on it, the A³ Mixer mainboard rev v0.2; housings v03.2) and the
  firmware is GPL-3.0-or-later; boards and 3D-print files stay CERN-OHL-S-2.0.
- No KiCad or FreeCAD backups or caches in the hardware repositories any more.
- The pro-DJ knowledge — best practice, gear, playing on 3D systems, the movement lab — lives in
  [a3-pro-dj](https://github.com/a3-audio/a3-pro-dj); manufacturer manuals only as links.

### a3-core (`a3-core`)

- **ABOUT** is its own page behind the A³ key and the window opens on it: the logo with
  "Spatial DJ setup", the PUBLISHED tree (system, repositories, pcb/housing/firmware with
  "rev …", a3-kicad-lib under the boards, one third-party node with each author's licence,
  JUCE's version compiled in), the links with Support A³ and the copyright.
- **STATUS** is one page: info and clock as "Label: value" rows; the Core row asks Core's API
  instead of counting quiet seconds; the delay note moved to MONITOR.
- **RIG** folds a3-core's services into one summary line; grey only for a unit that should run.
- The ABOUT tree lists every submodule at any depth; a repository already listed is not shown
  twice.

### a3-mixer (`a3-mixer`)

- Laid out like a3-motion: `firmware/`, `hardware/pcb/`, `hardware/housing/`, and the virtual
  desk as the submodule `a3-mixer-ui`.

### a3-system (`a3-system`)

- The release workflow attaches every built `.deb` with a signed `SHA256SUMS` to the release.
- `a3-update`: a package on every machine with a root helper that installs only signed A³
  release packages (one sudoers line, set once by hand), and the update service Core will call.
- The installer asks for the network once; `install --network` asks again.

## v03.1 (2026-10-31)

v03.1 is the first version without REAPER: A³ Core runs one program, **a3-core**, which
does the audio itself. The whole rig runs on **one clock**: a3-core locks the network's PTP
clock to the Scarlett, so StemDecks on other machines play over AES67 with 6 ms of buffer and
no crackle, and the window **measures the round trip** from input to output instead of only
estimating it. **The a3-core window is rebuilt** for the touch screen: cards on one grid, the
pages AUDIO, SPEAKERS, I/O, CALIBRATION, RIG and STATUS (A³ CORE and ABOUT), light and video
desks under I/O › DEPARTMENTS. Up to four StemDecks (A–D) send B-format and move their own
stems in the room; the desk and the A³ Mixer show the **delay** (BEAT, FEEDBK, COLOR, SPREAD)
on the return's display. StemDeck's stems now come from **stemseparator**, made on your own
computer, not on the rig. Gone: REAPER, its patchbay, QjackCtl, jackd, zita, and the
short-lived A³ Canvas (its content lives on as RIG and ABOUT). Every A³ user unit ships in one
place, the installer asks for the network once, the beat-analyzer keeps time and no longer
meters, and the copyright holder is Raphael Eismann.

### The whole system

- **One truth for OSC.** Every address, port and IP is written once, in `a3-osc.json`,
  shipped by a3-core; the network lives in `~/.config/a3/network.json` on the Core. Core serves
  the joined file; the A³ Mixer, StemDeck and A³ Motion fetch it, and each says with a hash
  which truth it speaks. See {ref}`Where addresses and ports live <osc-truth>`.
- **The vocabulary was straightened:** channels count 1–4 on the wire (were 0–3), `/fx/*` is
  `/filter/*`, the return is the **FX Return** (`/master/fx-return`), the meters are `/vu/n` by
  name. Anything outside the A³ repositories that speaks the old words has to follow.
- **PipeWire replaces jackd** on every machine: 44.1 kHz, the Scarlett drives the graph.
  Audio between machines goes over **AES67** on a second network socket with its own gigabit
  switch, Energy Efficient Ethernet off. See {ref}`the audio network <ports-audio-network>`.
- **Decks A to D.** Four StemDecks, each its own instance, on the Core or on another machine
  (a Raspberry Pi 5 works as a deck host). On a desk channel, **INPUT** picks a deck or **ST**,
  the stereo input.
- **The delay follows the music:** its tempo comes from a live beat clock, else the playing
  MASTER deck, else the playing deck on the loudest channel. A deck's stem AUX goes straight
  into the delay; the FX Return is the delay's master.
- **Total recall:** Core writes the evening down and plays it back at the next start; devices
  answer when Core asks, nobody pushes unasked.
- **One JUCE for every product**, 9.0.3.

### A³ Core (`a3-core`)

- **One program, `a3-core`.** The audio backend (from the archived `a3-engine`,
  with its history) runs channel strips, 3d, the DJ filter, the IEM encoder and decoders and
  the DualDelay; the Python Core is replaced by the same binary. Roles: `core`, `engine`,
  `clock`, `window`, `i3-bar`, `screencast-fanout`; `--headless` runs Core and the engine on a
  laptop without a screen.
- **REAPER, its patchbay and QjackCtl are gone.** The engine makes its own links from the I/O
  map; an upgrade moves the old units aside and never touches REAPER's files.
- **One clock:** `a3-clock.service` steers the PTP hardware clock from the Scarlett (only the
  frequency, ±20 ppm). The deck receivers become a plain FIFO with **6 ms** of buffer: 4 ms
  played clean on the rig, 2 ms crackled.
- **Round trip measured:** a quiet maximum-length sequence over a digital loop, or once over
  an analog test cable, gives the real delay from input to output on the AUDIO page.
- **The a3-core window, rebuilt:** cards on one grid, keys AUDIO, SPEAKERS (SPEAKERS, ZONES),
  I/O (INPUT, OUTPUT, DEPARTMENTS), CALIBRATION (with the FILTER card), RIG and STATUS
  (A³ CORE, ABOUT); a footer with KEYS, MONITOR, the clock's state and Save; the STEMDECK ▾
  workspace switch; an on-screen keyboard. No tooltips. See
  {ref}`Setting up a room <audio-engine-window>`.
- **Speakers in the window:** each zone has its own layout, edited in IEM's AllRADecoder and
  saved as your own variant; a 1 s pink-noise burst per speaker; a headphone EQ for PHONES.
- **RIG** lists every program of the rig with its state, host and version, and starts or
  stops them all; **DEPARTMENTS** adds light and video desks live, no restart.
- **MONITOR** (was OSC MONITOR): traffic, truths, the register and what Core did not
  understand, from Core's HTTP API; the web page is gone.
- **The engine meters** every `/vu` point, decks included (`/vu/37`–`/vu/40`), and Core
  forwards them.
- **Units in one place:** every A³ user unit ships under `/usr/lib/systemd/user`; copies in
  `~/.config` that the package once wrote are moved aside, hand-changed ones stay and are
  named.
- **Two packages:** `a3-core-app` carries the program, `a3-core` the Core machine; both are
  built for a public apt archive.
- **No lag from Core:** one loop per OSC port, the newest position wins, Core off Motion's
  processor core.

### A³ Mixer (`a3-mixer`)

- **Input selectors A B C D ST:** a channel's encoder picks a deck or the stereo input; the
  display shows each deck's meter and marks what plays.
- **The delay on the return display:** four rows BEAT, FEEDBK, COLOR and SPREAD beside the
  FX Return's meter; a push toggles select and edit, **DELAY CUE** puts the return in the
  headphones, TAP sits on strip 4. The virtual desk shows the same.
- **The virtual desk** in StemDeck's look: cards, line meters, a pot travel for a finger,
  StemDeck's workspace switch, full screen.
- **Calibrated pots and faders:** a calibration run takes every control to both ends; dead
  zones are mapped out.
- The channel LEDs have fixed colours, the main VU uses all 32 rows, the displays redraw only
  what changes (needs the new Teensy firmware).
- The desk reads its copy of `a3-osc.json` and asks Core for the state at start, so its lamps,
  pots and delay values are right from the first moment.

### A³ Motion (`a3-motion-ui`)

- **One clip per channel and six action buttons**, A1–A6; the ACTION page writes what you
  set into the action's script (what you see is what you get), and `then` chains buttons.
- **Recording:** ● arms, ▶ starts on the downbeat; pots are recorded by the same recmode as
  the path; a take overdubs and waits for SAVE or DISCARD.
- **Transport:** ❚❚ pauses at once and ▶ goes on, Shift waits for the downbeat, ■ goes back
  to the top.
- **FPV**, a second view for playing the floor: the room with a ship per clip, the guest
  groups on the dance floor, and pilots (OFF, HINT, FLY) that fly figures to the music.
- **The library:** 50 shapes, 70 clips, 71 actions and 14 mood sets.
- **The keyboard is the panel:** PADS has the panel's 44 keys; while the on-screen keyboard
  is up, the panel types.
- **No lag:** trajectories drawn on the graphics card (about 8 to 40 frames a second with four
  clips playing), knobs that follow only the first input of a gesture.
- **Decks:** a channel playing a deck shows the deck and sends no positions; StemDeck moves
  its own stems.
- **EXT follows smoothly:** half or double tempo counts as the same, a real change glides in.
- Motion is pure OSC; addresses, ports and hosts come from `a3-osc.json`. The workspace switch
  STEMDECK ▾ sits where StemDeck has MOTION.

### A³ Motion controller (`a3-motion`)

- The `v03.2` hardware branch is merged into `main`.
- **The key LEDs stay within what USB can supply:** the firmware dims all keys together only
  when their estimated draw goes over a budget, so playing is never dimmed.
- The panel is found by its USB ID; the pots follow the hand and end at 4095; a clockwise
  detent counts up; `host.py --pcb-test` checks a freshly built board.
- A v3 housing that prints on the A1.

### StemDeck (`stemdeck`)

- **One deck per instance**, A to Z, each with its own port, session and unit
  (`stemdeck@A` …); decks follow the MASTER deck.
- **B-format out:** each deck places its four stems in the room itself (one-shots ORBIT,
  PING, RISE, SCAT) and sends B-format, a binaural cue and phones to a3-core, locally or over
  AES67.
- **Stem n plays on channel n or on AUX**; the AUX pots are absolute, the lower encoder turns
  WIDTH.
- **Pro DJ Link like a CDJ-3000:** decks A–D are players 6, 5, 4 and 3; tempo master handed
  on as a CDJ-3000 does.
- **The one-deck screen:** transport band with LOOP, IN and OUT, CUE held + PLAY plays on,
  REPEAT and CONTINUE, track search, key lock (Rubber Band, R2 or R3) per deck.
- **The library:** a set is one to four stereo files; the stems come from stemseparator.
  Loop seams play without a gap, FLAC included.
- **AUTO DJ** hands stems over on downbeats through the desk buses and leaves alone what the
  DJ switched.
- **Recording** onto a USB stick when one is plugged in; a deck host records the Core's REC
  bus.
- StemDeck drives the A³ Motion panel; the workspace switch MOTION ▾ sits where Motion has
  STEMDECK.

### Beat analyzer (`beat-analyzer`)

- **The beat clock only:** the VU meters are gone (a3-core measures them). An old `.env` with
  VU keys still loads; they are named once and ignored.
- Its own Debian package, configured from `~/.config/beat-analyzer` and `conf.d`.
- EXT follows smoothly: tempo and phase from BTrack's beats, an octave lock with hysteresis; a
  tapped tempo holds for 16 bars, then detection takes over.
- JACK blocks of any size, also one that changes while running.

### The installer (`a3-system`)

- **One installer for the whole system:** `install` sets a machine up as Core, StemDeck deck
  host (also on Raspberry Pi OS), Motion or laptop (the whole rig on one machine), at one
  version. It installs from the public archive; `--from-source` builds as before.
- **The network is asked once**, on the first install; `install --network` asks again.
- The dialog is in English.
- The A³ Canvas came and went within the version; the a3-core window's RIG and ABOUT replace
  it.

### Documentation (`a3-doc`)

- **Written for the DJ:** every user page answers how the DJ gets what they want; one name per
  thing (A³ Core the hardware, a3-core the program, ST, AUX-Send, 3d), and a glossary.
- New pages: how A³ sounds, what you need, your first set, StemDeck, the beat analyzer, FPV,
  and setting up a room with a picture of every page of the a3-core window.
- The OSC reference and the ports page are rendered from `a3-osc.json`.
- Current pictures of the desk, StemDeck, A³ Motion and the a3-core window.
- These release notes.

## v03.0 (2026-09-12)

The first version tagged across all repositories at once. From here on `main` is the
integration branch everywhere and versions are tags. The per-hardware-revision branches
(`v03.2`, `dev/v03`) are merged and kept as history.

What came before is told in [History](history.md).
