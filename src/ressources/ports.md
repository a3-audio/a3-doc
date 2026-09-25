# Ports and endpoints

Every UDP port the devices listen on, and every place each one sends, stated
per device. One page, because the alternative is what happened on 2026-09-24:
three files disagreed about the A³ Mixer's address and port, and each of them
looked authoritative on its own.

Everything below was **measured on the running rig**, not read out of a config
file. Where a config disagrees with this page, the config is the thing to fix.

## Hosts

| Device | Address |
| :--- | :--- |
| A³ Core | `192.168.8.10` |
| A³ Mixer | `192.168.8.11` |

A³ Motion's UI currently runs **on the Core machine**, which is why Core and
the beat-analyzer address it as `127.0.0.1`. On a rig where it runs on its own
Raspberry Pi that becomes the Pi's address; nothing else changes.

## Cabling

The router has one free port, so the A³ Mixer hangs on the Core machine's
**second socket**, and the Core **bridges** its two sockets into one segment
(since 2026-09-25):

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
- The a3-core package writes this: its install asks for the second socket
  (`a3-core/bridge-with`, empty for no bridge) and for the address. See the
  a3-core README.

Measured on the rig after a cold boot (2026-09-25): the mixer answers in
0.7 ms, the router in 0.5 ms.

## The list

Per service: where it sends, and where its return arrives. A send is an
address and port on the far end; a return is a port this service holds open.

```text
A³ MIXER
  send    192.168.8.10:9000   Core           gain, EQ, volume, PFL, FX, 3D toggle
          192.168.8.10:7775   beat-analyzer  /tap
  return  7772                               VU and lamp state

A³ MOTION
  send    127.0.0.1:9000      Core           positions, clip settings, /state/recall
          127.0.0.1:7775      beat-analyzer  /tap, /beat, /clockmode
  return  7771                               relayed state, recall answer, /beat
          7772                               /vu/0..11
          7777                               /EnergyVisualizer/RMS

A³ CORE
  send    127.0.0.1:9001      REAPER         everything that becomes audio
          127.0.0.1:7771      A³ Motion      relayed state, recall answer
          192.168.8.11:7772   A³ Mixer       VU and lamp state
  return  9000                               commands from Mixer, Motion, analyzer
          9002                               REAPER feedback

REAPER
  send    127.0.0.1:9002      A³ Core        what a fader or a plugin did
          127.0.0.1:7777      A³ Motion      /EnergyVisualizer/RMS   (IEM plugin)
  return  9001                               from Core
          1337-1340                          its own OSC devices

BEAT-ANALYZER
  send    127.0.0.1:7771      A³ Motion      /beat
          127.0.0.1:7772      A³ Motion      /vu/0..11
          192.168.8.11:7772   A³ Mixer       /vu/0..11
          192.168.43.96:9000  radla          /beat
          192.168.43.96:9001  radla          /vu/0..11
  return  7775                               /beat, /tap, /clockmode
          50000-50002                        Pioneer Pro DJ Link
```

Three of these are worth reading twice.

**REAPER sends to A³ Motion directly.** `/EnergyVisualizer/RMS` is a VST3
plugin inside the REAPER project addressing Motion on 7777. It does not pass
through Core, which is why Core's register marks it `aside` and why it keeps
working across things that stop Core.

**A³ Core holds two return ports on purpose.** Reading REAPER's feedback on
the same port as commands would have Core answering its own reports — a loop
on a rig that is making sound.

**`radla` is off this subnet.** `192.168.43.96`, reached through the gateway
at `192.168.8.1`, and it answers — a live target, not a leftover. Worth saying
because the two other `192.168.43.x` addresses that used to sit in the
analyzer's config (`.55` for the Mixer, `.54` for Motion) are dead and were
wrong. What `radla` does with what it receives is not documented here.

## Ports, by listener

| Port | Listener |
| ---: | :--- |
| 7771 | A³ Motion UI — control |
| 7772 | A³ Motion UI — VU |
| 7772 | A³ Mixer — VU (same number, different host) |
| 7775 | beat-analyzer — beat clock |
| 7777 | A³ Motion UI — energy |
| 9000 | A³ Core — commands |
| 9001 | REAPER |
| 9002 | A³ Core — REAPER's feedback |
| 50000–50002 | beat-analyzer — Pioneer Pro DJ Link |
| 1337–1340 | REAPER — its own OSC devices |

