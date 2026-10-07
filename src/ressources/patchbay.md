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
on 2026-10-08. The maintainer builds REAPER's routing and the patchbay
himself; this page describes them and prescribes nothing.

## The audio interface

The Core's JACK server (`a3-jack.service`) runs on the USB sound card, ALSA
device `hw:USB`, at 44.1 kHz. In JACK the card is the client `system`:

| Direction | Ports | Used for |
| :--- | :--- | :--- |
| capture | `capture_1` … `capture_12` | the A³ Mixer's channels, the phones and the aux return, see REAPER's inputs 1–12 below |
| playback | `playback_1` … `playback_20` | Main (`playback_1` … `8`), Phones (`9`, `10`) and Booth (`11` … `18`); `19` and `20` are not cabled, see REAPER's outputs below |

(core-reaper-channel-map)=

## REAPER's inputs and outputs: the channel map

The inputs and outputs REAPER uses, as the package's REAPER template and
patchbay have them on 2026-10-08. The patchbay as shipped is described
[further down](#patchbay-shipped).

### REAPER's inputs

**What REAPER receives** — two blocks: an analog one (four stereo decks, the
phones, the aux return) and StemDeck's (four deck buses and the aux bus).

| In | Block | Content |
| :--- | :--- | :--- |
| 1–8 | Analog | decks 1–4, stereo (the A³ Mixer's channels 1–4) |
| 9–10 | Analog | phones |
| 11–12 | Analog | aux (the aux return's analog input, played in ANALOG mode) |
| 13–20 | StemDeck | decks 1–4, stereo (StemDeck's buses 1–4) |
| 21–22 | StemDeck | aux |
| 23–30 | free | StemDeck has no phones output any more (2026-10-07): the cue is a desk channel inside REAPER |

### REAPER's outputs

**What REAPER sends** — the outputs come in blocks of ten:

| Out | Block | Content |
| :--- | :--- | :--- |
| 1–10 | Main | 1 sub, 2–10 tops; only 1–8 reach the hardware; metered on a copy (out 41–50) |
| 11–20 | Booth | 11 sub, 12–20 tops; also metered as they are (`vu_booth_sub` … `vu_booth_top9`); only 11–18 reach the hardware |
| 21–22 | Phones | stereo, to the hardware's phones outputs; also metered as they are (`vu_phones_L`, `vu_phones_R`) |
| 23–24 | Rec | stereo, to the network (`zita-j2n`), StemDeck's `rec_L/R` and `bpm_1`; also metered as they are (`vu_rec_L`, `vu_rec_R`) |
| 25–26 | Aux | the aux return's analog input (analog 11–12), to the beat-analyzer's `vu_aux_L`, `vu_aux_R` |
| 27–30 | free | |
| 31–50 | VU meters | the analog inputs (31–38) and the Main meters (41–50), to the beat-analyzer, see below |
| 51–66 | Channel meters | every channel's L and R before (51–58) and after (59–66) its fader, to the beat-analyzer |

## The beat-analyzer's inputs

The beat-analyzer is a JACK client with one tempo input and the meter inputs.

| Ports | Count | Fed from | Used for |
| :--- | :---: | :--- | :--- |
| `bpm_1` | 1 | REAPER's rec pair (`out23`, `out24`), the first channel of the pair only | tempo detection in clock mode EXT — intern |
| `vu_analog1_L` … `vu_free70` | 40 | REAPER out 31–50 and 11–26 (see below) | the meters `/vu/1`–`/vu/40` |
| `vu_in1_pre_L` … `vu_in4_post_R` | 16 | REAPER out 51–66 | the channel meters `/vu/51`–`/vu/66` |
| `vu_stem_a1_L/R` … `vu_stem_b4_L/R` | 16 | StemDeck's eight stereo stems (`zita-n2j` and/or the local StemDeck); optional, off by default | the stem meters `/vu/41`–`/vu/48` |

### Tempo: `bpm_1`

Whatever REAPER hands `bpm_1` is what the beat-analyzer listens to in
clock mode 1 (EXT — intern, see the
{doc}`Beat Analyzer <../user/beat-analyzer>`). It takes one channel only.

(core-vu-map)=

### The VU meters: which REAPER out feeds which `/vu/n`

The beat-analyzer meters REAPER outputs, one JACK input each, and sends each
as `/vu/n` (peak and RMS). The StemDeck meters, `/vu/41`–`/vu/50`, come from
StemDeck itself (below). Which REAPER out feeds `/vu/n` depends on the range:

| `/vu/n` | REAPER out |
| :--- | :--- |
| 1–20 | *n* + 30 (out 31–50) |
| 21–36 | *n* − 10 (out 11–26) |
| 41–50 | none: StemDeck sends them (`stem_a1` … `stem_b4`, `stem_aux_L/R`) |
| 51–66 | *n* (out 51–66) |

`/vu/9`–`/vu/10` and `/vu/37`–`/vu/40` are free. A port
name without its `vu_` prefix is the meter's name in `a3-osc.json`'s
`vu_meters` (`analog1_L`, `main_sub`, …; an entry's position in that list is
its `/vu/n`), and the devices look their meters up by it:

| REAPER out | beat-analyzer in | beat-analyzer port | OSC | Meter |
| :--- | :--- | :--- | :--- | :--- |
| 31–38 | 1–8 | `vu_analog1_L` … `vu_analog4_R` | `/vu/1`–`/vu/8` | the four channels' analog inputs, L and R (track "analog", before any channel processing) |
| 39–40 | 9–10 | `vu_free39`, `vu_free40` | `/vu/9`, `/vu/10` | free |
| 41 | 11 | `vu_main_sub` | `/vu/11` | Main sub |
| 42–50 | 12–20 | `vu_main_top1` … `vu_main_top9` | `/vu/12`–`/vu/20` | Main tops 1–9 |
| 11 | 21 | `vu_booth_sub` | `/vu/21` | Booth sub |
| 12–20 | 22–30 | `vu_booth_top1` … `vu_booth_top9` | `/vu/22`–`/vu/30` | Booth tops 1–9 |
| 21–22 | 31–32 | `vu_phones_L`, `vu_phones_R` | `/vu/31`, `/vu/32` | Phones |
| 23–24 | 33–34 | `vu_rec_L`, `vu_rec_R` | `/vu/33`, `/vu/34` | Rec |
| 25–26 | 35–36 | `vu_aux_L`, `vu_aux_R` | `/vu/35`, `/vu/36` | the aux return's analog input, analog 11–12, whatever the return plays |
| – | 37–40 | `vu_free67` … `vu_free70` | `/vu/37`–`/vu/40` | free, no cable |
| 51–58 | – | `vu_in1_pre_L` … `vu_in4_pre_R` | `/vu/51`–`/vu/58` | the channels' inputs after TRIM/EQ, L and R |
| 59–66 | – | `vu_in1_post_L` … `vu_in4_post_R` | `/vu/59`–`/vu/66` | the channel buses after the fader, L and R |

How the ranges come about:

- **Main is metered on a copy 40 outputs up:** Main sub on out 1 is metered
  on out 41. The analog inputs are tapped onto out 31–38 (track "analog"),
  before any channel processing.
- **Booth, Phones, Rec and the aux return are metered as they are**, on the
  outputs that carry them (11–26), so `/vu/21`–`/vu/36` hear out *n* − 10.
- **The channel meters keep their number:** out 51–66 sends `/vu/51`–`/vu/66`.

The free meters' names (`free39`, `free40`, `free67` … `free70`) are
placeholders; nothing feeds them and the patchbay has no socket for them.

The beat-analyzer needs `NUM_VU_CHANNELS=40` in its `build/.env` to open all
forty REAPER inputs (see {ref}`Beat Analyzer <beat-analyzer-config>`). It sends
them as five OSC bundles: four of ten (inputs, Main, Booth, stereo) and a fifth
for the stems. The port names live in its `src/audio/vu_ports.cpp`.

A³ Motion and the A³ Mixer follow this map since 2026-09-30, by the meters'
names: which device shows which meter is listed under
{ref}`The meters <osc-vu-meters>` in the OSC reference.

### The stem meters

**StemDeck sends its own stem meters.** One per stem, `/vu/41`–`/vu/48`
(deck A stems 1–4 = 41–44, deck B = 45–48), 25 Hz, peak (the louder side) and
rms (over both channels), measured after the stem's knob and mute, before the
fader and the buses. The AUX bus has two more, `stem_aux_L` and `stem_aux_R`
(`/vu/49`, `/vu/50`), at the same rate. The beat-analyzer therefore meters no
stems by default.

The beat-analyzer still has 16 optional JACK inputs, `vu_stem_a1_L` …
`vu_stem_b4_R`, for the same eight stems. They are fed from `zita-n2j` and/or
the local StemDeck; the patchbay does not connect them. With them on, each
stem pair is one meter (the louder side) sent as `/vu/41`–`/vu/48`, the same
addresses StemDeck uses:

| beat-analyzer in | beat-analyzer ports | OSC | Meter (`vu_meters`) |
| :--- | :--- | :--- | :--- |
| 41–48 | `vu_stem_a1_L/R` … `vu_stem_a4_L/R` | `/vu/41`–`/vu/44` | `stem_a1` … `stem_a4` |
| 49–56 | `vu_stem_b1_L/R` … `vu_stem_b4_L/R` | `/vu/45`–`/vu/48` | `stem_b1` … `stem_b4` |

`NUM_STEM_METERS` in its `build/.env` sets how many (default 0 = off; 8 turns
them on, which would fight with StemDeck's own meters).
With stem meters on, a `NUM_VU_CHANNELS` above 40 is clamped to 40.

(patchbay-zita)=

## Network audio: zita

A StemDeck on another machine reaches the Core over the network with
`zita-njbridge`. The units are described under
{ref}`zita-j2n and zita-n2j <core-zita>`; the UDP ports are in
{doc}`ports`.

| Unit | Machine | Direction | Channels | JACK ports | Network |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `zita-n2j` | Core | StemDeck in | 10 | `out_1` … `out_10` | listens on `zita-n2j.audio`, 20 ms buffer |
| `zita-j2n` | Core | REAPER's rec pair (`out23`, `out24`) out, 24 bit | 2 | `in_1`, `in_2` | sends to `radla.zita-n2j` |
| `zita-j2n` | StemDeck machine | StemDeck out | 10 | inputs 1–10, patched by hand | sends to the Core's `zita-n2j.audio` |
| `zita-n2j` | StemDeck machine | rec pair in | 2 | outputs, patched by hand | listens for the Core's `zita-j2n` |

On the StemDeck machine nothing is connected automatically, neither by
StemDeck nor by the zita units. The StemDeck package ships a patchbay for a
machine without a Core, `/usr/share/stemdeck/stemdeck-without-core.xml`: load
it once in QjackCtl and activate it. It cables StemDeck's ten outputs into
`zita-j2n`'s `in_1` … `in_10` in order, and `zita-n2j`'s `out_1`, `out_2` (the
rec pair) into StemDeck's `rec_L`, `rec_R`. How to set that up is under
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

## StemDeck's ports

StemDeck is a JACK client named `StemDeck` with 10 outputs: `deck1_L` …
`deck4_R` and `aux_L/R` — its five buses, mixed inside StemDeck. It has no
phones or cue outputs (since 2026-10-07); the cue is a desk channel in REAPER.

| Ports | What is on them |
| :--- | :--- |
| `deck1_L`, `deck1_R` | bus 1: every stem switched to **1**, from either deck, after the fader |
| `deck2_L`, `deck2_R` | bus 2: every stem switched to **2** |
| `deck3_L`, `deck3_R` | bus 3: every stem switched to **3** |
| `deck4_L`, `deck4_R` | bus 4: every stem switched to **4** |
| `aux_L`, `aux_R` | every stem switched to **A** (AUX), from either deck, after the fader |

Despite the names, `deck1` … `deck4` are the **buses**, one per desk
channel, not the decks. Which stems are on them is set by StemDeck's bus
switches (see {ref}`StemDeck's mixer <stemdeck-mixer>`).

| Direction | Ports | Arrives on / comes from |
| :--- | :--- | :--- |
| out | 10 ports above | REAPER in 13–22 |
| in | `rec_L`, `rec_R` | REAPER's rec pair (`out23`, `out24`); feeds **REC** in StemDeck's top bar |

- **StemDeck never connects anything itself**; the cables are the
  patchbay's (on the Core) or yours (on another machine).
- StemDeck **never starts a JACK server**: it uses the one that is running,
  or PipeWire's JACK interface; with neither it falls back to a plain audio
  device (ALSA). With fewer than ten outputs there, the buses are summed
  down onto the ones there are.
- It takes the graph's sample rate and buffer size as they are.

(patchbay-shipped)=

## The patchbay's sockets as shipped

`a3-patchbay.xml` has these sockets. A client's ports are listed as the
file names them. A socket name may appear once among the outputs and once
among the inputs (`reaper_aux`, `local_stemdeck`, `zita_stemdeck`); a cable
names one of each. Ports are paired in order, so a socket with more ports than
its partner leaves the surplus unconnected.

**Output sockets** (what feeds the graph):

| Socket | Client | Ports |
| :--- | :--- | :--- |
| `system_in` | `system` | `capture_1` … `capture_12` |
| `local_stemdeck` | StemDeck | `deck1_L` … `deck4_R`, `aux_L/R` |
| `zita_stemdeck` | `zita-n2j` | `out_1` … `out_10` |
| `reaper_main` | REAPER | `out1` … `out10` |
| `reaper_booth` | REAPER | `out11` … `out20` |
| `reaper_phones` | REAPER | `out21`, `out22` |
| `reaper_rec` | REAPER | `out23`, `out24` |
| `reaper_aux` | REAPER | `out25`, `out26` |
| `reaper_vu_analog` | REAPER | `out31` … `out38` |
| `reaper_vu_main` | REAPER | `out41` … `out50` |
| `reaper_vu_channels_pre` | REAPER | `out51` … `out58` |
| `reaper_vu_channels_post` | REAPER | `out59` … `out66` |

**Input sockets** (what takes audio):

| Socket | Client | Ports |
| :--- | :--- | :--- |
| `reaper_analog` | REAPER | `in1` … `in12` |
| `reaper_stems` | REAPER | `in13` … `in22` |
| `reaper_aux` | REAPER | `in9`, `in10` (no cable) |
| `alsa-scarlett_main` | `system` | `playback_1` … `playback_8` |
| `alsa-scarlett_phones` | `system` | `playback_9`, `playback_10` |
| `alsa-scarlett_booth` | `system` | `playback_11` … `playback_18` |
| `local_stemdeck` | StemDeck | `rec_L`, `rec_R` |
| `zita_stemdeck` | `zita-j2n` | `in_1`, `in_2` |
| `beat-analyzer_bpm` | beat-analyzer | `bpm_1` |
| `beat_analyzer_vu_main` | beat-analyzer | `vu_main_sub`, `vu_main_top1` … `vu_main_top9` |
| `beat_analyzer_vu_booth` | beat-analyzer | `vu_booth_sub`, `vu_booth_top1` … `vu_booth_top9` |
| `beat-analyzer_vu_phones` | beat-analyzer | `vu_phones_L`, `vu_phones_R` |
| `beat-analyzer_vu_rec` | beat-analyzer | `vu_rec_L`, `vu_rec_R` |
| `beat\-analyzer_aux` | beat-analyzer | `vu_aux_L`, `vu_aux_R` |
| `beat-analyzer_analog` | beat-analyzer | `vu_analog1_L` … `vu_analog4_R` |
| `beat-analyzer_channels_pre` | beat-analyzer | `vu_in1_pre_L` … `vu_in4_pre_R` |
| `beat-analyzer_channels_post` | beat-analyzer | `vu_in1_post_L` … `vu_in4_post_R` |

**Cables:**

| From | → To | Note |
| :--- | :--- | :--- |
| `system_in` (`capture_1` … `12`) | `reaper_analog` (`in1` … `in12`) | the A³ Mixer's channels, the phones and the aux return |
| `local_stemdeck` (10 ports) | `reaper_stems` (`in13` … `in22`) | local StemDeck |
| `zita_stemdeck` (`out_1` … `out_10`) | `reaper_stems` (`in13` … `in22`) | StemDeck on another machine |
| `reaper_main` (`out1` … `out10`) | `alsa-scarlett_main` (`playback_1` … `8`) | `out9`, `out10` have no hardware output |
| `reaper_booth` (`out11` … `out20`) | `alsa-scarlett_booth` (`playback_11` … `18`) | `out19`, `out20` have no hardware output |
| `reaper_booth` | `beat_analyzer_vu_booth` | Booth meters |
| `reaper_phones` | `alsa-scarlett_phones` (`playback_9`, `10`) | hardware phones |
| `reaper_phones` | `beat-analyzer_vu_phones` | Phones meters |
| `reaper_rec` (`out23`, `out24`) | `zita_stemdeck` (`zita-j2n` `in_1`, `in_2`) | the recording mix to the network |
| `reaper_rec` | `local_stemdeck` (`rec_L`, `rec_R`) | local StemDeck |
| `reaper_rec` | `beat-analyzer_bpm` (`bpm_1`) | the first of the pair |
| `reaper_rec` | `beat-analyzer_vu_rec` | Rec meters |
| `reaper_aux` (`out25`, `out26`) | `beat\-analyzer_aux` | aux return meters |
| `reaper_vu_analog` (`out31` … `38`) | `beat-analyzer_analog` | analog input meters |
| `reaper_vu_main` (`out41` … `50`) | `beat_analyzer_vu_main` | Main meters |
| `reaper_vu_channels_pre` (`out51` … `58`) | `beat-analyzer_channels_pre` | channel meters before the fader |
| `reaper_vu_channels_post` (`out59` … `66`) | `beat-analyzer_channels_post` | channel meters after the fader |

On a machine without a Core, StemDeck's own patchbay
(`/usr/share/stemdeck/stemdeck-without-core.xml`, see
[Network audio](#patchbay-zita)) takes the place of the Core's: two cables,
StemDeck's ten outputs to `zita-j2n` and `zita-n2j` to `rec_L/R`.

## Open points

**Not in the patchbay, or open:**

- Main `out9`, `out10` and Booth `out19`, `out20` have no hardware output;
  the Main and Booth sockets carry ten ports, the interface sockets eight.
- `reaper_aux` as an input socket (`in9`, `in10`) has no cable; the analog
  phones arrive over `reaper_analog`, which overlaps it.
- Local StemDeck and `zita-n2j` are both cabled to the same REAPER inputs;
  use one at a time.
- The `bpm_1` input takes one channel of the pair only.
- The free meters (`/vu/9`, `/vu/10`, `/vu/37`–`/vu/40`) have no socket and no
  cable.
