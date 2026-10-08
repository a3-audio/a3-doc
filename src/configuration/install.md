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

(install-roles)=

## Roles

Any combination, installed in this order:

| Role | What it installs | Submodules it checks out |
| :--- | :--- | :--- |
| **Core** | the {ref}`a3-core package <core-package>` from this version, its questions asked up front, then held against `apt upgrade`; its {ref}`user installer <core-user-install>` builds the beat-analyzer | `a3-core`, `beat-analyzer` |
| **StemDeck** | builds {doc}`StemDeck <../user/stemdeck>`, enables `stemdeck.service`; without Core also the two zita units (JACK is then the machine's own) | `stemdeck` |
| **Motion** | builds {doc}`the UI <moc>`, enables `a3-motion.service`, adds the user to `dialout`, flashes the panel when its firmware changed | `a3-motion` (with `ui`) |
| **Mixer** | not installable yet: {ref}`by hand <mic-run>` | `a3-mixer` |

Only the needed submodules are checked out, at this version's commits; local
changes in one stop the update. StemDeck and Motion use the pinned
{ref}`JUCE <build-juce>`, built into `~/local/juce` if missing.

(install-options)=

## Options

| Command | What it does |
| :--- | :--- |
| `install` | asks: version, roles, their settings |
| `install --update [VERSION]` | no questions: the stored roles and settings, at `VERSION` (default: the newest tag) |
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
| `[system]` | `version` — a tag, or empty for what is checked out |
| `[roles]` | `core`, `stemdeck`, `motion`, `mixer` — `yes` or `no` |
| `[core]` | `configure_network`, `interface`, `address`, `gateway`, `dns`, `bridge_with`, `headless` — the package's install questions; `replace` — which differing parts of `~/.config` to replace: `all`, `none` or a list such as `reaper, i3` |
| `[motion]` | `flash_firmware` — `yes`, `no` or `ask`; `serial_port` — `auto` (found by USB ID, see {ref}`moc-serial`) or a device path |

The last flashed firmware is recorded in `~/.config/a3/install.state`.

## Limits

- **Debian only.**
- User **`aaa`**, checkout **`/home/aaa/a3-system`** (the units name that
  path); elsewhere only `--dry-run`.
