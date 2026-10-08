# A³ Core Development

## Python script a3-core.py

`home/aaa/.local/bin/a3-core.py` in [a3-core](https://github.com/a3-audio/a3-core)
turns OSC into DSP settings.

| In | Out |
| :--- | :--- |
| `core.osc`: Mixer, Motion, StemDeck, beat-analyzer (`/beat`) | REAPER (`reaper.osc`) |
| `core.reaper-feedback`: REAPER's reports | IEM MultiEncoders (`iem.multiencoder-1..3`) |
| `core.web`: the window and `/api/truth` (HTTP) | IEM DualDelay (`dualdelay.osc`) |
| | Mixer, Motion, StemDeck |

All names and addresses come from `/usr/share/a3/a3-osc.json` joined with
`~/.config/a3/network.json` by `lib/a3_osc.py` ({ref}`truth <osc-truth>`,
{doc}`ports <../ressources/ports>`). Value curves are pure functions in
`lib/a3_core_curves.py`.

| Topic | Code | Rule |
| :--- | :--- | :--- |
| data beside the source | `layout.json`, `curves-golden.json`, `osc-register.json` | {ref}`files <core-files>` |
| total recall | `a3_core_recall.py`, `a3_core_state.py`, `a3_core_evening.py` | {ref}`/state/recall <osc-recall>` |
| everything to everyone | `lib/a3_core_subscribers.py` | {ref}`rule <osc-everyone>`, {ref}`new subscriber <core-subscriber>` |
| the way back | `lib/a3_core_reverse.py` (`invert()`); `tools/tests/test_reverse_covers_forward.py` keeps it in step with the forward path | {ref}`The way back <osc-way-back>` |
| tempo to the delay | `lib/a3_core_tempo.py` | {ref}`/beat and the delay <osc-beat-delay>` |

## The window

`http://<core>:9080` (`core.web`) shows what actually crosses the wire —
because over UDP every silent link looks the same.

![The traffic view of Core's window](pics_development/a3core-window-traffic.png)

One row per address: count, rate, last value, peer, age, direction; a dot per
peer says when it was last heard.

- **The filter is applied on the server**: hiding rows in the browser while
  streaming everything can freeze the browser's machine.
- **Stream and query are separate**: live values stream, the big table is
  fetched on demand.
- **The window never blocks Core's start**: a broken state file, odd register
  or taken port gives a window with a problem, never an exception.

### Which truth each device speaks

Mixer, StemDeck and Motion send `/device/hello` with the sha256 of their truth
({ref}`desk <mic-truth>`, {ref}`Following Core <osc-follow>`);
`lib/a3_core_devices.py` compares it with Core's fingerprint and the window
shows *a3-osc.json is Core's* or, red, *DIFFERS* ({ref}`what to do <osc-differs>`).

### The register

A traffic log can't show what is *possible* (REAPER reports sends only for
tracks in its bank window). `tools/osc_register.py` writes
`share/a3-core/osc-register.json` from `a3-osc.json`: one row per address shape
and device, direction from Core's side (`in`, `out`, `both`, `aside`);
REAPER's and IEM's words as `both`. `tools/tests/test_osc_register.py` keeps it
in step.

![The register, filtered by device](pics_development/a3core-window-register.png)

Filter by device and tick *nur tote Drähte*: every address that exists and
never arrived.

![The register filtered to the mixer](pics_development/a3core-window-register-mixer.png)

### The address list survives a restart

REAPER announces its vocabulary once, on connecting, so the **list** of
addresses (not values or history) is kept in
`$XDG_STATE_HOME/a3-core/seen.json`. Never written from the hot path (`seen()`
runs ~100 times a second): a thread writes once new rows stop appearing.
19,335 rows: 1.27 MB, 24 ms; the 50,000-row cap: 3.29 MB, 62 ms. Restored rows
have **no value** — an old knob position would look live; `/state/recall`
answers that.

## Beat-Analyzer

[beat-analyzer](https://github.com/rafjagger/beat-analyzer), a C++/CMake
service on the same JACK graph: the beat clock and the meters
({ref}`VU map <core-vu-map>`), independent of REAPER's transport. Use:
{doc}`../user/beat-analyzer`; build: {doc}`build`.
