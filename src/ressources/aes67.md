(aes67-streams)=

# AES67 streams

Every audio stream the rig sends on the audio network, and where a receiver
patches it in. The table is rendered from `a3-osc.json`
({ref}`truth <osc-truth>`); the receiver section below is written by hand.
The audio network itself (second socket, PTP, EEE) is on the
{ref}`ports page <ports-audio-network>`.

## What is sent

All streams: 44.1 kHz, 24 bit, multicast, port 5004.

<!-- a3-osc:aes67 -->
| Stream | Group:port | Packet time (ms) | Channels |
| --- | --- | --- | --- |
| `AES67 {host} out` | 239.69.150.243:5004 | 0.5 | 12 |
| `AES67 deck {deck}` | 239.69.150.244 + slot:5004 | 0.25 | 41 |
| `A3 Core MAIN` | 239.69.200.1:5004 | 0.5 | n + 1 |
| `A3 Core BOOTH` | 239.69.200.2:5004 | 0.5 | n + 1 |
| `A3 Core REC` | 239.69.200.3:5004 | 0.5 | 2 |
| `A3 Core PHONES` | 239.69.200.4:5004 | 0.5 | 2 |
<!-- /a3-osc:aes67 -->

- `{host}` is the sending machine's hostname, `{deck}` the deck letter. A
  deck's group is the base address plus one per deck slot (A = `.244`, B =
  `.245`, and so on).
- **A zone stream** (`A3 Core MAIN`, `A3 Core BOOTH`) carries the zone's
  loudspeakers plus the sub: `n + 1` channels, **sub first**, then T1..Tn. The
  packaged default layout is 4.1, so 5 channels. `REC` and `PHONES` carry two
  channels, L R.
- **A deck stream** has 41 channels: MAIN1-16, AUX1-16, CUE1-9.
- A packet must fit an MTU of 1500: at most 22 channels at 0.5 ms, 44 at
  0.25 ms.

## Finding a stream

Streams are announced with SAP/SDP on `239.255.255.255`, port 9875. PipeWire's
`module-rtp-sap` both announces and discovers them, so a receiver needs nothing
but that module loaded. The clock is PTP on the audio network.

## Where a receiver patches it

The Core receives streams as input ports of the engine. They are not linked
for you: patch them by hand in qjackctl or Helvum.

| Stream received | Engine input ports |
| :--- | :--- |
| `deck X B-format` | `deckX_1` ... `deckX_16` |
| `deck X return B-format` | `deckX_aux_1` ... `deckX_aux_16` (these feed the delay) |
| `analog 1-2`, `analog 3-4`, ... | `analog_N`, `analog_N+1` for a pair N, N+1 |
| `return stereo` | `analog_11`, `analog_12` |

```{warning}
The `analog_N` ports are **shared with the sound card's capture ports**. A
stream patched onto them adds to whatever the card delivers on the same
channel; it does not replace it.
```
