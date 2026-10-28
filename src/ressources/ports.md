# Ports and endpoints

Every UDP port and who sends to it, rendered from `a3-osc.json`
({ref}`truth <osc-truth>`). Other pages name a port by its listener
(`core.osc`, `motion.vu`, …).

## Hosts

Named in `hosts`; see the [listener table](#ports-by-listener). On the rig A³
Motion runs **on the Core**, hence `127.0.0.1`; on its own machine
({ref}`hardware <moc-hardware>`) that machine's address replaces it.

## Cabling

The Core has two network sockets, each on a network of its own:

```text
router 192.168.8.1 ───── eno1    A³ Core 192.168.8.10/24    control network
A³ Mixer 192.168.8.11 ── router or switch, same network

StemDeck machine ─────── enp5s0  A³ Core 192.168.9.10/24    audio network (AES67, PTP)
```

- **First socket** (`eno1`): the Core's address, the gateway and the DNS
  server (`192.168.8.1`), file `10-a3.network`. OSC, the web window and the
  desk run here. The A³ Mixer reaches the Core over this network through the
  switch or router; the Core no longer sits between them.
- **Second socket** (`enp5s0`, optional): the audio network, file
  `20-a3-aes67.network`. Its own subnet `192.168.9.0/24`, Core
  `192.168.9.10/24`, **no gateway and no DNS**: the only way out is the first
  socket, and a reply always leaves by the socket it came in on.
- There is no `br0` bridge and no spanning tree any more (until 2026-10-14 the
  second socket was bridged with the first); a cable drop on one socket does
  not touch the other.
- Written by the package ({ref}`install <core-postinst>`); an upgrade retires
  the old bridge files.

(ports-audio-network)=

## The audio network: AES67 and PTP

Audio between machines runs on the second socket, apart from OSC:

| What | Detail |
| :--- | :--- |
| Socket, subnet | the second socket, `192.168.9.0/24`, Core `192.168.9.10/24` |
| Clock | PTP: `ptp4l` on the second socket, the Core as master unless a better clock is on the network |
| Core sends | **12 channels**, stream `AES67 <hostname> out`, 44.1 kHz, 24 bit, packet time 0.5 ms, **multicast** (`239.69.150.243`, port 5004) |
| Announcement | SAP on `239.255.255.255`, port 9875; receivers find the stream by its name |
| Who drives the stream | the audio interface: the samples leave unconverted and the engine is never pulled onto the PTP clock |
| Deck streams | one per deck, sent by the machine that runs the deck: **41 channels** (MAIN1–16, AUX1–16, CUE1–9), stream `AES67 deck <X>`, 44.1 kHz, 24 bit, packet time **0.25 ms** (1393 bytes on the wire, so every packet fits a 1500-byte frame), **multicast**, one group per deck (`239.69.150.244` deck A, `.245` deck B), port 5004 |
| Receive rule | the Core receives deck streams **outside** the PTP clock: the sound card stays the Core's clock and the stream is resampled into it, so a deck stream never pulls the engine. The receiver needs an MTU of 1500 |
| Deck host | a machine that runs a deck (a3nuc2 for deck B) runs its own sender, unit `a3-aes67-deck@<X>`, which the StemDeck package ships. The sender needs the package's base unit `stemdeck-aes67.service` (PTP client and receiver), which stays off where a3-core's own AES67 unit exists, and the audio socket from `STEMDECK_AUDIO_PORT`; the installer's deck-host role sets both up ({ref}`StemDeck <stemdeck-one-deck>`). The sender sends unconverted. It also receives the Core's stream, channels 1 and 2 of which are the REC bus |
| Latency | a deck on another machine arrives about 18 ms later than a local one (calculated, not measured). StemDeck's *path latency* setting ({ref}`StemDeck <stemdeck-one-deck>`) makes up for it |

**EEE is off** on the audio socket of every machine that has one, a deck host
included: with it on the link drops every minute or two.

PTP and the AES67 sender start only when a second socket is configured
(`audio-port`); without one the Core has neither and uses one network. The
streams are audio, not OSC, so they are not in the port tables below. Unit:
{ref}`a3-aes67 <core-aes67>`; the engine's JACK links: {ref}`I/O map <audio-engine-io>`.

(ports-by-listener)=

## Ports, by listener

Rendered: edit `a3-osc.json`, not this. `core.web` also serves
`GET /api/truth`. `devices.announce` is where Core broadcasts `/core/here` every
2 s for the devices that follow it. Host `any` (`0.0.0.0`): every interface;
`local`: this machine only.

<!-- a3-osc:ports -->
| Program | Role | Host | Port | Carries |
| --- | --- | --- | --- | --- |
| core | osc | any (0.0.0.0) | 9000 | every controller's messages, and /beat from the analyzer |
| core | vu-relay | local (127.0.0.1) | 9003 | the engine's and StemDeck's /vu bundles, forwarded unchanged to Motion, the mixer, radla, the remote Motion followed and every desk followed |
| core | web | any (0.0.0.0) | 9080 | the traffic window (HTTP, not OSC); every interface, decided 2026-09-30 |
| motion | osc | any (0.0.0.0) | 7771 | Core's relays (StemDeck's preview among them), /beat |
| motion | vu | any (0.0.0.0) | 7772 | Core's /vu bundles (the engine's meters, forwarded) |
| motion | energy | any (0.0.0.0) | 7777 | the IEM EnergyVisualizer's /EnergyVisualizer/RMS |
| stemdeck | osc | any (0.0.0.0) | 7780 | Core's bus switches and its request for all of them; a one-deck instance k (--deck A..D) listens on this port + (k - 1): A 7780, B 7781, C 7782, D 7783 (Core's deck relay sends deck k there); the two-deck StemDeck keeps 7780 |
| devices | announce | any (0.0.0.0) | 7790 | Core's /core/here broadcast: where every device fetches the truth |
| mixer | osc | mixer (192.168.8.11) | 7772 | Core's relays and lamps, /beat, /vu |
| desk | osc | any (0.0.0.0) | 7773 | Core's relays, lamps and stems, /beat -- every virtual desk Core follows (four at most) |
| desk | vu | any (0.0.0.0) | 7774 | the engine's and StemDeck's /vu bundles, forwarded unchanged by Core (core.vu-relay) |
| beat-analyzer | clock | any (0.0.0.0) | 7775 | /tap, /clockmode, and /beat from Motion in clock mode 0 |
| engine | control | local (127.0.0.1) | 9005 | the a3-core window's view of the engine (HTTP JSON, loopback only; not OSC) |
| engine | osc | local (127.0.0.1) | 9004 | a3-engine: Core's words in engine mode -- channel.gain/eq.*/volume/3d/filter.frequency/filter.q/aux-send/cue/filter/azimuth/elevation/source, filter.frequency/resonance/mode, master.*, aux-return.cue, delay.bpm, engine.open |
| x11vnc | vnc | any (0.0.0.0) | 5901 | the Core's screen (VNC, not OSC) |
| screencast | stream | any (0.0.0.0) | 9930 | the screen's picture as MPEG-TS, several viewers on one encode (OBS, the pro-DJ apps) (listener, not OSC) |
| radla | osc | radla (192.168.43.96) | 9000 | /beat |
| radla | vu | radla (192.168.43.96) | 9001 | /vu |
| prolink | announce | any (0.0.0.0) | 50000 | Pro DJ Link keep-alives (broadcast, not OSC) |
| prolink | beat | any (0.0.0.0) | 50001 | Pro DJ Link beat packets (broadcast, not OSC) |
| prolink | status | any (0.0.0.0) | 50002 | Pro DJ Link status packets (broadcast, not OSC) |
| aes67 | stream | aes67-core (239.69.150.243) | 5004 | the Core's 12 channels as AES67 (RTP, L24, 44.1 kHz, 0.5 ms packets), multicast on the audio socket; not OSC |
| aes67 | deck | aes67-deck-{deck} (239.69.150.244, 239.69.150.245) | 5004 | one deck's 41 channels: MAIN1-16, AUX1-16, CUE1-9 (L24, 44.1 kHz, ptime 0.25 ms), sess.name "AES67 deck <X>"; the receiver needs net.mtu = 1500 (the default 1280 truncates the 1365-byte RTP packet); not OSC |
| aes67 | sap | sap (239.255.255.255) | 9875 | AES67 stream announcements (SAP/SDP), multicast on the audio socket, every sender and receiver; not OSC |
| ptp4l | event | ptp (224.0.1.129) | 319 | PTP event messages; the Core is master on the audio socket; not OSC |
| ptp4l | general | ptp (224.0.1.129) | 320 | PTP general messages (announce, follow-up); not OSC |
<!-- /a3-osc:ports -->

