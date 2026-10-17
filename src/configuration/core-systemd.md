(core-services)=

# A³ Core services

## How they hang together

`systemd --user` units under the umbrella **`a3-main.service`** (oneshot,
`/bin/true`, `RemainAfterExit=yes`). It *wants* the components; each is
`PartOf=a3-main.service`.

- **Start** `a3-main`: starts `qjackctl`, `a3-reaper`, `a3-core`,
  `beat-analyzer`, `a3-motion`.
- **Stop/restart** `a3-main`: stops/restarts all its parts. The audio server is not one of them: PipeWire belongs to the user session and runs whether `a3-main` does or not.
- **One component** can stop or fail alone: `Wants=`, not `Requires=` (which
  made `stop a3-core` take REAPER down too).
- `a3-motion` is not shipped here; where Motion has its own machine the name
  matches nothing, harmlessly.

```text
pipewire + wireplumber  (the user session's audio server, JACK via libjack)
 ├─ a3-core          (before REAPER)
 ├─ a3-reaper        (waits until JACK accepts clients)
 ├─ beat-analyzer
 ├─ qjackctl         (waits until JACK accepts clients, connects the patchbay)
 └─ a3-aes67         (only with an audio socket)
```

```sh
systemctl --user start a3-main          # the whole group
systemctl --user restart a3-reaper      # one component
systemctl --user status a3-core
journalctl --user -u a3-core -f
```

## User units at a glance

In `~/.config/systemd/user/` ({ref}`the tree <core-config-tree>`). RT =
`CPUSchedulingPolicy=rr` at that priority; CPUs 1–3 = `CPUAffinity=1 2 3`,
keeping CPU 0 free.

CPU 0 is where the screen lives: x11vnc (`x11vnc.service.d/cpu.conf`) and Xorg
(`~/.xserverrc`, installed by the package, runs the server under `taskset -c 0`)
are pinned there. With a VNC client connected Xorg took most of CPU 1 on the rig
(2026-10-17). Only the X server is pinned, not the login session, so i3 and the
programs it starts keep their own CPUs.

| Unit | Starts | Part of `a3-main` | After | Restarts | Scheduling |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `a3-main` | the umbrella | — | `graphical.target` | — | — |
| `qjackctl` | QjackCtl, A³ patchbay | yes | PipeWire, REAPER, beat-analyzer | on failure | RT 83, CPUs 1–3 |
| `a3-reaper` | REAPER, A³ template | yes | `graphical.target`, PipeWire | no | normal, CPUs 1–3; audio workers RT 76 by the preload below |
| `a3-core` | `a3-core.py` | yes | PipeWire; before REAPER | no | normal, every CPU |
| `beat-analyzer` | tempo, meters | yes | PipeWire | no | RT 65, CPUs 1–3 |
| `a3-aes67` | AES67 sender, PTP clock reading | no | PipeWire | always, 2 s | PipeWire's own |
| `a3-bar-per-workspace` | i3bar on/off | no | `graphical.target` | always, 2 s | normal |
| `a3-user-install` | `user_install.sh` | no | — | no | normal |

`a3-aes67` and `a3-bar-per-workspace` start at login through shipped
`default.target.wants` links. All are `WantedBy=default.target`.

## PipeWire — the audio server

`jackd` and `a3-jack.service` are gone (2026-10-14): **PipeWire** with
wireplumber is the audio server, and JACK programs use PipeWire's `libjack`,
system-wide through `/etc/ld.so.conf.d/pipewire-jack-x86_64-linux-gnu.conf`.
The Scarlett (pro-audio profile) drives the graph. Shipped settings under
`~/.config/pipewire/`:

- `pipewire.conf.d/10-a3-rate.conf`: 44.1 kHz only, quantum 64 (1.45 ms),
  never lower: the AES67 nodes would otherwise pull the graph down to 32
  samples.
- `jack.conf.d/10-a3.conf`: the default device answers as the JACK client
  `system`, so the patchbay's `system:playback_N` and `system:capture_N` stay.

