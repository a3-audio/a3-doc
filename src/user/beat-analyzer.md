# Beat Analyzer

(beat-analyzer-at-a-glance)=

## At a glance

The system's **beat clock** and **level meters**: a program on the A³ Core,
on the same JACK graph as REAPER, with no screen.

- **The beat:** `/beat` (beat in bar, bar, tempo) to every device. A³ Motion
  follows it in **EXT** and **PIO**; the desk's tap keys blink with it.
- **The meters:** peak/RMS, 25 a second: A³ Motion's coronas, glow and
  lightning, and the desk's VU meters.

You choose the beat's source on A³ Motion's clock key. Source:
[beat-analyzer](https://github.com/rafjagger/beat-analyzer) (outside the
`a3-audio` organisation, versioned with the system), tempo detection by
[BTrack](https://github.com/adamstark/BTrack).

(beat-analyzer-modes)=

## Clock modes

Each tap on A³ Motion's clock key steps INT → EXT → PIO and sends `/clockmode`.

| A³ Motion reads | `/clockmode` | Mode | Where the beat comes from |
| :--- | :---: | :--- | :--- |
| **INT** | 0 | a3motion | **A³ Motion**: tapped there, relayed to all |
| **EXT** | 1 | intern | **the music**, analysed |
| **PIO** | 2 | pioneer | **the Pro DJ Link tempo master**: a CDJ, or [StemDeck](stemdeck.md) |

### What each mode needs

**INT — a3motion.** Only A³ Motion: it sends `/beat` to `beat-analyzer.clock`,
and the analyzer relays it to every target **except `motion`**. Its own clock
pauses; `/tap` does nothing.

**EXT — intern.** Music on its input (patched from REAPER,
{doc}`Patchbay <../ressources/patchbay>`). It finds onsets and a tempo; its
clock counts on between beats, and at the last tempo when music stops. Taps:

- The first tap after a 2 s pause sets **the one** (beat 1, tempo kept).
- From the second, the tempo follows your taps (median of the last eight
  intervals); from the third, every tap resets the beat to 1.
- Taps outside `BPM_MIN`–`BPM_MAX` are ignored.

```{warning}
**A tapped tempo stays.** After a tap the phase still follows the music, the
tempo does not. New taps change it; only a restart hands it back to the
analysis.
```

**PIO — pioneer.** The Core on a Pro DJ Link network: it joins as **player 7**
on the `prolink.*` ports and follows the **tempo master** (the player that
says master while playing; until known, any player). Tempo = the master's
track tempo with pitch. `/beat`'s bar is always 0 (Pro DJ Link knows the beat
in the bar, not the bar). Ask the venue before joining their network; not
affiliated with AlphaTheta or Pioneer ({doc}`../ressources/trademarks`).

