(core-services)=

# A³ Core services

## How they hang together

`systemd --user` units under the umbrella **`a3-main.service`** (oneshot,
`/bin/true`, `RemainAfterExit=yes`). It *wants* the components; each is
`PartOf=a3-main.service`.

- **Start** `a3-main`: starts `a3-jack`, `qjackctl`, `a3-reaper`, `a3-core`,
  `beat-analyzer`, `a3-motion`.
- **Stop/restart** `a3-main`: stops/restarts all its parts, zita included.
- **One component** can stop or fail alone: `Wants=`, not `Requires=` (which
  made `stop a3-core` take JACK and REAPER down too).
- `a3-motion` is not shipped here; where Motion has its own machine the name
  matches nothing, harmlessly.

```text
a3-jack  (waits for the USB sound card)
 ├─ a3-core          (before REAPER)
 ├─ a3-reaper        (waits until JACK accepts clients)
 ├─ beat-analyzer
 ├─ qjackctl         (waits until JACK accepts clients, connects the patchbay)
 └─ zita-j2n, zita-n2j
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

| Unit | Starts | Part of `a3-main` | After | Restarts | Scheduling |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `a3-main` | the umbrella | — | `graphical.target` | — | — |
| `a3-jack` | `jackd` on the USB card | yes | `sound.target` | no | RT 85, CPUs 1–3 |
| `qjackctl` | QjackCtl, A³ patchbay | yes | JACK, REAPER, beat-analyzer | on failure | RT 83, CPUs 1–3 |
| `a3-reaper` | REAPER, A³ template | yes | `graphical.target`, JACK | no | RT 75, CPUs 1–3 |
| `a3-core` | `a3-core.py` | yes | JACK; before REAPER | no | normal, every CPU |
| `beat-analyzer` | tempo, meters | yes | JACK | no | RT 65, CPUs 1–3 |
| `zita-j2n` | network audio out | stopped with it, not started | JACK | always, 2 s | RT 64, CPUs 1–3 |
| `zita-n2j` | network audio in | stopped with it, not started | JACK | always, 2 s | RT 64, CPUs 1–3 |
| `a3-bar-per-workspace` | i3bar on/off | no | `graphical.target` | always, 2 s | normal |
| `a3-user-install` | `user_install.sh` | no | — | no | normal |

The zita units and `a3-bar-per-workspace` start at login through shipped
`default.target.wants` links. All are `WantedBy=default.target`.

## `a3-jack.service` — the JACK server

`jackd`, RT 19, ALSA `hw:USB`, 44.1 kHz, 256 frames. Waits for
`/proc/asound/USB` (`jackd` fails if the card is late; `sound.target` is not
enough).

## `qjackctl.service` — the patchbay

QjackCtl with `~/.config/rncbc.org/a3-patchbay.xml`, connecting clients as they
appear. Waits for JACK (`jack_wait -w`). Restarts on failure.

## `a3-reaper.service` — the audio engine

REAPER (no splash, no error dialogs) on the template
`~/.config/REAPER/ProjectTemplates/a3-reaper.RPP`, after `jack_wait -w`.
**Stopping saves nothing** (`reaper -closeall:nosave`): every start opens the
template on disk. Core's recall restores what Core controls; anything changed
**only in REAPER** (a plug-in setting, a route) is lost unless saved into the
template. Listens on `reaper.osc`, reports to `core.reaper-feedback`.

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

- **After JACK, before REAPER**: one state burst instead of two (Core also asks
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

(core-zita)=

## `zita-j2n.service` and `zita-n2j.service` — network audio

For a StemDeck on another machine: `zita-j2n` sends 2 channels (24 bit) to
`radla.zita-n2j`; `zita-n2j` receives 10 on `zita-n2j.audio`, 20 ms buffer.
Addresses from `~/.config/a3/osc.env`. Restart 2 s after any exit (zita may
exit 0), never give up (`StartLimitIntervalSec=0`). Channels:
{doc}`Patchbay <../ressources/patchbay>`.

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
| `x11vnc.service` | `x11vnc` as `aaa` on `:0`, 5 s after `graphical.target`, `-shared -forever`, restart on failure; port on its command line, not in `a3-osc.json` | yes |
| `set_irq_prio.service` | at boot, the USB controller's IRQ threads (`irq/…-xhci_hcd`) to FIFO 95, so the sound card comes first | yes |
| `vnc-display.service` | `recipes/vnc-display.sh`: a monitor on HDMI/DP moves `10-headless.conf` aside to `.bak`, none moves it back | no, shipped only |

Over VNC: QjackCtl, REAPER's arrangement and mixer. Debian's own: the postinst
enables `systemd-networkd` (when configuring the network); LightDM logs `aaa`
into i3 ([Under /etc](#core-etc)).
