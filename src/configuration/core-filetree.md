(core-files)=

# A³ Core files

Three ways a file reaches the machine, and they behave differently on an
update:

| How | What | On every update |
| :--- | :--- | :--- |
| **dpkg** | everything in the package tree | replaced with the package's version |
| **dpkg, conffile** | the files under `/etc` listed in `DEBIAN/conffiles` | kept if you changed them; dpkg asks |
| **postinst, file by file** | `~/.local/share/a3-core/config/*` → `~/.config/` | new files arrive; a differing file is replaced only if its part is chosen, after a backup (see [step 4](#core-postinst)) |

Plus what the postinst and `user_install.sh` *write* rather than copy: the
network files, `~/.config/a3/network.json` (once, never overwritten), the headless X config, `~/.venv`, `~/.config/a3/osc.env`, the
beat-analyzer's `.env` block, REAPER and the plug-ins.

**Edit the package, not the machine** — except where the tables below say
otherwise. A file that is replaced on update loses a local edit at the next
install.

## The one truth: `/usr/share/a3/a3-osc.json` and `~/.config/a3/network.json`

The truth is in two parts.

`/usr/share/a3/a3-osc.json` is the **contract**: every OSC address, its
arguments, its senders and receivers, the ports, the routes and the forty
meters, with the package's default hosts and network. Replaced on every
install. **Do not edit it on the machine:** change it in the a3-core
repository and install the package again.

`~/.config/a3/network.json` is the **network**, and it is yours: the `hosts`
(the machines' addresses) and `network` (Core's own interface, bridge,
gateway, DNS). The installer creates it once from the package's values and
never overwrites it. Core joins it over the contract key by key; a host the
file does not name comes from the package. A file that does not parse, or
lacks the `hosts` or `network` object, is refused: Core says why in its
journal and uses the package's values.

**To change an address:** edit `network.json`, restart Core. The beat-analyzer
and zita addresses are rendered at Core's start, and the desk restarts itself
within seconds. How Core serves the joined truth is in
{ref}`Where addresses and ports live <osc-truth>`.

(core-etc)=

## Under `/etc`

All of these are conffiles: dpkg installs them, and keeps a version you
changed.

| File | What it does |
| :--- | :--- |
| `/etc/default/grub` | one-second boot menu; kernel command line `threadirqs cpufreq.default_governor=performance reboot=cold` — interrupts in threads (so they can be prioritised), CPUs at full speed, cold reboot. `update-grub` runs in the postinst |
| `/etc/lightdm/lightdm.conf.d/99-a3-core.conf` | logs `aaa` in automatically into the `i3` session; `logind-check-graphical=false` |
| `/etc/security/limits.d/audio.conf` | the `audio` group may use realtime priority up to 95, lock unlimited memory, nice down to −19. It is the file `dpkg-reconfigure jackd2` manages |
| `/etc/rtirq.conf` | interrupt priorities for `snd-usb-audio`, `usb`, `xhci_hcd` (90, stepping down by 5, lowest 51), unthreaded where the kernel allows. Read by `rtirq`, which the package does not depend on |
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
| `a3-osc-render` | writes the one truth out as text: `user` for `osc.env` and the beat-analyzer's block, `network` for the postinst's default network |
| `a3-bar-per-workspace.py` | shows i3bar on the tool workspaces, run by `a3-bar-per-workspace.service` |
| `a3-wait-for-the-screen` | waits until X reports the screen the app will run on, so a UI does not start at the wrong scale; at most a minute, then it starts anyway and says so in the journal |
| `a3-interface.py` | an older small launcher window (start/stop REAPER, media folders); started by no unit |
| `reaper` | a link to `~/.local/opt/REAPER/reaper`, made by `user_install.sh` |

## `~/.local/lib` — Core's modules

The Python modules `a3-core.py` and `a3-osc-render` import; replaced on every
install. Each does one thing:

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
| `layout.json` | the map between an A³ channel and the REAPER project: track numbers, FX slots, plug-in parameter numbers (`gain_params`, `fx_params`), REAPER's and the IEM plug-ins' addresses. It ships beside the REAPER template it has to agree with, and an update replaces it **on purpose**: a track number that no longer matches the shipped project is worse than a lost local edit |
| `curves-golden.json` | the value curves as they were recorded, which is what lets Core turn a REAPER value back into an A³ value |
| `osc-register.json` | every address the system can speak, generated from `a3-osc.json` by `tools/osc_register.py` — never edited by hand |
| `web/index.html` | Core's window onto the OSC traffic |
| `x11/10-headless.conf` | the dummy-screen X config the headless question copies to `/etc/X11/xorg.conf.d/` |
| `docs/channelmap.ods` | a channel-map spreadsheet |
| `recipes/user_install.sh` | the [user-side installer](#core-user-install) |
| `recipes/requirements.txt` | the Python packages for `~/.venv` |
| `recipes/vnc-display.sh` | the script behind `vnc-display.service` |
| `recipes/a3vnc.sh` | opens a VNC viewer on the Core, from another machine |
| `recipes/clear_home.sh` | **deletes** `~/.config/REAPER`, `~/.local`, `~/.config/rncbc.org`, `~/.config/systemd` and `~/beat-analyzer` — a reset to before the install. Not run by anything |
| `config/` | the configuration tree copied into `~/.config` — next section |

(core-config-tree)=

## `~/.config` — the configuration

From `~/.local/share/a3-core/config/`, installed file by file (see
[step 4](#core-postinst)). **These are the files that are tuned at the rig** —
and an install replaces a tuned file when its part is chosen, keeping the old
one in `~/.config/a3-replaced/`. Take a tuning worth keeping into the package
(see [Machine and package stay one](#core-mirror)).

| In `~/.config` | What it is |
| :--- | :--- |
| `REAPER/ProjectTemplates/a3-reaper.RPP` | the REAPER project every start opens; the template itself starts the three outputs muted (not `a3-reaper.service`). It is the package's version only if you took it at the replace-config question — tracks, routing, plug-ins and their state. See [REAPER](#core-reaper) |
| `REAPER/OSC/a3-core.ReaperOSC` | REAPER's OSC pattern file: which REAPER parameters answer to which OSC address |
| `REAPER/Effects/a3crossover.jsfx` | a JSFX crossover effect |
| `REAPER/FXChains/purestgain_8.RfxChain` | an FX chain |
| `REAPER/presets/*.ini` | plug-in presets: the IEM encoders, decoders and DualDelay, Airwindows Consolidated, the container |
| `REAPER/.config.RPP` | a REAPER project file shipped next to the template |
| `IEM/4sp_a3.json` | the loudspeaker layout for the AllRADecoder |
| `IEM/AllRADecoder.settings`, `IEM/Decoder.settings` | the IEM decoders' own settings |
| `rncbc.org/QjackCtl.conf` | QjackCtl's settings |
| `rncbc.org/a3-patchbay.xml` | the JACK patchbay `qjackctl.service` loads: which client connects where |
| `i3/config` | the window manager — see [The screen](#core-config-screen) |
| `systemd/user/*.service` | the [user units](#core-services), with `a3-core.service.d/cpu.conf` |

Not copied but written into `~/.config` by the installation:
`a3/osc.env` (by `a3-osc-render user`) and two keys in `REAPER/reaper.ini` (by
`user_install.sh`).

## Installed by `user_install.sh`

| Path | What |
| :--- | :--- |
| `~/.local/opt/REAPER/` | REAPER |
| `~/.local/vst/TAL-Filter-2.vst3` | TAL-Filter-2 |
| `~/.local/clap/airwindows.clap` | Airwindows Consolidated |
| `~/a3-system/beat-analyzer/build/` | the built beat-analyzer, and its `.env` if there was none |

(core-mirror)=

## Machine and package stay one

The development Core is mirrored back into the package: what it runs is what
the package should ship. `tools/mirror_check.py` in the a3-core repository
lists every shipped file that is changed on the machine and not in the
package; the push script runs it before every push and **stops when the
machine and the package differ**. A file that is merely an *older* version of
the package's own is named as behind instead and does not stop a push.
`mirror_check.py --take` copies the machine's version into the package; check
each diff before taking it.

`tools/config-status.py` is the same comparison for the two ways the package
writes into `$HOME`, with `--export` (machine → repository) and `--install`
(repository → machine).

(core-config-screen)=

## The screen: i3 workspaces and the bar

The i3 config (`~/.config/i3/config`, shipped as
`~/.local/share/a3-core/config/i3/config`) names the rig's workspaces and
moves each program's window to its own:

| Workspace | Rule |
| :--- | :--- |
| `1:MOTION` | `for_window [class="A3 Motion UI"]` |
| `2:STEMDECK` | `assign [class="StemDeck"]`; the main window (`title="^StemDeck$"`) gets `border none`, every other StemDeck window floats |
| `3:REAPER` | `for_window [class="REAPER"]` |
| `4:QJACKCTL` | `for_window [class="QjackCtl"]` |
| `5:SCARLETT` | `for_window [title="Scarlett 18i20 USB"]` |

The names are what the two touch apps' workspace switch and i3bar show; both
read them from i3 (`i3-msg -t get_workspaces`), so a workspace renamed or
added here shows up without a change to either app. `workspace number N`
still finds them, as do `$mod+1` … `$mod+5`.

StemDeck's main window is tiled without a border instead of set to i3's full
screen: each dialog StemDeck opened ended the full screen. Its dialogs float
over it.

**The bar.** i3bar (`bar { id a3 … }`) sits at the top, with
`strip_workspace_numbers yes` and `status_command i3status`. i3 has no bar
per workspace, so `a3-bar-per-workspace.service` follows i3's workspace
events and sets the bar's mode: `dock` on workspace 3 and up, `invisible` on
1 and 2, where A³ Motion and StemDeck fill the screen and switch between each
other themselves.

**StemDeck** runs as `stemdeck.service`, shipped in the StemDeck repository
(`.config/systemd/user/`), not in the a3-core package — see
{ref}`Always running on the Core <stemdeck-on-the-core>`. Its
`tools/rig-keep-the-screen.sh` puts back the workspace that was showing when
StemDeck (re)starts. A StemDeck restart changes the JACK graph and costs a
burst of xruns: not during a set.

The i3 config also switches the screen saver and power management off,
re-sets the touch panel's output at start-up (off and on again, rotated, as a
workaround for a first mode-set that sometimes leaves the panel black) and
hides the mouse cursor on touch.

(core-reaper)=

## REAPER: the template, the plug-ins, the routing

### IEM Plug-in Suite

[IEM Plug-in Suite](https://plugins.iem.at/) VST3 plugins for 3D audio
processing, from Debian (`iem-plugin-suite-vst3`). What the shipped project
actually loads:

| Plugin | What it does here |
| :--- | :--- |
| MultiEncoder | Where a channel's sound sits in the room. A³ Core writes `azimuth` and `elevation` straight to the plug-in's **own OSC receiver** (`iem.multiencoder-1` … `-3` in the one truth), never through a REAPER track — which is why REAPER can never report a position back, and why Core has to remember it |
| AllRADecoder | Must be configured to fit your speaker setup (`IEM/4sp_a3.json`) |
| BinauralDecoder | For headphones |
| SimpleDecoder | |
| EnergyVisualizer | Sends the energy field to A³ Motion's `motion.energy` listener, once its "OSC send" is switched on in the lower left of the plug-in |
| DualDelay | On the FX bus, following the beat-analyzer's tempo, which Core passes to its receiver `dualdelay.osc` |

```{warning}
**Two of these have a receiver that has to be opened by hand**, and nothing
says so when it is shut. The DualDelay needs *Listen to port* → the port of
`dualdelay.osc` in `a3-osc.json` → **OPEN** in its status line, with `Sync`
**off**; the EnergyVisualizer needs its OSC send switched on. The
MultiEncoders' receivers are set inside the plug-ins the same way. All of it
is plug-in state and lives in the REAPER project, not in any repository.
```

### TAL-Filter-2

- [TAL-Filter-2](https://tal-software.com/products/tal-filter) resonance
  filter, one per channel — the high-pass and low-pass the FX key switches
  between. Installed by `user_install.sh`.

### Airwindows Consolidated

- [Airwindows](https://www.airwindows.com/) plugins are loaded through the
  **Consolidated** container rather than individually, which is why one
  instance has fourteen parameters and the gain of each sits on parameter
  1, 15, 29 and so on. `gain_params` in `layout.json` is that list.
  Installed by `user_install.sh`.
- Carries the channel gains, the EQ and the bus volumes.

### Inputs and outputs

The audio inputs and outputs — REAPER's channel map, the VU meters, the
beat-analyzer's, zita's and StemDeck's ports, and the patchbay's sockets —
are all on one page, {doc}`../ressources/patchbay`. What happens inside
REAPER between its inputs and its outputs is not documented there or here
yet; it will be documented separately.