Look at it with `wpctl status` and `pw-top`; the JACK tools
(`jack_lsp`, `jack_connect`) talk to PipeWire.

## `qjackctl.service` — the patchbay

QjackCtl with `~/.config/rncbc.org/a3-patchbay.xml`, connecting clients as they
appear. Waits for the JACK interface (`jack_wait -w`). Restarts on failure.

## `a3-reaper.service` — the audio engine

REAPER (no splash, no error dialogs) on the template
`~/.config/REAPER/ProjectTemplates/a3-reaper.RPP`, after `jack_wait -w`.
**Stopping saves nothing** (`reaper -closeall:nosave`): every start opens the
template on disk. Core's recall restores what Core controls; anything changed
**only in REAPER** (a plug-in setting, a route) is lost unless saved into the
template. Listens on `reaper.osc`, reports to `core.reaper-feedback`.

Core's feedback port has a **4 MB receive buffer**, so REAPER's OSC surface may
send fast (packets of 8192 bytes, 1 ms apart) without the kernel dropping
reports. That cuts a joint restart of REAPER and Core to about 7 s (it took
about 34 s with the default buffer).

(core-silent-start)=

### The silent start

The template starts with main, booth, phones and `main_vu` (the main meter's
track) **muted**. About 0.2 s after the recall, Core pulls each fader to
minimum, unmutes and fades to the template level over 1 s.

- **Only outputs REAPER reports muted are opened.** A Core restart mid-set
  changes nothing — except a track you muted by hand, which Core can't tell
  apart and opens too.
- **Silent after a start:** Core is not up, REAPER never answered (no `gate:`
  line; look for `startup: REAPER does not answer yet`), or REAPER restarted
  alone. Restarting `a3-core` is enough once REAPER runs. A gated track with no
  reported state stays shut, noted in the journal.
- **Rec stays open**, so the beat analyzer has its input.
- The desk's meters stay dark until the fade; the main meter still measures
  programme level, independent of the main fader.

```sh
journalctl --user -u a3-core | grep 'gate:'
```

## `a3-core.service` — the OSC router

`a3-core.py` on `~/.venv/bin/python3`, `Type=idle`, private `/tmp`. Takes
commands on `core.osc`, drives REAPER and the IEM plug-ins, relays REAPER's
reports to every subscriber.

- **After PipeWire, before REAPER**: one state burst instead of two (Core also asks
  REAPER for everything once bound, so either order works).
- **Every CPU** (`a3-core.service.d/cpu.conf`): pinned to CPU 0, it starved
  whenever the Motion UI peaked there, and OSC was dropped.
- **Needs the truth**: `/usr/share/a3/a3-osc.json` (or `$A3_OSC_TRUTH`), joined
  with `network.json`, served on `core.web`, announced every 2 s
  ({ref}`truth <osc-truth>`).
- No `Restart=`.

### Its arguments

None by default; a drop-in can point any default elsewhere (useful on a bench).

| Argument | Default / meaning |
| :--- | :--- |
| `--ip`, `--port` | `core.osc` |
| `--feedback-port` | `core.reaper-feedback`, separate so reports are never commands |
| `--web-bind` | `core.web`, every interface. The window can send OSC with no login; bind locally to keep it to the machine |
| `--mixer`, `--motion` | `mixer.osc`, `motion.osc` |
| `--reaper`, `--dualdelay` | `reaper.osc`, `dualdelay.osc` |
| `--subscriber NAME=HOST:PORT` | another department; repeatable |
| `--print-osc` | log every message (off: 300,000 lines an hour on one address) |
| `--no-web` | no window |
| `--save-project` | ask REAPER to save every few minutes (off: a template has no file, and saving opens a dialog) |

(core-subscriber)=

### Adding a department

A light or video desk: one argument each, in a drop-in:

```
a3-core.py --subscriber light=HOST:PORT \
           --subscriber video=HOST:PORT
```

