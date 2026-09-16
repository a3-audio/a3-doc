# Welcome

## The A³ System

- [A³ System Repository](https://github.com/a3-audio/a3-system)

Three devices on one ethernet switch, which also powers them (PoE). They talk
to each other **exclusively over OSC** — never through each other, never over
audio cables.

| Device | What it is | What it does |
| :--- | :--- | :--- |
| [**A³ Core**](https://a3-audio.github.io/a3-doc/user/a3core.html) | the sound server | takes the analog signals, computes the 3D field, sends it out. Remote controlled; no interface of its own |
| [**A³ Mixer**](https://a3-audio.github.io/a3-doc/user/a3mix.html) | a 4-channel DJ mixer | gain, EQ, filter, faders, cue — every control sends OSC to Core |
| [**A³ Motion**](https://a3-audio.github.io/a3-doc/user/a3motion.html) | the motion sampler | records and plays back *where a sound is* and how it travels, like a loopstation for movement |

Your decks, headphones and the booth and main speakers connect to A³ Core's
audio hardware. The other two devices carry no audio at all.

![Connection Diagram](pics_user/a3-connecting-diagram.png)

## One state, told to everyone

Because the devices talk over OSC rather than through each other, there is only
ever **one** state, and every device is told all of it.

| What you do | What follows |
| :--- | :--- |
| turn a knob on the A³ Mixer | A³ Motion's screen follows |
| move a fader in Core's own mixer | both devices follow |
| switch a device on mid-evening | it asks what is already sounding before it says anything, so nothing jumps |

The same feed can be given to anything else — a light or video desk, say — by
naming it when the Core starts. See
[A³ Core Configuration](https://a3-audio.github.io/a3-doc/configuration/core.html).

## The beat

A³ Core also runs the **Beat-Analyzer**: it listens to the music and produces
the tempo the whole system follows, together with the VU meters the other two
devices show. Its clock can come from its own analysis, from A³ Motion's tap
key, or from a Pioneer Pro DJ Link master — chosen on A³ Motion's clock key.

Everything that moves on its own is counted in **bars**, off that clock. A
figure that takes four bars keeps taking four bars when the tempo changes.

## Where to go next

| Section | What is in it |
| :--- | :--- |
| **User** | the three devices, control by control — start here |
| **Assembly** | prototype pictures and how the boxes go together |
| **Configuration** | the files each device reads at startup |
| **Development** | building and hacking on the software |
| [**History**](https://a3-audio.github.io/a3-doc/ressources/history.html) | project impressions |
| [**OSC reference**](https://a3-audio.github.io/a3-doc/ressources/osc.html) | every address the system speaks |

![](pics_user/a3-motion-icon_light.png)

![](pics_user/a3-mix-icon_light.png)

![](pics_user/a3-core-icon_light.png)
