# A³ Mixer

- [A³ Mixer Repository](https://github.com/a3-audio/a3-system)
- Standalone OSC controller, four channels
- Input VU meter per channel, eight output VU meters

A³ Mixer is a DJ mixer that makes no sound: every control sends OSC to A³
Core, and Core does the audio. That is why the same values appear on A³
Motion's MIX page and move when you turn them here — there is one state and
every device is told all of it.

![A³ Mixer numbered](pics_user/a3-mix-icon_light_numbered.png)

The numbers below refer to that picture. It is older than the V02 panel: FX
SEND and AUX RETURN are real knobs on the device but have no place in the drawing,
so they are listed without a number.

## The channel strip

Four identical strips, top to bottom in the order a signal passes through
them.

| № | Control | What it does | Range |
| :--- | :--- | :--- | :--- |
| – | **AUX SEND** | one per channel: how much of it goes to the tape delay on the FX bus, which follows the beat. Not in the picture | −inf … 0 dB |
| 1 | **TRIM** | the level of the signal coming in | −inf … 0 dB |
| 2 | **EQ HIGH** | high band | −inf … 0 dB (24 kHz) |
| 3 | **EQ MID** | middle band | −inf … 0 dB (1 kHz) |
| 4 | **EQ LOW** | low band | −inf … 0 dB (20 Hz) |
| 5 | **INPUT VU** | the level *before* the fader (`in1_pre` … `in4_pre` in the {ref}`meter map <core-vu-map>`) |  |
| 6 | **TAP** | taps the tempo — see *Tempo* below. All four strips' keys do the same, and their lamps flash red on the beat |  |
| 7 | **FADER** | the level going out | −inf … 0 dB |
| 8 | **FX** | switches this channel's VCF filter on. Lit green while it is on |  |
| 9 | **CUE** | puts this channel on the headphones: opens its cue send, taken before the fader (see *The cue* below). Lit blue while it is on |  |

```{note}
Until 2026-09-12 the AUX SEND knob did something else entirely: it drove the **3D
blend** — how far the channel was spread into the room — because it was the
only continuous control the desk had for that. A³ Motion's per-channel pot
took that job over, and the knob got its own name back.

The price, named: the desk has no 3D control any more. The 3D blend is A³
Motion's pot, and only that.
```

```{note}
**The keys were rearranged on 2026-09-19.** Key 9 used to be **3D**; on
2026-09-12 its job moved to A³ Motion's per-channel pot, where 3D is a blend
rather than a switch, and the key was left without one. It carries the cue
now, because its blue lamp is the bright one and a cue lamp has to be
readable in the dark. Key 6, where CUE used to be, has the dim red lamp and
carries the tap, which only flashes.
```

## The filter section

One filter, shared by all four channels; the **FX** key on a strip decides
which channels go through it.

| № | Control | What it does |
| :--- | :--- | :--- |
| 10 | **FREQUENCY** | the cutoff |
| 11 | **RESONANCE** | the Q, or sharpness, at the cutoff |
| 12 | **HPF** | high-pass: lets what is above the cutoff through |
| 13 | **LPF** | low-pass: lets what is below the cutoff through |

The section's lamp shows which mode is on: blue for HPF, green for LPF.

## Tempo

| № | Control | What it does |
| :--- | :--- | :--- |
| 6 | **TAP** | taps the tempo, the same as A³ Motion's TAP key — on the press, not the release |

It goes **straight to the beat-analyzer**, not through A³ Core: a tap is
timing, and timing does not want a relay in the middle. Until 2026-09-12 it
went to Core, which had never subscribed to it — the key worked, the message
left the desk, and nothing happened at the other end.

## Monitoring and outputs

| № | Control | What it does | Range |
| :--- | :--- | :--- | :--- |
| 14 | **HEADPHONE LEVEL** | the headphone output |  |
| 15 | **CUE/MIX** | the phones-mix knob: left is cue only, right is the mix, in between a crossfade at constant power (see *The cue* below) |  |
| 16 | **BOOTH** | the monitor outputs | −inf … 0 dB |
| 17 | **MASTER** | the public address outputs | −inf … 0 dB |
| – | **AUX RETURN** | the level of the aux return — the fifth stereo input beside the four channels, where an external effect comes back into the mix (the gain on REAPER's *Return* track). Not in the picture | 0 dB at full travel |
| 18 | **DISPLAY** | BPM for the master and per input channel — work in progress |  |
| 19 | **OUTPUT VU** | the level of eight main outputs: the sub and tops 1–7 (`main_sub`, `main_top1` … `main_top7`) |  |

(a3mix-cue)=

## The cue

The cue used to be called PFL (pre-fader listen); since 2026-10-01 it is the
cue everywhere, on the desk, on A³ Motion's key and on the wire
(`/channel/{ch}/cue`).

What the headphones hear is set in the REAPER project, in the sends of the
channel buses, not on separate tracks. Each channel bus sends to
`enc_phones` twice: send 3 is taken **before** the fader (the cue), send 4
**after** it (the mix). The **CUE/MIX** knob crossfades the two at constant
power, cue on the left, mix on the right. A deck's cue send opens only while
its cue key is on; the mix sends follow the knob alone.

A channel's cue is its **CUE** key on the desk, or the CUE key on A³ Motion,
and nothing else: the encoder push no longer touches it. **The cue plays what
comes in on the channel:**

- **With a stem on the channel**, Core switches that stem's **C** (CUE) switch
  in StemDeck and keeps the channel's own cue send (channel bus send 3) shut.
  The stem is heard once, dry, from StemDeck's CUE bus, before the fader.
  Push another stem onto the channel while it is cued and the C moves with it.
  Core overrides C clicks on StemDeck's own screen while this holds.
- **With A on the channel** it is the normal channel cue, and all of
  StemDeck's C switches are off.

The **return's cue send opens on the cue side while any deck cue is on**, so a
cued deck brings its FX along.

Two more things reach the headphones, on `dec_phones`:

- **StemDeck's own CUE bus.** Core keeps this send always open, on the cue
  side of the crossfade. What is on the bus is StemDeck's decision: a stem's CUE
  switch, or a deck's PHONES/CUE button on StemDeck, which puts the whole deck
  there before the fader. It is heard through StemDeck's headphone bus
  (REAPER inputs 23–24). That is how you pre-listen a stem that is on no
  channel.
- **The analog phones** (REAPER inputs 11–12) always go to `dec_phones`, with
  no switch.

(a3mix-displays)=

## The stem displays

The desk remote-controls [StemDeck](stemdeck.md) through A³ Core. StemDeck has
two decks with four stems each, eight stems in all. Each stem has six bus
switches in StemDeck: buses 1–4 (they feed the desk's channels 1–4), AUX
(the aux return) and CUE (StemDeck's headphone bus). **StemDeck owns these
switches**; Core only relays what the desk asks for and what StemDeck reports.

The desk has five small OLED displays: one for each channel 1–4 and one for
the aux return. Together they show StemDeck's eight stems — deck A's stems 1–4
in the top row, deck B's stems 1–4 in the bottom row — and a fifth field at the
bottom right.

![The five stem displays, scaled up three times: channels 1 to 4, then the aux return](pics_user/a3-mix-stem-displays.png)

*Left to right: channels 1–4, then the return. Channel 1 has stem A1 (●) with
its frame on it. Channel 2 plays B2 (■) while its frame rests on the free A4.
Channel 3 plays A3 (▲), framed. Channel 4 plays its analog input (◆ in the A
field), framed. The return has B3 (★), framed.*

**Symbols, not numbers.** Every place owns a symbol: channel 1 is ● (circle),
2 is ■ (square), 3 is ▲ (triangle), 4 is ◆ (diamond), the aux return is ★
(star). A stem's field shows the symbol of the place where that stem plays, or
nothing when it plays nowhere. There are no labels and no digits. Under each
stem field a small level bar shows that stem's level (the `/vu/41`–`/vu/48`
meters StemDeck sends).

**The fifth field.** On a channel display it is the channel's analog input,
**A**: it shows the channel's own symbol while the channel plays its analog
input. On the aux-return display it is an empty field, meaning no stem on the
return.

- **Turn a channel's encoder** to move the frame — the selected field is drawn
  filled white — over **A** and the stems that are not playing anywhere else.
  Nothing switches while you turn.
- **Push the encoder** to load the selection onto the channel. StemDeck
  switches that stem onto the channel's bus and the previous one off. **A**
  takes every stem off the channel, and the analog input plays.
- **One input per channel, and a stem is in one place only**: never on two
  channels, and never on a channel and the return. While a stem is on a
  channel, Core shuts that channel's analog input.
- **The aux return works like a fifth channel.** Turn to select a stem or the
  empty field; push puts exactly that one stem on the return (its AUX switch in
  StemDeck) and the previous one leaves. The empty field takes every stem off
  the return.
- **No C field.** A channel's cue is its CUE key (see {ref}`the cue <a3mix-cue>`).
- Core holds the four channels' selections and the return's, keeps them across
  a restart and announces them. Without StemDeck, turning still moves the
  frame, a push does nothing and every channel shows A.
- A fresh StemDeck starts with every stem on AUX only, so every channel shows
  **A** until you load a stem; a session saved earlier restores its own
  switches.

The desk shows what StemDeck reports, so a click on a bus switch on StemDeck's
own screen shows on the desk too.

StemDeck says hello to Core every 30 seconds. If it is silent for a minute,
Core shows **A** on every channel and the analog inputs play again; Core
notices at the next hello of any device, which the desk sends every 30 seconds,
so it can take up to about 90 seconds.

## Connectors

| Where | Socket | For |
| :--- | :--- | :--- |
| Front | **PHONES OUT** | headphones, 6.3 mm stereo jack |
| Back | **PHONES IN** | the cue outputs coming back, 2× female XLR |
| Back | **ETHERNET** | the PoE switch — power and every message, on one cable |

## A³ Mix Specification

Shipping revision, V02:

- PoE, 24 W max
- Raspberry Pi 3B and Teensy 4.1
- A³ Mixer Mainboard PCB V02

**V03 is in development** and replaces that pair with a single Raspberry Pi
Pico with Ethernet (WIZnet W5500-EVB-Pico), plus USB-C, 45 mm faders and a
6.3 mm front jack. See
[Configuration](https://a3-audio.github.io/a3-doc/configuration/mic.html).