It gets every A³ message exactly as Mixer and Motion do; the name shows in the
window. **An unparsable subscriber stops Core from starting** — better than a
desk that silently hears nothing. What arrives: {doc}`OSC reference <../ressources/osc>`.

### What it keeps across a restart

`~/.local/state/a3-core/` (or `$XDG_STATE_HOME/a3-core/`): `state.json` (what
only Core knows) and `evening.json` (every continuous value passed on). Outside
the package; updates don't touch them.

## `beat-analyzer.service` — tempo and meters

`~/a3-system/beat-analyzer/build/beat-analyzer`, `Type=idle`, 3 s after start,
configured by `build/.env` (OSC targets in the [rendered block](#core-postinst),
the rest {ref}`its own <beat-analyzer-config>`). Sends `/beat` to Core, the
controllers and `radla`, and the forty `/vu/n` ({ref}`VU map <core-vu-map>`).

(core-aes67)=

## `a3-aes67.service` and `ptp4l` — the audio network

Only on a Core with a second socket ({ref}`install <core-postinst>`,
`audio-port`); otherwise `a3-aes67` has no config and does not start.

- `ptp4l@<socket>.service` (linuxptp, system unit, enabled by the postinst):
  the PTP clock on the second socket. The Core is master unless a better
  clock is on the network.
- `a3-aes67.service` (user unit): a second PipeWire instance running
  `~/.config/pipewire/pipewire-aes67.conf`, rendered by `a3-osc-render` from
  the truth's `network.audio_port`. It sends the Core's 12 channels as the
  multicast stream `AES67 <hostname> out` (44.1 kHz, 24 bit, packet time
  0.5 ms), announces it by SAP and receives the streams of other machines.
  The Scarlett drives it, not the PTP clock, so the samples go out
  unconverted. Restarts 2 s after any exit.

Network, streams and cabling: {ref}`ports <ports-audio-network>`,
{doc}`Patchbay <../ressources/patchbay>`.

## REAPER and the realtime priority

pipewire-jack answers REAPER's question for the audio workers' priority wrongly.
`a3-reaper.service` therefore preloads a small shim,
`~/.local/lib/a3/libjack-rt-priority.so` (built by the postinst from
`~/.local/share/a3-core/src/jack-rt-priority.c`); the workers then run at RT 76,
under PipeWire's own data loop. The unit sets no `CPUScheduling`: raising the
whole process puts REAPER's GUI and OSC threads above the audio threads.

## `a3-bar-per-workspace.service` — i3bar on the tool workspaces

`a3-bar-per-workspace.py` on `:0`, after `a3-wait-for-the-screen`. Shows the
bar on workspace 3 and up, hides it on 1 and 2 ([The screen](#core-config-screen));
restarts whenever it ends (an i3 restart ends the event stream).

## `a3-user-install.service` — the user-side installer

Runs `user_install.sh` once (`bash -e`) on every install; see
[a3-user-install.service](#core-user-install).

(core-system-units)=

## System units

In `/etc/systemd/system/`, dpkg conffiles.

| Unit | What it does | Enabled |
| :--- | :--- | :--- |
| `x11vnc.service` | `x11vnc` as `aaa` on `:0`, 5 s after `graphical.target`, `-shared -forever`, restart on failure; CPU 0 only (`x11vnc.service.d/cpu.conf`); port on its command line, not in `a3-osc.json` | yes |
| `set_irq_prio.service` | at boot, the USB controller's IRQ threads (`irq/…-xhci_hcd`) to FIFO 95, so the sound card comes first | yes |
| `vnc-display.service` | `recipes/vnc-display.sh`: a monitor on HDMI/DP moves `10-headless.conf` aside to `.bak`, none moves it back | no, shipped only |

Over VNC: QjackCtl, REAPER's arrangement and mixer. Debian's own: the postinst
enables `systemd-networkd` (when configuring the network); LightDM logs `aaa`
into i3 ([Under /etc](#core-etc)).