(ports-routes)=

## Who sends where

The file's `routes`, rendered. *Carries*: the route's mark (`vu`: meters), else
what the listener takes. Sender `iem` is the IEM EnergyVisualizer, which no longer runs (see below);
`prolink`: any Pro DJ Link player; StemDeck as master has its own rows.

<!-- a3-osc:routes -->
| From | To | Carries |
| --- | --- | --- |
| mixer | `core.osc` | every controller's messages, and /beat from the analyzer |
| mixer | `beat-analyzer.clock` | /tap, /clockmode, and /beat from Motion in clock mode 0 |
| desk | `core.osc` | every controller's messages, and /beat from the analyzer |
| desk | `beat-analyzer.clock` | /tap, /clockmode, and /beat from Motion in clock mode 0 |
| prodj | `core.osc` | every controller's messages, and /beat from the analyzer |
| prodj | `beat-analyzer.clock` | /tap, /clockmode, and /beat from Motion in clock mode 0 |
| motion | `core.osc` | every controller's messages, and /beat from the analyzer |
| motion | `beat-analyzer.clock` | /tap, /clockmode, and /beat from Motion in clock mode 0 |
| core | `motion.osc` | Core's relays (StemDeck's preview among them), /beat |
| core | `motion.vu` | Core's /vu bundles (the engine's meters, forwarded) |
| core | `mixer.osc` | Core's relays and lamps, /beat, /vu |
| core | `desk.osc` | Core's relays, lamps and stems, /beat -- every virtual desk Core follows (four at most) |
| core | `desk.vu` | vu |
| core | `mixer.osc` | vu |
| core | `radla.vu` | /vu |
| core | `engine.osc` | a3-engine: Core's words in engine mode -- channel.gain/eq.*/volume/3d/filter.frequency/filter.q/aux-send/cue/filter/azimuth/elevation/source, filter.frequency/resonance/mode, master.*, aux-return.cue, delay.bpm, engine.open |
| core | `stemdeck.osc` | Core's bus switches and its request for all of them; a one-deck instance k (--deck A..D) listens on this port + (k - 1): A 7780, B 7781, C 7782, D 7783 (Core's deck relay sends deck k there); the two-deck StemDeck keeps 7780 |
| core | `devices.announce` | Core's /core/here broadcast: where every device fetches the truth |
| engine | `core.osc` | every controller's messages, and /beat from the analyzer |
| engine | `core.vu-relay` | vu |
| beat-analyzer | `core.osc` | every controller's messages, and /beat from the analyzer |
| beat-analyzer | `motion.osc` | Core's relays (StemDeck's preview among them), /beat |
| beat-analyzer | `mixer.osc` | Core's relays and lamps, /beat, /vu |
| beat-analyzer | `radla.osc` | /beat |
| iem | `motion.energy` | the IEM EnergyVisualizer's /EnergyVisualizer/RMS |
| stemdeck | `prolink.announce` | Pro DJ Link keep-alives (broadcast, not OSC) |
| stemdeck | `prolink.status` | Pro DJ Link status packets (broadcast, not OSC) |
| stemdeck | `prolink.beat` | Pro DJ Link beat packets (broadcast, not OSC) |
| stemdeck | `core.osc` | every controller's messages, and /beat from the analyzer |
| stemdeck | `mixer.osc` | vu |
| stemdeck | `core.vu-relay` | vu |
| prolink | `prolink.beat` | Pro DJ Link beat packets (broadcast, not OSC) |
<!-- /a3-osc:routes -->