---

## A³ Core

The machine that makes the sound. It has no interface of its own; everything
it does, something else asked for.

**Receives**

| Port | From | What |
| ---: | :--- | :--- |
| 9000 | A³ Mixer, A³ Motion, beat-analyzer | Commands: gain, EQ, volume, PFL, FX, positions, `/state/recall` |
| 9002 | REAPER | Feedback: what a fader or a plugin actually did |

**Sends**

| To | Port | What |
| :--- | ---: | :--- |
| REAPER | 9001 | Everything that becomes audio |
| A³ Motion UI | 7771 | Relayed state and the answer to `/state/recall` |
| A³ Mixer | 7772 | VU and lamp state |

Two receive ports rather than one is deliberate: reading REAPER's reports on
the same port as commands would have Core answering its own feedback — a loop
on a rig that is making sound. See [OSC](osc.md).

## A³ Mixer

Four channels of desk. Sends what the hands do; receives what the meters and
lamps should show.

**Receives**

| Port | From | What |
| ---: | :--- | :--- |
| 7772 | A³ Core, beat-analyzer | `/vu/0..11`, and the PFL and FX lamp states |

**Sends**

| To | Port | What |
| :--- | ---: | :--- |
| A³ Core | 9000 | gain, EQ, volume, PFL, FX, the 3D toggle |
| beat-analyzer | 7775 | `/tap` |

`/tap` goes straight at the beat-analyzer rather than through Core. Core's
handler for it is gone.

## A³ Motion

The one with the screen. Records movement trajectories and plays them back in
time.

**Receives**

| Port | From | What |
| ---: | :--- | :--- |
| 7771 | A³ Core, beat-analyzer | Relayed channel state, the recall answer, `/beat` |
| 7772 | beat-analyzer | `/vu/0..11` |
| 7777 | A³ Core | `/EnergyVisualizer/RMS`, the 426-point sphere |

**Sends**

| To | Port | What |
| :--- | ---: | :--- |
| A³ Core | 9000 | Positions, clip settings, `/state/recall` |
| beat-analyzer | 7775 | `/tap`, `/beat` |

Three receive ports because the three streams have nothing to do with each
other and very different rates: control is occasional, VU is 25 Hz, and the
energy sphere is 426 floats a frame.

## beat-analyzer

Beat detection and VU metering, straight off JACK.

**Receives**

| Port | From | What |
| ---: | :--- | :--- |
| 7775 | A³ Motion, A³ Mixer | `/beat`, `/tap`, `/clockmode` |
| 50000–50002 | Pioneer Pro DJ Link | Keep-alive, beat packets, status |

**Sends**

| To | Port | What |
| :--- | ---: | :--- |
| A³ Motion UI | 7771 | `/beat` |
| A³ Motion UI | 7772 | `/vu/0..11` |
| A³ Mixer | 7772 | `/vu/0..11` |

Targets are named in its `.env` as `OSC_HOST_<name>` and `OSC_VU_<name>`. With
no `.env` present it falls back to a single target on `127.0.0.1` — so a build
directory without one reaches nothing off the machine, quietly.

## REAPER

Core's engine. Not a device anyone touches, but it holds ports and it is easy
to confuse with Core because the numbers are adjacent.

**Receives** on 9001, from Core. **Sends** to Core on 9002. It also holds
1337–1340 for its own OSC devices.

---

## Two things worth knowing

**The same port number appears on more than one host, on purpose.** 7772 is
"the VU port" on both A³ Motion and the A³ Mixer. Reading a port number
without its host is how `192.168.43.55:7771` came to sit in a config file: the
port was taken from the wrong device and the address from an older network.

**A port a device sends *from* is not a port anything listens on.** Every
device also holds a handful of high-numbered ephemeral sockets; those are the
kernel's, they change on every start, and they mean nothing. Only the ports on
this page are fixed.

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

**This is a proposal, not the current state.** Renumbering touches all four
devices plus the REAPER OSC config, and a half-done renumbering is worse than
an untidy one that works — a device sending into a port nobody holds is
silent, and silence is the hardest fault here to see. The tables above are
what the rig does today.
