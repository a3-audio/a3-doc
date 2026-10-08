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

| Word | Meaning |
| :--- | :--- |
| **channel** | one of the four mixer channels; channel 1 is leftmost on screen and panel, each in its own colour |
| **selected channel** | the one the bar shows; tap its field in the channel row |
| **shape** | the path the sound traces; labelled **SVG** |
| **clip** | a shape plus speed, height, width, spin, direction; one per channel |
| **pass** | one time through the shape |
| **action** | a short script on pads **A1–A6** that changes the clip while held (or once) |
| **set** | clip and six actions for each channel, plus 3d, freq and Q |
| **take** | a new shape drawn with your finger |
| **lane** | a knob movement recorded in a take |
| **downbeat** | beat one of a bar; Play waits for it |
| **3d** | how much of a channel is in the room: down is plain stereo |
| **bar**, **global strip** | the bottom of the screen: five tabs and their page (left), a column of keys (right) |
| **LENGTH** | beats per pass: 16 is four bars |

(motion-get-started)=

## Get started: your first ten minutes

You need A³ Motion, A³ Core and the A³ Mixer on the A³ switch, and music on a
mixer channel.

1. **Plug in** to the A³ switch (power comes over the cable). Ready when the
   sphere and four channel fields show; the meters move with the music (else
   [Troubleshooting](#motion-troubleshooting)).
2. **Check the clock** (top left): tap to **PIO** for CDJs on Pro DJ Link,
   **EXT** for the beat analyser, **INT** to tap yourself. The BPM should match.
3. **Load a set**: **FILES** › **SETS** › *Warmup* › **Load**; **FILES** closes.
4. **Turn 3d up** on your track's channel (its pot, or **3D** in the channel
   row). **At 3d = 0 you hear no movement.**
5. **Press Play\|Pause** (top left of its pads): it blinks, then starts on the
   downbeat.
6. **Hold A1**: the movement changes, and returns when you let go. Left pads
   push energy up, right pads down; top row gentle, middle row strong.
7. **Press Play\|Pause again**: it stops on the downbeat; the sound stays.

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