- **Motion's energy listener has no sender.** `/EnergyVisualizer/RMS` came
  straight from the EnergyVisualizer plug-in inside REAPER, bypassing Core
  (`aside` in the register). REAPER is gone and the engine does not send it,
  so the listener stays open and nothing arrives (an open issue).
- **Core has two receive ports**: commands on `core.osc`, meters on
  `core.vu-relay`; **Motion three** (control, 25 Hz meters, 426-float energy frames).
- **`/tap` goes straight to the beat-analyzer**: timing wants no relay.
- **`radla`** is off this subnet, via the gateway: beat, meters, network audio.
- **Read a port with its host**: 7772 is both Motion's and the Mixer's meter
  port. A sending port is ephemeral and means nothing.

## The numbering, and what would be better

The numbers grew: `7771`, `7772`, `7775`, `7777` have three owners and two
gaps; `9000`–`9005` interleave Core and the engine; no number names its owner.
**Proposal** — the block names the owner:

| Block | Owner |
| :--- | :--- |
| `9000–9009` | A³ Core |
| `9010–9019` | Core's engine |
| `7700–7709` | A³ Motion |
| `7710–7719` | A³ Mixer |
| `7720–7729` | beat-analyzer |

with fixed offsets: `+0` control, `+1` VU, `+2` energy, `+5` beat clock.

**Not the current state.** The devices follow one edit of `a3-osc.json`, but
a half-done renumbering is silent. The tables above are what the rig does today.
