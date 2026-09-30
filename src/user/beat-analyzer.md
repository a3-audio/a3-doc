# Beat Analyzer

(beat-analyzer-at-a-glance)=

## At a glance

The beat-analyzer is the system's **beat clock** and its **level meters**. It
has no box and no screen of its own: it is a program on the A³ Core machine,
sitting on the same JACK audio graph as REAPER.

It does two jobs:

- **The beat.** It sends `/beat` — the beat in the bar, the bar and the tempo
  — to the devices. A³ Motion follows it in **EXT** and **PIO**, the A³ Mixer's
  tap keys blink with it.
- **The meters.** Twelve peak/RMS meters, 25 times a second. The coronas
  around A³ Motion's channel blobs, the glow of its sphere, the lightning of
  its speakers and the A³ Mixer's VU meters all come from here.

Where the beat comes from is your choice, and you make it on A³ Motion's
clock key.

- [beat-analyzer repository](https://github.com/rafjagger/beat-analyzer) —
  not under the `a3-audio` organisation, but part of the same system and
  versioned along with it
- Built on [BTrack](https://github.com/adamstark/BTrack) for the tempo
  detection

(beat-analyzer-modes)=

## Clock modes

The beat-analyzer has three clock modes. A³ Motion's clock key picks one: each
tap on the key steps INT → EXT → PIO and tells the beat-analyzer the new mode
with `/clockmode`.

| A³ Motion reads | `/clockmode` | Mode | Where the beat comes from |
| :--- | :---: | :--- | :--- |
| **INT** | 0 | a3motion | **A³ Motion.** You tap the tempo on Motion, Motion sends `/beat`, and the beat-analyzer passes it on to everyone else |
| **EXT** | 1 | intern | **The music.** The beat-analyzer listens to the audio and finds the beat itself |
| **PIO** | 2 | pioneer | **The Pro DJ Link tempo master** — a CDJ, or [StemDeck](stemdeck.md) as master |

### What each mode needs

**INT — a3motion.** Nothing but A³ Motion. Motion sends its own `/beat` to
port 7775; the beat-analyzer relays each one to every target in its
configuration **except the one named `motion`**, so Motion never hears its
own beat come back. In this mode the beat-analyzer's own clock is paused,
and a `/tap` it receives does nothing here.

**EXT — intern.** Music on the beat-analyzer's input. Its JACK input `bpm_1`
is patched from REAPER by Core's patchbay, so whatever REAPER hands it is what
it listens to. From that it finds onsets and a tempo, and a clock of its own
counts the beats — it keeps counting between detected beats, and at the last
tempo if the music stops. Tapping works here:

- The first tap after a pause of more than two seconds sets **the one**: the
  beat restarts at 1, at the tempo it had.
- From the second tap on, the tempo is taken from your taps (the middle of the
  last eight intervals); from the third on, every tap also puts the beat back
  on 1.
- A tapped tempo outside `BPM_MIN`–`BPM_MAX` is ignored.

```{warning}
**A tapped tempo stays.** Once you have tapped a tempo in EXT, the
beat-analyzer keeps it: it still follows the music's beats for the phase,
but no longer changes its tempo by itself. A new tempo takes new taps; the
analysis only goes back to finding the tempo on its own after the
beat-analyzer is restarted.
```

<!-- QUESTION (maintainer): beat_processing.cpp calls BTrack's fixTempo() on every accepted tap and nothing ever calls unfixTempo() (btrack_wrapper.h has it). So after one tap, EXT never follows a tempo change again until the service restarts. Intended ("the DJ has spoken"), or should the lock be released — after a time, or on a double tap? The page describes it as it is. -->

**PIO — pioneer.** A Pro DJ Link network the Core machine is on. The
beat-analyzer joins it as a **virtual CDJ, number 7**, and listens on UDP
ports 50000–50002. It follows the **tempo master**: the player whose status
says master while it plays. Until it has heard who the master is, it takes the
beats of any player. The tempo it sends is the master's track tempo with its
pitch applied — what the master's display shows.

The Pro DJ Link beat says where the beat is in the bar, not which bar it is,
so in PIO the bar number in `/beat` is always 0.

```{note}
**No CDJs? Use StemDeck as the master.** StemDeck can be the tempo master on
the link by itself, and PIO then follows StemDeck exactly as it would follow a
CDJ. See [Playing without CDJs](#beat-analyzer-without-cdjs).
```

### Switching modes by hand

A³ Motion's clock key is the normal way. Anything that can send OSC can do the
same — `/clockmode` with an integer to port **7775** on the Core machine. With
`oscsend` from liblo-tools, on the Core machine itself:

```sh
oscsend localhost 7775 /clockmode i 2     # 0 a3motion, 1 intern, 2 pioneer
```

A value outside 0–2 is clamped to the nearest mode. A³ Motion does not hear
about a change made this way: its clock key keeps showing what it showed.

(beat-analyzer-without-cdjs)=

## Playing without CDJs: StemDeck as the tempo master

With no CDJs in the booth, [StemDeck](stemdeck.md) can drive the whole clock.
The chain, as the code runs it:

```text
StemDeck, deck with MASTER on
   │  Pro DJ Link: a beat packet on every beat, a status packet every 200 ms,
   │  as virtual CDJ 6, sent as broadcast on UDP 50001 / 50002
   ▼
beat-analyzer, clock mode 2 (pioneer), virtual CDJ 7
   │  takes StemDeck as the tempo master: it says master, and it plays
   │  /beat  beat-in-bar, 0, bpm
   ▼
A³ Motion on PIO, A³ Mixer's tap keys, every other /beat target
```

1. Start StemDeck and load a set on a deck. Wait for the BPM readout: a deck
   sends nothing until its tempo analysis is done.
2. Press **MASTER** on that deck — or just press PLAY on it: with no master
   chosen, the only playing deck becomes master by itself (not under
   **SYNC: PIO**, and not once you have turned MASTER off by hand). The top
   bar reads `PIO master: A` (or B).
3. On A³ Motion, tap the clock key until it reads **PIO**.
4. The BPM on A³ Motion now follows the master deck, tempo fader included.

**Where the one is.** StemDeck counts the bar from the first beat of the
track's beat grid, not from anything it knows about the music. If A³ Motion's
downbeat falls on the wrong beat, that is where to look.

**A stopped master** stays master and sends no beats. A³ Motion then carries
on at the last tempo it had, as it does whenever the beats stop.

The same works on one machine: StemDeck and the beat-analyzer both listen on
ports 50000–50002, and because StemDeck sends as broadcast, both of them get
every packet regardless of which started first.

(beat-analyzer-meters)=

## The meters

The beat-analyzer measures forty JACK inputs, fed from REAPER's outputs
31–70, and sends each as a peak and an RMS value between 0 and 1, as three
OSC bundles of 16, 16 and 8. It gives a channel no meaning of its own beyond
its port name: **which signal is on which meter is decided by the JACK
patching alone.** Input *i*, counted from 0, is REAPER out 31 + *i* and sends
on `/vu/i` — `vu_main_sub` on out 41 arrives as `/vu/10`, for instance. The
whole table is the {ref}`VU meter map <core-vu-map>` on the Core's
configuration page.

`NUM_VU_CHANNELS=40` in `build/.env` opens all forty; builds from before
2026-09-30 name their inputs `vu_1` … `vu_12` instead.

```{warning}
A³ Motion and the A³ Mixer still read the old twelve positions — Motion
`/vu/0`–`/vu/3` as the channels, `/vu/4` as the subwoofer, `/vu/5`–`/vu/8` as
the speakers; the Mixer `/vu/0`–`/vu/3` as its inputs and `/vu/4`–`/vu/11` as
its outputs. Until both are moved to the new indices, their meters show the
wrong signals.
```

(beat-analyzer-config)=

## Where it runs and where its settings live

The beat-analyzer runs on the A³ Core machine as the `systemd --user` service
`beat-analyzer.service`, started and stopped together with the rest of Core
(it is part of `a3-main.service`). The a3-core package installs the unit and
builds the program from the beat-analyzer checkout in the a3-system
workspace.

Its settings are a **`.env` file** in its working directory, `build/` in the
beat-analyzer checkout. It reads, in this order, the first of:

1. `build/.env`
2. `.env` one directory up, in the checkout itself
3. `.env.example` in the working directory

and with none of them, it sends to a single target on `127.0.0.1:9000`. The
template is `.env.example` in the checkout:

```sh
cp .env.example build/.env
```

The settings that matter most:

| Setting | What it does |
| :--- | :--- |
| `OSC_HOST_<name>=host:port` | one target for `/beat` (and the meters, unless `OSC_VU_<name>` is set). As many as you like. The name `motion` is special: in INT mode that target does not get the relayed beat |
| `OSC_VU_<name>=host:port` | a separate port for that target's meters, so `/beat` and `/vu` do not share a socket |
| `OSC_PORT_A3MOTION` | where `/beat`, `/clockmode` and `/tap` arrive. 7775 |
| `BPM_MIN`, `BPM_MAX` | the tempo range the clock counts in. A tempo outside it is doubled or halved into it |
| `PIONEER_DEVICE_NUM` | its player number on the Pro DJ Link network. 7 |
| `NUM_VU_CHANNELS` | how many meters. 40, the A³ channel map; at most 64 |
| `OSC_SEND_RATE` | meter updates per second. 25 |
| `VU_RMS_ATTACK`, `VU_RMS_RELEASE`, `VU_PEAK_FALLOFF` | how fast the meters rise and fall |
| `DEBUG_BEAT_CONSOLE`, `DEBUG_PIONEER_CONSOLE` | print every beat, or every Pro DJ Link beat, to the log |

The settings are read at start. After a change, restart the service:

```sh
systemctl --user restart beat-analyzer
```

The clock mode is **not** a setting. The beat-analyzer always starts in mode 1
(intern) and changes when it is told to.

Which port on which device gets what is listed, as measured on the rig, in
[Ports and endpoints](../ressources/ports.md). The messages themselves are in
the {ref}`OSC reference <osc-beat-analyzer>`.

(beat-analyzer-troubleshooting)=

## Troubleshooting

| Symptom | What to do |
| :--- | :--- |
| A³ Motion reads PIO or EXT, but the tempo follows the wrong source | The beat-analyzer restarted, or started after A³ Motion, and is back in its start mode (intern). Tap Motion's clock key once round, back to the mode you want: every step tells the beat-analyzer again |
| EXT: no beat, the BPM stands still | Is the service running (`systemctl --user status beat-analyzer`)? Is `bpm_1` connected in qjackctl? Is music reaching REAPER? |
| EXT: half or double your tempo | Set `BPM_MIN`–`BPM_MAX` to one octave around the music, for house and techno e.g. 70–140. A wider range lets the clock count either one |
| EXT: the tempo no longer follows the track | You tapped: a tapped tempo stays. Tap the new tempo, or restart the service |
| PIO: nothing arrives | The Core machine has to be on the same network as the players, and nothing else on it may hold ports 50000–50002 exclusively. The log says `Pioneer Receiver konnte nicht gestartet werden` if it could not bind them |
| PIO: it follows the wrong player | It follows whoever says master while playing. Set master on the player you mean |
| The meters all sit one channel across | The JACK patching is off by one: REAPER out *N* belongs on the port that sends `/vu/(N-31)` |
| The meters don't move at all | Check the service, then the `OSC_VU_*` / `OSC_HOST_*` entries in `build/.env` against [Ports and endpoints](../ressources/ports.md) |

Its log is the service's journal:

```sh
journalctl --user -u beat-analyzer -f
```

With `DEBUG_BEAT_CONSOLE=1` it prints a line per beat with the tempo and how
far the beat was off; with `DEBUG_PIONEER_CONSOLE=1`, a line per Pro DJ Link
beat, naming the player and whether it is master.
