(motion-how-it-thinks)=

# How it thinks

(motion-clock)=

## Beat clock and clock modes

| Mode | Where the tempo comes from |
| :--- | :--- |
| **INT** | this device. Tap the beat display, or TAP on the panel |
| **EXT** | the beat analyser, listening to the music |
| **PIO** | Pro DJ Link: the tempo master on the link |

**Which one?** PIO when you play CDJs on a link, or [StemDeck](stemdeck.md)
as master; INT and tap for vinyl or a lone laptop; EXT when the beat analyser
is fed the music. What each one needs on the other end is on the
[Beat Analyzer](beat-analyzer.md) page.

In EXT and PIO, A³ Motion counts on by itself between beats and pulls itself
gently onto each beat that arrives. If the beats stop coming, it carries on at
the last tempo it had: clips keep playing, and slowly drift off the music
until the beats come back.

**The clock lives in one place**: the clock key top left, or **clock** on the
panel. It is not in the menu, and not saved in a set, because every booth is
wired differently. Check it at soundcheck, not at the drop. The rec mode isn't
saved in a set either.

(motion-start-up)=

## When the device comes up

A³ Motion asks A³ Core where each sound already is, and takes the answer
before it says anything itself. So switching the device on, or restarting it
mid-evening, doesn't move the room: the blobs appear where the sound actually
is, and the pots are where they were.

Before its window appears it waits up to 10 s for Core to announce the OSC
address file, so the screen comes up once, with the right addresses. Without
an announcement it opens on the file on disk; a change announced later
restarts it. See {ref}`Where addresses and ports live <osc-truth>`.

Loading a **set** is the other way round. That is a deliberate act, so the set
wins: it stops what was running, sets each channel's 3d, freq and Q, and
starts what the set says was running again, from the top, on the next
**downbeat**. Four clips starting together is the whole point of a set. The
shipped sets say nothing was running, so they load standing still; Play all on
PADS starts all four.

(motion-shape-on-sphere)=

## How a shape sits on the sphere

The recorded shape is a flat disc, wrapped over the room like a cap centred on
the height `elv` sets. A point pushed past `clip-top` or `clip-bot` keeps its
direction and only gives up its height, so a shape reaching into the ceiling
travels *around* it.

**`rot` goes all the way round**, the only knob that does: turn it far enough
and the shape is back where it began. **A spin that isn't running turns
nothing**: switched off, the shape stays at whatever angle it stopped at.

**The squeeze belongs to the shape.** Squeeze a circle into an ellipse and set
it spinning, and the ellipse turns with it.

(motion-rec-modes)=

## Touch, Latch, Write

Recording runs round and round inside the take's length, so each pass writes
over the pass before it. The **rec mode** says how much of the old take a pass
destroys, and it shows its own colour. If you know DAW automation, these are
the same three modes:

| Mode | What it does | Use it for |
| :--- | :--- | :--- |
| **Touch** | only changes where your finger is. Lift it, and the old movement carries on | drawing, and fixing a corner |
| **Latch** | once you've touched, the rest of the pass follows your finger's last spot, and the shape that was there is gone | parking a sound |
| **Write** | records over the whole pass, finger or not | starting clean |

**Drawing a shape? Use Touch, not Latch.** In Latch, lifting your finger
halfway parks the rest of the pass on that spot: a shape that goes somewhere
and then just… stays there.

A take is always the **last pass you finished**: stop halfway through one and
that half is dropped. Knob lanes are written with the same rec mode.

(motion-actions-play)=

## How actions play

**The accent** rises while an action pad is held, stays up as long as it is
held, and falls when you let go: `atk` is how long it takes to rise, `dec` how
long to fall, in bars. Your finger is the sustain, which is why there is no
sustain control. On the 3d row, the knob in the channel row shows the floor
you set, and the arc from there to where the accent has taken it is filled in.
When the fall is over, the clip does what its END-ACTION says, once.

**Hold or 1shot.** A Hold action belongs to your finger: it lasts while the
pad is down. A 1shot fires and runs its course on its own, like a sample pad.

**Actions are relative.** An action is worked out the moment you press,
against the clip as it is then: *half* halves whatever the clip is doing right
now, so the same pad hits harder on a wide clip than on a tight one.

**A random action is random once**, when you put it on the button. After that,
the pad lands in the same place every time, so you can learn it. Put it on
again to roll the dice again.

**Chains.** When a button's accent is over, the button its **then** names
fires, as a one-shot (no finger holds it). Chains may loop; to get out, press
another action pad, Play\|Pause or ■ on that channel.

**Two actions at once:** the last one pressed wins, and when it has fallen the
clip is back to itself, not to the first action.

**The set only names the actions.** What a button does lives in its script,
so every set that uses an action plays it the same way.

(motion-touchscreen)=

## Why the screen is not optional

The screen *is* the instrument. Menus, lists and the bar are driven by touch;
without the screen, the panel can't drive the device. Treat it like your CDJ
screens, and keep the drinks on the other side.

(motion-how-it-feels)=

## How a movement feels

The shipped library is built on what is known about how movement in sound is
heard:

- **Speed carries energy.** Faster turns and tempo-locked cycles read as more energetic; long,
  slow cycles as calm.
- **Height carries lift.** Up and overhead reads as open and bright, low and under the floor as
  heavy and dark.
- **Coming closer raises the tension.** Sound that approaches is heard as more arousing than
  sound that recedes, above all when it is already dark.
- **Smooth or angular.** Circles, roses and Lissajous figures read as pleasant; corners, zigzags
  and sudden jumps as tense.

The vocabulary the shapes and actions are made from:

- **Smalley's motion typology.** Rising and falling, oscillation, rotation around a centre,
  flying out from it or into it, dilation and contraction, vortex.
- **Rhythm cells.** The four-to-the-floor kick, the off-beat hi-hat, the tresillo (3+3+2) that EDM
  builds its tension on, the son clave in both directions, the shuffle and the gallop. A position
  that jumps on their sixteenths grooves in space.
- **Dub.** The desk as instrument: throws into the delay, repeats that fall away, filter
  sweeps, spring reverb, reversed tape.
- **Build-up, drop, breakdown.** The build widens, rises and opens the filter; the drop releases
  it all at once; the breakdown strips it back.

### The research behind it

- Russell's circumplex model of affect, and the Mood Meter built on it;
- studies of approaching and receding sound (Tajadura-Jiménez et al., *Embodied auditory
  perception*, 2010);
- the mapping of pitch and height;
- Denis Smalley's *Spectromorphology* (1997);
- Stockhausen's work with rotating sound, which found that past about sixteen rotations a second,
  movement stops being heard as movement at all;
- dub and dance-music production practice.

