# Ports and endpoints

Every UDP port the four devices listen on, and every place each one sends. One
page, because the alternative is what happened on 2026-09-24: three files
disagreed about the A³ Mixer's address and port, and each of them looked
authoritative on its own.

Everything below was **measured on the running rig**, not read out of a config
file. Where a config disagrees with this page, the config is the thing to fix.

## Hosts

| Device | Address |
| :--- | :--- |
| A³ Core | `192.168.8.10` |
| A³ Mixer | `192.168.8.11` |

A³ Motion's UI currently runs **on the Core machine**, which is why Core
addresses it as `127.0.0.1`. On a rig where it runs on its own Raspberry Pi
that becomes the Pi's address; nothing else changes.

## What listens where

| Port | Listener | What arrives |
| ---: | :--- | :--- |
| 7771 | A³ Motion UI | Commands and state: positions, the channel strip, the answer to `/state/recall` |
| 7772 | A³ Motion UI | VU meters, `/vu/0..11` |
| 7772 | A³ Mixer | VU meters — the same port number on a different host, deliberately |
| 7775 | beat-analyzer | `/beat`, `/tap`, `/clockmode` |
| 7777 | A³ Motion UI | `/EnergyVisualizer/RMS`, the 426-point sphere |
| 9000 | A³ Core | Commands from Mixer, Motion and the analyzer |
| 9001 | REAPER | What Core sends REAPER |
| 9002 | A³ Core | REAPER's feedback, `/track/*` and `/fx/*` |
| 50000–50002 | beat-analyzer | Pioneer Pro DJ Link: keep-alive, beat packets, status |
| 1337–1340 | REAPER | REAPER's own OSC devices |

Why Core needs two of its own: reading REAPER's reports on the same port as
commands would have Core answering its own feedback — a loop on a rig that is
making sound. See [OSC](osc.md).

## What sends where

| Sender | Target | Port | Carrying |
| :--- | :--- | ---: | :--- |
| A³ Mixer | Core | 9000 | gain, EQ, volume, PFL, FX, the 3D toggle |
| A³ Mixer | beat-analyzer | 7775 | `/tap` |
| A³ Motion UI | Core | 9000 | positions, clip settings, `/state/recall` |
| A³ Motion UI | beat-analyzer | 7775 | `/tap`, `/beat` |
| A³ Core | REAPER | 9001 | everything that becomes audio |
| A³ Core | A³ Motion UI | 7771 | relayed state and the recall answer |
| A³ Core | A³ Mixer | 7772 | VU and lamp state |
| REAPER | Core | 9002 | what a fader or a plugin actually did |
| beat-analyzer | A³ Motion UI | 7771 | `/beat` |
| beat-analyzer | A³ Motion UI | 7772 | `/vu/0..11` |
| beat-analyzer | A³ Mixer | 7772 | `/vu/0..11` |

## Two things worth knowing

**The same port number appears on more than one host, on purpose.** 7772 is
"the VU port" on both Motion and the Mixer. Reading a port number without its
host is how `192.168.43.55:7771` came to sit in a config file: the port was
copied from the wrong device and the address from an older network.

**A port a device sends *from* is not a port anything listens on.** Every
device also holds a handful of high-numbered ephemeral sockets; those are the
kernel's, they change on every start, and they mean nothing. Only the ports
above are fixed.

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
silent, and silence is the hardest fault here to see. The table above is what
the rig does today.
