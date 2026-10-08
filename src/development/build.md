# Building and testing

Everything is built from source. To just run the system, use the
{doc}`installer <../configuration/install>`; this page is for working on the
code.

(build-juce)=

## JUCE

A³ Motion's UI and StemDeck build against **one JUCE, 9.0.3**, pinned as
`JUCE_VERSION` in [a3-system](https://github.com/a3-audio/a3-system)'s
`installer/roles/base.py` and built into `~/local/juce`. Keep only that one
version there: with two, a search without a version takes either. Bump it in
that line on purpose; the installer says when a newer release exists.

(build-commands)=

## Build and test, per repository

From each repository's root:

| Repository | Build | Test |
| :--- | :--- | :--- |
| a3-core | `cd platform-config/debian-x86_64 && dpkg-deb --build --root-owner-group a3-core` (normally the GitHub workflow builds the package, see {ref}`The Debian package <core-package>`) | `~/.venv/bin/python3 -m unittest discover -s tools/tests` — with the venv's Python; the system `python3` lacks packages and skips tests |
| a3-mixer | — (Python) | `A3_OSC_TRUTH=<path to a3-osc.json> python3 -m unittest discover -s software/tests` |
| a3-mixer panel firmware | `pio run` in `hardware/mainboard/firmware/` | |
| a3-motion panel firmware | `pio run` in `firmware/`; `pio run -t upload` flashes it (the port is found by USB ID, see {ref}`moc-serial`) | `pio test -e native` and `python3 -m unittest test_host` in `firmware/` |
| a3-motion-ui | `./build.sh` (`-d` for Debug) | `./test.sh` |
| beat-analyzer | `git submodule update --init`, then `./build.sh` | `cd build && ctest` |
| StemDeck | `./start.sh` builds and starts it, see {ref}`Build and start <stemdeck-build>` | `cmake -S . -B build -DSTEMDECK_TESTS=ON -DCMAKE_PREFIX_PATH=$HOME/local/juce`, `cmake --build build --target stemdeck-tests`, `ctest --test-dir build`; the Python tools: `python3 -m unittest discover -s tools/tests` |
| a3-doc | `sphinx-build src doc` | |

**`ctest` builds nothing**; it runs the last-built tests. For A³ Motion UI use
`./test.sh`: it builds the tests, runs them against the committed library
(HEAD's `config/` and `pattern/` in `build/committed/`) and prints the runner's
build time (`ARCHITECTURE.md` in [a3-motion-ui](https://github.com/a3-audio/a3-motion-ui)).
For StemDeck and the beat-analyzer, build the test target first. Build
packages: each repository's `README.md`.
