# Ports and endpoints

Every UDP port the devices listen on, and who sends to it. Both are facts of
`a3-osc.json` — see {ref}`Where addresses and ports live <osc-truth>`: the
listener table below is rendered from it, and the other pages name a port by
its listener name (`core.osc`, `motion.vu`, …) rather than by its number.

## Hosts

The machines are named in the file's `hosts` section; the Host column of the
[listener table](#ports-by-listener) shows each name with its address.

A³ Motion's UI runs **on the Core machine** on the rig, which is why Core and
the beat-analyzer address it as `127.0.0.1`. Where it runs on a machine of its
own (see {ref}`A³ Motion hardware <moc-hardware>`), that becomes the machine's
address; nothing else changes.

## Cabling

The router has one free port, so the A³ Mixer hangs on the Core machine's
**second socket**, and the Core **bridges** its two sockets into one segment:

```text
router 192.168.8.1 ───── eno1   ┐
                                ├─ br0  A³ Core 192.168.8.10
A³ Mixer 192.168.8.11 ── enp5s0 ┘
```

- The address lives on `br0`, not on either socket. `networkctl` shows `br0`
  as *routable* and both sockets as *enslaved*.
- Spanning tree is on, so the bridge forwards about **thirty seconds** after
  boot, not at once.
- **The Core sits in the path.** With the Core machine off, the A³ Mixer has
  no network.
- The a3-core package writes this; see {ref}`What the installation does
  <core-postinst>`.

(ports-by-listener)=

## Ports, by listener

Rendered from `a3-osc.json` — edit the file, not this table. `core.web` serves
the traffic window and also `GET /api/truth`, the joined truth.
`devices.announce` is not Core's listener but the announcement: Core
broadcasts `/core/here` to it every 2 s, and every device that follows Core's
truth — the A³ Mixer, StemDeck and A³ Motion — listens there. A host of `any`
(`0.0.0.0`) means the program listens on every interface of its own machine;
`local` means only on the machine itself.

<!-- a3-osc:ports -->
| Program | Role | Host | Port | Carries |
| --- | --- | --- | --- | --- |
| core | osc | any (0.0.0.0) | 9000 | every controller's messages, and /beat from the analyzer |
| core | reaper-feedback | local (127.0.0.1) | 9002 | REAPER's own OSC feedback |
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
| radla | osc | radla (192.168.43.96) | 9000 | /beat |
| radla | vu | radla (192.168.43.96) | 9001 | /vu |
| radla | zita-n2j | radla (192.168.43.96) | 55100 | network audio from Core (zita-j2n, 2 channels, not OSC) |
| prolink | announce | any (0.0.0.0) | 50000 | Pro DJ Link keep-alives (broadcast, not OSC) |
| prolink | beat | any (0.0.0.0) | 50001 | Pro DJ Link beat packets (broadcast, not OSC) |
| prolink | status | any (0.0.0.0) | 50002 | Pro DJ Link status packets (broadcast, not OSC) |
<!-- /a3-osc:ports -->

(ports-routes)=

## Who sends where

The file's `routes`, by sender. Each target is a listener of the table above.

| Sender | Sends to |
| :--- | :--- |
| A³ Mixer | `core.osc` (gain, EQ, volume, cue, filter, `/device/hello`), `beat-analyzer.clock` (`/tap`) |
| A³ Motion | `core.osc` (positions, clip settings, mixer, `/state/recall`), `beat-analyzer.clock` (`/tap`, `/beat`, `/clockmode`) |
| A³ Core | `reaper.osc`, `iem.multiencoder-1` … `-3`, `dualdelay.osc` (the engine); `motion.osc`, `mixer.osc`, `stemdeck.osc` (relayed state, lamps, the recall answer, bus switches); `devices.announce` (`/core/here`) |
| REAPER | `core.reaper-feedback` (what a fader or a plug-in did); its IEM EnergyVisualizer sends to `motion.energy` |
| beat-analyzer | `core.osc`, `motion.osc`, `mixer.osc`, `radla.osc` (`/beat`); `motion.vu`, `mixer.osc`, `radla.vu` (`/vu`) |
| StemDeck | `core.osc` (bus switch reports, hello), `mixer.osc` (stem meters), `prolink.announce`, `prolink.status` and the beat packets (as tempo master) |
| zita-j2n (Core) | `radla.zita-n2j` (2 channels) |
| radla | `zita-n2j.audio` (10 channels) |

Worth knowing:

- **REAPER sends to A³ Motion directly.** `/EnergyVisualizer/RMS` comes from a
  plug-in inside the REAPER project and does not pass Core, which is why
  Core's register marks it `aside`.
- **A³ Core holds two receive ports on purpose.** Reading REAPER's feedback
  on the command port would have Core answering its own reports — a loop.
- **A³ Motion holds three**, because control, meters (25 Hz) and the energy
  sphere (426 floats a frame) have nothing to do with each other.
- **`/tap` goes straight to the beat-analyzer**, from the desk and from A³
  Motion, not through Core: a tap is timing.
- **`radla` is off this subnet**, reached through the gateway; it receives
  the beat, the meters and network audio.
- **The same port number appears on more than one host, on purpose** (7772 is
  the meter port of both A³ Motion and the A³ Mixer): read a port with its
  host. A port a device sends *from* is an ephemeral one and means nothing.

## The numbering, and what would be better

The present allocation grew rather than being chosen, and it shows:

- `7771`, `7772`, `7775`, `7777` are four ports in one range with three
  different owners and two gaps.
- `9000`, `9001`, `9002` interleave Core and REAPER, so "the 900x port" is
  ambiguous in exactly the conversation where it matters.
- Nothing about a number says which device owns it.

A scheme where the **block says the owner** would remove a class of mistake:

| Block | Owner |
| :--- | :--- |
| `9000–9009` | A³ Core |
| `9010–9019` | REAPER, as Core's engine |
| `7700–7709` | A³ Motion |
| `7710–7719` | A³ Mixer |
| `7720–7729` | beat-analyzer |

with the offset inside a block keeping its meaning everywhere: `+0` control,
`+1` VU, `+2` energy, `+5` beat clock.

**This is a proposal, not the current state.** The devices' side of a
renumbering is one edit in `a3-osc.json`, but the ports set inside REAPER and
its plug-ins still have to follow by hand; the desk, StemDeck and A³ Motion
follow Core's announcement by themselves. A half-done renumbering is worse than an untidy
one that works — a device sending into a port nobody holds is silent, and
silence is the hardest fault here to see. The tables above are what the rig
does today.
