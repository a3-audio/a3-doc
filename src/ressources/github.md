# Github

## The A³ repositories

| Repository | What it is |
| :--- | :--- |
| [a3-system](https://github.com/a3-audio/a3-system) | The umbrella: what the system is and how it fits together |
| [a3-core](https://github.com/a3-audio/a3-core) | The sound server — its Debian package tree, the OSC router and the REAPER project |
| [a3-mixer](https://github.com/a3-audio/a3-mixer) | The DJ mixer: control scripts and KiCad hardware |
| [a3-motion](https://github.com/a3-audio/a3-motion) | The motion sampler: ESP32-S3 panel firmware and hardware |
| [a3-motion-ui](https://github.com/a3-audio/a3-motion-ui) | The JUCE/C++ touchscreen UI, also a submodule of a3-motion |
| [a3-doc](https://github.com/a3-audio/a3-doc) | These pages |
| [a3-audio.github.io](https://github.com/a3-audio/a3-audio.github.io) | The homepage |

## Beside them

- [beat-analyzer](https://github.com/rafjagger/beat-analyzer) — the beat clock
  and the VU meters. Runs on the Core, on the same JACK graph. Not under the
  `a3-audio` organisation, but part of the same system. See
  [Beat Analyzer](../user/beat-analyzer.md)
- [stemdeck](https://github.com/rafjagger/stemdeck) — the stem player: two
  decks of four stems, each stem on its own output, and a Pro DJ Link tempo
  master when there are no CDJs. Also outside the organisation, and carried by
  a3-system as a submodule. See [StemDeck](../user/stemdeck.md)
- [osccontrol-light](https://github.com/drlight-code/osccontrol-light) — an
  audio plugin that speaks OSC

There are **no builds to download.** Everything here is built from source —
see {doc}`../development/build`, or let the
{doc}`installer <../configuration/install>` do it.
