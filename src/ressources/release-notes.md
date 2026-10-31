# Release notes

One version is one tag, set on every repository at once: the devices are built and played
together, so they are released together. Each section lists what changed, grouped by device,
newest version first. Each group names the repository the changes live in. To put a version
on a machine, use {doc}`install <../configuration/install>` (`install --update VERSION`).

For how the system got here, the reasoning and the wrong turns included, see
[History](history.md).

## Unreleased

On `main` since `v03.1`, not tagged yet.

### The whole system

- **Each repository sits under the one it belongs to, at its own name.** The virtual desk is
  its own repository, [a3-mixer-ui](https://github.com/a3-audio/a3-mixer-ui), a submodule of
  a3-mixer as a3-motion-ui is of a3-motion (whose `ui` is now `a3-motion-ui`);
  a3-beat-analyzer is a3-core's submodule, a3-stem-separator a3-stemdeck's and part of the
  release, and a3-prodj joins the umbrella. beat-analyzer, stemdeck and stemseparator moved to
  the `a3-audio` organisation as a3-beat-analyzer, a3-stemdeck and a3-stem-separator; the
  packages keep their names. A checkout follows with `git submodule sync --recursive` and
  `git submodule update --init --recursive`.

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
