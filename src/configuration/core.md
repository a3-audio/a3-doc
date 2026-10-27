# A³ Core Configuration

A³ Core is one Debian package, `a3-core`: the program `a3-core` (the OSC
router, the audio engine, the window) and the installation around it, built from
one repository. It replaces the earlier pair of packages `a3-core` and
`a3-engine` (`Conflicts`/`Replaces: a3-engine`). In order:

1. [The Debian package](#core-package): what it is, how to install, what it needs.
2. [What the installation does](#core-postinst): the install script, step by step.
3. {doc}`The services <core-systemd>`: every systemd unit.
4. {doc}`The files <core-filetree>`: every file, and whether to edit it.

The usual route is the a3-system {doc}`installer <install>` (role Core).

| Part | What it is |
| :--- | :--- |
| OS | Debian testing, realtime kernel |
| Window manager | i3, named workspaces ([The screen](#core-config-screen)) |
| Audio | PipeWire (with JACK compatibility); the engine ({doc}`user page <../user/audio-engine>`) with the IEM code compiled in. REAPER, its patchbay and QjackCtl are not part of the package |
| The program | `/usr/bin/a3-core`: the core role (OSC router, HTTP API), the engine role, the window; no Python at runtime |
| Services | `a3-core.service`, `a3-engine.service`, both `systemd --user` ({ref}`services <core-services>`) |
| Beat clock | the beat-analyzer (`/beat` only; the engine measures the meters, {ref}`where <core-meters>`) |

```{note}
**No addresses or ports here.** They are in `a3-osc.json`
({ref}`Where addresses and ports live <osc-truth>`); this page names
listeners (`core.osc`, `motion.energy`, …), the file says where they are.
```

(core-package)=

## 1. The Debian package

Built from [a3-core](https://github.com/a3-audio/a3-core): the C++ program is
compiled from its source (`packaging/stage`), and its tree
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
sudo dpkg-reconfigure a3-core     # network, audio network, headless screen
```

Updates: `sudo apt update && sudo apt install a3-core`.

### The version

A GitHub workflow rebuilds the archive on every push to `main`. Version: last
`v*` tag plus commits since (`v03.0` + 63 = `03.0+63`), written into
`packaging/DEBIAN/control` at build. The checked-in `0` is a placeholder: a hand
build stamps it. `python3 tools/package_version.py` prints the next version. The
history of the old `a3-engine` repository is part of a3-core's now, so the
number counts it too and is above every earlier `a3-core` version, and apt
upgrades normally.

By hand, from a clean checkout with JUCE installed, use the umbrella's builder:

```sh
python3 <a3-system>/installer/package.py <a3-core checkout> --out <dir> --juce ~/local/juce
```

### What it depends on

| Purpose | Packages |
| :--- | :--- |
| Realtime and audio | `linux-image-rt-amd64`, `pipewire`, `pipewire-jack`, `wireplumber`, `linuxptp`, `libjack-jackd2-dev` (headers only, for building), `jack-example-tools`, `libsamplerate0-dev` |
| Screen | `i3`, `i3status`, `xinit`, `xserver-xorg-video-dummy`, `xserver-xorg-video-amdgpu`, `x11vnc`, `x11-utils`, `x11-xserver-utils`, `libgtk2.0-0`, `pcmanfm`, `dex`, `unclutter-xfixes`, `maim`, `xclip`, `brightnessctl` |
| Build tools | `build-essential`, `cmake`, `pkg-config`, `git` |
| Tools | `systemd`, `sudo`, `openssh-server`, `curl`, `wget`, `gpg`, `liblo-tools`, `net-tools`, `htop`, `vim`, `tree`, `ffmpeg` |

The shared libraries the program links come from the build (`${shlibs:Depends}`).
The 3D code is IEM's, compiled into the program, so there is no
`iem-plugin-suite-vst3`; `qjackctl` and `unzip` went with REAPER.

It **recommends** `beat-analyzer`, its own package; apt installs it along unless
Recommends are switched off.

It **conflicts with and removes**: `a3-engine` (the former package of the
program), `network-manager`, `wpasupplicant`,
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
  `debconf-set-selections`): interface, address, gateway, DNS and audio socket come
  from the truth's `network` section (`a3-core --render-truth network`).
- Otherwise it asks **address**/prefix, **gateway**, **DNS**, pre-filled (an
  answer on the pre-September-2026 network is reset to the default), and the
  **interface** (priority *medium*, hidden; default `eno1`).
- **Audio network** (`a3-core/audio-port`, `a3-core/audio-address`): a second
  socket (e.g. `enp5s0`) for AES67 and PTP, on a subnet of its own. First asked
  pre-filled with the other wired socket; empty means one socket only. The
  address defaults to `192.168.9.10/24`; there is no gateway and no DNS on it.
  There is no bridge: the A³ Mixer reaches the Core over the first network.

Written to `/etc/systemd/network/`:

| Answer | Files |
| :--- | :--- |
| first socket | `10-a3.network`: address, gateway (`192.168.8.1`), DNS |
| audio socket | `20-a3-aes67.network`: address on `192.168.9.0/24`, no gateway, no DNS |

Each file is replaced only when its content changes, and the old one is kept
beside it as `<name>.bak-<time>`. An upgrade retires the former single
`a3.network` and the bridge files (`10-a3-bridge.netdev`,
`20-a3-bridge-ports.network`, `30-a3-bridge-address.network`) the same way.
Without a second socket the AES67 sender and PTP are not enabled
({ref}`a3-aes67 <core-aes67>`). The interfaces' lines in
`/etc/network/interfaces` are commented out (`# a3-core: networkd owns …`).
`systemd-networkd` is enabled, not started: the network changes at next boot.

Energy Efficient Ethernet is switched off on every wired port by a drop-in to the stock link file,
`/etc/systemd/network/99-default.link.d/a3-eee.conf` (needs systemd 258 or newer): with EEE active the audio port dropped its link every minute or two, each time a three-second hole in the AES67 stream.

### 2. The headless screen

**"Draw to a dummy screen?"** (`a3-core/headless-display`, default *no*), for a
Core used only over VNC.

- *Yes*: `~/.local/share/a3-core/x11/10-headless.conf` →
  `/etc/X11/xorg.conf.d/`. X draws a virtual 1920×1080; **a plugged-in monitor
  stays black**.
- *No*: the shipped file, if present, is renamed `.off`; a hand-written one is
  left.

Answer *no* on a machine with a screen (e.g. running A³ Motion).

### 3. No Python environment

The package builds none: Core and the engine are the compiled `a3-core`
program. (An old `~/.venv` on an upgraded machine is harmless and unused.)

### 4. The configuration, installed into `~/.config`

From `~/.local/share/a3-core/config/` ({ref}`the tree <core-config-tree>`),
file by file:

- missing → installed; same → left;
- **differs** → replaced only if its part is ticked in
  `a3-core/replace-config` (only differing parts offered, all ticked;
  unattended takes all). Parts: `i3`, `systemd`, `pipewire`, `other`.
- Replaced files are first copied to `~/.config/a3-replaced/<date_time>/`;
  kept ones are named.

The install never restarts the rig: **after an upgrade, restart `a3-main`**
when you can, not mid-set. One file at a time, from an a3-core checkout:

```sh
python3 tools/config-status.py                  # list what differs
python3 tools/config-status.py --install PATH   # repo -> machine, one file
```

`--install` shows the diff and keeps the old file.

### 5. An ssh key (optional)

**"Public ssh key allowed to log in as aaa"** (`a3-core/ssh-key`, default
empty). One public-key line is appended to `~/.ssh/authorized_keys`, once;
empty adds nothing, anything else is refused. The answer is forgotten
afterwards, so an upgrade never puts back a removed key. The package ships no
`authorized_keys` of its own.

### 6. Ownership and permissions

`~/.local`, `~/.config` → `aaa`; directories in `~/.config` `0755`, files
`0664`.

### 7. Rendering the one truth: `a3-core --render-truth user`

As `aaa`, for programs that can't read JSON:

- `~/.config/pipewire/pipewire-aes67.conf`: the AES67 sender, from the truth's audio socket (only with one).
- the `# >>> a3-osc` … `# <<< a3-osc` block in
  `~/a3-system/beat-analyzer/build/.env` (if present): targets, clock port,
  OSC words, Pro DJ Link ports. The rest of the file is yours; truth keys found
  outside the block are commented out.

A failure is reported. Core re-renders both at
its own start; run it by hand only to refresh without a restart.

### 8. System services

Enables `x11vnc.service` and `set_irq_prio.service`
([System units](#core-system-units)), and, with an audio socket,
`ptp4l@<socket>.service` ({ref}`the audio network <core-aes67>`).

### 9. User services, and what REAPER left

`loginctl enable-linger aaa`, `systemctl --user daemon-reload`, stop the retired
units, enable the rig and (with an audio socket) AES67; linger off again.
`a3-main`, `a3-aes67` and `a3-bar-per-workspace` start at boot through the
shipped `default.target.wants` links.

**On a machine that ran REAPER** the upgrade retires what it needs
(`retire_reaper_files`): it stops and disables `qjackctl.service`,
`a3-reaper.service` and `a3-user-install.service`, and moves them with their
drop-in folders, every drop-in that calls the removed helper `a3-engine-runs`,
and `~/.config/rncbc.org/a3-patchbay.xml` and `QjackCtl.conf` into the backup
folder (`~/.config/a3-replaced/<date_time>/`), naming each one. Nothing is
deleted. **Never touched:** `~/.config/REAPER`, `~/.local/opt/REAPER`,
`~/.local/vst`, `~/.local/clap` are yours to delete by hand.

### 10. The boot loader

`update-grub`, for the kernel command line in `/etc/default/grub`
([Under /etc](#core-etc)). The postinst ends with:

```text
use 'systemctl --user status a3-main.service' to check the rig
use 'dpkg-reconfigure a3-core' to configure network and the headless screen
Please Reboot or manage a3-core manually with 'systemctl --user start a3-main.service'
```

### Removing the package: `postrm`

`apt purge a3-core` removes `/etc/systemd/network/a3.network`, disables
`systemd-networkd`, reloads systemd. Commented ifupdown lines,
the headless X config and the home directory stay.

```{toctree}
:hidden:

core-systemd
core-filetree
```
