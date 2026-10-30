(install)=

# Installing the system

[a3-system](https://github.com/a3-audio/a3-system) carries every part as a
submodule; `install` sets a machine up as one or more parts, or updates it,
built from source at one system version.

```sh
git clone https://github.com/a3-audio/a3-system ~/a3-system
~/a3-system/install
```

It asks version, roles and their settings, shows a summary, installs on yes;
root steps use `sudo`.

```{warning}
**A current limit: user `aaa` in `/home/aaa`.** The rig's roles (Core,
StemDeck, deck host, Motion, desk) install only when you run the installer
as the user **`aaa`** from the checkout **`/home/aaa/a3-system`**: their
services name that path. Anywhere else the installer only shows what it
would do (`--dry-run`). The **laptop** role is the exception: it runs as any
user, from anywhere ([Limits](#install-limits)).
```

(install-roles)=

## Roles

Any combination, installed in this order:

| Role | What it installs | Submodules it checks out |
| :--- | :--- | :--- |
| **Core** | the {ref}`a3-core package <core-package>` from this version, its questions asked up front, then held against `apt upgrade`; the `beat-analyzer` package comes with it as a recommendation | `a3-core`, `beat-analyzer` |
| **StemDeck** | installs {doc}`StemDeck <../user/stemdeck>`. On a Core, deck A runs as `stemdeck@A` with the Core, and the package's two-deck unit `stemdeck.service` stays off. On a machine without the Core the role enables `stemdeck.service`, the {ref}`older two-deck app <stemdeck-two-deck>`; for a deck that plays into a Core use **deck host** | `stemdeck` |
| **deck host** | one StemDeck deck on a machine without the Core: asks the deck letter, the path latency and the audio socket, starts `stemdeck@<letter>` with its AES67 sender and PTP clock ({ref}`StemDeck on another machine <stemdeck-with-motion-remote-machine>`). Not beside Core or StemDeck | `stemdeck` |
| **desk** | the {ref}`virtual desk <a3mix-virtual>` (`a3-desk`), on any machine with a screen | `a3-mixer` |
| **Motion** | builds {doc}`the UI <moc>`, enables `a3-motion.service`, adds the user to `dialout`, flashes the panel when its firmware changed | `a3-motion` (with `ui`) |
| **Mixer** | the A³ Mixer hardware's own computer: not installable yet, {ref}`by hand <mic-run>` | `a3-mixer` |
| **laptop** | the whole rig on one machine: Core and the Engine, the StemDecks, the desk, the Motion UI and the beat-analyzer, packages only, no AES67. The Engine plays the binaural mix on the laptop's output. New, still being tested. Excludes every other role | none |

By default the apps (Core, StemDeck, the UIs, the desk) are installed as
packages from the apt archive: no JUCE build and no source checkout beyond the
configuration. `install --from-source` builds them from the pinned submodules
as before.

Only the needed submodules are checked out, at this version's commits; local
changes in one stop the update. StemDeck and Motion use the pinned
{ref}`JUCE <build-juce>`, built into `~/local/juce` if missing.

(install-options)=

## Options

| Command | What it does |
| :--- | :--- |
| `install` | asks: version, roles, their settings |
| `install --network` | asks the Core's network questions again; a plain `install` asks them only the first time, afterwards the stored answers stand |
| `install --update [VERSION]` | no questions: the stored roles and settings, at `VERSION` (default: the newest tag); a `VERSION` needs `--from-source`, the archive holds only the newest packages |
| `install --from-source` | builds the apps from the pins instead of installing packages, e.g. `install --from-source --update v03.0` |
| `install --config FILE` | no questions: the roles and settings in `FILE`, which is not saved over the stored ones |
| `install --dry-run` | shows every command and runs none |
| `install --flash-firmware` | flashes the Motion panel even if its firmware is unchanged |

A version is a tag, the same in every repository
({doc}`release notes <../ressources/release-notes>`).

(install-settings)=

## Settings

Answers are kept in **`~/.config/a3/install.conf`** (INI); Enter keeps them
next time. Copy it and run `install --config <file>` to clone a setup.

| Section | Keys |
| :--- | :--- |
| `[system]` | `version` — a tag, or empty for what is checked out; `archive` — `public` (GitHub archive) or `lan` (the rig's own apt source); `public` on a fresh machine, but an installed machine must set it once, else the installer stops before any change |
| `[roles]` | `core`, `stemdeck`, `deck-host`, `motion`, `desk`, `mixer`, `laptop` — `yes` or `no` |
| `[core]` | `configure_network`, `interface`, `address`, `gateway`, `dns`, `audio_port`, `audio_address`, `headless` — the package's install questions; `replace` — which differing parts of `~/.config` to replace: `all`, `none` or a list such as `pipewire, i3` |
| `[motion]` | `flash_firmware` — `yes`, `no` or `ask`; `serial_port` — `auto` (found by USB ID, see {ref}`moc-serial`) or a device path |

The last flashed firmware is recorded in `~/.config/a3/install.state`.

(install-limits)=

## Limits

- **Debian only** (Debian testing on amd64; StemDeck also on Raspberry Pi OS).
- User **`aaa`**, checkout **`/home/aaa/a3-system`** for every role but
  **laptop**: the units name that path; elsewhere only `--dry-run`. This is a
  current limit, not a design choice: the units are to name no user and no
  path.

(install-audio-network)=

## The audio network: EEE

Energy Efficient Ethernet (EEE) must be off on every audio socket. The a3-core
package switches it off on the Core; the stemdeck package does it on every deck
host (a udev rule, for every systemd version) — right at install, no reboot.

**Symptoms when it is on:** ptp4l logs `timed out while polling for tx
timestamp` and goes to `FAULTY`; a deck on another machine is silent or
crackles; the link drops every minute or two.

**Check** (on the machine, its audio socket, e.g. `eth0` or `enp5s0`):

```
ethtool --show-eee eth0
```

`EEE status: disabled` is right. **Switch it off by hand** if it says enabled:

```
sudo ethtool --set-eee eth0 eee off
```

A deck that crackles while its PTP is fine is usually the switch, not EEE: see
{ref}`what-you-need-audio-network`.