No CDJs: [StemDeck as master](#beat-analyzer-without-cdjs).

### Switching modes by hand

Any OSC sender can switch it: `/clockmode` (int) to the clock port, **7775**
in today's `a3-osc.json`. On the Core:

```sh
oscsend localhost 7775 /clockmode i 2     # 0 a3motion, 1 intern, 2 pioneer
```

Out-of-range values are clamped. A³ Motion's clock key does not notice.

(beat-analyzer-without-cdjs)=

## Playing without CDJs: StemDeck as the tempo master

With no CDJs, [StemDeck](stemdeck.md) drives the clock:

```text
StemDeck, deck with MASTER on
   │  Pro DJ Link: a beat packet on every beat, a status packet every 200 ms,
   │  as player 6, sent as broadcast on UDP 50001 / 50002
   ▼
beat-analyzer, clock mode 2 (pioneer), player 7
   │  takes StemDeck as the tempo master: it says master, and it plays
   │  /beat  beat-in-bar, 0, bpm
   ▼
A³ Motion on PIO, A³ Mixer's tap keys, every other /beat target
```

1. Load a set in StemDeck and wait for its BPM (nothing is sent before).
2. Press **MASTER**, or PLAY: the only playing deck becomes master (not
   under **SYNC: PIO**, not after you turned MASTER off). Top bar:
   `PIO master: A`.
3. Tap A³ Motion's clock key to **PIO**. Its BPM follows the master deck,
   tempo fader included.

- **The one** is counted from the first beat of the track's grid: a wrong
  downbeat is fixed there.
- **A stopped master** sends no beats; A³ Motion carries on at the last tempo.
- On one machine both share the Pro DJ Link ports; broadcast reaches both
  whatever started first.

(beat-analyzer-meters)=

## The meters

Forty JACK inputs, each sent as peak and RMS (0–1), in four bundles of ten.
**Which signal is on which meter is decided by the JACK patching alone**:
{ref}`VU meter map <core-vu-map>`. `NUM_VU_CHANNELS=40` opens all forty.
Devices look meters up by name ({ref}`The meters <osc-vu-meters>`).

(beat-analyzer-config)=

## Where it runs and where its settings live

`beat-analyzer.service`, part of `a3-main`; the a3-core package installs the
unit and builds the program from the a3-system checkout.

Settings: a **`.env`** in its working directory `build/`. First found of
`build/.env`, `../.env`, `.env.example`. Template: `cp .env.example build/.env`.

**Targets and ports are rendered**, not hand-written: `a3-osc-render user`
writes a block at the end of `build/.env` from `a3-osc.json`:

```sh
# >>> a3-osc: rendered from a3-osc.json by a3-osc-render -- edit the truth, not this
OSC_HOST_core=127.0.0.1:9000
…
# <<< a3-osc
```

The rest of the file is yours. Block keys written outside it are commented
out (`# was: …`) at the next install. No targets: it reports the block
missing. To change one, change `a3-osc.json`
({ref}`truth <osc-truth>`).

| Setting | What it does |
| :--- | :--- |
| `OSC_HOST_<name>` *(block)* | a `/beat` target (and meters, unless `OSC_VU_<name>`). `motion` gets no relayed beat in INT |
| `OSC_VU_<name>` *(block)* | a separate meter port for that target |
| `OSC_PORT_A3MOTION` *(block)* | where `/beat`, `/clockmode`, `/tap` arrive |
| `OSC_ADDRESS_BEAT`, `_TAP`, `_CLOCKMODE`, `_VU` *(block)* | its addresses |
| `PIONEER_PORT_ANNOUNCE`, `_BEAT`, `_STATUS` *(block)* | Pro DJ Link ports |
| `BPM_MIN`, `BPM_MAX` | tempo range; outside it, doubled or halved in |
| `PIONEER_DEVICE_NUM` | player number, 7 |
| `NUM_VU_CHANNELS` | meters: 40 (max 64) |
| `NUM_STEM_METERS` | 0; 8 would fight StemDeck's own stem meters |
| `OSC_SEND_RATE` | meter rate, 25 |
| `VU_RMS_ATTACK`, `VU_RMS_RELEASE`, `VU_PEAK_FALLOFF` | meter ballistics |
| `DEBUG_BEAT_CONSOLE`, `DEBUG_PIONEER_CONSOLE` | log every beat / Pro DJ Link beat (with tempo, offset, player, master) |

Read at start; restart after a change. The clock mode is **not** a setting:
it always starts in mode 1 (intern).

```sh
systemctl --user restart beat-analyzer
```

Ports: [Ports and endpoints](../ressources/ports.md). Messages:
{ref}`OSC reference <osc-beat-analyzer>`.

(beat-analyzer-troubleshooting)=

## Troubleshooting

| Symptom | What to do |
| :--- | :--- |
| Motion on PIO/EXT, tempo from the wrong source | The analyzer restarted into mode 1. Step Motion's clock key once round |
| EXT: no beat | Service running? `bpm_1` patched ({doc}`Patchbay <../ressources/patchbay>`)? Music in REAPER? |
| EXT: half or double tempo | `BPM_MIN`–`BPM_MAX` one octave around the music, e.g. 70–140 |
| EXT: tempo stopped following | You tapped; tap again or restart the service |
| PIO: nothing arrives | Core on the players' network, ports free? Log: `Pioneer Receiver konnte nicht gestartet werden` |
| PIO: wrong player | It follows whoever says master while playing |
| Meters one channel across | JACK patching off by one |
| Meters still | Service running? `build/.env` ends with the `a3-osc` block? Else `a3-osc-render user`, restart |

Log: `journalctl --user -u beat-analyzer -f`.
