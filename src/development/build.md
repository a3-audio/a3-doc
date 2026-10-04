# Building and testing

Everything in the A³ system is built from source; there are no builds to
download. On a machine that only has to run the system, the
{doc}`installer <../configuration/install>` does the building. This page is
for working on the code.

(build-juce)=

## JUCE

Every product that uses JUCE — A³ Motion's UI and StemDeck — builds against
**one JUCE, 9.0.3**, the release tag. It is pinned as `JUCE_VERSION` in
[a3-system](https://github.com/a3-audio/a3-system)'s
`installer/roles/base.py`. The installer builds that version into
`~/local/juce`, which is where both products look for it by default. Keep only
the one version in that prefix: JUCE's CMake package matches exactly, and with
two versions there a search without a version takes either.

A new JUCE is bumped on purpose, in that one line, and then built and tested
like any other change. The installer says when a newer release is out.

(build-commands)=

## Build and test, per repository

Run each command from the root of the repository named.

| Repository | Build | Test |
| :--- | :--- | :--- |
| a3-core | `cd platform-config/debian-x86_64 && dpkg-deb --build --root-owner-group a3-core` (normally the GitHub workflow builds the package, see {ref}`The Debian package <core-package>`) | `~/.venv/bin/python3 -m unittest discover -s tools/tests` — with the venv's Python; the system `python3` lacks packages and skips tests |
| a3-mixer | — (Python) | `A3_OSC_TRUTH=<path to a3-osc.json> python3 -m unittest discover -s software/tests` |
| a3-mixer panel firmware | `pio run` in `hardware/mainboard/firmware/` | |
| a3-motion panel firmware | `pio run` in `firmware/`; `pio run -t upload` flashes it (the port is found by USB ID, see {ref}`moc-serial`) | `pio test -e native` and `python3 -m unittest test_host` in `firmware/` |
| a3-motion-ui | `./build.sh` (`-d` for Debug) | `./test.sh` |
| beat-analyzer | `git submodule update --init`, then `./build.sh` | `cd build && ctest` |
| StemDeck | `./start.sh` builds and starts it, see {ref}`Build and start <stemdeck-build>` | `cmake -S . -B build -DSTEMDECK_TESTS=ON`, `cmake --build build --target stemdeck-tests`, `ctest --test-dir build`; the Python tools: `python3 -m unittest discover -s tools/tests` |
| a3-doc | `sphinx-build src doc` | |

**A³ Motion UI: use `./test.sh`, not `ctest` on its own.** `ctest` runs the
test binary that was built last; it does not build one, and `build.sh` builds
only the app. `test.sh` builds the tests first, runs them against the library
as committed (`config/` and `pattern/` of HEAD, exported into
`build/committed/`), and prints when the runner it ran was built. The reasons
are in `ARCHITECTURE.md` in
[a3-motion-ui](https://github.com/a3-audio/a3-motion-ui).

The same caution holds for StemDeck and the beat-analyzer: `ctest` runs what
was built, so build the test target first.

Each repository's `README.md` lists the packages its build needs.
