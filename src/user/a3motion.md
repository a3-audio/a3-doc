# A³ Motion

(motion-at-a-glance)=

## At a glance

<!-- GIF: howto-hero-sphere.gif | region: 0,36,768,624 | recorded 2026-09-29, 5.8 s | steps: A set playing on all four channels; no interaction. | "Four channels, one room" | bonus -->

![A set playing on all four channels; no interaction.](pics_user/howto-hero-sphere.gif)

A³ Motion moves up to four mixer channels through the room, in time with the
music. Each channel's sound travels along a **shape** — a circle, a rose, a
zigzag, a jump on every beat. A³ Motion makes no sound itself: it tells A³ Core
where each channel should be, and Core moves the sound.

Think of each channel as a deck. It has one **clip** loaded (a shape, plus how
fast, wide and high it runs) and six **action pads** for accents you play by
hand. A **set** loads all four channels at once. Everything counts in bars off
the beat clock, so a four-bar shape stays four bars when the tempo changes.

![A³ Motion](pics_user/a3-motion-icon_light.png)

A panel of encoders, pots and pads beside a 7" multi-touch screen; it talks
OSC only. Source: [a3-motion](https://github.com/a3-audio/a3-motion).

<!-- The screenshots and GIFs on these pages are to be (re)made in the skin
quiet-indigo-2. The recording plan is kept outside this repository. -->

(motion-glossary)=

### Words you will meet

| Word | What it means here |
| :--- | :--- |
| **channel** | one of the four mixer channels A³ Motion moves. Channel 1 is the leftmost field on the screen and the leftmost column on the panel. Each channel keeps its own colour wherever it appears |
| **selected channel** | the one the bar shows and edits. Tap its field in the channel row to select it |
| **shape** | the path the sound traces. The screen labels it **SVG**, after the file format it is kept in |
| **clip** | a shape plus every value it is played with: speed, height, width, spin, direction. Each channel has one |
| **pass** | one time through the shape |
| **action** | a short script on one of a channel's six action pads, **A1–A6**. It changes the clip while you hold the pad (or once, on a tap), then lets go |
| **set** | which clip and which six actions each of the four channels has, plus their 3d, freq and Q |
| **take** | a new recording of a shape, drawn with your finger on the sphere |
| **lane** | a knob movement recorded in a take |
| **downbeat** | the one: the first beat of a bar. Play waits for it |
| **3d** | how much of a channel is in the room. Fully down: plain stereo, like any mixer. Up: the channel follows its blob |
| **bar** and **global strip** | the bottom of the screen. The **bar** is the five tabs and their page, on the left three quarters; the **global strip** is the column of keys on the right quarter |
| **LENGTH** | how long one pass takes, **counted in beats**: 16 is four bars, 4 is one bar |

(motion-get-started)=

## Get started: your first ten minutes

You need A³ Motion, A³ Core and the A³ Mixer on the A³ network switch, and
music playing on at least one mixer channel.

1. **Plug in.** Connect A³ Motion to the A³ switch. It is powered over the
   network cable and starts by itself. It is ready when the screen shows the
   sphere — the room, seen from above — with the four channel fields under it.
   Play some music on the mixer: the meters in the channel row move. If they
   stay still, see [Troubleshooting](#motion-troubleshooting).
2. **Check the clock.** Top left of the screen is the clock key with the BPM
   beside it. Tap the key until it reads **PIO** if your CDJs are on Pro DJ
   Link, **EXT** if the beat analyser is listening to the music, or **INT** if
   you want to tap the tempo yourself. The BPM should match your deck.
3. **Load a set.** Tap **FILES** (top of the global strip), then **SETS**, tap
   *Warmup* and tap **Load**. All four channels now have a clip and six
   actions. Tap **FILES** again to close it.
4. **Turn 3d up** on the channel your track is on: that channel's pot on the
   panel (above its pads), or **3D** in its field in the channel row.
   **At 3d = 0 you hear no movement.** The channel stays in plain stereo,
   whatever its blob does on the screen.
5. **Press Play.** Press that channel's **Play\|Pause** pad (top left of its
   eight pads). It blinks while it waits for the next downbeat, then the clip
   starts and your track travels the room.
6. **Fire an action.** Hold the channel's **A1** pad. The movement changes
   while you hold it and comes back when you let go. In every shipped set the
   left pads push the energy up and the right pads take it down; the top row
   is gentle, the middle row strong.
7. **Stop.** Press **Play\|Pause** again: the clip stops on the next downbeat,
   and the sound stays where it is.

That's the whole loop. Before your first gig, read
[On stage](a3motion-on-stage.md).

## Where next

| Page | What is in it |
| :--- | :--- |
| [How to …](a3motion-howto.md) | every task, one at a time, each with a GIF |
| [On stage](a3motion-on-stage.md) | stopping everything now, what not to do mid-set, the pre-gig check, troubleshooting |
| [Screen and panel](a3motion-reference.md) | every window, field, pad and key |
| [Menu, skins and keyboard](a3motion-menu.md) | the menu and its pages, skins, the on-screen keyboard |
| [How it thinks](a3motion-concepts.md) | the clock, start-up, how a shape sits on the sphere, rec modes, how actions play |
| [Library and scripting](a3motion-library.md) | the shipped sets, shapes, clips and actions, and how to script your own |

```{toctree}
:hidden:
:titlesonly:

a3motion-howto
a3motion-on-stage
a3motion-reference
a3motion-menu
a3motion-concepts
a3motion-library
```
