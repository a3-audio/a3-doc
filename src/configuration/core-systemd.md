(core-services)=

# A³ Core services

## How they hang together

Core is a group of `systemd --user` units with **`a3-main.service`** as the
umbrella. `a3-main` does nothing itself (`Type=oneshot`, `ExecStart=/bin/true`,
`RemainAfterExit=yes`); it *wants* the components, and each component is
`PartOf=a3-main.service`:

- **Starting** `a3-main` starts `a3-jack`, `qjackctl`, `a3-reaper`,
  `a3-core`, `beat-analyzer` and `a3-motion`.
- **Stopping or restarting** `a3-main` stops or restarts everything that is
  part of it — the zita units included.
- **One component** can be stopped, restarted or fail on its own without
  taking the others along. That is why the umbrella uses `Wants=`, not
  `Requires=`: with `Requires=`, a single `systemctl --user stop a3-core` took
  down JACK, REAPER, QjackCtl and the beat-analyzer with it.

`a3-motion.service` is listed although this package does not ship it: on a
machine that also runs A³ Motion the group is then whole; where Motion has its
own machine, the name matches nothing and that is not an error.

The start order:

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

All live in `~/.config/systemd/user/` (installed from the package's
configuration, see [part 4](#core-config-tree)). "RT" is `CPUSchedulingPolicy=rr` with the
priority given; "CPUs 1–3" is `CPUAffinity=1 2 3`, which keeps CPU 0 free.

| Unit | Starts | Part of `a3-main` | Ordered after | Restarts | Scheduling |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `a3-main` | nothing — the umbrella | — | `graphical.target` | — | — |
| `a3-jack` | `jackd` on the USB sound card | yes | `sound.target` | no | RT 85, CPUs 1–3 |
| `qjackctl` | QjackCtl with the A³ patchbay | yes | JACK, REAPER, beat-analyzer | on failure | RT 83, CPUs 1–3 |
| `a3-reaper` | REAPER with the A³ template | yes | `graphical.target`, JACK | no | RT 75, CPUs 1–3 |
| `a3-core` | the OSC router, `a3-core.py` | yes | JACK; before REAPER | no | normal, every CPU |
| `beat-analyzer` | tempo detection and VU meters | yes | JACK | no | RT 65, CPUs 1–3 |
| `zita-j2n` | network audio out | yes (not wanted) | JACK | always, after 2 s | RT 64, CPUs 1–3 |
| `zita-n2j` | network audio in | yes (not wanted) | JACK | always, after 2 s | RT 64, CPUs 1–3 |
| `a3-bar-per-workspace` | shows or hides i3bar | no | `graphical.target` | always, after 2 s | normal |
| `a3-user-install` | `recipes/user_install.sh` | no | — | no | normal |

"Not wanted" means `a3-main` does not start the zita units, but stops them
with itself: they start at login on their own, through the
`default.target.wants` links the package ships for them (step 4 copies them
into `~/.config`). The same goes for `a3-bar-per-workspace`. Every unit is
`WantedBy=default.target`.

## `a3-jack.service` — the JACK server

Runs `jackd` with realtime priority 19 on ALSA device `hw:USB` at 44.1 kHz
and 256 frames per period. Before it starts it waits until the sound card is
actually there (`/proc/asound/USB`), not a fixed time: `jackd` fails outright
if the card has not appeared yet, and `sound.target` only says the subsystem
is up. Stopping it kills `jackd`.

## `qjackctl.service` — the patchbay

Runs QjackCtl with the A³ patchbay, `~/.config/rncbc.org/a3-patchbay.xml`,
which connects every JACK client as it appears. It waits until JACK accepts
clients (`jack_wait -w`); REAPER and the beat-analyzer do not have to be up
first, since the patchbay reconnects them when they come. Restarts on
failure.

## `a3-reaper.service` — the audio engine

Runs `~/.local/opt/REAPER/reaper` without splash screen and error dialogs,
opening the template `~/.config/REAPER/ProjectTemplates/a3-reaper.RPP`. It
waits until JACK accepts clients (`jack_wait -w`) — JACK has no readiness
notification, and "started" is not "ready". **Stopping it saves nothing**
(`ExecStop=… reaper -closeall:nosave`, since 2026-10-07; REAPER's own help
documents `-close[all][:save|:nosave][:exit]`, and with spaces `all` and
`:nosave` would be read as file names): every start opens the template as it
lies on disk, which is the package's version only if you took the package's
template at the replace-config question. The earlier stop command never wrote
the template either, so REAPER-only changes were not kept on stop before this
change. What Core controls comes back through Core's start-up recall, which
replays every controlled value. What was changed **only in REAPER** — a
plug-in setting, a route — is lost on stop unless you save it deliberately
into the template. REAPER takes Core's commands on its listener
`reaper.osc` and reports back to Core's `core.reaper-feedback`.

(core-silent-start)=

### The silent start

The template starts with the three outputs — main, booth and phones — and the
main meter's track `main_vu` **muted**, so a cold start is silent instead of
playing the template's levels for the seconds before the recall lands. Core
opens them once the start-up recall has been applied: about 0.2 s later it
takes each fader to minimum, unmutes the track and fades back to the
template's fader level over 1 s.

- **Only what REAPER reports muted is opened.** If Core restarts during a set,
  REAPER reports the outputs open and Core sends it nothing: a Core restart
  changes nothing audible, except a track you muted by hand in REAPER: Core
  cannot tell a hand mute from the template's, so it opens that one too
  (decided).
- **A silent rig after a start means Core is not up**, or REAPER never
  answered Core's OSC, or REAPER was restarted on its own, without Core to open
  the outputs. In the second case there is no `gate:` line; look for
  `startup: REAPER does not answer yet`. Once REAPER runs, restarting
  `a3-core` alone is enough to open the outputs (lighter than `a3-main`). If
  REAPER answers but reports no mute or fader state for a gated track, Core
  leaves that one shut and says so in the journal.
- **Rec stays open**, so the beat analyzer has its BPM input while the outputs
  are shut.
- **The desk's meters stay dark while the room is silent.** The booth and
  phones meters are measured after their tracks; the main meter has a track of
  its own, `main_vu`, which the gate mutes with the outputs. All of them rise
  with the fade. What the main meter measures is unchanged: the programme
  level, independent of the main fader.

```sh
journalctl --user -u a3-core | grep 'gate:'
```

## `a3-core.service` — the OSC router

Runs `~/.local/bin/a3-core.py` on the venv's Python (`~/.venv/bin/python3`),
`Type=idle`, with a private `/tmp`. It is the only part of Core that knows
which device is which: it takes the controllers' messages on `core.osc`,
drives REAPER and the IEM plug-ins, and relays what REAPER reports to the A³
Mixer, A³ Motion and any further subscriber.

- **After JACK, before REAPER.** Core relays what REAPER reports, and REAPER
  announces its whole state when it starts. Since 2026-09-26 Core asks REAPER
  to say everything again once its own ports are bound, so either order
  works; Core-first stays because it gives one burst instead of two.
- **Every CPU.** The drop-in `a3-core.service.d/cpu.conf` resets the CPU
  mask. Core was pinned to CPU 0, the CPU the Motion UI draws on; whenever
  the UI peaked, Core got no time and the kernel dropped its incoming OSC.
  The audio threads on the other CPUs run realtime, so an ordinary Core only
  takes what they leave.
- **It needs the one truth.** Core reads `/usr/share/a3/a3-osc.json` once at
  start-up and does not start without it (or `$A3_OSC_TRUTH` naming another
  file). It then joins `~/.config/a3/network.json` over it, serves the result
  on `core.web` and announces it every 2 s on `devices.announce` (see
  {ref}`Where addresses and ports live <osc-truth>`).
- **No restart.** The unit has no `Restart=`.

### Its arguments

The shipped unit passes none: every default comes from the one truth. A rig
can add arguments in a drop-in; each one points a default somewhere else,
which is what makes the whole path testable on a bench instead of only in
front of the rig.

| Argument | What it is |
| :--- | :--- |
| `--ip`, `--port` | where commands arrive; by default `core.osc` |
| `--feedback-port` | where REAPER's feedback arrives — its own port, so REAPER's reports can never be read as commands; by default `core.reaper-feedback` |
| `--web-bind` | the window, as `host:port`; by default `core.web` — every interface, since 2026-09-30. Mind that the window can send OSC into a running rig, with no login; a local address keeps it to the machine |
| `--mixer`, `--motion` | the two devices that ship, as `host:port`; by default `mixer.osc` and `motion.osc` |
| `--reaper`, `--dualdelay` | the audio engine's own endpoints; by default `reaper.osc` and `dualdelay.osc` |
| `--subscriber NAME=HOST:PORT` | **another department.** Repeatable |
| `--print-osc` | also print every message, the way Core did before the window existed. Off by default: it was 301,385 journal lines an hour on one address alone |
| `--no-web` | do not open the window at all |
| `--save-project` | ask REAPER to save its project every few minutes when something has moved. Off by default: with REAPER started from a template there is no project file, and saving opens a dialog over the panel |

(core-subscriber)=

### Adding a department

A light or video desk that wants to follow the show needs no change to any
source file — one more argument per desk, in a drop-in for `a3-core.service`:

```
a3-core.py --subscriber light=HOST:PORT \
           --subscriber video=HOST:PORT
```

Every A³-shaped message then reaches it — every channel's gain, EQ, volume and
send, the master section, the filter, the positions, the lamps and the flags —
in exactly the form the A³ Mixer and A³ Motion get them. The name is what the
window shows in its peer column.

A subscriber that cannot be parsed stops Core from starting, rather than being
skipped. That is deliberate: a mistyped subscriber is a department that hears
nothing all evening, and OSC over UDP has no way of saying so.

See the {doc}`OSC reference <../ressources/osc>` for what arrives.

### What it keeps across a restart

Not installed, but written by Core while it runs, under
`~/.local/state/a3-core/` (or `$XDG_STATE_HOME/a3-core/`): `state.json`, what
only Core knows, and `evening.json`, every continuous value it passed on —
both outside the package, so an update never touches them.

## `beat-analyzer.service` — tempo and meters

Runs `~/a3-system/beat-analyzer/build/beat-analyzer` from its `build/`
directory, `Type=idle`, three seconds after it is started. It takes its
configuration from `build/.env` there — its OSC targets in the block the
package renders (see [step 6](#core-postinst)), the rest is the analyzer's
own (see {ref}`Beat Analyzer <beat-analyzer-config>`). It sends `/beat` to
Core, the controllers and `radla`, and the forty `/vu/n`
meters (see the {ref}`VU map <core-vu-map>`).

(core-zita)=

## `zita-j2n.service` and `zita-n2j.service` — network audio

Network audio with the StemDeck machine that is not the Core: `zita-j2n`
sends two channels (24 bit) out of JACK to its `radla.zita-n2j` listener;
`zita-n2j` receives ten channels into JACK on `zita-n2j.audio`, with a
20 ms buffer. Both take address and port from `~/.config/a3/osc.env`
(`EnvironmentFile=`), which `a3-osc-render user` writes from the one truth.
Both wait two seconds, restart two seconds after any exit — zita can end with
status 0 — and never give up (`StartLimitIntervalSec=0`). The channels and ports are on the
{doc}`Patchbay page <../ressources/patchbay>`.

## `a3-bar-per-workspace.service` — i3bar on the tool workspaces

Runs `~/.local/bin/a3-bar-per-workspace.py` on display `:0`, after
`a3-wait-for-the-screen` has seen the screen settle. i3 has no bar per
workspace, so it follows i3's workspace events and sets the bar's mode: shown
on workspace 3 and up, hidden on 1 and 2 (see
[The screen](#core-config-screen)). It restarts whenever it ends, since an
i3 restart ends the event stream.

## `a3-user-install.service` — the user-side installer

Runs `recipes/user_install.sh` once with `bash -e`; described under
[a3-user-install.service](#core-user-install). The postinst starts it on
every install.

(core-system-units)=

## System units

In `/etc/systemd/system/`, installed by dpkg as conffiles.

| Unit | What it does | Enabled by the postinst |
| :--- | :--- | :--- |
| `x11vnc.service` | runs `x11vnc` as `aaa` on display `:0`, five seconds after `graphical.target`, shared and kept open across clients (`-shared -forever`); restarts on failure. The way to the Core's screen without a monitor | yes |
| `set_irq_prio.service` | once at boot (after `multi-user.target`), gives the USB controller's interrupt threads (`irq/…-xhci_hcd`) realtime FIFO priority 95 — the USB sound card's interrupts come before everything else | yes |
| `vnc-display.service` | runs `recipes/vnc-display.sh`: if any HDMI or DisplayPort connector reports a monitor, moves `/etc/X11/xorg.conf.d/10-headless.conf` aside to `.bak`; if none does, moves a `.bak` back | **no** — shipped only |

`x11vnc` is a network service. Its port is set on its command line in the
unit, not in `a3-osc.json`.

Over VNC you reach:

- QjackCtl, for patching
- REAPER's arrangement, for recording
- REAPER's mixer

The other services the package relies on are Debian's own: the postinst
enables `systemd-networkd` (when it configures the network), and LightDM logs
`aaa` in to i3 (see [Under /etc](#core-etc)).

