(core-files)=

# A³ Core files

How a file arrives decides what an update does to it:

| How | What | On every update |
| :--- | :--- | :--- |
| **dpkg** | everything in the package tree | replaced with the package's version |
| **dpkg, conffile** | the files under `/etc` listed in `DEBIAN/conffiles` | kept if you changed them; dpkg asks |
| **postinst, file by file** | `~/.local/share/a3-core/config/*` → `~/.config/` | new files arrive; a differing file is replaced only if its part is chosen, after a backup (see [step 4](#core-postinst)) |

Written rather than copied: network files, `~/.config/a3/network.json` (once),
headless X config, `~/.config/a3/osc.env`, the beat-analyzer's
`.env` block.

**Edit the package, not the machine**, except where noted: a replaced file
loses local edits.

(core-the-one-truth)=

## The one truth: `/usr/share/a3/a3-osc.json` and `~/.config/a3/network.json`

| File | Owner | Edit |
| :--- | :--- | :--- |
| `/usr/share/a3/a3-osc.json` | the package: the contract | never on the machine; change a3-core and reinstall |
| `~/.config/a3/network.json` | you: `hosts`, `network`, optional `meters`; created once | edit, then restart Core |

How they join and propagate: {ref}`Where addresses and ports live <osc-truth>`.

**Tuning the meters on the rig:** a `meters` block joins key by key over the
package's {ref}`ballistics <osc-meter-ballistics>`, so this changes the hold
and nothing else:

```json
{ "hosts": {"...": "..."}, "network": {"...": "..."}, "meters": { "peak_hold_seconds": 2.5 } }
```

Keys: `attack_ms` (≥ 0), `release_db_per_second` (> 0), `peak_hold_seconds`
(≥ 0). Restart Core; the new fingerprint makes the desk, A³ Motion and
StemDeck refetch and restart. A wrong type, out-of-range value or unknown key
refuses the whole block: Core logs `network.json's meters refused, the
package's are used: …` and keeps hosts and network.

(core-etc)=

## Under `/etc`

Conffiles: dpkg keeps a version you changed.

| File | What it does |
| :--- | :--- |
| `/etc/default/grub` | 1 s menu; `threadirqs cpufreq.default_governor=performance reboot=cold` (prioritisable IRQ threads, full CPU speed, cold reboot) |
| `/etc/lightdm/lightdm.conf.d/99-a3-core.conf` | autologin `aaa` into `i3`; `logind-check-graphical=false` |
| `/etc/security/limits.d/audio.conf` | `audio` group: RT up to 95, unlimited memlock, nice −19 (shipped by the package) |
| `/etc/systemd/system/*.service` | the three [system units](#core-system-units) |

Written by the postinst, not shipped:

| File | When |
| :--- | :--- |
| `/etc/systemd/network/10-a3.network`, and `20-a3-aes67.network` with an audio socket | network answered *yes* (see [step 1](#core-postinst)) |
| `/etc/network/interfaces` | lines for the configured interfaces commented out |
| `/etc/X11/xorg.conf.d/10-headless.conf` | headless answered *yes*; renamed to `.off` on *no* |

## `~/.local/bin` — programs

Replaced on every install.

| Program | What it is |
| :--- | :--- |
| `a3-screencast` | the ffmpeg command behind `a3-screencast.service` |
| `a3-wait-for-the-screen` | waits (max 1 min) for X to report the screen, so a UI starts at the right scale |

## `~/.local/lib` — no modules any more

Core is the compiled `a3-core` program (`/usr/bin/a3-core`): there are **no Python modules** on the machine, and no `~/.venv` is
needed. Only the real-time priority shim for the audio threads,
`~/.local/lib/a3/libjack-rt-priority.so`, is built here by the postinst.

## What the a3-core program keeps

Written by the program, outside the package; an update never touches them.

| Path | What it is |
| :--- | :--- |
| `~/.local/state/a3-core/state.json` | what only Core knows (positions, 3D), for the next start |
| `~/.local/state/a3-core/evening.json` | every continuous value Core passed on, replayed after a restart |
| `~/.local/state/a3-core/seen.json` | the addresses the OSC monitor has seen (not values, not history) |
| `~/.config/a3/engine/engine.json` | the engine's settings, written by the window's **Save** |
| `~/.config/a3/core/window.settings` | the OSC MONITOR switch, written only when flipped |
| `~/.config/a3/core/departments.json` | the departments (light, video desks), written by the window's DEPARTMENTS page ([adding one](#core-subscriber)) |
| `~/.config/a3/screencast.env` | optional encoder settings for the screencast |

`$XDG_STATE_HOME` replaces `~/.local/state` where set.

## The program's files under `/usr`

Replaced on every install; not edited on the machine.

| Path | What it is |
| :--- | :--- |
| `/usr/bin/a3-core` | the program: window, Core, engine |
| `/usr/lib/systemd/user/` | every A³ user unit: `a3-engine`, `a3-core`, `a3-core-window`, `a3-clock` from `a3-core-app`; `a3-main`, `a3-aes67`, `a3-screencast`, `a3-bar-per-workspace` and the drop-ins on StemDeck's and the analyzer's units from `a3-core` ([where the units live](#core-units-one-place)) |
| `/usr/share/a3-engine/engine.json`, `spatial/` | the engine's default settings and the speaker layouts with the IEM data. `~/.config/a3/engine/engine.json` (written by the window's Save) overrides the settings |
| `/usr/share/a3/a3-osc.json` | the one truth ([above](#core-the-one-truth)) |
| `/usr/share/doc/a3-core/copyright` | the licence texts |

## `~/.local/share/a3-core` — the package's own data

Replaced on every install. Not meant to be edited on the machine.

| Path | What it is |
| :--- | :--- |
| `osc-register.json` | all addresses, generated by `tools/osc_register.py`; never hand-edited |
| `x11/10-headless.conf` | the dummy-screen X config the headless question copies to `/etc/X11/xorg.conf.d/` |
| `docs/channelmap.ods` | a channel-map spreadsheet |
| `recipes/vnc-display.sh` | the script behind `vnc-display.service` |
| `recipes/a3vnc.sh` | opens a VNC viewer on the Core, from another machine |
| `recipes/clear_home.sh` | **deletes** `~/.local`, `~/.config/systemd`, `~/beat-analyzer`. Run by nothing |
| `config/` | the configuration tree copied into `~/.config` — next section |

(core-config-tree)=

## `~/.config` — the configuration

Copied file by file ([step 4](#core-postinst)). **These are tuned at the
rig**; an install replaces a tuned file when its part is chosen (backup in
`~/.config/a3-replaced/`). Keep a tuning by taking it into the package
([Machine and package stay one](#core-mirror)).

| In `~/.config` | What it is |
| :--- | :--- |
| `i3/config` | the window manager — see [The screen](#core-config-screen) |
| `pipewire/` | `pipewire.conf.d/10-a3-rate.conf`, `jack.conf.d/10-a3.conf`, `pipewire-aes67.conf.d/10-a3-rate.conf`: rate, quantum and the AES67 instance |
| `systemd/user/` | nothing shipped: only this machine's own drop-ins ([where the units live](#core-units-one-place)) |

Written, not copied: `a3/osc.env`.

REAPER, its project template and presets, the IEM and QjackCtl settings and the
patchbay are no longer shipped. On a machine that had them, the upgrade moved
the units and the patchbay into `~/.config/a3-replaced/` ([step 9](#core-postinst));
`~/.config/REAPER` and `~/.local/opt/REAPER` are the maintainer's own and are
deleted by hand, if at all.

(core-mirror)=

## Machine and package stay one

What the development Core runs is what the package ships.
`tools/mirror_check.py` (a3-core) lists shipped files changed on the machine
but not in the package; the push script **stops when they differ** (an older
copy is reported as behind, not blocking). `--take` copies the machine's file
into the package — check each diff. `tools/config-status.py` compares the
`$HOME` files both ways (`--export`, `--install`).

(core-config-screen)=

## The screen: i3 workspaces and the bar

`~/.config/i3/config` names the workspaces and places each program:

| Workspace | Rule |
| :--- | :--- |
| `1:MOTION` | `for_window [class="A3 Motion UI"]` |
| `2:STEMDECK` | `assign [class="StemDeck"]`; the main window (`title="^StemDeck$"`) gets `border none`, every other StemDeck window floats |
| `3:ENGINE` | `for_window [class="a3-core"]`: the program's window |
| `4` | no rule; the number is kept free |
| `5:SCARLETT` | `for_window [title="Scarlett 18i20 USB"]` |

Both touch apps' switches and i3bar read the names from i3, so renaming here
needs no app change; `$mod+1` … `$mod+5` still work. StemDeck's main window is
tiled borderless (i3 full screen would make its dialogs full screen); dialogs
float.

**The bar** (`bar { id a3 … }`, top, `strip_workspace_numbers yes`,
`i3status`): `a3-bar-per-workspace.service` sets `dock` on workspaces 3+,
`invisible` on 1–2, where Motion and StemDeck fill the screen.

**StemDeck** runs as `stemdeck.service` from the StemDeck repository
({ref}`Always running on the Core <stemdeck-on-the-core>`). Not restarted
during a set: it causes xruns.

The i3 config also disables screen saver and power management, re-sets the
touch panel's output at start (off/on, rotated: a first mode-set can leave it
black) and hides the cursor on touch.
