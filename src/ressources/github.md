# Github

## The A³ repositories

| Repository | What it is |
| :--- | :--- |
| [a3-system](https://github.com/a3-audio/a3-system) | The umbrella: what the system is and how it fits together |
| [a3-core](https://github.com/a3-audio/a3-core) | The sound server — its Debian package tree, the OSC router, the SuperCollider backend and the REAPER project |
| [a3-mixer](https://github.com/a3-audio/a3-mixer) | The DJ mixer: control scripts and KiCad hardware |
| [a3-motion](https://github.com/a3-audio/a3-motion) | The motion sampler: ESP32-S3 panel firmware and hardware |
| [a3-motion-ui](https://github.com/a3-audio/a3-motion-ui) | The JUCE/C++ touchscreen UI, also a submodule of a3-motion |
| [a3-doc](https://github.com/a3-audio/a3-doc) | These pages |
| [a3-audio.github.io](https://github.com/a3-audio/a3-audio.github.io) | The homepage |

## Beside them

- [beat-analyzer](https://github.com/rafjagger/beat-analyzer) — the beat clock
  and the VU meters. Runs on the Core, on the same JACK graph. Not under the
  `a3-audio` organisation, but part of the same system
- [osccontrol-light](https://github.com/drlight-code/osccontrol-light) — an
  audio plugin that speaks OSC

There are **no builds to download.** Everything here is built from source; the
A³ Motion UI has a `build.sh` and runs standalone, with the full interface and
no controller attached, which is how it can be tried without the hardware in
the room.
