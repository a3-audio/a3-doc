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
| `AES67 Core MAIN` | 239.69.200.1:5004 | 0.5 | n + 1 |
| `AES67 Core BOOTH` | 239.69.200.2:5004 | 0.5 | n + 1 |
| `AES67 Core REC` | 239.69.200.3:5004 | 0.5 | 2 |
| `AES67 Core PHONES` | 239.69.200.4:5004 | 0.5 | 2 |
<!-- /a3-osc:aes67 -->

- `{host}` is the sending machine's hostname, `{deck}` the deck letter. A
  deck's group is the base address plus one per deck slot (A = `.244`, B =
  `.245`, and so on).
- **A zone stream** (`AES67 Core MAIN`, `AES67 Core BOOTH`) carries the zone's
  `n` loudspeakers and its sub, if it has one: `n + 1` channels with a sub
  (**sub first**: SUB, T1..Tn), `n` without (T1..Tn). The packaged default
  layout is 4.1, so 5 channels. `REC` and `PHONES` carry two channels, L R.
- **A deck stream** has 41 channels: MAIN1-16, AUX1-16, CUE1-9.
- A packet must fit an MTU of 1500: at most 22 channels at 0.5 ms, 44 at
  0.25 ms.

## Finding a stream

Streams are announced with SAP/SDP on `239.255.255.255`, port 9875. PipeWire's
`module-rtp-sap` both announces and discovers them. The clock is PTP on the
audio network.

Which announced streams a receiver turns into sources depends on its
`module-rtp-sap` config:

- **No explicit `stream.rules`**: PipeWire creates a source for every announced
  stream.
- **Explicit rules**: only the sessions they match. The A3 rig's own configs
  list rules (they match `~^AES67 deck ` and `~ out$`), so they ignore the
  `AES67 Core` streams. A host that should receive them needs one more rule in
  its `stream.rules`:

```text
{ matches = [ { rtp.session = "~^AES67 Core " } ]
  actions = { create-stream = { node.virtual = false media.class = Audio/Source device.api = aes67 } } }
```

## Where a receiver patches it

The Core receives streams as input ports of the engine. They are not linked
for you: patch them by hand in qjackctl or Helvum.

| Stream received | Engine input ports |
| :--- | :--- |
| `deck X B-format` | `deckX_1` ... `deckX_16` |
| `deck X return B-format` | `deckX_aux_1` ... `deckX_aux_16` (these feed the delay) |
| `analog 1-2`, `analog 3-4`, ... | `analog_N`, `analog_N+1` for a pair N, N+1 |

```{warning}
The `analog_N` ports are **shared with the sound card's capture ports**. A
stream patched onto them adds to whatever the card delivers on the same
channel; it does not replace it.
```

(aes67-stereo-deck)=

## A deck in stereo mode

A deck set to **Output: Stereo** ({ref}`StemDeck settings <stemdeck-output-mode>`)
does not send the 41-channel stream. It sends **one stereo master pair** as
a **2-channel** stream, named like the full one (`AES67 deck <X>`), with its
channels called `MASTER_L` and `MASTER_R`. A receiver sees them as
`receive_MASTER_L` and `receive_MASTER_R`.

Every deck slot of the Core has its own pair of inputs for it,
`deckX_stereo_L` and `deckX_stereo_R`, beside its B-format inputs. The link
map links them from the slot's source, the same source as its B-format: the
local StemDeck's `master_L`/`master_R`, or the stream's
`receive_MASTER_L`/`receive_MASTER_R`.

| Deck | Left | Right | Core input |
| :--- | :--- | :--- | :--- |
| A (local StemDeck) | `StemDeck-A:master_L` | `StemDeck-A:master_R` | `deckA_stereo_L`, `deckA_stereo_R` |
| B (AES67 stream) | `AES67 deck B:receive_MASTER_L` | `AES67 deck B:receive_MASTER_R` | `deckB_stereo_L`, `deckB_stereo_R` |
| C, D, ... | the slot's source, as for A or B | | `deckX_stereo_L`, `deckX_stereo_R` |

No patching is needed. The links are made as soon as the deck is in stereo
mode and skipped while its ports do not exist. A link map saved before these
inputs existed gets them when it is loaded, from each slot's source. The pair
does not touch `analog_N`, so it never adds to the sound card's capture.

**How Core tells the modes apart:** by the links, not by the signal. A slot
whose stereo pair is linked and whose B-format inputs are not is in stereo
mode. A slot with both linked, or neither, is treated as B-format.

**On the desk** the deck keeps its letter on the channels'
{ref}`input selectors <a3mix-displays>`, as in B-format mode, and is picked
the same way. On a channel, its pair runs through that channel's strip
like an analog input: TRIM, the 3-band EQ, the DJ filter, the 3D band and
VOLUME, encoded at the channel's position. CUE and AUX-Send act on it as on
any analog input. A change of source, or of the deck's mode while it plays, is
smoothed over 10 ms. The deck's bar shows the middle of its pair.

```{note}
Core and A³ Motion still treat a channel playing a deck as a deck channel:
the channel's 3D, FREQ, Q and position are not sent while it plays a stereo
deck, so they stay where they were when the channel last played its own
analog input.
```
