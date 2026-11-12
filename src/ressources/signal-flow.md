(signal-flow)=

# Audio signal flow

The audio path of the whole rig, block by block, as read on the rig on 2026-11-10. Each block is its own
diagram and can be read alone.

**Legend.** Solid arrows (`-->`) are audio. Dashed arrows (`-.->`) are control (OSC) or clock (PTP,
SAP announcements). Subgraphs are machines. A label with **(?)** marks something that could not be verified;
each one is listed under *Open points* at the end. "Live" means read on the rig on 2026-11-10 with
`pw-link -l`, `pw-top -b`, `pw-metadata -n settings` and `cat` of configs (read-only). Port names are
exactly as PipeWire/JACK show them.

---

## 1. Rig overview

Three machines carry audio: a3nuc1 (Core engine, deck A, the Scarlett), a3motionV02 (deck B) and
a3nuc2 (deck C). Decks B and C reach the Core as AES67 streams on the audio network (192.168.9.0/24);
the Core sends one stream back (`AES67 a3nuc1 out`, carrying REC) that the deck hosts receive for
their recorders. Controllers only send OSC.

```mermaid
flowchart LR
  subgraph N1["a3nuc1 · Core + deck A · 192.168.9.10"]
    SDA["StemDeck-A"]
    ENG["a3-engine"]
    CORE["a3-core Core (OSC)"]
    BAN["beat-analyzer"]
    RXB["AES67 deck B (receiver)"]
    RXC["AES67 deck C (receiver)"]
    TXO["AES67 a3nuc1 out (sender, 12 ch)"]
    TXZ["AES67 Core MAIN / BOOTH / REC / PHONES (senders)"]
  end
  subgraph N3["a3motionV02 · deck B · 192.168.9.23"]
    SDB["StemDeck-B (?) stopped at read time"]
    TXB["aes67-deck-b (sender, 41 ch)"]
    RXO3["AES67 a3nuc1 out (receiver)"]
  end
  subgraph N2["a3nuc2 · deck C · 192.168.9.20"]
    SDC["StemDeck-C"]
    TXC["aes67-deck-c (sender, 41 ch)"]
    RXO2["AES67 a3nuc1 out (receiver)"]
  end
  SCAR["Scarlett 18i20 3rd Gen (USB on a3nuc1)"]
  SRC["Analog sources (?)"]
  PA["PA main 4.1 (?)"]
  HP["Headphones (?)"]
  ARC["Analog recorder (?)"]
  BTH["Booth (?) no receiver found"]
  CTL["Mixer · desk · Motion UI · pro-DJ apps"]

  SRC --> SCAR
  SCAR -->|"capture 1-8"| ENG
  SDA -->|"JACK, 41 links"| ENG
  SDB -->|"(?)"| TXB
  SDC -->|"41 links"| TXC
  TXB -->|"RTP multicast"| RXB
  TXC -->|"RTP multicast"| RXC
  RXB --> ENG
  RXC --> ENG
  ENG -->|"main 1-5, phones 9-10, rec 11"| SCAR
  SCAR --> PA
  SCAR --> HP
  SCAR --> ARC
  ENG --> SDA
  ENG --> BAN
  ENG --> TXO
  ENG --> TXZ
  TXZ -.->|"AES67 Core BOOTH"| BTH
  TXO -->|"RTP multicast"| RXO2
  TXO -->|"RTP multicast"| RXO3
  RXO2 -->|"rec_L/R"| SDC
  RXO3 -.->|"(?) deck B stopped"| SDB
  CTL -.->|"OSC :9000"| CORE
  CORE -.->|"OSC :9004"| ENG
  CORE -.->|"PTP grandmaster (ptp4l)"| N2
  CORE -.->|"PTP grandmaster (ptp4l)"| N3
```

Sources: live `pw-link -l`/`pw-top` on a3nuc1, a3nuc2, a3motionV02; `ip -br a` on each; truth
`a3-osc.json` (`hosts`, `aes67_streams`, `listeners`); `systemctl --user is-active` on each host.

---

## 2. One StemDeck deck (one-deck `-bformat` instance, `StemDeck-<X>`)

