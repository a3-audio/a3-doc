# Ports and endpoints

Every UDP port and who sends to it, rendered from `a3-osc.json`
({ref}`truth <osc-truth>`). Other pages name a port by its listener
(`core.osc`, `motion.vu`, …).

## Hosts

Named in `hosts`; see the [listener table](#ports-by-listener). On the rig A³
Motion runs **on the Core**, hence `127.0.0.1`; on its own machine
({ref}`hardware <moc-hardware>`) that machine's address replaces it.

## Cabling

The router has one free port, so the A³ Mixer hangs on the Core's **second
socket**, bridged with the first:

```text
router 192.168.8.1 ───── eno1   ┐
                                ├─ br0  A³ Core 192.168.8.10
A³ Mixer 192.168.8.11 ── enp5s0 ┘
```

- The address is on `br0` (`networkctl`: `br0` *routable*, sockets *enslaved*).
- STP on: forwarding starts about **30 s** after boot.
- **Core off, Mixer offline.**
- Written by the package ({ref}`install <core-postinst>`).

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
| core | reaper-feedback | local (127.0.0.1) | 9002 | REAPER's own OSC feedback |
| core | vu-relay | local (127.0.0.1) | 9003 | the analyzer's /vu bundles, forwarded unchanged to a remote Motion while one is followed (the analyzer needs OSC_VU_core=127.0.0.1:9003; Core renders it into the analyzer's conf.d, 50-a3-osc.env) |
| core | web | any (0.0.0.0) | 9080 | the traffic window (HTTP, not OSC); every interface, decided 2026-09-30 |
| motion | osc | any (0.0.0.0) | 7771 | Core's relays, /beat |
| motion | vu | any (0.0.0.0) | 7772 | the analyzer's /vu bundles |
| motion | energy | any (0.0.0.0) | 7777 | the IEM EnergyVisualizer's /EnergyVisualizer/RMS |
| stemdeck | osc | any (0.0.0.0) | 7780 | Core's bus switches and its request for all of them |
| devices | announce | any (0.0.0.0) | 7790 | Core's /core/here broadcast: where every device fetches the truth |
| mixer | osc | mixer (192.168.8.11) | 7772 | Core's relays and lamps, /beat, /vu |
| beat-analyzer | clock | any (0.0.0.0) | 7775 | /tap, /clockmode, and /beat from Motion in clock mode 0 |
| reaper | osc | local (127.0.0.1) | 9001 | Core's /track/... control |
| iem | multiencoder-1 | local (127.0.0.1) | 1337 | /MultiEncoder/... (receiver set inside the plug-in, in the REAPER project) |
| iem | multiencoder-2 | local (127.0.0.1) | 1338 | /MultiEncoder/... (receiver set inside the plug-in, in the REAPER project) |
| iem | multiencoder-3 | local (127.0.0.1) | 1339 | /MultiEncoder/... (receiver set inside the plug-in, in the REAPER project) |
| dualdelay | osc | local (127.0.0.1) | 1340 | /DualDelay/delayBPML\|R (receiver set inside the plug-in, in the REAPER project) |
| zita-n2j | audio | any (0.0.0.0) | 65100 | network audio from radla (10 channels, not OSC) |
| x11vnc | vnc | any (0.0.0.0) | 5901 | the Core's screen (VNC, not OSC) |
| radla | osc | radla (192.168.43.96) | 9000 | /beat |
| radla | vu | radla (192.168.43.96) | 9001 | /vu |
| radla | zita-n2j | radla (192.168.43.96) | 55100 | network audio from Core (zita-j2n, 2 channels, not OSC) |
| prolink | announce | any (0.0.0.0) | 50000 | Pro DJ Link keep-alives (broadcast, not OSC) |
| prolink | beat | any (0.0.0.0) | 50001 | Pro DJ Link beat packets (broadcast, not OSC) |
| prolink | status | any (0.0.0.0) | 50002 | Pro DJ Link status packets (broadcast, not OSC) |
<!-- /a3-osc:ports -->

(ports-routes)=

## Who sends where

The file's `routes`, rendered. *Carries*: the route's mark (`vu`: meters), else
what the listener takes. Sender `iem`: the EnergyVisualizer in REAPER;
`prolink`: any Pro DJ Link player; StemDeck as master has its own rows.

