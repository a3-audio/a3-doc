# OSC communication

What the messages *mean*. Every port is on [Ports and endpoints](ports.md).

(osc-truth)=

## Where addresses and ports live

Every OSC address, port and IP is written **once**, in `a3-osc.json`, in two
parts:

| Part | Owner | Where |
| :--- | :--- | :--- |
| **contract**: addresses, arguments, senders, listeners, ports, routes, VU map | the a3-core package, replaced on every install | `/usr/share/a3/a3-osc.json` (source: `platform-config/debian-x86_64/a3-core/usr/share/a3/a3-osc.json` in [a3-core](https://github.com/a3-audio/a3-core)) |
| **network**: `hosts`, Core's own `network` | the maintainer; created once by the installer, never overwritten | `~/.config/a3/network.json` on the Core |

Core **joins** them key by key; `network.json` wins, missing hosts come from
the package. A `network.json` that does not parse or lacks `hosts` or `network`
is **refused** (reason in the journal) and the package's values are used.

Core serves the result at `http://<core>:9080/api/truth` (`core.web`). Header
`X-A3-Truth` is its **fingerprint**: sha256 of the canonical JSON (sorted keys,
no spaces, UTF-8).

| Section | Holds |
| :--- | :--- |
| `network` | Core's interface, bridge, address, gateway, DNS |
| `hosts` | machines by name: `core`, `mixer`, `radla`, `local`, `any` |
| `listeners` | program, role, host, port |
| `routes` | who sends to which listener |
| `addresses` | pattern, types, sender, hearer, meaning |
| `vu_meters` | the forty meters by name, in `/vu/1..40` order |
| `external` | REAPER's and the IEM plug-ins' words |

The tables here and on the ports page are rendered from it.

### Who reads it, and how

| Device | How it gets the truth |
| :--- | :--- |
| A³ Core | the package's contract joined with `network.json` (`a3_osc.py`); serves it |
| A³ Motion | fetches it from Core, shared cache `~/.cache/a3/a3-osc.json`; see [Following Core](#osc-follow). No addresses in its `config.json` or menu |
| A³ Mixer | fetches it from Core on `/core/here`, cache as above, restarts on a new fingerprint; waits without one; see {ref}`the desk <mic-truth>` |
| StemDeck | like Motion; reads `prolink.*` and `stemdeck.bus`. Without: `PIO: no a3-osc.json` |
| beat-analyzer | the `a3-osc` block in `build/.env`, written by `a3-osc-render user`; see {ref}`Beat Analyzer <beat-analyzer-config>` |
| zita-j2n, zita-n2j | `~/.config/a3/osc.env`, same renderer |
| installer | offers the package's `network` and creates `network.json` from it once |

- **Core will not start without the package's file** (or `$A3_OSC_TRUTH`).
- **Core announces itself** every 2 s: `/core/here` broadcast on
  `devices.announce`, with the `/api/truth` URL and the fingerprint. Broadcasts
  don't cross routers; a device on another subnet uses `~/.config/a3/core`
  ([radla](#osc-radla)).

(osc-follow)=

### Following Core: StemDeck and A³ Motion

Both run on the Core as `aaa`, share the cache and listen for `/core/here`. At
start each takes `$A3_OSC_TRUTH`, else a valid cache, else the package file.

On an unknown fingerprint the app fetches `/api/truth` off the UI thread,
checks body sha256, header and announcement agree and the truth is usable
(StemDeck needs `stemdeck.bus`, Motion every address it speaks), writes the
cache and **exits 1**; systemd restarts it after 5 s. A refusal is logged once
per reason. With `$A3_OSC_TRUTH` set it does not follow.

**What you see:** after a truth change their windows close and reopen once,
about 5 s. Motion saves its state first.

(osc-radla)=

#### StemDeck on radla

radla is on another subnet:

1. Write Core's address into `~/.config/a3/core`, e.g.
   `http://192.168.8.10:9080` (a trailing slash or the full `/api/truth` URL
   also works; empty means unset).
2. Restart StemDeck.

It polls `/api/truth` at start and every 30 s; on a new header it fetches,
checks, writes the cache and exits 1 to restart. Core unreachable: one journal
line, it plays on. radla's zita units (`tools/zita-from-truth.py`) read the
cache, then `/usr/share/a3/a3-osc.json`, at their start only: after a change
restart them after StemDeck (`systemctl --user restart zita-j2n zita-n2j`).

### When a port or an address has to change

| Change | Do |
| :--- | :--- |
| address or host | edit `~/.config/a3/network.json`, restart Core; restart zita and the beat-analyzer (Core re-renders their files at start). Desk, StemDeck, Motion follow |
| port, address or word of the contract | edit `a3-osc.json` in a3-core, reinstall, restart Core; the rest follows as above |

Never set a port on a device: that is a second truth.

(osc-differs)=

### "DIFFERS from Core's"

The A³ Mixer and StemDeck send `/device/hello` (name, sha256 of their truth)
with each state request. Core's window shows per device **a3-osc.json is
Core's**, or in red **DIFFERS from Core's**. The desk, StemDeck and Motion fix
that within seconds; if it stays red, look for a refused fetch in the device's
log — until then it may send where nobody listens.

(osc-addresses)=

## Addresses

Every address of ours. `{ch}` is **1–4**, as on the panel. "Core passes it on":
Core acts on it, then relays or announces it.

<!-- a3-osc:addresses -->
| Address | Types | From | To | Meaning |
| --- | --- | --- | --- | --- |
| `/channel/{ch}/gain` | f | mixer, motion | core (Core passes it on to mixer, motion) | input trim |
| `/channel/{ch}/eq/high` | f | mixer, motion | core (Core passes it on to mixer, motion) | EQ high band |
| `/channel/{ch}/eq/mid` | f | mixer, motion | core (Core passes it on to mixer, motion) | EQ mid band |
| `/channel/{ch}/eq/low` | f | mixer, motion | core (Core passes it on to mixer, motion) | EQ low band |
| `/channel/{ch}/volume` | f | mixer, motion | core (Core passes it on to mixer, motion) | channel fader |
| `/channel/{ch}/aux-send` | f | mixer, motion | core (Core passes it on to mixer, motion) | send to the FX bus (the beat-synced DualDelay) |
| `/channel/{ch}/cue` | f | mixer, motion | core (Core passes it on to mixer, motion) | cue the channel to the headphones (its pre-fader send to enc_phones); was pfl until 2026-10-01 |
| `/channel/{ch}/cue/led` | f | core | mixer, motion | the cue lamp, 1 = lit |
| `/channel/{ch}/filter` | f | mixer, motion | core (Core passes it on to mixer, motion) | this channel through the master filter |
| `/channel/{ch}/filter/led` | f | core | mixer, motion | the filter key's lamp, 1 = lit |
| `/channel/{ch}/filter/frequency` | f | motion | core (Core passes it on to mixer, motion) | the channel's own filter cutoff (was pot_1) |
| `/channel/{ch}/filter/q` | f | motion | core (Core passes it on to mixer, motion) | the channel's own filter Q (was pot_2) |
| `/channel/{ch}/3d` | f | motion | core (Core passes it on to mixer, motion) | how much of the channel's isolated band moves, as an amplitude 0..1; the steady rest never changes |
| `/channel/{ch}/azimuth` | f | motion | core | the channel's direction, degrees |
| `/channel/{ch}/elevation` | f | motion | core | the channel's height, degrees |
| `/channel/{ch}/stem/turn` | i | mixer | core | the channel's encoder turned by this many clicks (signed): moves its selector's cursor over the nine positions (eight stems, then A, the analog input) in a ring: left from the first stem is A, right from A the first stem; switches nothing |
| `/channel/{ch}/stem` | i | core | mixer, motion | the stems on this channel's bus as a bit mask of pairs 1-8 (bit 0 = pair 1 = deck A stem 1); 0 = the analog input |
| `/channel/{ch}/stem/push` | i | mixer | core | the channel's encoder pushed: on a stem, it becomes the channel's only input -- a stem playing on another channel or on the return moves here; on the stem that already plays here, it leaves the channel as a push on A does; on A, the analog input, every stem leaves the channel so the analog input plays (in stem mode a released stem goes to the return), and while analog already plays nothing changes; without StemDeck nothing switches |
| `/channel/{ch}/stem/cursor` | i | core | mixer, motion | the channel's selector cursor: 0-3 deck 1's stems 1-4, 4-7 deck 2's stems 1-4, 8 = A, the analog input |
| `/filter/frequency` | f | mixer, motion | core (Core passes it on to mixer, motion) | the master filter's cutoff (was /fx/frequency) |
| `/filter/resonance` | f | mixer, motion | core (Core passes it on to mixer, motion) | the master filter's resonance (was /fx/resonance) |
| `/filter/mode` | f\|s | mixer, motion | core (Core passes it on to mixer, motion) | high-pass or low-pass (was /fx/mode) |
| `/filter/led` | s | core | mixer, motion | the filter section's lamp: blue HPF, green LPF (was /fx/led) |
| `/master/volume` | f | mixer, motion | core (Core passes it on to mixer, motion) | the main outputs |
| `/master/booth` | f | mixer, motion | core (Core passes it on to mixer, motion) | the booth outputs |
| `/master/phones-mix` | f | mixer, motion | core (Core passes it on to mixer, motion) | cue <-> main in the headphones |
| `/master/phones-volume` | f | mixer, motion | core (Core passes it on to mixer, motion) | the headphone level |
| `/master/aux-return` | f | mixer, motion | core (Core passes it on to mixer, motion) | the aux return, the fifth stereo input (was /master/return) |
| `/aux-return/stem/turn` | i | mixer | core | the aux return's encoder turned by this many clicks (signed): moves its cursor in a ring along the display, STEM (1) -> ANALOG (0) -> CUE (2) -> STEM; switches nothing |
| `/aux-return/stem/push` | i | mixer | core | the aux return's encoder pushed: switches the return to the mode under the cursor; on CUE it toggles the return's cue and switches no mode |
| `/aux-return/stem` | iiiiiiiii | core | mixer, motion | the aux return's cursor (0 = analog, 1 = stem, 2 = cue), then pairs 1-8: 1 = on the return (AUX) |
| `/aux-return/stem/mode` | i | core | mixer, motion | the aux return's mode, which chooses its source: 1 = stem (StemDeck's AUX bus plays on the return and every stem on no channel goes there; analog 11/12 is shut), 0 = analog (analog inputs 11/12 play on the return; no stem is on it and StemDeck's AUX is shut). Never both |
| `/aux-return/cue/led` | f | core | mixer, motion | the aux return's cue lamp, 1 = on |
| `/stemdeck/{deck}/{stem}/bus/{bus}` | i | core | stemdeck | set one bus switch of a stem, 1 on 0 off; bus 1-4 the desk channels, 5 AUX (StemDeck's own cue bus 6 is gone since 2026-10-07: a channel is cued through its own bus) |
| `/stemdeck/{deck}/{stem}/buses` | i | stemdeck | core | a stem's bus switches as a bit mask (bit 0 = bus 1), after every change and for all 8 stems after /stemdeck/recall |
| `/stemdeck/recall` | i | core | stemdeck | report every stem's buses once; Core asks when StemDeck's hello is news |
| `/device/hello` | ss | mixer, stemdeck, motion | core | a device names itself and the sha256 of its copy of this file, at start and every 30 s; Core's window shows whether it is Core's own. Core follows the StemDeck and the Motion that arrived last (one of each), a remote Motion instead of the rig's own, and forgets one silent for a minute |
| `/core/here` | ss | core | mixer, motion, stemdeck, radla | Core, every 2 s by broadcast: the URL of the joined truth and its fingerprint (sha256 of the canonical JSON) |
| `/state/recall` | i | motion | core | say the state again; the answer is the ordinary messages |
| `/beat` | iif | beat-analyzer, motion | core, motion, mixer, radla, beat-analyzer | beat in bar, bar, tempo -- the clock (Motion sends it only in clock mode 0) |
| `/tap` | i | mixer, motion | beat-analyzer | a tap on the beat |
| `/clockmode` | i | motion | beat-analyzer | 0 a3motion, 1 intern, 2 pioneer |
| `/vu/{n}` | ff | beat-analyzer, stemdeck | motion, mixer, radla | peak, rms (linear) of VU channel n. REAPER out per range: 1-20 = out n + 30, 21-36 = out n - 10, 51-66 = out n; 41-50 come from StemDeck, 9-10 and 37-40 are free. 1-8 analog1_L ... analog4_R the four channels' analog inputs, L and R each (REAPER track "analog" = system:capture_1-8, before any channel processing, shown under the desk's A even while a stem plays); 11-20 main_sub, main_top1 ... main_top9 the main outputs; 21-30 booth_sub, booth_top1 ... booth_top9 the booth outputs; 31-34 phones_L, phones_R, rec_L, rec_R the phones and the recording bus; 35-36 aux_L, aux_R the return's analog input, L and R (REAPER track "analog" channels 11-12 = system:capture_11-12, shown under the return's ANALOG whatever the return plays); 41-48 StemDeck's stems, one each (stem_a1 ... stem_b4: peak of the louder side, rms over both, after knob and mute); 49-50 StemDeck's AUX bus, L and R: peak and rms of each side after the bus; 51-66 the channels in stereo, L and R each: 51-58 in1_pre_L ... in4_pre_R (input after TRIM/EQ, post-fader), 59-66 in1_post_L ... in4_post_R (channel bus post-fader, moving + steady); see vu_meters. A remote Motion gets the analyzer's from Core (core.vu-relay), unchanged |
<!-- /a3-osc:addresses -->

### Renamed addresses

Code written against old words must follow:

| Old | Now |
| :--- | :--- |
| `/channel/0..3/…` | `/channel/1..4/…` |
| `/fx/frequency`, `/fx/resonance`, `/fx/mode`, `/fx/led` | `/filter/…` |
| `/channel/{ch}/fx` | `/channel/{ch}/filter` |
| `/channel/{ch}/led/pfl`, `/channel/{ch}/pfl`, `/channel/{ch}/pfl/led` | `/channel/{ch}/cue`, `/channel/{ch}/cue/led` |
| `/channel/{ch}/led/fx` | `/channel/{ch}/filter/led` |
| `/channel/{ch}/pot_1`, `pot_2` | `/channel/{ch}/filter/frequency`, `/filter/q` |
| `/master/phones_mix`, `phones_volume` | `/master/phones-mix`, `phones-volume` |
| `/master/return`, `/master/fx-return` | `/master/aux-return` |
| `/vu/0..39` | `/vu/1..40` |
| `/channel/{ch}/stem/menu` (ii) | `/channel/{ch}/stem/cursor` (i): 0–7 stems, 8 = **A** (analog input) |
| `/stem/cue`, `/stem/cue/led` | dropped |

`/channel/{ch}/stem` is a bit mask of the stems on a channel. On the desk,
turning only moves a selection (`…/stem/turn`, `/aux-return/stem/turn`) and a
push loads it (`…/stem/push`, `/aux-return/stem/push`; `…/stem/selected`).
`/aux-return/stem` carries the return's selection (0 = empty) before eight
flags. Cursor 8 pushed takes a playing stem off; Core remembers no last stem.
See {ref}`the desk's input selectors <a3mix-displays>`.

(osc-vu-meters)=

## The meters

The beat-analyzer sends `/vu/n` with peak and RMS (linear, 0–1); `/vu/n` is
REAPER out 30 + *n* ({ref}`REAPER channel map <core-vu-map>`). **Devices find a
meter by name** in `vu_meters`, not by number:

| Device | Shows |
| :--- | :--- |
| A³ Motion | channel inputs `in1_pre_L` … `in4_pre_R` (`/vu/51`–`/vu/58`, louder side); sphere glow `main_sub` (`/vu/11`); towers `main_top1`–`4` (`/vu/12`–`/vu/15`); MIXER master `main_sub`, `main_top1`–`9` (`/vu/11`–`/vu/20`) |
| A³ Mixer | inputs `in1_pre_L` … `in4_pre_R` (`/vu/51`–`/vu/58`); outputs `main_sub`, `main_top1`–`7` (`/vu/11`–`/vu/18`); channel displays `stem_a1` … `stem_b4` (`/vu/41`–`/vu/48`) and under A `analog1_L` … `analog4_R` (`/vu/1`–`/vu/8`); return `stem_aux_L/R` (`/vu/49`–`/vu/50`) and `aux_L/R` (`/vu/35`–`/vu/36`) |

`/vu/1`–`/vu/8` are the analog inputs before any processing, whatever the
channel plays.

<!-- a3-osc:vu -->
| Address | Meter |
| --- | --- |
| `/vu/1` | analog1_L |
| `/vu/2` | analog1_R |
| `/vu/3` | analog2_L |
| `/vu/4` | analog2_R |
| `/vu/5` | analog3_L |
| `/vu/6` | analog3_R |
| `/vu/7` | analog4_L |
| `/vu/8` | analog4_R |
| `/vu/9` | free39 |
| `/vu/10` | free40 |
| `/vu/11` | main_sub |
| `/vu/12` | main_top1 |
| `/vu/13` | main_top2 |
| `/vu/14` | main_top3 |
| `/vu/15` | main_top4 |
| `/vu/16` | main_top5 |
| `/vu/17` | main_top6 |
| `/vu/18` | main_top7 |
| `/vu/19` | main_top8 |
| `/vu/20` | main_top9 |
| `/vu/21` | booth_sub |
| `/vu/22` | booth_top1 |
| `/vu/23` | booth_top2 |
| `/vu/24` | booth_top3 |
| `/vu/25` | booth_top4 |
| `/vu/26` | booth_top5 |
| `/vu/27` | booth_top6 |
| `/vu/28` | booth_top7 |
| `/vu/29` | booth_top8 |
| `/vu/30` | booth_top9 |
| `/vu/31` | phones_L |
| `/vu/32` | phones_R |
| `/vu/33` | rec_L |
| `/vu/34` | rec_R |
| `/vu/35` | aux_L |
| `/vu/36` | aux_R |
| `/vu/37` | free67 |
| `/vu/38` | free68 |
| `/vu/39` | free69 |
| `/vu/40` | free70 |
| `/vu/41` | stem_a1 |
| `/vu/42` | stem_a2 |
| `/vu/43` | stem_a3 |
| `/vu/44` | stem_a4 |
| `/vu/45` | stem_b1 |
| `/vu/46` | stem_b2 |
| `/vu/47` | stem_b3 |
| `/vu/48` | stem_b4 |
| `/vu/49` | stem_aux_L |
| `/vu/50` | stem_aux_R |
| `/vu/51` | in1_pre_L |
| `/vu/52` | in1_pre_R |
| `/vu/53` | in2_pre_L |
| `/vu/54` | in2_pre_R |
| `/vu/55` | in3_pre_L |
| `/vu/56` | in3_pre_R |
| `/vu/57` | in4_pre_L |
| `/vu/58` | in4_pre_R |
| `/vu/59` | in1_post_L |
| `/vu/60` | in1_post_R |
| `/vu/61` | in2_post_L |
| `/vu/62` | in2_post_R |
| `/vu/63` | in3_post_L |
| `/vu/64` | in3_post_R |
| `/vu/65` | in4_post_L |
| `/vu/66` | in4_post_R |
<!-- /a3-osc:vu -->

(osc-core)=

## A³ Core

Three listeners ({ref}`ports <ports-by-listener>`); the port decides the meaning:

| Listener | Receives |
| :--- | :--- |
| `core.osc` | commands from Mixer, Motion, StemDeck, beat-analyzer |
| `core.reaper-feedback` | REAPER's reports. Separate, so Core never takes a report for a command and answers it: a feedback loop |
| `core.web` | HTTP: the {doc}`window <../development/core>` and `/api/truth` |

(osc-everyone)=

### Everything goes to everyone

Every A³ message Core produces goes to **every subscriber**; there is no
recipient list (a missing recipient fails silently over UDP).

```
      what comes in                        what goes out

   A³ Mixer                                   A³ Mixer
   A³ Motion            ──▶   A³ Core   ──▶   A³ Motion
   beat-analyzer             core.osc         light    (--subscriber)
   REAPER                    core.reaper-     video    (--subscriber)
                             feedback

   One message in, the same message out to every subscriber:
       /channel/*    /master/*    /filter/*    /state/recall

   And, each in its own language, to exactly one:
       /track/…            REAPER           reaper.osc
       /MultiEncoder/…     IEM encoders     iem.multiencoder-1..3
       /DualDelay/…        IEM DualDelay    dualdelay.osc
```

New subscriber: {ref}`Adding a department <core-subscriber>`.

- The engine is not a subscriber: REAPER, the MultiEncoders and the DualDelay
  each get their own language from one handler.
- **Lamps are broadcast too** (`/channel/{ch}/cue/led`,
  `/channel/{ch}/filter/led`, `/filter/led`), beside the flags: a lamp is a
  light, a flag a setting.
- Only changes are sent; a value already passed on is dropped.

### What the address table does not say

- **Values are 0–1**, except `azimuth` −180…180 and `elevation` −90…90,
  clamped; the clamped value is replayed.
- **gain, EQ, volume, `aux-send`** return to all devices when REAPER reports
  them ([The way back](#osc-way-back)).
- **`cue`, `filter`** take [two spellings](#osc-two-spellings); Core sends the
  state back as a number.
- **`3d`**: see [/channel/{ch}/3d](#osc-3d).
- **`/master/phones-mix`** goes out unbent, as a track volume.
- **`/master/aux-return`** drives PurestGain on track 28 "Return"; full travel
  is 0 dB.
- **`/filter/mode`**: `high_pass`/`low_pass` or a number (1 = high pass); sent
  as a number, the word goes to the desk on `/filter/led`.
- **`/beat`**: only the tempo is used, for the [delay](#osc-beat-delay).
- **`/vu/{n}`** comes from the beat-analyzer.
- `/channel/{ch}/reverb`, `/width`, `/order`: no handler; counted as
  unrecognised.

(osc-two-spellings)=

### The two spellings of a button

The A³ Mixer sends a button's **edge** as a string (`"1"` down, `"0"` up); A³
Motion sends a **state** as a number. Core tells them apart by type. Make
`a3-mixer.py` send `int(value)` and the desk's cue becomes momentary — and no
test catches it.

(osc-recall)=

### /state/recall

A device that just started asks; Core answers with **the ordinary messages**,
each to the device it belongs to:

1. **Lamps**: Core's own flags, from its state file.
2. **Position and 3d** per channel, held by Core because nobody else can be
   asked (positions go straight to the IEM plug-ins; `3d` can't be read back
   below −40 dB).
3. **Continuous values**: what REAPER last reported.

**A cold Core asks REAPER** for everything (action 41743, also a key in the
window) and replays once the report is in. A value never seen is **left out**,
not sent as zero: zero degrees is a real position.

(osc-way-back)=

### The way back: what REAPER reports

Core reads REAPER's feedback on `core.reaper-feedback`, bends it back through
its curve and broadcasts it:

| REAPER reports | comes back as |
| :--- | :--- |
| `/track/{12,16,20,24}/fx/1/fxparam/1/value` | `/channel/{ch}/gain` |
| `/track/{12,16,20,24}/fx/2/fxparam/{1,2,3}/value` | `/channel/{ch}/eq/{high,mid,low}` |
| `/track/{9,13,17,21}/fx/1/fxparam/*` | `/channel/{ch}/volume` |
| `/track/{9,13,17,21}/send/3/volume` | `/channel/{ch}/aux-send` |
| `/track/{12,16,20,24}/fx/3/fxparam/7/value` | `/filter/frequency` |
| `/track/{12,16,20,24}/fx/3/fxparam/6/value` | `/filter/resonance` |
| `/track/1/fx/1/fxparam/*` | `/master/volume` |
| `/track/2/fx/1/fxparam/*` | `/master/booth` |
| `/track/3/fx/2/fxparam/1/value` | `/master/phones-volume` |
| `/track/8/volume` | `/master/phones-mix` |
| `/track/28/fx/1/fxparam/1/value` | `/master/aux-return` |

The filter is reported per track and answered globally; duplicates are dropped.

```{warning}
**Relay only what no action script can drive.** `3d`, `freq` and `Q` carry the
accent envelope in REAPER; writing that back as the base would ratchet them up.
Gain, EQ, volume and `aux-send` are safe.
```

The desk ignores these values: its pots are analog.

(osc-beat-delay)=

### /beat, and the delay that follows it

```
beat-analyzer  ──/beat b bar bpm──▶  A³ Core (core.osc)
                                       │
                                       └──/DualDelay/delayBPML,R──▶  DualDelay (dualdelay.osc)
```

Core passes the tempo to the IEM DualDelay on the FX bus only when it has held
still **a whole bar** and differs by **≥ 0.1 BPM** (a changing delay shifts
pitch). Both lines get the same tempo; their multipliers stay in the plug-in.
The plug-in's OSC receiver must be opened and `Sync` off; see
{ref}`REAPER <core-reaper>`. REAPER's project tempo can't be used: the plug-in
reads it only on transport start.

### The aux send

```
/channel/{ch}/aux-send  ──▶  /track/{1,5,9,13}/send/1/volume   (normalised 0..1)
```

Send **1** reaches `enc_fx`. The number is the send's position on the sending
track (the `enc_phones` sends are 3 and 4); it lives in Core's `layout.json`.
3D is A³ Motion's alone (`/channel/{ch}/3d`).

## A³ Motion

Three listeners: `motion.osc` (Core's relays, `/beat`), `motion.vu` (meters),
`motion.energy` (IEM EnergyVisualizer), so high-rate streams don't share the
clock's socket. One handler serves all three.

- **Position** (`azimuth`, `elevation`) is sent while a blob moves.
- **`3d`** from the pot; **`filter/frequency`**, **`filter/q`** from the
  channel row and the encoders.
- **The MIX pages** send the A³ Mixer's addresses and receive Core's relays;
  `cue` and `filter` as states, `/filter/mode` as a number.
- **`/state/recall`** once at start-up.
- **`/beat`** sent in INT, received in EXT and PIO (syncs tempo and phase);
  floats are truncated.
- **`/tap`**, **`/clockmode`** go to the beat-analyzer.

| External address | Direction | What |
| :--- | :--- | :--- |
| `/EnergyVisualizer/RMS` | received, `motion.energy` | energy per direction lighting the sphere; see [below](#osc-energy) |
| `/StereoEncoder/azimuth`, `/elevation` | sent | alternative backend: straight into an IEM chain |

Addresses and ports come only from `a3-osc.json`. A meter's meaning exists
only in the file: the analyzer sends one meter per JACK input in port order.

(osc-3d)=

### /channel/{ch}/3d

Each channel is split in REAPER: `n-multi-enc` carries the steady signal;
`n-stereo-enc` carries two Airwindows Isolator3 — FX 2 isolates the moving
band, FX 3 removes the same band from a phase-inverted copy of the steady
signal. `filter/frequency` and `filter/q` go to both.

`3d` sets the gain on `n-stereo-enc` (FX 1, parameters 1 and 15) to
20·log10(3d) dB, floored at −40 dB for 3d ≤ 0.01; `n-multi-enc` stays at 0 dB.
Band and rest always sum to the input: **3d moves sound without changing the
level**. It is continuous.

(osc-energy)=

### /EnergyVisualizer/RMS

From the [IEM EnergyVisualizer](https://plugins.iem.at/docs/energyvisualizergrid/)
≥ 1.0.0, with "OSC send" on: **426 float32** per message, one per point of its
grid, about 9 a second, linear. Directions come from
`resources/EnergyVisualizerGrid.json` in the A³ Motion UI. Any other length is
discarded. Unlike the VU meters it carries elevation.

### Total recall at start-up

Motion sends `/state/recall` and stays silent until the answer (or a short
grace period). **At start-up Core wins; when a set is loaded the set wins.**
Asking once is safe; reporting continuously would loop (see
[The way back](#osc-way-back)).

(osc-beat-analyzer)=

## beat-analyzer

Listens on `beat-analyzer.clock` (`OSC_PORT_A3MOTION` in its `.env`) and the
Pro DJ Link ports (`prolink.*`, not OSC); sends to every target in its
`a3-osc` block ({ref}`config <beat-analyzer-config>`).

- **`/beat`** (beat 1–4, bar, bpm): sent in every mode to every target (mode 0:
  not to `motion`). Received and relayed only in mode 0; beats outside 1–4
  dropped. Mode 2: bar always 0.
- **`/vu/{n}`**: one per JACK input `vu_analog1_L` … `vu_free70` (REAPER out
  31–70), four bundles of ten, 25 per second, to `OSC_VU_*` if set, else
  `OSC_HOST_*`.
- **`/clockmode`**: 0 a3motion, 1 intern, 2 pioneer; clamped; not stored
  (starts in 1).
- **`/tap`**: mode 1 only; always sets the beat to 1.

Modes: {ref}`Beat Analyzer <beat-analyzer-modes>`.

## IP and Port

All listeners: [ports page](ports.md). Two ports are set **in a plug-in** and
must match the file by hand: the IEM DualDelay's (`dualdelay.osc`) and the
MultiEncoders' (`iem.multiencoder-1..3`, in the REAPER project).

### Known inconsistencies

- A device on an older truth shows *DIFFERS from Core's* ([above](#osc-differs)).
- A target hand-written into the beat-analyzer's `.env` outside the block is
  commented out (`# was: …`) at the next install.

## The register: which addresses exist at all

Core's window holds the **register** — every address the system can speak,
from `a3-osc.json` — against the traffic it has seen. **An address that exists
and never arrived is a dead wire.**

![The register, filtered to the A³ Mixer](../development/pics_development/a3core-window-register-mixer.png)

*nie* in that column: never heard. The window: {doc}`../development/core`.
