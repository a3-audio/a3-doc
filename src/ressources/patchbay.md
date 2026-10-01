# Patchbay — audio inputs and outputs

This is the one page for every audio input and output of the system: which
JACK port is connected to which, and what is on it. Other pages link here
instead of repeating it.

What is on this page is the JACK graph on the A³ Core: the audio interface,
REAPER's inputs and outputs, the beat-analyzer's inputs, the network audio
(zita) and StemDeck's ports. **REAPER's internal routing** (tracks, encoders,
decoders) **is not on this page** and will be documented separately. The
cables are made by the patchbay `~/.config/rncbc.org/a3-patchbay.xml`
(QjackCtl, shipped by the a3-core package; see
[`qjackctl.service`](#core-services)); the state described here is that file
on 2026-10-01. The maintainer builds REAPER's routing and the patchbay
himself; this page describes them and prescribes nothing.

## The audio interface

The Core's JACK server (`a3-jack.service`) runs on the USB sound card, ALSA
device `hw:USB`, at 44.1 kHz. In JACK the card is the client `system`:

| Direction | Ports | Used for |
| :--- | :--- | :--- |
| capture | `capture_1` … `capture_10` | the A³ Mixer's channels and the aux return, see REAPER's inputs 1–10 below |
| playback | `playback_1` … `playback_20` | the Main and the Booth outputs, see REAPER's outputs 1–20 below |

(core-reaper-channel-map)=

## REAPER's inputs and outputs: the channel map

The inputs and outputs REAPER uses (outputs decided on 2026-09-30, inputs on
2026-10-01). REAPER's routing
and the JACK patchbay are rebuilt to this map; the patchbay as shipped is
described [further down](#patchbay-shipped).

### REAPER's inputs

**What REAPER receives** — two blocks, configured the same way: four stereo
decks, one aux, one phones.

| In | Block | Content |
| :--- | :--- | :--- |
| 1–8 | Analog | decks 1–4, stereo (the A³ Mixer's channels 1–4) |
| 9–10 | Analog | aux (the aux return) |
| 11–12 | Analog | phones |
| 13–20 | StemDeck | decks 1–4, stereo (StemDeck's buses 1–4) |
| 21–22 | StemDeck | aux |
| 23–24 | StemDeck | phones |
| 25–30 | free | |

### REAPER's outputs

**What REAPER sends** — the outputs come in blocks of ten:

| Out | Block | Content |
| :--- | :--- | :--- |
| 1–10 | Main | 1 sub, 2–10 tops |
| 11–20 | Booth | 11 sub, 12–20 tops |
| 21–22 | Phones | stereo |
| 23–24 | Rec | stereo |
| 25–26 | Aux | stereo |
| 27–30 | free | |
| 31–70 | VU meters | to the beat-analyzer, see below |

## The beat-analyzer's inputs

The beat-analyzer is a JACK client with one tempo input and the meter inputs.

| Ports | Count | Fed from | Used for |
| :--- | :---: | :--- | :--- |
| `bpm_1` | 1 | REAPER's rec pair (`out7`, `out8`), the first channel of the pair only | tempo detection in clock mode EXT — intern |
| `vu_in1_pre` … `vu_free70` | 40 | REAPER out 31–70 | the meters `/vu/1`–`/vu/40` |
| `vu_stem_a1_L/R` … `vu_stem_b4_L/R` | 16 | StemDeck's eight stereo stems (`zita-n2j` and/or the local StemDeck) | the stem meters `/vu/41`–`/vu/48` |

### Tempo: `bpm_1`

Whatever REAPER hands `bpm_1` is what the beat-analyzer listens to in
clock mode 1 (EXT — intern, see the
{doc}`Beat Analyzer <../user/beat-analyzer>`). It takes one channel only.

(core-vu-map)=

### The VU meters: REAPER out 31–70

Outputs 31–70 go to the beat-analyzer's forty JACK inputs, one meter each,
and the beat-analyzer sends each as `/vu/n` (peak and RMS). Eight more
meters, for the StemDeck stems, come on top (below). Input *n*,
counted from 1, is fed from REAPER out 30 + *n* and sends on `/vu/n`. A port
name without its `vu_` prefix is the meter's name in `a3-osc.json`'s
`vu_meters` (`in1_pre`, `main_sub`, …), and the devices look their meters up
by it:

| REAPER out | beat-analyzer in | beat-analyzer port | OSC | Meter |
| :--- | :--- | :--- | :--- | :--- |
| 31–34 | 1–4 | `vu_in1_pre` … `vu_in4_pre` | `/vu/1`–`/vu/4` | channel inputs 1–4, pre-fader, post-FX |
| 35–38 | 5–8 | `vu_in1_post` … `vu_in4_post` | `/vu/5`–`/vu/8` | channel inputs 1–4, post-fader |
| 39–40 | 9–10 | `vu_free39`, `vu_free40` | `/vu/9`, `/vu/10` | free |
| 41 | 11 | `vu_main_sub` | `/vu/11` | Main sub |
| 42–50 | 12–20 | `vu_main_top1` … `vu_main_top9` | `/vu/12`–`/vu/20` | Main tops 1–9 |
| 51 | 21 | `vu_booth_sub` | `/vu/21` | Booth sub |
| 52–60 | 22–30 | `vu_booth_top1` … `vu_booth_top9` | `/vu/22`–`/vu/30` | Booth tops 1–9 |
| 61–62 | 31–32 | `vu_phones_L`, `vu_phones_R` | `/vu/31`, `/vu/32` | Phones |
| 63–64 | 33–34 | `vu_rec_L`, `vu_rec_R` | `/vu/33`, `/vu/34` | Rec |
| 65–66 | 35–36 | `vu_aux_L`, `vu_aux_R` | `/vu/35`, `/vu/36` | Aux |
| 67–70 | 37–40 | `vu_free67` … `vu_free70` | `/vu/37`–`/vu/40` | free |

Two rules carry the whole table:

- **A meter sits 40 outputs above what it measures:** Main sub on out 1 is
  metered on out 41, Booth sub on 11 on 51, Phones on 21 on 61.
- **beat-analyzer channel = REAPER out − 30 = the OSC number**, counted from
  1 (since 2026-09-30; it was 0 before): out 31 is the first channel and sends
  `/vu/1`, out 70 the fortieth and sends `/vu/40`.

The beat-analyzer needs `NUM_VU_CHANNELS=40` in its `build/.env` to open all
forty REAPER inputs (see {ref}`Beat Analyzer <beat-analyzer-config>`). It sends
them as five OSC bundles: four of ten (inputs, Main, Booth, stereo) and a fifth
for the stems. The port names live in its `src/audio/vu_ports.cpp`. Builds from
before 2026-09-30 name their forty inputs `vu_1` … `vu_12` (twelve) instead.

A³ Motion and the A³ Mixer follow this map since 2026-09-30, by the meters'
names: which device shows which meter is listed under
{ref}`The meters <osc-vu-meters>` in the OSC reference.

### The stem meters

**Since 2026-10-01.** The beat-analyzer has 16 more JACK
inputs, `vu_stem_a1_L`, `vu_stem_a1_R` … `vu_stem_b4_R`, for the StemDeck's
eight stereo stems. They are fed from `zita-n2j` and/or the local StemDeck;
the patchbay does not connect them yet. Each stem pair is one meter (the
louder side) and is sent as `/vu/41`–`/vu/48`:

| beat-analyzer in | beat-analyzer ports | OSC | Meter (`vu_meters`) |
| :--- | :--- | :--- | :--- |
| 41–48 | `vu_stem_a1_L/R` … `vu_stem_a4_L/R` | `/vu/41`–`/vu/44` | `stem_a1` … `stem_a4` |
| 49–56 | `vu_stem_b1_L/R` … `vu_stem_b4_L/R` | `/vu/45`–`/vu/48` | `stem_b1` … `stem_b4` |

`NUM_STEM_METERS` in its `build/.env` sets how many (default 8, 0 = off).
With stem meters on, a `NUM_VU_CHANNELS` above 40 is clamped to 40.

## Network audio: zita

A StemDeck on another machine reaches the Core over the network with
`zita-njbridge`. The units are described under
{ref}`zita-j2n and zita-n2j <core-zita>`; the UDP ports are in
{doc}`ports`.

| Unit | Machine | Direction | Channels | JACK ports | Network |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `zita-n2j` | Core | StemDeck in | 10 | `out_1` … `out_10` | listens on `zita-n2j.audio`, 20 ms buffer |
| `zita-j2n` | Core | REAPER's rec pair out, 24 bit | 2 | `in_1`, `in_2` | sends to `radla.zita-n2j` |
| `zita-j2n` | StemDeck machine | StemDeck out | 10 | inputs 1–10, patched by hand | sends to the Core's `zita-n2j.audio` |
| `zita-n2j` | StemDeck machine | rec pair in | 2 | outputs, patched by hand | listens for the Core's `zita-j2n` |

On the StemDeck machine nothing is connected automatically, neither by
StemDeck nor by the zita units: StemDeck's outputs go into `zita-j2n`'s
inputs in order, once, and saved. How to set that up is under
{ref}`StemDeck × A³ Motion <stemdeck-with-motion-setup>`.

The ten network channels are StemDeck's first ten outputs, and on the Core
they belong on REAPER's inputs 13–22:

| StemDeck output | Network channel | REAPER in |
| :--- | :---: | :---: |
| `deck1_L`, `deck1_R` (bus 1) | 1–2 | 13–14 |
| `deck2_L`, `deck2_R` (bus 2) | 3–4 | 15–16 |
| `deck3_L`, `deck3_R` (bus 3) | 5–6 | 17–18 |
| `deck4_L`, `deck4_R` (bus 4) | 7–8 | 19–20 |
| `aux_L`, `aux_R` | 9–10 | 21–22 |
| `phones_L`, `phones_R` | – | not sent (23–24 only from a local StemDeck) |

## StemDeck's ports

StemDeck is a JACK client named `StemDeck` with 12 outputs: `deck1_L` …
`deck4_R`, `aux_L/R`, `phones_L/R` — its six buses, mixed inside StemDeck.

| Ports | What is on them |
| :--- | :--- |
| `deck1_L`, `deck1_R` | bus 1: stem 1 of deck A plus stem 1 of deck B |
| `deck2_L`, `deck2_R` | bus 2: the two stems 2 |
| `deck3_L`, `deck3_R` | bus 3: the two stems 3 |
| `deck4_L`, `deck4_R` | bus 4: the two stems 4 |
| `aux_L`, `aux_R` | every stem switched to **A** (AUX), from either deck, after the fader |
| `phones_L`, `phones_R` | every stem switched to **C** and every deck on **CUE**, before the fader |

Despite the names, `deck1` … `deck4` are the **buses**, one per stem
position, not the decks.

| Direction | Ports | Arrives on / comes from |
| :--- | :--- | :--- |
| out | 12 ports above | REAPER in 13–24 |
| in | `rec_L`, `rec_R` | REAPER's rec pair (`out7`, `out8`); feeds **REC** in StemDeck's top bar |

- **StemDeck never connects anything itself**; the cables are the
  patchbay's (on the Core) or yours (on another machine).
- StemDeck **never starts a JACK server**: it uses the one that is running,
  or PipeWire's JACK interface; with neither it falls back to a plain audio
  device (ALSA). With fewer than twelve outputs there, the buses are summed
  down onto the ones there are.
- It takes the graph's sample rate and buffer size as they are.

(patchbay-shipped)=

## The patchbay's sockets as shipped

`a3-patchbay.xml` has these sockets. A client's ports are listed as the
file names them.

**Output sockets** (what feeds the graph):

| Socket | Client | Ports |
| :--- | :--- | :--- |
| `MPD` | Music Player Daemon | `left`, `right` |
| `reaper_vu` | REAPER | `out21` … `out32` |
| `reaper_rec` | REAPER | `out7`, `out8` |
| `reaper_main` | REAPER | `out1` … `out20` |
| `system_in` | `system` | `capture_1` … `capture_10` |
| `StemDeck` | StemDeck | `deck1_L` … `deck4_R`, `aux_L/R`, `phones_L/R` |
| `zita_stemdeck` | `zita-n2j` | `out_1` … `out_10` |

**Input sockets** (what takes audio):

| Socket | Client | Ports |
| :--- | :--- | :--- |
| `reaper_deck_4` | REAPER | `in7`, `in8` |
| `reaper-analog` | REAPER | `in1` … `in10` |
| `reaper-stemdeck` | REAPER | `in11` … `in22` |
| `beat_analyzer_vu` | beat-analyzer | `vu_1` … `vu_12` |
| `beat_analyzer_bpm` | beat-analyzer | `bpm_1` |
| `zita_rec` | `zita-j2n` | `in_1`, `in_2` |
| `StemDeck` | StemDeck | `rec_L`, `rec_R` |
| `system_out` | `system` | `playback_1` … `playback_20` |

**Cables:**

| From | → To | Note |
| :--- | :--- | :--- |
| `system_in` (`capture_1` … `10`) | `reaper-analog` (`in1` … `in10`) | the A³ Mixer's channels and the aux return |
| `StemDeck` (12 ports) | `reaper-stemdeck` (`in11` … `in22`) | local StemDeck, 6× stereo mode |
| `zita_stemdeck` (`out_1` … `out_10`) | `reaper-stemdeck` (`in11` … `in20`) | StemDeck on another machine |
| `MPD` (`left`, `right`) | `reaper_deck_4` (`in7`, `in8`) | overlaps the interface's inputs 7–8 |
| `reaper_main` (`out1` … `out20`) | `system_out` (`playback_1` … `20`) | hardware playback |
| `reaper_rec` (`out7`, `out8`) | `zita_rec` (`in_1`, `in_2`) | the recording mix to the network |
| `reaper_rec` (`out7`, `out8`) | `beat_analyzer_bpm` (`bpm_1`) | the first of the pair |
| `reaper_rec` (`out7`, `out8`) | `StemDeck` (`rec_L`, `rec_R`) | |
| `reaper_vu` (`out21` … `out32`) | `beat_analyzer_vu` (`vu_1` … `vu_12`) | twelve meters |

## Open points

**Not yet in the patchbay, or open:**

- The input layout of 2026-10-01 (analog 1–12, StemDeck 13–24) is the target;
  the patchbay as shipped still cables the hardware to `in1` … `in10` and
  StemDeck to `in11` … `in22`.
- StemDeck still offers an "8× stereo" output mode from an earlier plan; it is
  being removed — leave Output on 6× stereo.
- The beat-analyzer's sixteen stem inputs `vu_stem_a1_L` … `vu_stem_b4_R`
  come from the same earlier plan and are being removed; the stems' levels
  will come from StemDeck itself.
- StemDeck's phones (23–24) do not travel over the network: `zita-n2j` carries
  ten channels.
- The beat-analyzer's VU socket has twelve ports (`vu_1` … `vu_12`) fed from
  REAPER's `out21` … `out32`; the [channel map](#core-reaper-channel-map)
  above has forty inputs on outputs 31–70, and its output blocks reach
  beyond the twenty hardware playback ports the patchbay connects.
- `reaper_main` and `reaper_rec` both list `out7`, `out8`: those two outputs
  go to hardware playback and to the recording mix at once. The channel map
  puts Rec on out 23–24.
- Local StemDeck and `zita-n2j` are both cabled to the same REAPER inputs;
  use one at a time.
- The Music Player Daemon socket exists, but MPD may not be installed.
- The `bpm_1` input takes one channel of the pair only.
