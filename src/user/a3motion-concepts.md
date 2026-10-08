(motion-how-it-thinks)=

# How it thinks

(motion-clock)=

## Beat clock and clock modes

| Mode | Tempo from | Use for |
| :--- | :--- | :--- |
| **INT** | this device: tap the beat display or TAP | vinyl, a lone laptop |
| **EXT** | the beat analyser, listening | music fed to the analyser |
| **PIO** | the Pro DJ Link tempo master | CDJs, or [StemDeck](stemdeck.md) as master |

Details: [Beat Analyzer](beat-analyzer.md). In EXT and PIO the device counts
on between beats and eases onto each one; if beats stop, it keeps the last
tempo and slowly drifts. **The clock is set only on the clock key** (or panel
**clock**), never saved in a set, since every booth differs: check it at
soundcheck. The rec mode isn't saved in a set either.

(motion-start-up)=

## When the device comes up

**Start-up never moves the room**: Motion asks Core where every sound is and
takes the answer before sending anything. It waits up to 10 s for Core's
address file, so its window opens once with the right addresses (no
announcement: the file on disk; a later change restarts it;
{ref}`truth <osc-truth>`).

**Loading a set is the opposite**: the set wins. It stops everything, sets 3d,
freq and Q, and restarts what the set says was playing, together, on the next
**downbeat**. Shipped sets say nothing was playing; PADS › Play all starts them.

(motion-shape-on-sphere)=

## How a shape sits on the sphere

- The shape is a flat disc wrapped over the room like a cap, centred at `elv`.
- Past `clip-top` or `clip-bot` a point keeps its direction and loses height,
  so a shape travels **around** a ceiling.
- **`rot` goes all the way round**; a stopped spin leaves the shape where it is.
- **The squeeze belongs to the shape**: a squeezed circle spins as an ellipse.

(motion-rec-modes)=

## Touch, Latch, Write

Recording loops inside the take's length, each pass over the last. The rec
mode (in its own colour) says how much a pass replaces — as in DAW automation:

| Mode | What it does | Use it for |
| :--- | :--- | :--- |
| **Touch** | changes only where your finger is | drawing, fixing a corner |
| **Latch** | after a touch, holds your last spot for the rest of the pass | parking a sound |
| **Write** | overwrites the whole pass | starting clean |

**Draw in Touch, not Latch**: in Latch, lifting halfway parks the rest of the
pass. A take is the **last finished pass**; lanes use the same mode.

(motion-actions-play)=

## How actions play

- **The accent** rises (`atk`, bars) while the pad is held, holds, and falls
  (`dec`) on release: your finger is the sustain. On 3d, the channel-row knob
  shows the floor and the filled arc the accent. After the fall the clip does
  its END-ACTION once.
- **Hold** lasts while the pad is down; **1shot** runs its course alone.
- **Relative**: worked out at the press against the clip as it is, so *half*
  hits harder on a wide clip.
- **Random once**, when assigned; then the same every time. Reassign to reroll.
- **Chains**: when an accent ends, **then** fires its button as a one-shot.
  Chains may loop; stop with another pad, Play\|Pause or ■.
- **Two at once**: the last press wins; afterwards the clip returns to itself.
- **A set only names actions**; the script decides what they do, everywhere.

(motion-touchscreen)=

## Why the screen is not optional

The screen *is* the instrument: menus, lists and the bar need touch. Treat it
like your CDJ screens; keep drinks away.

(motion-how-it-feels)=

## How a movement feels

The library is built on how moving sound is heard:

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