Four stereo stems pass their stem knob (the "pre-mute block"), then each stem is split into a moving
share (IEM StereoEncoder at the stem's pose) and a steady share (a SteadyBed of four fixed sources),
summed to 3rd-order B-format. The instance exposes exactly 43 output ports (B-format, AUX, cue,
phones) and two inputs (`rec_L/R`); it has no stereo buses.

```mermaid
flowchart LR
  FILE["Stem file (NI Stems)"] --> PLAY["Player: 4 stereo stems (8 ch)"]
  PLAY --> KNOB["Stem knob (gain) = pre-mute block"]
  KNOB -->|"moving share g·x"| SENC["Per stem: IEM StereoEncoder (az / el / width)"]
  KNOB -->|"steady share (1-g)·x"| SBED["SteadyBed (MultiEncoder, 4 bed sources)"]
  MOT["DeckMotion one-shots, deck 3D"] -.->|"pose, g"| SENC
  SENC --> MSUM["Main sum, order 3 SN3D, 16 ch"]
  SBED --> MSUM
  MSUM --> MUTE["Stem MUTE after the encoder (R5)"]
  MUTE --> OBF["bformat_1..16"]
  KNOB --> AUXS["Per-stem AUX send 0..1"]
  AUXS --> ABUS["AUX bus 16 ch (encoder out + steady via aux bed)"]
  ABUS --> OAUX["aux_1..16"]
  KNOB --> CUES["Per-stem CUE switch (pre-mute)"]
  CUES --> CBED["Cue bed, 3rd-order sum"]
  CBED -->|"ACN 0..8 only"| OCUE["cue_1..9 (2nd order)"]
  CBED --> PDEC["BinauralDecoder (standalone use)"]
  PDEC --> OPH["phones_L / phones_R (not linked on rig)"]
  IREC["rec_L / rec_R (inputs)"] --> RECF["Recorder: 24-bit FLAC"]
```

Sources: `a3-stemdeck/Source/DeckSpatial.h` (stems pre-mute, g·x / (1-g)·x, R5, cue = first 9 ACN, aux
bus, phones decoder), `Outputs.h` (`outputs::oneDeck::layout`, 43 ports, `portName`),
`SpatialLaw.h` (`order = 3`, `bformatChannels = 16`, `stemsPerDeck = 4`), `SteadyBed.h`,
`StemDeckPlayer.h` (pre-mute block, cue send pre-mute), `Recorder.h`, `DeckLinks.h`; live a3nuc1/a3nuc2
(`phones_*` unlinked). The two-deck StemDeck's five stereo buses (1-4 + AUX, `Buses.h`) are the legacy
mode and are not drawn.

---

## 3. Deck-to-Core transport

Deck A is a local JACK client linked straight to the engine. Decks B and C each run a PipeWire
`module-rtp-sink` with 41 channels (MAIN1-16, AUX1-16, CUE1-9) in the PTP group, announced by SAP;
the Core's `module-rtp-sap` turns every session matching `~^AES67 deck ` into a 41-port receiver with a
4 ms buffer, whose ports `engine.json` links onto the engine's deck slot.

```mermaid
flowchart LR
  subgraph HA["a3nuc1 · deck A (local)"]
    SA["StemDeck-A: bformat_1..16 · aux_1..16 · cue_1..9"]
  end
  subgraph HB["a3motionV02 · deck B"]
    SB["StemDeck-B (?) stopped"]
    TB["aes67-deck-b · 'AES67 deck B' · 41 ch S24BE · ptime 0.25 ms · sess.latency 1 ms"]
  end
  subgraph HC["a3nuc2 · deck C"]
    SC["StemDeck-C: bformat · aux · cue"]
    TC["aes67-deck-c · 'AES67 deck C' · 41 ch S24BE · ptime 0.25 ms · sess.latency 1 ms"]
  end
  SAPG["SAP/SDP 239.255.255.255:9875"]
  subgraph HCORE["a3nuc1 · Core"]
    RB["AES67 deck B: receive_MAIN1..16 · AUX1..16 · CUE1..9 · sess.latency 4 ms"]
    RC["AES67 deck C: receive_MAIN1..16 · AUX1..16 · CUE1..9 · sess.latency 4 ms"]
    EA["a3-engine deckA_1..16 · deckA_aux_1..16 · deckA_cue_1..9"]
    EB["a3-engine deckB_1..16 · deckB_aux_1..16 · deckB_cue_1..9"]
    EC["a3-engine deckC_1..16 · deckC_aux_1..16 · deckC_cue_1..9"]
    ED["a3-engine deckD_* (?) mapped to StemDeck-D, not running"]
  end
  SA -->|"41 JACK links"| EA
  SB -->|"(?) 41 links"| TB
  SC -->|"41 links"| TC
  TB -->|"RTP 239.69.150.245:5004"| RB
  TC -->|"RTP 239.69.150.246:5004"| RC
  TB -.->|"announce"| SAPG
  TC -.->|"announce"| SAPG
  SAPG -.->|"rule ~^AES67 deck"| RB
  SAPG -.->|"rule ~^AES67 deck"| RC
  RB -->|"MAIN→deckB_n · AUX→deckB_aux_n · CUE→deckB_cue_n"| EB
  RC -->|"MAIN→deckC_n · AUX→deckC_aux_n · CUE→deckC_cue_n"| EC
```

Sources: live `pw-link -l` on a3nuc1 and a3nuc2; live `~/.config/pipewire/pipewire-aes67.conf` (a3nuc1),
`pipewire-aes67-deck-C.conf` (a3nuc2), `pipewire-aes67-deck-B.conf` (a3motionV02); template
`a3-stemdeck/tools/pipewire-aes67-deck.conf.in` (`sess.latency.msec = 1`, 41 channels); live
`engine.json` `io.jack` (deckA-D maps); truth `aes67_streams.deck` (group base .244, step 1);
`a3-doc/src/ressources/aes67.md`.

---

## 4. Core engine inputs and channel strips

Four channels (N = 4 on the rig); each selects one source: its analog pair or a deck slot. Analog
goes through the stereo strip and is encoded at the channel's position (moving band) plus the shared
steady bed; a deck's 16 B-format channels go through the 16-channel deck strip and are added to the
bus directly. AUX sends feed `enc_fx` and the beat-synced DualDelay, whose output is the FX Return.

```mermaid
flowchart LR
  subgraph INP["a3-engine inputs"]
    AN["analog_1..8 (Scarlett capture 1-8)"]
    ANX["analog_9..12 (not linked)"]
    DKB["deckX_1..16 (B-format), X = A..D"]
    DKA["deckX_aux_1..16"]
  end
  AN -->|"pairs 1/2, 3/4, 5/6, 7/8 → ch 1-4"| SEL["ChannelSelect per channel: analog pair or deck k (channel.source)"]
  DKB --> SEL
  SEL -->|"analog"| CST["ChannelStrip: TRIM → 3-band EQ → DJ filter → 3D band (Isolator3) → VOLUME"]
  SEL -->|"deck k"| DST["DeckStrip 16 ch: TRIM → EQ → SVF filter → VOLUME"]
  CST -->|"moving, at azimuth/elevation"| AEB["AmbiEncoderBus (IEM MultiEncoder, order 3)"]
  CST -->|"steady → bed sources"| AEB
  AEB --> EMAIN["enc_main (16 ch)"]
  DST -->|"16 ch post-VOLUME, added directly"| EMAIN
  CST -->|"× AUX send"| EFX["enc_fx"]
  DST -->|"× AUX send"| EFX
  DKA --> DST2["2nd DeckStrip on the channel's controls, VOLUME at unity"]
  DST2 --> EFX
  EFX --> DDL["IEM DualDelay, 2nd order: BEAT · FEEDBK · COLOR · SPREAD"]
  DDL --> RET["FX Return × RETURN"]
  CST -.->|"pre-VOLUME / post-VOLUME taps"| EPH["enc_phones (block 6)"]
  DST -.->|"pre-VOLUME / post-VOLUME taps"| EPH
```

Sources: `a3-core/PROGRAM.md` (Plan 4a: Channels, Buses, FX Return, delay page, Orders), `src/a3-engine/Engine.h`
(graph comment), `ChannelStrip.h`, `DeckStrip.h`, `AmbiEncoderBus.h`; live `engine.json` (`channels 4`,
`analogPairs [1,2,3,4]`, `analogInputs 12`, `filterKind svf`); live `pw-link -l` (only `analog_1..8` linked).
A deck channel ignores positions, 3D, FREQ and Q (PROGRAM.md). The dashed taps into `enc_phones` are
audio drawn dashed only to keep this block readable; block 6 draws them solid.

---

## 5. Core spatial mixing and outputs

`enc_main` plus the FX Return feeds three decoders: main and booth (IEM SimpleDecoder, AllRAD 4.1,
3rd order) and rec (IEM BinauralDecoder, 2nd order). Main and booth pass MASTER/BOOTH, then the
calibration trim and gate; every output port goes both to the Scarlett (where mapped) and to its own
AES67 stream.

```mermaid
flowchart LR
  EMAIN["enc_main (order 3, 16 ch)"] --> BUS["main bus = enc_main + FX Return"]
  RET["FX Return"] --> BUS
  BUS --> DMAIN["SimpleDecoder main: tops ±45°, ±135°, sub on ch 1 (150 Hz)"]
  BUS --> DBOOTH["SimpleDecoder booth: same 4.1 layout"]
  BUS --> DREC["BinauralDecoder rec (2nd order)"]
  DMAIN --> MAS["MASTER (master.volume)"]
  DBOOTH --> BOO["BOOTH (master.booth)"]
  MAS --> TMAIN["trim main −30 dB + gate"]
  BOO --> TBOOTH["trim booth −30 dB + gate"]
  DREC --> TREC["trim rec 0 dB, never gated"]
  TMAIN --> PMAIN["main_sub, main_top_1..4"]
  TBOOTH --> PBOOTH["booth_sub, booth_top_1..4"]
  TREC --> PREC["rec_L, rec_R (block 7)"]
  PMAIN -->|"playback 1-5 (sub, T1-T4)"| SCAR["Scarlett 18i20 outputs"]
  PMAIN --> SMAIN["AES67 Core MAIN · 5 ch SUB,T1-T4 · 239.69.200.1"]
  PBOOTH --> SBOOTH["AES67 Core BOOTH · 5 ch · 239.69.200.2"]
  PBOOTH -.->|"no analog output linked"| NOB["booth speakers (?)"]
  SCAR --> PA["PA main 4.1 (?)"]
```

Sources: `PROGRAM.md` (Outputs, Orders, Gate), `Engine.h`, `Engine.cpp` `decode()` (busMain += busFx;
main/booth/rec from busMain); `data/spatial/main.decoder.json` and `booth.decoder.json` (loudspeakers at
az 45, −45, −135, 135, el 0, on decoder channels 2-5; imaginary ±90° el), `main.parameters.json`
(`swMode 1`, `swChannel 1`, low/high pass 150 Hz), `variant.json` ("Default 4.1"); live `engine.json`
(`trimsDb` main −30, booth −30, phones 0, rec 0; `spatial` both `/usr/share/a3-engine/spatial`); live
`pw-link -l` (main → `playback_AUX0..4`, booth only → `rtp-sink-core-booth`); live a3nuc1
`pipewire-aes67.conf` (Core senders: 5/5/2/2 ch, ptime 0.5 ms, sess.latency 3 ms, S24BE).

---

## 6. Cue and phones path

The phones bus collects each channel's pre-VOLUME tap (when its CUE is on) and post-VOLUME tap,
weighted by the CUE↔MIX knob, the delay's output (with RETURN on the mix side, and as a PFL when the
return's cue is on), and every deck's 9-channel stem cue. One 2nd-order BinauralDecoder renders it;
the headphone EQ is off on the rig.

```mermaid
flowchart LR
  subgraph DECKS["StemDeck-A..D"]
    SCUE["cue_1..9 (cued stems, ACN 0..8, pre-mute)"]
  end
  SCUE -->|"deckX_cue_1..9, local or AES67 CUE1..9"| WSC["× cueWeight (CUE↔MIX), on a channel or not"]
  CHPRE["channel pre-VOLUME tap"] -->|"channel.cue on"| WCUE["× cueWeight"]
  CHPOST["channel post-VOLUME tap"] --> WMIX["× mixWeight"]
  DDL["DualDelay output"] --> WRET["× (RETURN × mixWeight + cueWeight if aux-return.cue)"]
  WSC --> EPH["enc_phones (order 3; decoder reads ACN 0..8)"]
  WCUE --> EPH
  WMIX --> EPH
  WRET --> EPH
  EPH --> BDEC["BinauralDecoder phones, 2nd order, KU100 HRIR, phonesHeadphoneEq off"]
  BDEC --> PHV["PHONES (master.phones-volume)"]
  PHV --> PHT["trim phones 0 dB + gate"]
  PHT --> PPH["phones_L, phones_R"]
  PPH -->|"playback 9-10"| SCAR["Scarlett 18i20"]
  PPH --> SPH["AES67 Core PHONES · 2 ch · 239.69.200.4"]
  SCAR --> HP["Headphones (?)"]
```

Sources: `Engine.h` (enc_phones and phones lines), `Engine.cpp` (`addStemCues`, cue/mix/returnCue weights),
`PROGRAM.md` (Stem cue R13, Orders: headphone decoders 2nd order, KU100 data), `EngineConfig.h`
(`phonesHeadphoneEq` "off" or an IEM headphone model); live `engine.json` (`phonesHeadphoneEq: "off"`,
phones → `system:playback_9/10`); live `pw-link -l` (`phones_L/R` → `playback_AUX8/9` and
`rtp-sink-core-phones`); truth (`channel.cue`, `master.phones-mix`, `master.phones-volume`, `aux-return.cue`).

---

## 7. REC path

`rec_L/R` (the binaural rec decoder, block 5) fans out to five places: the Scarlett, StemDeck-A's
recorder, the beat-analyzer's tempo input (left only), the legacy 12-channel `AES67 a3nuc1 out`
stream (CH1/CH2, the one the deck hosts receive for their recorders) and the `AES67 Core REC` stream.

```mermaid
flowchart LR
  PREC["a3-engine rec_L / rec_R"]
  PREC -->|"L and R both onto playback 11"| SCAR["Scarlett 18i20 out 11"]
  SCAR --> ARC["Analog recorder (?)"]
  PREC --> SDA["StemDeck-A rec_L/R → FLAC"]
  PREC -->|"rec_L only"| BAN["beat-analyzer:bpm_1"]
  PREC -->|"built-in link → CH1/CH2"| TXO["rtp-sink 'AES67 a3nuc1 out' · 12 ch · 239.69.150.243 · sess.latency 3 ms"]
  PREC --> TXR["rtp-sink-core-rec 'AES67 Core REC' · 2 ch · 239.69.200.3"]
  TXR -.-> NOR["receiver (?) none found"]
  subgraph HC["a3nuc2"]
    RXC["AES67 a3nuc1 out · receive_CH1/2 · sess.latency 12 ms"] --> SDC["StemDeck-C rec_L/R → FLAC"]
  end
  subgraph HB["a3motionV02"]
    RXB["AES67 a3nuc1 out (receiver)"] -.->|"(?) StemDeck-B stopped"| SDB["StemDeck-B rec_L/R"]
  end
  TXO -->|"RTP multicast"| RXC
  TXO -->|"RTP multicast"| RXB
```

Sources: live `pw-link -l` on a3nuc1 (`rec_L/R` → `StemDeck-A:rec_L/R`, `playback_AUX10`, `beat-analyzer:bpm_1`,
`rtp-sink:send_CH1/2`, `rtp-sink-core-rec:send_L/R`) and on a3nuc2 (`AES67 a3nuc1 out:receive_CH1/2` →
`StemDeck-C:rec_L/R`); live `pw-top` on a3motionV02 (`AES67 a3nuc1 out` node present, nothing linked);
`PROGRAM.md` (built-in links P40/P46, beat-analyzer link, P39); live `engine.json` (`rec_L`, `rec_R` →
`system:playback_11`); `a3-stemdeck/tools/pipewire-stemdeck-aes67.conf.in` (rule `~ out$`, 12 ms);
`a3-stemdeck/Source/Recorder.h`.

---

## 8. Clock and sync

One sample clock: the Scarlett drives a3nuc1's graph; `a3-core --role clock` steers the audio port's
PTP hardware clock to it, ptp4l on the Core serves it as grandmaster, and the deck hosts' PipeWire
graphs are driven by `PTP0-Driver` from their PTP-locked clocks. The beat clock (BTrack on the rec
signal) and StemDeck's Pro DJ Link are tempo, not sample clock.

```mermaid
flowchart LR
  subgraph N1["a3nuc1"]
    SCAR["Scarlett 18i20 (ALSA driver) · quantum 64 @ 44100 Hz"]
    PROF["pw-profiler -J (10 ms records)"]
    CLK["a3-clock: --role clock · LOCKED"]
    PHC["PHC /dev/ptp0 on enp5s0"]
    PTPM["ptp4l@enp5s0 · MASTER · free_running"]
    G1["engine, StemDeck-A, receivers, senders follow the Scarlett"]
    BAN["beat-analyzer (BTrack)"]
    CORE["Core tempo follower"]
    ENGD["engine DualDelay tempo"]
  end
  subgraph N2["a3nuc2 / a3motionV02"]
    PTPS["ptp4l@enp5s0 / ptp4l@eth0"]
    PTPD["PTP0-Driver · clock.system.ptp0 · resync 1.5 ms · quantum 64 @ 44100"]
    DECK["aes67-deck-c / -b, StemDeck-C, AES67 a3nuc1 out receiver"]
    SDT["StemDeck: Pro DJ Link (tempo master option)"]
  end
  RECL["a3-engine rec_L"] -->|"bpm_1 (audio)"| BAN
  SCAR -.->|"driver clock records"| PROF
  PROF -.-> CLK
  CLK -.->|"clock_adjtime ADJ_FREQUENCY"| PHC
  PHC -.-> PTPM
  SCAR -.->|"drives graph"| G1
  PTPM -.->|"PTP 224.0.1.129 :319/:320"| PTPS
  PTPS -.-> PTPD
  PTPD -.->|"drives graph"| DECK
  BAN -.->|"/beat"| CORE
  SDT -.->|"/stemdeck/deck/tempo"| CORE
  CORE -.->|"/delay/bpm (?) inputs"| ENGD
  SDT -.->|"prolink :50000-50002"| PDJ["Pro DJ Link network"]
```

Sources: `PROGRAM.md` ("The one clock: --role clock", "Block on PipeWire"); live a3nuc1
`$XDG_RUNTIME_DIR/a3/clock.json` (`master scarlett-ptp`, `health locked`, `frequencyPpm 14.37`,
`errorNs 594`) and `/run/a3/ptp-state.json` (`MASTER`); live `pw-top` (a3nuc1: Scarlett input node drives
at quantum 64, PTP0-Driver idle; a3nuc2 and a3motionV02: PTP0-Driver drives at 64); live
`pw-metadata` (all three: `clock.rate 44100`, `clock.quantum 64`, `force-quantum 0`); live
`pipewire-stemdeck-aes67.conf` (PTP0-Driver, `resync.ms 1.5`); `pgrep ptp4l` on the deck hosts; live
`20-a3-profiler.conf`; truth (`ptp4l.event/general`, `beat`, `stemdeck.tempo`, `delay.bpm`,
`prolink.*`, `clockmode`); `CLAUDE.md` (beat-analyzer clock modes 0/1/2).

---

## 9. Control paths that move audio parameters (OSC, not audio)

Every controller talks only to Core (`core.osc`, UDP 9000); Core passes what the engine needs on
`engine.osc` (loopback 9004) and switches StemDeck instances on `stemdeck.osc` (7780 + deck − 1).
Positions only move analog channels; a deck's movement is StemDeck's own.

```mermaid
flowchart LR
  MIX["A³ Mixer"] -.->|"gain, eq, volume, aux-send, cue, filter, master.*"| CORE["Core :9000"]
  DESK["desk / pro-DJ apps"] -.->|"same words, channel.stem.push"| CORE
  MOT["Motion UI"] -.->|"azimuth, elevation, 3d, filter freq/q"| CORE
  CORE -.->|"engine.osc :9004: strips, positions, channel.source, delay.*, engine.open"| ENG["a3-engine"]
  CORE -.->|"stemdeck.osc 7780 + k−1: stemdeck.3d, bus switches"| SDK["StemDeck-A..D"]
  ENG -.->|"engine.hello, deck audio state"| CORE
  ENG -.->|"/vu bundles → core.vu-relay :9003"| CORE
  CORE -.->|"/vu, lamps, relays"| MIX
  CORE -.->|"/vu, relays"| MOT
```

Sources: truth `a3-osc.json` (`listeners`, `routes`, `addresses`: `channel.*`, `master.*`,
`channel.azimuth/elevation/3d` from motion, `channel.source`, `aux-return.delay.*`, `engine.open`,
`engine.hello`, `engine.deck-audio`, `stemdeck.3d`, `stemdeck.bus`); `PROGRAM.md` (positions on
`engine.osc` 9004; deck channel ignores positions/3D/FREQ/Q; /vu meters).

---

## Latency budget

| Stage | Value | Kind | Source |
|---|---|---|---|
| PipeWire block, all three hosts | 64 frames @ 44.1 kHz = 1.45 ms | configured | live `pw-metadata`, `engine.json` `blockSize 64` |
| Core digital round trip (Scarlett S/PDIF loop) at Block 64 | 212 samples = 4.8 ms | measured (2026-11-06) | `PROGRAM.md` "Block on PipeWire" |
| same at Block 128 (before) | 343 samples = 7.8 ms | measured | `PROGRAM.md` |
| Deck sender (B, C) | `sess.latency.msec` 1 ms, packet 0.25 ms | configured | live deck-B/C confs, template |
| Core deck receiver | `sess.latency.msec` 4 ms (2 and 3 ms crackled at Block 64) | configured | live a3nuc1 conf, `PROGRAM.md` |
| Deck → Core, calculated | 7.3 ms | calculated, assumes a 3 ms sender | `PROGRAM.md` STATUS row |
| Core senders (MAIN/BOOTH/REC/PHONES, `out`) | `sess.latency.msec` 3 ms, packet 0.5 ms | configured | live a3nuc1 conf |
| Deck host receive of `AES67 a3nuc1 out` | `sess.latency.msec` 12 ms | configured | live a3nuc2 / a3motionV02 conf |
| Deck → Core end to end, Core → booth | — | not measured | — |

---

## Open points

1. **Deck B audio**: `stemdeck@B` was inactive on a3motionV02 at read time (sender `a3-aes67-deck@B` and
   `stemdeck-aes67` active). Its links into `aes67-deck-b` and from `AES67 a3nuc1 out` are assumed to
   match deck C's.
2. **Deck D**: `engine.json` maps `deckD_*` to a local `StemDeck-D` on a3nuc1; no such client ran, and
   which host would play deck D was not checked.
3. **What is plugged into the Scarlett**: the port mapping is verified (capture 1-8 → analog_1..8;
   out 1-5 main, 9-10 phones, 11 rec, 12 round-trip loop), but the PA, headphones, analog recorder and
   analog sources behind them are not.
4. **Booth**: no analog output is linked (`booth_*` only to `AES67 Core BOOTH`), and neither deck host
   receives any `AES67 Core *` stream. Accepted for now: the booth is not used in the home setup.
5. **Deck internals**: whether a one-deck instance applies a deck fader, and whether MUTE also acts on
   the AUX and cue buses (the cue is pre-mute by design), was not checked in code.
6. **Core's tempo follower**: which inputs it uses for `/delay/bpm` (`/beat` from the analyzer, deck
   tempo, or both) was not read.
7. **analog_9..12**: the engine has 12 analog inputs, only 1-8 are linked. The stale `return stereo`
   row was removed from `aes67.md`.
8. **rec on one output**: `rec_L` and `rec_R` both go to Scarlett out 11 (L+R summed), verified live
   and in `engine.json`; the maintainer corrects this in the engine configuration.
9. **Small source drifts**: the live round-trip loop is channel 12/12 (`PROGRAM.md` names 11 as the
   default); `PROGRAM.md`'s 7.3 ms deck-to-Core calculation assumes a 3 ms sender while the shipped and
   live sender is 1 ms; `PROGRAM.md` puts MASTER after the decoder, `Engine.h` before (linear gain, no
   audible difference).
10. **Mermaid syntax**: no Mermaid CLI is installed locally (`mmdc` absent; adding it would be a new
    dependency), so the diagrams were checked by eye only.
