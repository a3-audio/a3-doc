# Github

## The A³ repositories

| Repository | What it is |
| :--- | :--- |
| [a3-system](https://github.com/a3-audio/a3-system) | The umbrella: carries the others as submodules, and the {doc}`installer <../configuration/install>`. Every submodule sits at its repository's name; a3-beat-analyzer, a3-mixer-ui, a3-motion-ui and a3-stem-separator inside the repository that pins them |
| [a3-core](https://github.com/a3-audio/a3-core) | The sound server — the `a3-core` C++ program (Core, audio engine, window), its Debian package tree and the one package `a3-core` |
| [a3-beat-analyzer](https://github.com/a3-audio/a3-beat-analyzer) | The beat clock (package `beat-analyzer`), a submodule of a3-core. Runs on the Core, on the same JACK graph. See [Beat Analyzer](../user/beat-analyzer.md) |
| [a3-mixer](https://github.com/a3-audio/a3-mixer) | The DJ mixer: control scripts (`software/`), panel firmware (`firmware/`), KiCad boards, one folder per revision, and housing (`hardware/`) and the virtual desk (the submodule a3-mixer-ui) |
| [a3-mixer-ui](https://github.com/a3-audio/a3-mixer-ui) | The virtual desk (`a3-desk`), JUCE/C++, a submodule of a3-mixer |
| [a3-motion](https://github.com/a3-audio/a3-motion) | The motion sampler: ESP32-S3 panel firmware and hardware |
| [a3-motion-ui](https://github.com/a3-audio/a3-motion-ui) | The JUCE/C++ touchscreen UI, also a submodule of a3-motion |
| [a3-stemdeck](https://github.com/a3-audio/a3-stemdeck) | StemDeck (package `stemdeck`), the stem player: two decks of four stems, each stem on its own output, and a Pro DJ Link tempo master when there are no CDJs. See [StemDeck](../user/stemdeck.md) |
| [a3-stem-separator](https://github.com/a3-audio/a3-stem-separator) | Makes StemDeck's stem sets off the rig, on a rented cloud GPU; a submodule of a3-stemdeck |
| [a3-prodj](https://github.com/a3-audio/a3-prodj) | The pro-DJ: the set seen from the floor's centre, later the autopilot. Planned, part of the release from v03.2 |
| [a3-engine](https://github.com/a3-audio/a3-engine) | **Archived.** The audio engine's former repository; its code moved into a3-core and its package `a3-engine` is replaced by `a3-core`. The name lives on as the engine role and its unit `a3-engine.service` |
| [a3-doc](https://github.com/a3-audio/a3-doc) | These pages |
| [a3-audio.github.io](https://github.com/a3-audio/a3-audio.github.io) | The homepage |

## Beside them

- [osccontrol-light](https://github.com/drlight-code/osccontrol-light) — an
  audio plugin that speaks OSC

There are **no builds to download.** Everything here is built from source —
see {doc}`../development/build`, or let the
{doc}`installer <../configuration/install>` do it.
