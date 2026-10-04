(install)=

# Installing the system

[a3-system](https://github.com/a3-audio/a3-system) carries every part of the
A³ system as a submodule, and its `install` sets a machine up as one or more
parts — or updates it. It builds everything from source, at one version of the
whole system.

```sh
git clone https://github.com/a3-audio/a3-system ~/a3-system
~/a3-system/install
```

`install` asks three things — which version, which roles this machine has,
and each role's settings — shows a summary, and installs after a yes. Steps
that need root run through `sudo`.

(install-roles)=

## Roles

A machine can have any of them; they are installed in this order.

| Role | What it installs | Submodules it checks out |
| :--- | :--- | :--- |
| **Core** | the {ref}`a3-core Debian package <core-package>`, built from this version's a3-core, its install questions (network, headless screen, which local configuration to replace) asked up front, and then held so `apt upgrade` does not move it. The package's {ref}`user-side installer <core-user-install>` builds the beat-analyzer | `a3-core`, `beat-analyzer` |
| **StemDeck** | builds {doc}`StemDeck <../user/stemdeck>` and enables `stemdeck.service`. On a machine without the Core role, also StemDeck's two zita units, which carry the audio to the Core; JACK is then that machine's own business | `stemdeck` |
| **Motion** | builds {doc}`A³ Motion's UI <moc>` and enables `a3-motion.service`, adds the user to `dialout` for the panel's serial port, and flashes the panel firmware when it changed since the last flash | `a3-motion` (with its `ui`) |
| **Mixer** | listed, but not installable yet: the desk is set up by hand, see {ref}`Running the desk <mic-run>` | `a3-mixer` |

Only the submodules the chosen roles need are checked out, at the commits this
version of a3-system records. A submodule with local changes stops the update
rather than being overwritten.

StemDeck and Motion build against the one pinned JUCE; the installer builds it
into `~/local/juce` if it is not there (see {ref}`JUCE <build-juce>`).

(install-options)=

## Options

| Command | What it does |
| :--- | :--- |
| `install` | asks: version, roles, their settings |
| `install --update [VERSION]` | no questions: the stored roles and settings, at `VERSION` (default: the newest tag) |
| `install --config FILE` | no questions: the roles and settings in `FILE`, which is not saved over the stored ones |
| `install --dry-run` | shows every command and runs none |
| `install --flash-firmware` | flashes the Motion panel even if its firmware is unchanged |

A version is a tag, the same in every repository; see the
{doc}`release notes <../ressources/release-notes>`.

(install-settings)=

## Settings

The answers are kept in **`~/.config/a3/install.conf`**, a plain INI file, and
the next run starts from them, so Enter keeps every earlier answer. Copy it to
another machine and run `install --config <file>` to set that machine up the
same way.

| Section | Keys |
| :--- | :--- |
| `[system]` | `version` — a tag, or empty for what is checked out |
| `[roles]` | `core`, `stemdeck`, `motion`, `mixer` — `yes` or `no` |
| `[core]` | `configure_network`, `interface`, `address`, `gateway`, `dns`, `bridge_with`, `headless` — the package's install questions; `replace` — which differing parts of `~/.config` to replace: `all`, `none` or a list such as `reaper, i3` |
| `[motion]` | `flash_firmware` — `yes`, `no` or `ask`; `serial_port` — `auto` (found by USB ID, see {ref}`moc-serial`) or a device path |

What the installer has done that the repository does not record — which
firmware it flashed last — is in `~/.config/a3/install.state`.

## Limits

- **Debian only.**
- It runs as the user **`aaa`**, from **`/home/aaa/a3-system`**: the systemd
  units the parts ship name that path. Anywhere else it refuses, except with
  `--dry-run`.
