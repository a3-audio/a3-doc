(core-files)=

# A³ Core files

How a file arrives decides what an update does to it:

| How | What | On every update |
| :--- | :--- | :--- |
| **dpkg** | everything in the package tree | replaced with the package's version |
| **dpkg, conffile** | the files under `/etc` listed in `DEBIAN/conffiles` | kept if you changed them; dpkg asks |
| **postinst, file by file** | `~/.local/share/a3-core/config/*` → `~/.config/` | new files arrive; a differing file is replaced only if its part is chosen, after a backup (see [step 4](#core-postinst)) |

Written rather than copied: network files, `~/.config/a3/network.json` (once),
headless X config, `~/.venv`, `~/.config/a3/osc.env`, the beat-analyzer's
`.env` block, REAPER and plug-ins.

**Edit the package, not the machine**, except where noted: a replaced file
loses local edits.

## The one truth: `/usr/share/a3/a3-osc.json` and `~/.config/a3/network.json`

| File | Owner | Edit |
| :--- | :--- | :--- |
| `/usr/share/a3/a3-osc.json` | the package: the contract | never on the machine; change a3-core and reinstall |
| `~/.config/a3/network.json` | you: `hosts`, `network`; created once | edit, then restart Core |

How they join and propagate: {ref}`Where addresses and ports live <osc-truth>`.

(core-etc)=

## Under `/etc`

Conffiles: dpkg keeps a version you changed.

| File | What it does |
| :--- | :--- |
| `/etc/default/grub` | 1 s menu; `threadirqs cpufreq.default_governor=performance reboot=cold` (prioritisable IRQ threads, full CPU speed, cold reboot) |
| `/etc/lightdm/lightdm.conf.d/99-a3-core.conf` | autologin `aaa` into `i3`; `logind-check-graphical=false` |
| `/etc/security/limits.d/audio.conf` | `audio` group: RT up to 95, unlimited memlock, nice −19 (managed by `dpkg-reconfigure jackd2`) |
| `/etc/rtirq.conf` | IRQ priorities for `snd-usb-audio`, `usb`, `xhci_hcd` (90, −5 steps, lowest 51); for `rtirq`, not a dependency |
| `/etc/systemd/system/*.service` | the three [system units](#core-system-units) |

Written by the postinst, not shipped:

| File | When |
| :--- | :--- |
| `/etc/systemd/network/a3.network`, or the three `*-a3-bridge*` files | network answered *yes* (see [step 1](#core-postinst)) |
| `/etc/network/interfaces` | lines for the configured interfaces commented out |
| `/etc/X11/xorg.conf.d/10-headless.conf` | headless answered *yes*; renamed to `.off` on *no* |

## `~/.local/bin` — programs

Replaced on every install.

| Program | What it is |
| :--- | :--- |
| `a3-core.py` | the OSC router, run by `a3-core.service` |
| `a3-osc-render` | the truth as text: `user` (`osc.env`, analyzer block), `network` (postinst default) |
| `a3-bar-per-workspace.py` | i3bar per workspace |
| `a3-wait-for-the-screen` | waits (max 1 min) for X to report the screen, so a UI starts at the right scale |
| `a3-interface.py` | old launcher window; started by nothing |
| `reaper` | link to `~/.local/opt/REAPER/reaper` |

## `~/.local/lib` — Core's modules

Imported by `a3-core.py` and `a3-osc-render`; replaced on install.

| Module | What it does |
| :--- | :--- |
| `a3_osc.py` | reads the one truth |
| `a3_osc_render.py` | writes the one truth out for what cannot read JSON |
| `a3_core_layout.py` | where the OSC addresses and REAPER track numbers live (`layout.json`) |
| `a3_core_reaper.py` | what Core asks REAPER to do beyond setting values |
| `a3_core_reverse.py` | turns REAPER's feedback back into an A³ message |
| `a3_core_curves.py` | turns a REAPER value back into the A³ value that produced it |
| `a3_core_crossfade.py` | how much of a channel moves: the 3D law (the band's gain; the steady rest stays at 0 dB) and the filter messages for both Isolators |
| `a3_core_buttons.py` | what a button message asks for, when two senders mean two things |
| `a3_core_echo.py` | tells Core's own echo apart from news |
| `a3_core_tempo.py` | passes the tempo on, but not every flicker |
| `a3_core_subscribers.py` | who gets told, and how a new one is added |
| `a3_core_devices.py` | which truth each device speaks, and whether it is Core's own |
| `a3_core_state.py` | what only Core knows, kept across a restart |
| `a3_core_evening.py` | the evening as Core saw it, for the next start |
| `a3_core_snapshot.py` | saves in between, so a power cut does not cost the evening |
| `a3_core_gate.py` | opens main, booth, phones and the main meter's track after the start-up recall, with a 1 s fade. See [the silent start](#core-silent-start) |
| `a3_core_recall.py` | Core saying its state again |
| `a3_core_startup.py` | what Core has to say at start-up so everyone means the same |
| `a3_core_seen.py` | the addresses Core has seen, kept across a restart |
| `a3_core_register.py` | the catalogue of addresses the system can speak, held against the traffic |
| `a3_core_traffic.py` | what went past Core, counted |
| `a3_core_web.py` | the window onto what Core is passing about |

## `~/.local/share/a3-core` — the package's own data

Replaced on every install. Not meant to be edited on the machine.

| Path | What it is |
| :--- | :--- |
| `layout.json` | A³ channel ↔ REAPER: tracks, FX slots, parameters (`gain_params`, `fx_params`), plug-in addresses. Replaced **on purpose**, to match the shipped template |
| `curves-golden.json` | recorded value curves, to turn REAPER values back into A³ values |
| `osc-register.json` | all addresses, generated by `tools/osc_register.py`; never hand-edited |
| `web/index.html` | Core's window onto the OSC traffic |
| `x11/10-headless.conf` | the dummy-screen X config the headless question copies to `/etc/X11/xorg.conf.d/` |
| `docs/channelmap.ods` | a channel-map spreadsheet |
| `recipes/user_install.sh` | the [user-side installer](#core-user-install) |
| `recipes/requirements.txt` | the Python packages for `~/.venv` |
| `recipes/vnc-display.sh` | the script behind `vnc-display.service` |
| `recipes/a3vnc.sh` | opens a VNC viewer on the Core, from another machine |
| `recipes/clear_home.sh` | **deletes** `~/.config/REAPER`, `~/.local`, `~/.config/rncbc.org`, `~/.config/systemd`, `~/beat-analyzer`. Run by nothing |
| `config/` | the configuration tree copied into `~/.config` — next section |

(core-config-tree)=

## `~/.config` — the configuration

Copied file by file ([step 4](#core-postinst)). **These are tuned at the
rig**; an install replaces a tuned file when its part is chosen (backup in
`~/.config/a3-replaced/`). Keep a tuning by taking it into the package
([Machine and package stay one](#core-mirror)).

| In `~/.config` | What it is |
| :--- | :--- |
| `REAPER/ProjectTemplates/a3-reaper.RPP` | the project every start opens, outputs muted ([REAPER](#core-reaper)) |
| `REAPER/OSC/a3-core.ReaperOSC` | REAPER's OSC pattern file |
| `REAPER/Effects/a3crossover.jsfx` | a JSFX crossover effect |
| `REAPER/FXChains/purestgain_8.RfxChain` | an FX chain |
| `REAPER/presets/*.ini` | plug-in presets: the IEM encoders, decoders and DualDelay, Airwindows Consolidated, the container |
| `REAPER/.config.RPP` | a REAPER project file shipped next to the template |
| `IEM/4sp_a3.json` | the loudspeaker layout for the AllRADecoder |
| `IEM/AllRADecoder.settings`, `IEM/Decoder.settings` | the IEM decoders' own settings |
| `rncbc.org/QjackCtl.conf` | QjackCtl's settings |
| `rncbc.org/a3-patchbay.xml` | the JACK patchbay |
| `i3/config` | the window manager — see [The screen](#core-config-screen) |
| `systemd/user/*.service` | the [user units](#core-services), with `a3-core.service.d/cpu.conf` |

Written, not copied: `a3/osc.env` and two keys in `REAPER/reaper.ini`.

## Installed by `user_install.sh`

| Path | What |
| :--- | :--- |
| `~/.local/opt/REAPER/` | REAPER |
| `~/.local/vst/TAL-Filter-2.vst3` | TAL-Filter-2 |
| `~/.local/clap/airwindows.clap` | Airwindows Consolidated |
| `~/a3-system/beat-analyzer/build/` | the built beat-analyzer, and its `.env` if there was none |

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
| `3:REAPER` | `for_window [class="REAPER"]` |
| `4:QJACKCTL` | `for_window [class="QjackCtl"]` |
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

(core-reaper)=

## REAPER: the template, the plug-ins, the routing

### IEM Plug-in Suite

[IEM Plug-in Suite](https://plugins.iem.at/), from Debian. Used:

| Plugin | What it does here |
| :--- | :--- |
| MultiEncoder | channel position; Core writes `azimuth`/`elevation` to its **own OSC receiver** (`iem.multiencoder-1` … `-3`), bypassing REAPER — so Core must remember positions |
| AllRADecoder | fit to your speakers (`IEM/4sp_a3.json`) |
| BinauralDecoder | headphones |
| SimpleDecoder | |
| EnergyVisualizer | energy field to `motion.energy`, once "OSC send" is on |
| DualDelay | FX bus; tempo from Core on `dualdelay.osc` |

```{warning}
**Receivers to open by hand, silently shut otherwise:** DualDelay *Listen to
port* (`dualdelay.osc`'s port) → **OPEN**, `Sync` **off**; EnergyVisualizer OSC
send on; MultiEncoder receivers. This is plug-in state in the REAPER project,
not in any repository.
```

### TAL-Filter-2

[TAL-Filter-2](https://tal-software.com/products/tal-filter), one per channel:
the HPF/LPF the FX key switches. From `user_install.sh`.

### Airwindows Consolidated

[Airwindows](https://www.airwindows.com/) through the **Consolidated**
container: 14 parameters per instance, gains on 1, 15, 29, … (`gain_params` in
`layout.json`). Channel gains, EQ, bus volumes. From `user_install.sh`.

### Inputs and outputs

All on {doc}`../ressources/patchbay`. REAPER's internal routing is not
documented yet.