<!-- a3-osc:routes -->
| From | To | Carries |
| --- | --- | --- |
| mixer | `core.osc` | every controller's messages, and /beat from the analyzer |
| mixer | `beat-analyzer.clock` | /tap, /clockmode, and /beat from Motion in clock mode 0 |
| motion | `core.osc` | every controller's messages, and /beat from the analyzer |
| motion | `beat-analyzer.clock` | /tap, /clockmode, and /beat from Motion in clock mode 0 |
| core | `motion.osc` | Core's relays, /beat |
| core | `motion.vu` | the analyzer's /vu bundles |
| core | `mixer.osc` | Core's relays and lamps, /beat, /vu |
| core | `reaper.osc` | Core's /track/... control |
| core | `iem.multiencoder-1` | /MultiEncoder/... (receiver set inside the plug-in, in the REAPER project) |
| core | `iem.multiencoder-2` | /MultiEncoder/... (receiver set inside the plug-in, in the REAPER project) |
| core | `iem.multiencoder-3` | /MultiEncoder/... (receiver set inside the plug-in, in the REAPER project) |
| core | `dualdelay.osc` | /DualDelay/delayBPML\|R (receiver set inside the plug-in, in the REAPER project) |
| core | `stemdeck.osc` | Core's bus switches and its request for all of them |
| core | `devices.announce` | Core's /core/here broadcast: where every device fetches the truth |
| reaper | `core.reaper-feedback` | REAPER's own OSC feedback |
| beat-analyzer | `core.osc` | every controller's messages, and /beat from the analyzer |
| beat-analyzer | `motion.osc` | Core's relays, /beat |
| beat-analyzer | `mixer.osc` | Core's relays and lamps, /beat, /vu |
| beat-analyzer | `radla.osc` | /beat |
| beat-analyzer | `motion.vu` | the analyzer's /vu bundles |
| beat-analyzer | `core.vu-relay` | vu |
| beat-analyzer | `mixer.osc` | vu |
| beat-analyzer | `radla.vu` | /vu |
| iem | `motion.energy` | the IEM EnergyVisualizer's /EnergyVisualizer/RMS |
| zita-j2n | `radla.zita-n2j` | network audio from Core (zita-j2n, 2 channels, not OSC) |
| radla | `zita-n2j.audio` | network audio from radla (10 channels, not OSC) |
| stemdeck | `prolink.announce` | Pro DJ Link keep-alives (broadcast, not OSC) |
| stemdeck | `prolink.status` | Pro DJ Link status packets (broadcast, not OSC) |
| stemdeck | `prolink.beat` | Pro DJ Link beat packets (broadcast, not OSC) |
| stemdeck | `core.osc` | every controller's messages, and /beat from the analyzer |
| stemdeck | `mixer.osc` | vu |
| prolink | `prolink.beat` | Pro DJ Link beat packets (broadcast, not OSC) |
<!-- /a3-osc:routes -->

- **REAPER → A³ Motion directly**: `/EnergyVisualizer/RMS` bypasses Core
  (`aside` in the register).
- **Core has two receive ports** so it never answers REAPER's reports as
  commands; **Motion three** (control, 25 Hz meters, 426-float energy frames).
- **`/tap` goes straight to the beat-analyzer**: timing wants no relay.
- **`radla`** is off this subnet, via the gateway: beat, meters, network audio.
- **Read a port with its host**: 7772 is both Motion's and the Mixer's meter
  port. A sending port is ephemeral and means nothing.

## The numbering, and what would be better

The numbers grew: `7771`, `7772`, `7775`, `7777` have three owners and two
gaps; `9000`–`9002` interleave Core and REAPER; no number names its owner.
**Proposal** — the block names the owner:

| Block | Owner |
| :--- | :--- |
| `9000–9009` | A³ Core |
| `9010–9019` | REAPER, as Core's engine |
| `7700–7709` | A³ Motion |
| `7710–7719` | A³ Mixer |
| `7720–7729` | beat-analyzer |

with fixed offsets: `+0` control, `+1` VU, `+2` energy, `+5` beat clock.

**Not the current state.** The devices follow one edit of `a3-osc.json`, but
ports set inside REAPER and its plug-ins must follow by hand, and a half-done
renumbering is silent. The tables above are what the rig does today.
