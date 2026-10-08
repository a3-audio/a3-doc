# A³ Core Configuration

A³ Core is one Debian package, `a3-core`. In order:

1. [The Debian package](#core-package): what it is, how to install, what it needs.
2. [What the installation does](#core-postinst): the install script, step by step.
3. {doc}`The services <core-systemd>`: every systemd unit.
4. {doc}`The files <core-filetree>`: every file, and whether to edit it.

The usual route is the a3-system {doc}`installer <install>` (role Core).

| Part | What it is |
| :--- | :--- |
| OS | Debian testing, realtime kernel |
| Window manager | i3, named workspaces ([The screen](#core-config-screen)) |
| Audio | JACK and REAPER, IEM plug-in suite |
| VU metering | the beat-analyzer ({ref}`VU map <core-vu-map>`) |
| OSC router | `~/.local/bin/a3-core.py`, a `systemd --user` service |

```{note}
**No addresses or ports here.** They are in `a3-osc.json`
({ref}`Where addresses and ports live <osc-truth>`); this page names
listeners (`core.osc`, `motion.energy`, …), the file says where they are.
```

(core-package)=

## 1. The Debian package

Built from [a3-core](https://github.com/a3-audio/a3-core), whose tree
`platform-config/debian-x86_64/a3-core/` mirrors the target paths
(`home/aaa/.local/bin/` → `/home/aaa/.local/bin/`). Built for one user,
**`aaa`**.

### Before you start

- Blank Debian, no desktop, SSH server, user `aaa`.
- `sudo` for `aaa`: as root `apt install sudo wget`,
  `/usr/sbin/usermod -aG sudo aaa`, log in again.

### Installing

With the {doc}`installer <install>`, or the newest package from a3-core's
`main`, as `aaa`:

```sh
wget -qO- "https://raw.githubusercontent.com/a3-audio/a3-core/main/platform-config/debian-x86_64/a3-core_install.sh" | sudo bash
```

`a3-core_install.sh` (as root):

1. Installs `wget`, `gnupg`, `ca-certificates`.
2. Installs the archive key as `/usr/share/keyrings/a3-core-archive-keyring.gpg`.
3. Adds `/etc/apt/sources.list.d/a3-core.sources` →
   `https://a3-audio.github.io/a3-core/`.
4. **Switches to Debian testing**: moves `/etc/apt/sources.list` to
   `.bck`, writes `debian.sources` (`testing`, `testing-security`,
   `testing-updates`; `main`, `non-free-firmware`), then `apt full-upgrade -y`,
   `apt install -y a3-core`, `dpkg-reconfigure a3-core`.

It runs non-interactively, so answer the questions afterwards:

```sh
sudo dpkg-reconfigure a3-core     # network, bridge, headless screen
sudo dpkg-reconfigure jackd2      # realtime priorities for JACK
```

Updates: `sudo apt update && sudo apt install a3-core`.

### The version

A GitHub workflow rebuilds the archive on every push to `main`. Version: last
`v*` tag plus commits since (`v03.0` + 63 = `03.0+63`), written into
`DEBIAN/control` at build. The checked-in `1.0.0` is for hand builds and is
older than anything published. `python3 tools/package_version.py` prints the
next version.

### What it depends on

| Purpose | Packages |
| :--- | :--- |
| Realtime and audio | `linux-image-rt-amd64`, `jackd2`, `libjack-jackd2-dev`, `jack-example-tools`, `qjackctl`, `zita-ajbridge`, `zita-njbridge`, `libsamplerate0-dev` |
| 3D audio | `iem-plugin-suite-vst3` |
| Screen | `lightdm`, `i3`, `i3status`, `xinit`, `xserver-xorg-video-dummy`, `x11vnc`, `x11-utils`, `x11-xserver-utils`, `libgtk2.0-0`, `pcmanfm` |
| Python (Core) | `python3`, `python3-pip`, `python3-venv`, `python3-rtmidi` |
| Building the beat-analyzer | `build-essential`, `cmake`, `pkg-config`, `git` |
| Tools | `systemd`, `sudo`, `curl`, `wget`, `gpg`, `unzip`, `liblo-tools`, `net-tools`, `htop`, `vim`, `tree` |

It **conflicts with and removes**: `network-manager`, `wpasupplicant`,
`modemmanager`, `dhcpcd-base`, `bluetooth`, `bluez`, `bluez-obexd`, `blueman`,
`plymouth`, `cron`, `gnome-keyring` and GNOME themes, `gvfs*`, `i3lock`.

(core-postinst)=

## 2. What the installation does

`DEBIAN/postinst` runs on **every** install and upgrade, possibly mid-show, so
most steps leave existing things alone.

### 1. The network (optional)

**"Configure networking for a3-core?"** (`a3-core/configure-network`, default
*no*: nothing touched). With *yes*:

- `a3-core/install-default-network` *yes* (preseed only, e.g.
  `debconf-set-selections`): interface, address, gateway, DNS and bridge come
  from the truth's `network` section (`a3-osc-render network`).
- Otherwise it asks **address**/prefix, **gateway**, **DNS**, pre-filled (an
  answer on the pre-September-2026 network is reset to the default), and the
  **interface** (priority *medium*, hidden; default `eno1`).
- **Bridge** (`a3-core/bridge-with`): a second socket (e.g. `enp5s0`) joined
  with the first as `br0`, so the A³ Mixer can hang on the Core. Empty: one
  socket. First asked pre-filled with the other wired socket; later the stored
  answer stands.

Written to `/etc/systemd/network/`:

| Answer | Files |
| :--- | :--- |
| no bridge | `a3.network` |
| bridge | `10-a3-bridge.netdev` (`br0`, **STP on**), `20-a3-bridge-ports.network`, `30-a3-bridge-address.network` (address on `br0`, also without a cable) |

Each variant removes the other's files. STP prevents a broadcast storm if both
cables reach one switch; it costs about 30 s at boot. The interfaces' lines in
`/etc/network/interfaces` are commented out (`# a3-core: networkd owns …`).
`systemd-networkd` is enabled, not started: the network changes at next boot.

### 2. The headless screen

**"Draw to a dummy screen?"** (`a3-core/headless-display`, default *no*), for a
Core used only over VNC.

- *Yes*: `~/.local/share/a3-core/x11/10-headless.conf` →
  `/etc/X11/xorg.conf.d/`. X draws a virtual 1920×1080; **a plugged-in monitor
  stays black**.
- *No*: the shipped file, if present, is renamed `.off`; a hand-written one is
  left.

Answer *no* on a machine with a screen (e.g. running A³ Motion).

### 3. The Python environment

`~/.venv` with `numpy`, `python-osc`, `mido`
(`recipes/requirements.txt`). Core runs on it.

### 4. The configuration, installed into `~/.config`

From `~/.local/share/a3-core/config/` ({ref}`the tree <core-config-tree>`),
file by file:

- missing → installed; same → left;
- **differs** → replaced only if its part is ticked in
  `a3-core/replace-config` (only differing parts offered, all ticked;
  unattended takes all). Parts: `reaper`, `i3`, `systemd`, `qjackctl`, `iem`,
  `other`.
- Replaced files are first copied to `~/.config/a3-replaced/<date_time>/`;
  kept ones are named.

The install never restarts REAPER: **after an upgrade, restart `a3-main`**
when you can, not mid-set. One file at a time, from an a3-core checkout:

```sh
python3 tools/config-status.py                  # list what differs
python3 tools/config-status.py --install PATH   # repo -> machine, one file
```

`--install` shows the diff and keeps the old file.

### 5. Ownership and permissions

`~/.local`, `~/.config` → `aaa`; directories in `~/.config` `0755`, files
`0664`.

### 6. Rendering the one truth: `a3-osc-render user`

As `aaa`, for programs that can't read JSON:

- `~/.config/a3/osc.env`: the [zita units'](#core-zita) targets.
- the `# >>> a3-osc` … `# <<< a3-osc` block in
  `~/a3-system/beat-analyzer/build/.env` (if present): targets, clock port,
  OSC words, Pro DJ Link ports. The rest of the file is yours; truth keys found
  outside the block are commented out.

A failure is reported (zita would lack addresses). Core re-renders both at
its own start; run it by hand only to refresh without a restart.

### 7. System services

Enables `x11vnc.service` and `set_irq_prio.service`
([System units](#core-system-units)).

### 8. User services and the REAPER installation

`loginctl enable-linger aaa`, `systemctl --user daemon-reload`, **start**
`a3-user-install.service` (next section); linger off again. `a3-main`, both
zita units and `a3-bar-per-workspace` start at boot through the shipped
`default.target.wants` links.

### 9. The boot loader

`update-grub`, for the kernel command line in `/etc/default/grub`
([Under /etc](#core-etc)). The postinst ends with:

```text
use 'systemctl --user status a3-user-install.service' to check status
use 'dpkg-reconfigure a3-core' to configure network and the headless screen
use 'dpkg-reconfigure jackd2' to enable rt-priority
Please Reboot or manage a3-core manually with 'systemctl --user start a3-main.service'
```

(core-user-install)=

### `a3-user-install.service`: REAPER, the plug-ins, the beat-analyzer

`recipes/user_install.sh` installs what Debian lacks. It runs on every upgrade,
on a live rig, so **each step runs only when its file is missing** (refetching
once emptied REAPER under a running REAPER).

| Step | What it does | Skipped when |
| :--- | :--- | :--- |
| REAPER | current Linux x86_64 release into `~/.local/opt/REAPER`, link `~/.local/bin/reaper` | `~/.local/opt/REAPER/reaper` exists |
| plug-in paths | sets `vstpath` (`~/.local/vst/`, `/usr/lib/vst3/`) and `clap_path_linux-x86_64` (`~/.local/clap`, `/usr/lib/clap`) in `reaper.ini`, or writes a stub | never; only these two keys |
| TAL-Filter-2 | `~/.local/vst/TAL-Filter-2.vst3` | it exists |
| Airwindows Consolidated | latest `DAWPlugin` Linux build → `~/.local/clap/airwindows.clap` | it exists |
| beat-analyzer | `./build.sh` in `~/a3-system/beat-analyzer`; `cp -n .env.example build/.env` | no checkout, or `build/beat-analyzer` exists |

- `reaper.ini` is the machine's; the package sets only those two keys. IEM
  comes from Debian.
- The beat-analyzer is built from the a3-system checkout (a submodule), not
  cloned; without it the step is skipped — clone a3-system ({doc}`install`)
  and start the service again. An existing `build/.env` is never overwritten.
- Fetch REAPER and the plug-ins again (REAPER is stopped meanwhile):

  ```sh
  A3_REINSTALL=1 bash ~/.local/share/a3-core/recipes/user_install.sh
  ```

### Removing the package: `postrm`

`apt purge a3-core` removes `/etc/systemd/network/a3.network`, disables
`systemd-networkd`, reloads systemd. Bridge files, commented ifupdown lines,
the headless X config and the home directory stay.

```{toctree}
:hidden:

core-systemd
core-filetree
```
