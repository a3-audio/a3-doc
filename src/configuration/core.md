# A³ Core Configuration

A³ Core is one Debian package, `a3-core`. These pages follow it onto a machine
in the order it happens:

1. [The Debian package](#core-package) — what it is, how it gets there, what
   it needs.
2. [What the installation does](#core-postinst) — the package's install
   script, step by step.
3. {doc}`The services <core-systemd>` (its own page) — every systemd unit
   it ships, and what each one starts.
4. {doc}`The files <core-filetree>` (its own page) — every file the
   installation puts on the machine, where it lands, and whether you are
   meant to edit it.

The usual way onto a machine is the a3-system {doc}`installer <install>`
(role Core): it builds this package from the version's a3-core, asks the
package's questions up front and installs it. The package then does what this
page describes either way.

| Part | What it is |
| :--- | :--- |
| OS | Debian testing with a Linux realtime kernel |
| Window manager | i3, with named workspaces — see [The screen](#core-config-screen) |
| Audio backend | JACK and REAPER, with the IEM plug-in suite |
| VU metering | the beat-analyzer — see the {ref}`VU map <core-vu-map>` |
| OSC router | `~/.local/bin/a3-core.py`, started by a `systemd --user` service |

```{note}
**No addresses and no ports on this page.** Every OSC address, port and IP of
the system is written once, in `a3-osc.json`: the contract in
`/usr/share/a3/a3-osc.json`, which this package installs, and the network
(hosts and Core's own interface) in `~/.config/a3/network.json`, which is
yours — see {ref}`Where addresses and ports live <osc-truth>`. Where a
program below talks to the network, this page names *what* it talks to, by
the name the file gives it (`core.osc`, `motion.energy`, …), and the file says
where that is.
```

(core-package)=

## 1. The Debian package

The package is built from the
[a3-core](https://github.com/a3-audio/a3-core) repository: that repository
*is* the deployment, the package tree under
`platform-config/debian-x86_64/a3-core/`, not application source. Every path
in that tree is where the file lands on the machine — `home/aaa/.local/bin/`
becomes `/home/aaa/.local/bin/`, `etc/` becomes `/etc/`. The package is built
for one user, **`aaa`**: its paths name that home directory.

### Before you start

- A blank Debian installation, without a desktop environment, with an SSH
  server.
- A user named `aaa`.
- `sudo` for that user. As root: `apt install sudo wget`, then
  `/usr/sbin/usermod -aG sudo aaa`; log out and back in.

### Installing

With the {doc}`installer <install>`, or — for the newest package from the
apt archive, on a3-core's `main` whatever version the rest is on — one
command, as `aaa`:

```sh
wget -qO- "https://raw.githubusercontent.com/a3-audio/a3-core/main/platform-config/debian-x86_64/a3-core_install.sh" | sudo bash
```

The install script (`platform-config/debian-x86_64/a3-core_install.sh`) has to
run as root and does four things:

1. Updates the package lists and installs `wget`, `gnupg` and
   `ca-certificates`.
2. Fetches the package archive's signing key and installs it as
   `/usr/share/keyrings/a3-core-archive-keyring.gpg`.
3. Adds the A³ archive as an apt source,
   `/etc/apt/sources.list.d/a3-core.sources`, pointing at
   `https://a3-audio.github.io/a3-core/`.
4. **Switches the machine to Debian testing.** It moves an existing
   `/etc/apt/sources.list` aside to `/etc/apt/sources.list.bck` and writes
   `/etc/apt/sources.list.d/debian.sources` with `testing`,
   `testing-security` and `testing-updates` (components `main` and
   `non-free-firmware`). Then `apt update`, `apt full-upgrade -y`,
   `apt install -y a3-core`, and finally `dpkg-reconfigure a3-core`.

The script exports `DEBIAN_FRONTEND=noninteractive`, so the installation's
questions (next section) take their stored or default answers instead of
being asked. Answer them afterwards yourself:

```sh
sudo dpkg-reconfigure a3-core     # network, bridge, headless screen
sudo dpkg-reconfigure jackd2      # realtime priorities for JACK
```

Once the apt source is in place, an update is an ordinary
`sudo apt update && sudo apt install a3-core`.

### The version

The archive is rebuilt by a GitHub workflow on every push to `main`. The
package version is set by that workflow, not by hand: the last `v*` tag plus
the commits since it — `v03.0` with 63 commits on top is `03.0+63`. It is
written into `DEBIAN/control` before the build. The `1.0.0` in the checked-in
`control` is only what a package built by hand gets, and apt treats it as
older than anything published. `python3 tools/package_version.py` in the
repository prints the version the next build will carry.

### What it depends on

`DEBIAN/control` pulls in, by purpose:

| Purpose | Packages |
| :--- | :--- |
| Realtime and audio | `linux-image-rt-amd64`, `jackd2`, `libjack-jackd2-dev`, `jack-example-tools`, `qjackctl`, `zita-ajbridge`, `zita-njbridge`, `libsamplerate0-dev` |
| 3D audio | `iem-plugin-suite-vst3` |
| Screen | `lightdm`, `i3`, `i3status`, `xinit`, `xserver-xorg-video-dummy`, `x11vnc`, `x11-utils`, `x11-xserver-utils`, `libgtk2.0-0`, `pcmanfm` |
| Python (Core) | `python3`, `python3-pip`, `python3-venv`, `python3-rtmidi` |
| Building the beat-analyzer | `build-essential`, `cmake`, `pkg-config`, `git` |
| Tools | `systemd`, `sudo`, `curl`, `wget`, `gpg`, `unzip`, `liblo-tools`, `net-tools`, `htop`, `vim`, `tree` |

It also **conflicts with and replaces** what does not belong on a show
machine: `network-manager`, `wpasupplicant`, `modemmanager`, `dhcpcd-base`,
the Bluetooth stack (`bluetooth`, `bluez`, `bluez-obexd`, `blueman`),
`plymouth`, `cron`, `gnome-keyring` and the GNOME themes, the `gvfs` packages
and `i3lock`. Installing `a3-core` removes them.

(core-postinst)=

## 2. What the installation does

After dpkg has unpacked the files, the package's `DEBIAN/postinst` runs. It
runs on **every** install and upgrade, on a machine that may be in the middle
of a show — so most steps are written to leave alone what is already there.
In order:

### 1. The network (optional)

**"Do you want to configure networking for a3-core?"**
(`a3-core/configure-network`, default *no*). With *no*, the network is not
touched. With *yes*:

- If `a3-core/install-default-network` is *yes*, the interface, address,
  gateway, DNS and bridge are taken from the `network` section of the one
  truth (via `a3-osc-render network`), without further questions. This
  question is not shown during the install; it is *no* unless it was set
  beforehand (for example with `debconf-set-selections`).
- Otherwise it asks for the **address** (with prefix length), **gateway** and
  **DNS** — on every install, pre-filled with the stored answer, so Enter
  keeps it. An answer still on the network the rig used before September 2026
  is reset to the template's default before it is shown. Then the
  **interface** to match (asked at debconf priority *medium*, so hidden by
  default; `eno1` unless changed).
- **"Second network socket to bridge with the first"**
  (`a3-core/bridge-with`). The router has one free port, so the A³ Mixer can
  hang on the Core's second socket. Name that socket (for example `enp5s0`)
  and both sockets become one network segment, `br0`, which carries the
  Core's address. Empty means one socket. The first time it is ever asked it
  is pre-filled with the machine's other wired socket; after that the stored
  answer stands, an empty one included.

What it writes, into `/etc/systemd/network/`, for systemd-networkd:

| Answer | Files |
| :--- | :--- |
| no bridge | `a3.network` (the address on the one interface) |
| bridge | `10-a3-bridge.netdev` (`br0`, **STP on**), `20-a3-bridge-ports.network` (both sockets into `br0`), `30-a3-bridge-address.network` (the address on `br0`, also without a cable) |

Each variant removes the other's files, so answering "no bridge" is also the
way back. STP is on because once a switch is added, two cables into it are a
loop, and a loop on a show network is a broadcast storm; the price is about
thirty seconds after boot.

The interfaces it configures are then **taken out of ifupdown's hands**: their
lines in `/etc/network/interfaces` are commented out (marked
`# a3-core: networkd owns …`), not deleted, so the change can be read and
undone. With both configuring one interface, the address the machine came up
with depended on which one was first.

`systemd-networkd` is **enabled but not started**: nothing is switched
during the install, the new network applies at the next boot.

### 2. The headless screen

**"Draw to a dummy screen instead of a monitor?"**
(`a3-core/headless-display`, default *no*). Only for a Core that runs without
a monitor and is used over VNC.

- *Yes* copies `~/.local/share/a3-core/x11/10-headless.conf` to
  `/etc/X11/xorg.conf.d/10-headless.conf`. X then draws to a virtual
  1920×1080 screen on the dummy driver, and **a monitor that is plugged in
  stays black**.
- *No* renames that file to `10-headless.conf.off` if it is there and is the
  shipped one — which mends a machine an older package left on the dummy
  screen. A config somebody wrote themselves is left alone.

X reads it on its next start. Answer *no* on a machine with a screen, such as
one that also runs A³ Motion with its touch panel.

### 3. The Python environment

A virtual environment at `~/.venv`, and into it the packages in
`~/.local/share/a3-core/recipes/requirements.txt`: `numpy`, `python-osc`,
`mido`, `FreeSimpleGUI`. Core runs on this environment's Python.

### 4. The configuration, installed into `~/.config`

The package carries its configuration under `~/.local/share/a3-core/config/`
(listed in [part 4](#core-config-tree)) and installs it into `~/.config`, file
by file:

- A file that is **missing** is installed.
- A file that is **the same** is left alone.
- A file that **differs** — left over from an older a3, or edited on this
  machine — is replaced only if its part was chosen. The install asks which
  parts to replace (`a3-core/replace-config`), offering only the parts that
  differ, all of them ticked; an unattended install takes them all. The parts
  are `reaper`, `i3`, `systemd`, `qjackctl` (QjackCtl and the patchbay), `iem`
  and `other`, by the folder a file sits in.
- Every replaced file is first copied to
  `~/.config/a3-replaced/<date_time>/`, under its own path, and the install
  names it. A file whose part was not chosen stays, and is named too.

The REAPER template can differ because it was edited on this machine. The
install never stops or starts REAPER (since 2026-10-07), so a replaced
template is read at REAPER's next start: **after an upgrade, restart
`a3-main`** when you can, not mid-set.

To compare one file with the package's version, or to bring one over on
purpose, use `tools/config-status.py` from an a3-core checkout:

```sh
python3 tools/config-status.py                  # list what differs
python3 tools/config-status.py --install PATH   # repo -> machine, one file
```

`--install` shows the diff and keeps the old file. Without a path it goes
through everything that differs.

### 5. Ownership and permissions

`~/.local` and `~/.config` are given to `aaa`. Every directory in
`~/.config` is set to `0755` and every file to `0664`.

### 6. Rendering the one truth: `a3-osc-render user`

Run as `aaa`. Some programs cannot read JSON, so their addresses are written
out from the joined truth (the package's file with `~/.config/a3/network.json`
over it) as text:

- `~/.config/a3/osc.env` — the targets of the two zita units (see
  [zita-j2n and zita-n2j](#core-zita)).
- the block between `# >>> a3-osc` and `# <<< a3-osc` in the beat-analyzer's
  `~/a3-system/beat-analyzer/build/.env`, if that file exists — its OSC
  targets, its clock port, its OSC words and the Pro DJ Link ports. Only that
  block is the package's; the rest of the file is yours. A key of the truth
  found outside the block is commented out, not deleted.

If it fails, the install says so: the zita units would start without their
addresses. Core renders the same two at **its own start**, so a changed
`network.json` reaches them with Core's restart; run `a3-osc-render user` by
hand only to refresh them without restarting Core (see
{ref}`When a port or an address has to change <osc-truth>`).

### 7. System services

`systemctl enable` for `x11vnc.service` and `set_irq_prio.service` (see
[System units](#core-system-units)).

### 8. User services and the REAPER installation

`loginctl enable-linger aaa`, so the user's systemd instance runs without a
login, then — as `aaa` — `systemctl --user daemon-reload` and **start**
`a3-user-install.service`, which runs `recipes/user_install.sh` in the
background (next section). Linger is switched off again at the end.

`a3-main.service` needs no `enable` of its own: the package ships the
`default.target.wants` links for it, for both zita units and for
`a3-bar-per-workspace` in the config tree, and step 4 copies them into
`~/.config/systemd/user/` — so the rig comes up at boot. (The postinst still
carries an `enable a3-main` line, commented out; the links made it
unnecessary.)

### 9. The boot loader

`update-grub`, which picks up the kernel command line from the shipped
`/etc/default/grub` (see [Under /etc](#core-etc)).

The postinst ends with what is left to you:

```text
use 'systemctl --user status a3-user-install.service' to check status
use 'dpkg-reconfigure a3-core' to configure network and the headless screen
use 'dpkg-reconfigure jackd2' to enable rt-priority
Please Reboot or manage a3-core manually with 'systemctl --user start a3-main.service'
```

(core-user-install)=

### `a3-user-install.service`: REAPER, the plug-ins, the beat-analyzer

`~/.local/share/a3-core/recipes/user_install.sh` installs what Debian does
not carry. Because the postinst starts it on every upgrade, on a running rig,
**each component is installed only when the file it leaves behind is
missing**. Fetching them again used to empty REAPER's directory under the
running REAPER, and quietly swapped in whatever version upstream offered that
day.

| Step | What it does | Skipped when |
| :--- | :--- | :--- |
| REAPER | downloads the current Linux x86_64 release from reaper.fm, installs it into `~/.local/opt/REAPER`, links `~/.local/bin/reaper` | `~/.local/opt/REAPER/reaper` exists |
| Plug-in paths | sets two keys in `~/.config/REAPER/reaper.ini`: `vstpath` (`~/.local/vst/` and `/usr/lib/vst3/`) and `clap_path_linux-x86_64` (`~/.local/clap` and `/usr/lib/clap`); writes a stub `reaper.ini` with just those if there is none | never — but only these two keys are touched |
| TAL-Filter-2 | downloads it and installs `~/.local/vst/TAL-Filter-2.vst3` | that file exists |
| Airwindows Consolidated | downloads the latest Linux build of the `DAWPlugin` release and installs `~/.local/clap/airwindows.clap` | that file exists |
| beat-analyzer | builds `~/a3-system/beat-analyzer` with its `./build.sh`; copies `.env.example` to `build/.env` with `cp -n` | the checkout is missing, or `build/beat-analyzer` exists |

Notes:

- `reaper.ini` is the machine's — audio device, window positions — so the
  package does not ship it; it sets only the two keys REAPER needs to find
  the plug-ins. The IEM suite comes from Debian, in `/usr/lib/vst3`.
- The beat-analyzer is **not** cloned: it is built from the a3-system
  checkout, which carries it as a submodule. If that checkout is not there
  yet, the step says so and is skipped — clone a3-system (see
  {doc}`install`), then start `a3-user-install.service` again. A `build/.env` that already exists is
  never overwritten. Without one, the analyzer reaches nothing off the
  machine.
- To fetch REAPER and the plug-ins again on purpose:

  ```sh
  A3_REINSTALL=1 bash ~/.local/share/a3-core/recipes/user_install.sh
  ```

  REAPER is stopped while its files are replaced and started again
  afterwards.

### Removing the package: `postrm`

`apt purge a3-core` removes `/etc/systemd/network/a3.network`, disables
`systemd-networkd` and reloads systemd. Nothing else is undone: the bridge
files, the commented ifupdown lines, the headless X config and everything in
the home directory stay.

```{toctree}
:hidden:

core-systemd
core-filetree
```
