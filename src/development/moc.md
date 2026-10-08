# A³ Motion Development

## A³ Motion Controller UI

A JUCE / C++17 app drawing the sphere in OpenGL:
[a3-motion-ui](https://github.com/a3-audio/a3-motion-ui), the `ui` submodule of
[a3-motion](https://github.com/a3-audio/a3-motion). It records motion from the
touchscreen, stores it as ticks, plays it back on the beat clock, and speaks
OSC to A³ Core. Build and test (`./build.sh`, `./test.sh`, JUCE version):
{doc}`build`. Hardware: {ref}`A³ Motion hardware <moc-hardware>`.

## Current Version — V03

![The A³ Motion UI, ACTION page open](../user/pics_user/a3-motion-ui-display-one-clip.png)

## The software mixer

A channel strip like the desk's plus a summing and filter page, sending exactly
the desk's addresses, so Core can't tell them apart.

![The MIX page](../user/pics_user/a3-motion-ui-mix.png)

- **It listens too.** Core relays REAPER's reports; the pages adopt them via
  `MixerState::setChannelFromPeer`, which sets **without sending** — sending
  would rebuild the echo loop out of Core's reach.
- Three handlers, `onMixerChannelValue`, `onMasterValue`, `onFilterValue`,
  each indexing its table in `OscAddresses`. Master and filter tables are
  walked **after** the channel ones: `/master/volume` and `/channel/1/volume`
  differ by one word.
- `/filter/mode` arrives as a number (1 = high pass); the desk's word goes on
  `/filter/led`.

### Rest positions

A double tap rests a control only where a rest means something. On the strip,
only SEND:

```cpp
constexpr std::optional<float>
mixerControlRestPosition (MixerControl control)
{
  if (control == MixerControl::AuxSend)
    return 0.f;
  return {};
}
```

A gain snapping to a default mid-set would make a channel jump. The same table
sets the start values; gain and volume start at zero with no rest. The
channel-value strip (`channelValueRestPosition`): `3d` and `freq` at twelve
o'clock, `Q` **shut** (a filter still resonating hasn't been reset).

## Hearing where the sound is

One handler, `onChannelValue`, accepts five per-channel values from Core:
azimuth, elevation, pot 1, pot 2, 3D. That makes total recall work: at start
the device sends `/state/recall`, holds its output and adopts the answer
({ref}`/state/recall <osc-recall>`). Output ramps count as primed only after a
tick that actually sent, so a 0.0 start still reaches Core.

## The status bar and the signal dots

No VU meters in the status bar: outputs are on the master column, inputs are a
**dot on each channel's face**.

```cpp
struct VuDot
{
  bool visible = false;      // false below the meter's floor: silence is nothing
  std::size_t band = vuGreenBand;
  float alpha = 0.f;         // follows the level; the size stays put
};
```

- **A warning light, not a meter**: a dot has no length to show how far over.
- **Silence is no dot**, not a dim one.
- **RMS, not peak**, or it would flicker on every hit.
- Colour from `vuBandColour`, the meter's own rule; a test pins the yellow
  threshold to the meter's.
- Repaint compares the drawn dot, not the level, which wobbles every frame.

## Older Versions

The sphere before the touch rework, and before that:

![](pics_development/a3motion_ui_new.png)

![](pics_development/a3motion_ui_old.png)

## Before

![](pics_development/a3motion-software-mockup.png)

![](pics_development/a3motion-software-mockup_01.png)

## Panel firmware

A microcontroller ({ref}`hardware <moc-hardware>`) handles buttons, encoders,
pots and LEDs and talks to the UI by a binary poll-frame protocol on USB
serial. PlatformIO project:
[`firmware/`](https://github.com/a3-audio/a3-motion/tree/main/firmware);
build, test, flash: {doc}`build`.
