# Patchbay — audio inputs and outputs

Every audio input and output on the A³ Core's JACK graph: interface, REAPER,
beat-analyzer, zita and StemDeck. Other pages link here. REAPER's internal
routing is not here. The cables come from `~/.config/rncbc.org/a3-patchbay.xml`
(QjackCtl, shipped by a3-core; see [`qjackctl.service`](#core-services)), as of
2026-10-08. The maintainer owns the routing and the patchbay; this page only
describes them.

## The audio interface

JACK (`a3-jack.service`) runs on the USB card `hw:USB` at 44.1 kHz, client
`system`:

| Direction | Ports | Used for |
| :--- | :--- | :--- |
| capture | `capture_1` … `capture_12` | the A³ Mixer's channels, the phones and the aux return, see REAPER's inputs 1–12 below |
| playback | `playback_1` … `playback_20` | Main (`playback_1` … `8`), Phones (`9`, `10`) and Booth (`11` … `18`); `19` and `20` are not cabled, see REAPER's outputs below |

(core-reaper-channel-map)=

## REAPER's inputs and outputs: the channel map

### REAPER's inputs

| In | Block | Content |
| :--- | :--- | :--- |
| 1–8 | Analog | decks 1–4, stereo (the A³ Mixer's channels 1–4) |
| 9–10 | Analog | phones |
| 11–12 | Analog | aux (the aux return's analog input, played in ANALOG mode) |
| 13–20 | StemDeck | decks 1–4, stereo (StemDeck's buses 1–4) |
| 21–22 | StemDeck | aux |
| 23–30 | free | |

### REAPER's outputs

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

| Ports | Count | Fed from | Used for |
| :--- | :---: | :--- | :--- |
| `bpm_1` | 1 | REAPER's rec pair (`out23`, `out24`), the first channel of the pair only | tempo detection in clock mode EXT — intern |
| `vu_analog1_L` … `vu_free70` | 40 | REAPER out 31–50 and 11–26 (see below) | the meters `/vu/1`–`/vu/40` |
| `vu_in1_pre_L` … `vu_in4_post_R` | 16 | REAPER out 51–66 | the channel meters `/vu/51`–`/vu/66` |
| `vu_stem_a1_L/R` … `vu_stem_b4_L/R` | 16 | StemDeck's eight stereo stems (`zita-n2j` and/or the local StemDeck); optional, off by default | the stem meters `/vu/41`–`/vu/48` |

`bpm_1` is what the beat-analyzer listens to in EXT (one channel); see
{doc}`Beat Analyzer <../user/beat-analyzer>`.

(core-vu-map)=

### The VU meters: which REAPER out feeds which `/vu/n`

One JACK input per meter, sent as `/vu/n` (peak, RMS):

| `/vu/n` | REAPER out |
| :--- | :--- |
| 1–20 | *n* + 30 (out 31–50) |
| 21–36 | *n* − 10 (out 11–26) |
| 41–50 | none: StemDeck sends them (`stem_a1` … `stem_b4`, `stem_aux_L/R`) |
| 51–66 | *n* (out 51–66) |

`/vu/9`–`/vu/10` and `/vu/37`–`/vu/40` are free placeholders, with no socket.
A port name without `vu_` is the meter's name in `vu_meters`; devices look
meters up by it:

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

The beat-analyzer needs `NUM_VU_CHANNELS=40` in `build/.env`
({ref}`config <beat-analyzer-config>`); it sends five bundles (four of ten,
one for stems). Port names: `src/audio/vu_ports.cpp`. Who shows which meter:
{ref}`The meters <osc-vu-meters>`.

### The stem meters

**StemDeck sends its own**: `/vu/41`–`/vu/48` (deck A stems 1–4, then deck B),
25 Hz, peak of the louder side and RMS of both, after knob and mute, before
fader and buses; plus its AUX bus, `stem_aux_L/R` (`/vu/49`, `/vu/50`).

The beat-analyzer has 16 optional inputs for the same stems (unpatched, off by
default), one meter per pair:

| beat-analyzer in | beat-analyzer ports | OSC | Meter (`vu_meters`) |
| :--- | :--- | :--- | :--- |
| 41–48 | `vu_stem_a1_L/R` … `vu_stem_a4_L/R` | `/vu/41`–`/vu/44` | `stem_a1` … `stem_a4` |
| 49–56 | `vu_stem_b1_L/R` … `vu_stem_b4_L/R` | `/vu/45`–`/vu/48` | `stem_b1` … `stem_b4` |

`NUM_STEM_METERS` (default 0; 8 would fight StemDeck's meters). With them on,
`NUM_VU_CHANNELS` is clamped to 40.

(patchbay-zita)=

## Network audio: zita

`zita-njbridge` for a StemDeck on another machine. Units:
{ref}`zita <core-zita>`; ports: {doc}`ports`.

| Unit | Machine | Direction | Channels | JACK ports | Network |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `zita-n2j` | Core | StemDeck in | 10 | `out_1` … `out_10` | listens on `zita-n2j.audio`, 20 ms buffer |
| `zita-j2n` | Core | REAPER's rec pair (`out23`, `out24`) out, 24 bit | 2 | `in_1`, `in_2` | sends to `radla.zita-n2j` |
| `zita-j2n` | StemDeck machine | StemDeck out | 10 | inputs 1–10, patched by hand | sends to the Core's `zita-n2j.audio` |
| `zita-n2j` | StemDeck machine | rec pair in | 2 | outputs, patched by hand | listens for the Core's `zita-j2n` |

Nothing connects itself on the StemDeck machine. The StemDeck package ships
`/usr/share/stemdeck/stemdeck-without-core.xml`: load and activate it once in
QjackCtl. It cables the ten outputs to `zita-j2n` `in_1` … `in_10` and
`zita-n2j` `out_1/2` to `rec_L/R`
({ref}`setup <stemdeck-with-motion-remote-machine>`).

On the Core the ten network channels land on REAPER in 13–22:

| StemDeck output | Network channel | REAPER in |
| :--- | :---: | :---: |
| `deck1_L`, `deck1_R` (bus 1) | 1–2 | 13–14 |
| `deck2_L`, `deck2_R` (bus 2) | 3–4 | 15–16 |
| `deck3_L`, `deck3_R` (bus 3) | 5–6 | 17–18 |
| `deck4_L`, `deck4_R` (bus 4) | 7–8 | 19–20 |
| `aux_L`, `aux_R` | 9–10 | 21–22 |

## StemDeck's ports

Ten outputs, its five post-fader buses (`deck1` … `deck4` are buses, not
decks; see {ref}`StemDeck's mixer <stemdeck-mixer>`), and two inputs:

| Direction | Ports | Arrives on / comes from |
| :--- | :--- | :--- |
| out | `deck1_L` … `deck4_R`, `aux_L/R` | REAPER in 13–22 |
| in | `rec_L`, `rec_R` | REAPER's rec pair (`out23`, `out24`); feeds **REC** |

StemDeck connects nothing and starts no JACK server; see
{ref}`Audio out <stemdeck-audio>`.

(patchbay-shipped)=

## The patchbay's sockets as shipped

Ports pair in order; surplus ports stay unconnected. `reaper_aux`,
`local_stemdeck` and `zita_stemdeck` exist as both output and input sockets.

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

## Open points

- Main `out9`, `out10` and Booth `out19`, `out20` have no hardware output;
  the Main and Booth sockets carry ten ports, the interface sockets eight.
- `reaper_aux` as an input socket (`in9`, `in10`) has no cable; the analog
  phones arrive over `reaper_analog`, which overlaps it.
- Local StemDeck and `zita-n2j` are both cabled to the same REAPER inputs;
  use one at a time.
- The `bpm_1` input takes one channel of the pair only.
- The free meters (`/vu/9`, `/vu/10`, `/vu/37`–`/vu/40`) have no socket and no
  cable.
