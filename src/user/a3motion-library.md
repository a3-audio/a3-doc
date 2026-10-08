# Library and scripting

## Sets and moods

The library ships **50 shapes, 70 clips, 71 actions and 14 sets**, laid out along
**the arc of a night**: from the first half-empty hour, through the build and the
peak, to the last record. Every name starts with a **prefix** that says where it
belongs, so things that belong together sit together in every list in FILES:

| Kind | Prefix | Example |
| :--- | :--- | :--- |
| Sets | the phase of the night — the set *is* the prefix | `Peak` |
| Clips | the phase they are made for | `Peak Anthem` |
| Actions | what they do: **Move**, **Lift**, **Width**, **Speed**, **Dub**, **FX**, **Cue** | `Lift Up`, `FX Riser`, `Cue Peak Anthem` |
| Shapes | the family of the shape | `Flower Rose 5` |

The ten phases of the main arc, in the order a night usually runs:

`Warmup · Groove · Build · Peak · Drop · Break · Dub · Deep · Float · Closing`

Four **mood phases** sit beside it and are entered from it: **Tribal** after
Groove, **Tension** after Tribal, **Acid** after Break and **Ambient** after Deep.
That makes 14 phases, one set each.

**Any action may move and sound at once.** A gesture can turn the figure, open
the filter and push the 3d in one press; the mood sets are full of them. Only
**A5 stays the dedicated FX** and **A6 the Cue** into the next phase. So look at
an action's description before you press it in front of a full floor: a button
you have never used may change the mix as well as the position.

What makes a movement read one way or the other is well studied:

- **Speed carries energy.** Faster turns and tempo-locked cycles read as more energetic; long,
  slow cycles as calm.
- **Height carries lift.** Up and overhead reads as open and bright, low and under the floor as
  heavy and dark.
- **Coming closer raises the tension.** Sound that approaches is heard as more arousing than
  sound that recedes, above all when it is already dark.
- **Smooth or angular.** Circles, roses and Lissajous figures read as pleasant; corners, zigzags
  and sudden jumps as tense.

The moods are placed on the **mood meter**: energy, from calm to driving, against
pleasantness, from dark to open. The actions name the quarter they move the room
towards:

| Quarter | Energy | Feel |
| :--- | :--- | :--- |
| **Q1** euphoric | up | open, bright |
| **Q2** driving | up | tense, dark |
| **Q3** deep | down | dark, heavy |
| **Q4** calm | down | open, soft |

And the vocabulary the shapes and actions are made from:

- **Smalley's motion typology.** Rising and falling, oscillation, rotation around a centre,
  flying out from it or into it, dilation and contraction, vortex.
- **Rhythm cells.** The four-to-the-floor kick, the off-beat hi-hat, the tresillo (3+3+2) that EDM
  builds its tension on, the son clave in both directions, the shuffle and the gallop. A position
  that jumps on their sixteenths grooves in space.
- **Dub.** The desk as instrument: throws into the delay, repeats that fall away, filter
  sweeps, spring reverb, reversed tape.
- **Build-up, drop, breakdown.** The build widens, rises and opens the filter; the drop releases
  it all at once; the breakdown strips it back.

### The fourteen sets

One set per phase. Each loads the phase's first four clips onto channels 1–4;
the fifth clip of the phase is the **spare**, for a Cue or for loading by hand
from FILES › CLIPS.

| Set | Clips (channels 1–4) | Spare | A1 / A2 | A3 / A4 | A5 (FX) | A6 (Cue) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Warmup | Halo, Breath, Sunrise, Horizon | Drift | Lift Up / Width Close | Move Spin / Move Freeze | FX Swell | Cue Groove Four Floor |
| Groove | Four Floor, Tresillo, Clave, Offbeat | Shuffle | Move Spin / Speed Half | Speed Double / Move Freeze | FX Punch | Cue Build Riser |
| Build | Riser, Pulse, Loop, Gallop | Vortex | Width Open / Width Close | Speed Double / Speed Half | FX Riser | Cue Peak Anthem |
| Peak | Anthem, Festival, Carousel, Star | Euphoria | Width Full / Lift Ear Level | Move Spin Fast / Move Unwind | FX Impact | Cue Drop Impact |
| Drop | Impact, Warehouse, Strobe, Whirlwind | Ping Pong | Speed Stutter / Speed Halt | Width Full / Width Point | FX Punch | Cue Break Standstill |
| Break | Standstill, Collapse, Monolith, Suspend | Heartbeat | Lift Overhead / Move Freeze | Width Breathe / Width Point | FX Sweep | Cue Build Pulse |
| Dub | Echo, Pendulum, Tunnel, Kepler | Skank | Dub Spring / Dub Stitch | Dub Bounce Back / Dub Echo Throw | FX Sweep | Cue Deep Undertow |
| Deep | Undertow, Sub, Fog, Lurk | Cellar | Lift Sway / Lift Floor | Move Rock / Lift Down | FX Resonate | Cue Float Aurora |
| Float | Aurora, Canopy, Blossom, Lullaby | Cloud | Lift Overhead / Width Close | Width Breathe / Move Unwind | FX Swell | Cue Closing Sunset |
| Closing | Sunset, Farewell, Tide, Ember | Still | Lift Up / Lift Down | Width Open / Speed Tape Stop | FX Swell | Cue Warmup Halo |
| Tribal | Gallop, Ping Pong, Clave, Zigzag | Echo | Move Stomp / Move Call | Width Drum Roll / Speed Double Gallop | FX Thunder | Cue Tension Siren |
| Tension | Siren, Vortex, Helix, Riser | Collapse | Move Siren / Lift Climb | Speed Accelerate / Width Tighten | FX Filter Rise | Cue Drop Impact |
| Acid | Loop, Infinity, Epicycle, Pulse | Hypocycle | Move Squeeze Sweep / Width Inhale | Move Phase Drift / Speed Double Twist | FX Resonance Climb | Cue Dub Echo |
| Ambient | Drift, Wave, Breath, Kepler | Ellipse | Lift Cloud / Move Wind | Width Fog / Speed Slow Tide | FX Rain | Cue Float Aurora |

<!-- QUESTION (maintainer): the layout rule below says A3 is a strong "more", but Break and Float carry Width Breathe on A3, whose own Mood: line says "less" (library agent, 37b2001). The table shows what ships. Swap the actions, or change the rule? -->

The clip names in the table leave out the phase: channel 1 of *Peak* plays
`Peak Anthem`. All four channels of a set carry the same six actions.

**The six buttons sit the same way in every set**, so the hands learn one
panel rather than fourteen:

| | left | right |
| :--- | :--- | :--- |
| **top row** (A1 / A2) | a gentle **more** | a gentle **less** |
| **middle row** (A3 / A4) | a strong **more** | a strong **less** |
| **bottom row** (A5 / A6) | **FX** — the dedicated sound button: 3d and filter | **Cue** into the next phase |

In the ten main sets, *more* moves the room towards energy and openness, *less* towards calm and
weight. The four mood sets use the top two rows for their own gestures instead. Every action script says which it is on its `Mood:` line.

<!-- GIF: howto-library-load-set.gif | region: 0,0,768,1024 | recorded 2026-10-01, quiet-indigo-2, --fuzz 0 (quantized before optimizing) | steps: With four channels playing, open FILES › SETS, tap Warmup, tap Load, close FILES: the set is loaded, stopped. | "Four channels playing" / "FILES › SETS" / "Tap Warmup: it only shows" / "Load: the set is on, all stopped" / "Close FILES, then ▶ when ready" | a shipped set loads stopped, so it ends with FILES closed and ▶ ready -->

![With four channels playing, open FILES › SETS, tap Warmup, tap Load, close FILES: the set is loaded, stopped.](pics_user/howto-library-load-set.gif)

### The four mood sets

Each of these is one mood, built the way *Groove* is: four figures that belong
together, one per channel, and six gestures that each move several things at
once. Any channel can take any gesture. Where a gesture says *held*, it lasts
only while the pad is held. The first two rows are not "more" and "less" here,
they are different gestures of the same mood.

**Tribal** — percussive, close to the ground, call and answer. Sits after
*Groove*; A6 cues **Tension Siren**.

- Clips: Gallop (Rhythm Gallop), Ping Pong (Rhythm Ping Pong, which answers
  channel 1 from the opposite side), Clave (Rhythm Clave 2-3, Groove's clave turned
  round), Zigzag (Edge Zigzag, hard corners) · spare: Echo (Rhythm Echo).
- Actions: **Move Stomp** (held; the figure stamps round once a bar and leans to
  the floor), **Move Call** (the figure jumps to the opposite side and answers),
  **Width Drum Roll** (held; a fast squeeze sweep, front-back against
  left-right), **Speed Double Gallop** (held; twice as fast, low and rolling),
  **FX Thunder** (held; the 3d hits full and the filter goes low and dark),
  **Cue Tension Siren**.

**Tension** — circling, rising, faster. Sits after *Tribal* (or a *Build*); A6
cues **Drop Impact**.

- Clips: Siren (Orbit Circle), Vortex (Spiral Vortex), Helix (Spiral Helix),
  Riser (Spiral Riser) · spare: Collapse (Spiral Collapse), the moment before
  the drop.
- Actions: **Move Siren** (held; circles once a bar, brighter as it goes),
  **Lift Climb** (held; climbs to the ceiling while held), **Speed Accelerate**
  (held; four times as fast and turning), **Width Tighten** (held; narrows to a
  point and pulses), **FX Filter Rise** (held; the filter opens all the way,
  slowly, resonance high), **Cue Drop Impact**.

**Acid** — one figure turning slowly, hypnotic, with resonance. Sits after
*Break*; A6 cues **Dub Echo**.

- Clips: Loop (Loop 3-4), Infinity (Loop Infinity), Epicycle (Cycle Epi 3-1),
  Pulse (Orbit Pulse) · spare: Hypocycle (Cycle Hypo 5-3), the long one.
- Actions: **Move Squeeze Sweep** (held; the figure is squeezed and the squeeze
  sweeps), **Width Inhale** (held; the spread breathes out and in, the filter with
  it), **Move Phase Drift** (the figure slips a quarter turn and drifts out of
  phase, at most one turn in eight bars), **Speed Double Twist** (held; twice as
  fast and twisting), **FX Resonance Climb** (held; the acid line opens:
  resonance high, cutoff climbing), **Cue Dub Echo**.

**Ambient** — weather overhead, slow and wide. Sits after *Deep*; A6 cues
**Float Aurora**.

- Clips: Drift (Wander Drift, overhead), Wave (Wander Wave), Breath (Spiral
  Breath), Kepler (Orbit Kepler) · spare: Ellipse (Orbit Ellipse), calm and flat.
- Actions: **Lift Cloud** (held; the figure rises slowly into the ceiling and
  drifts there), **Move Wind** (held; a slow turn with a pull downwards),
  **Width Fog** (held; spreads wide and soft), **Speed Slow Tide** (held; half as
  fast, rising and falling like a tide), **FX Rain** (held; some 3d, the cutoff
  low, a long tail), **Cue Float Aurora**.

### Across a night

The A6 Cues chain the sets into the arc of a night:

- **The main line:** Warmup → Groove → Build → Peak → Drop → Break, and Break
  cues **Build** again, because after a breakdown comes the next build and the
  next drop. Round that loop as often as the floor asks for it.
- **The side road:** Dub → Deep → Float → Closing, and Closing cues **Warmup**
  for the next night (or the next DJ).
- **The mood sets** hang off the arc: Groove is followed by **Tribal**, which
  cues **Tension**, which cues **Drop** (Groove's own A6 still cues Build). **Acid**
  follows Break and cues **Dub**; **Ambient** follows Deep and cues **Float**.
  You enter them by loading the set in FILES.
- **Getting onto the side road** is up to you: load the Dub or the Deep set in
  FILES, or put one of the two spare Cues on a button — **Cue Dub Echo**, the dub
  escape, or **Cue Closing Still**, the emergency calm for when the fire alarm
  goes off.

**A Cue works on its own channel.** A6 on channel 2 puts the next phase's clip on
channel 2 and nowhere else, so you can walk the room into the next phase one
channel at a time. PADS' scene column fires only A1, A3 and A5 across the
channels, so no key cues the same clip onto all four at once; for all four
clips of the next phase, **Load the next set** in FILES.

**How a Cue plays:**

- The clip is loaded onto the channel and starts on the **next downbeat**; the
  old clip plays on until then. **SHIFT + Cue** starts it at once.
- The clip **stays**. A Cue fires no accent and nothing comes back afterwards:
  it changes *what* plays, not *how* it plays, like a clip launcher.
- While a take is recording on that channel a Cue does nothing; with a take
  waiting to be saved it says `-- SAVE THE TAKE FIRST`. A Cue whose clip has been
  deleted or renamed says `-- NO SUCH CLIP`.
- A Cue can cue any clip, your own takes included: copy one and change the
  clip it names (see [Scripting actions](#motion-scripting)).

<!-- GIF: howto-library-cue.gif | region: full screen 0,0,768,1024 | steps: load set "Warmup"; play all; open PADS (730,700); tap ch1 A6 (724,255); wait for the downbeat, 3 s | "A6: the Cue into the next phase" / "Groove Four Floor on the downbeat" / "The clip stays" -->

<!-- GIF: howto-library-cue-shift.gif | region: pads 0,36,768,590 | steps: set "Warmup" playing; hold SHIFT; tap ch2 A6; release SHIFT | "SHIFT + Cue: at once" -->

### Shapes (50)

![All fifty shapes; the rhythm figures are points, numbered in the order they are jumped to](pics_user/a3-motion-shapes-50.png)

A shape is the path alone — no speed, no height, no width; the clip adds those.
They are named `<Family> <Name>`. On disk the file name starts with the
shape's **length in beats**: `04_Rhythm_Four_Floor.svg` is one bar,
`32_Spiral_Riser.svg` eight. The number in brackets below is that length.

| Family | Shapes | Idea |
| :--- | :--- | :--- |
| **Rhythm** (9) | Four Floor (4), Offbeat (4), Tresillo (4), Ping Pong (4), Shuffle (4), Gallop (4), Clave 3-2 (8), Clave 2-3 (8), Echo (16) | positions that jump on the beat grid |
| **Orbit** (6) | Arc (8), Pendulum (8), Circle (16), Ellipse (16), Pulse (16), Kepler (32) | round the listener, or swinging |
| **Loop** (6) | Figure 8, Infinity, 1-2, 2-3, 3-2, 3-4 (all 16) | Lissajous loops: two tempos crossing |
| **Spiral** (5) | Collapse (16), Riser, Vortex, Helix, Breath (32) | out of the middle or into it |
| **Flower** (9) | Rose 3, Rose 4, Rose 5, Rose 7, Clover, Petal, Heart, Trefoil, Blossom 8 (all 16) | petals: smooth and open |
| **Cycle** (5) | Epi 3-1 (16), Epi 5-2, Epi 7-3, Hypo 5-3, Hypo 7-2 (32) | gears: loops inside a turn |
| **Edge** (8) | Square, Triangle, Diamond, Corner (4), Star, Zigzag, Cross (8), Astroid (16) | angular, tense |
| **Wander** (2) | Wave (16), Drift (32) | organic, no fixed shape |

The rhythm shapes are points, not lines — the sound jumps from one to the next
on the sixteenths of its rhythm:

- **Four Floor:** a jump on every beat, front → right → back → left.
- **Offbeat:** a jump on every off-beat eighth between two points — the house hi-hat.
- **Tresillo:** 3+3+2 sixteenths, the cell EDM builds its tension on before a drop.
- **Clave 3-2** and **Clave 2-3:** the son clave over two bars, either way round.
- **Ping Pong:** left and right.
- **Shuffle:** swung eighths between two points.
- **Gallop:** the sixteenth gallop, x.xx on every beat, over three points.
- **Echo:** throws that halve, like a delay's repeats.

### Clips (70), by phase

A clip is a shape plus everything it is played with: speed, height, width,
spin, the accent. Five per phase, 14 phases, named `<Phase> <Name>`; the first four are
the set's, the fifth is the spare.

| Phase | Clips (shape) | Character |
| :--- | :--- | :--- |
| **Warmup** | Halo (Orbit Circle), Breath (Spiral Breath), Sunrise (Flower Rose 7), Horizon (Loop Infinity) · spare: Drift (Wander Drift) | slow, high, open |
| **Groove** | Four Floor (Rhythm Four Floor), Tresillo (Rhythm Tresillo), Clave (Rhythm Clave 3-2), Offbeat (Rhythm Offbeat) · spare: Shuffle (Rhythm Shuffle) | jumps on the beat grid, at ear height |
| **Build** | Riser (Spiral Riser), Pulse (Orbit Pulse), Loop (Loop 3-4), Gallop (Rhythm Gallop) · spare: Vortex (Spiral Vortex) | opening, speeding up, rising |
| **Peak** | Anthem (Flower Rose 5), Festival (Loop 2-3), Carousel (Cycle Epi 7-3), Star (Edge Star) · spare: Euphoria (Flower Trefoil) | wide, fast, lifted |
| **Drop** | Impact (Edge Astroid), Warehouse (Edge Square), Strobe (Edge Corner), Whirlwind (Cycle Epi 3-1) · spare: Ping Pong (Rhythm Ping Pong) | hard, angular, close |
| **Break** | Standstill (Orbit Arc), Collapse (Spiral Collapse), Monolith (Edge Diamond), Suspend (Loop Figure 8) · spare: Heartbeat (Flower Heart) | still, suspended, drawn in |
| **Dub** | Echo (Rhythm Echo), Pendulum (Orbit Pendulum), Tunnel (Spiral Helix), Kepler (Orbit Kepler) · spare: Skank (Rhythm Offbeat) | throws, swings, near and far |
| **Deep** | Undertow (Spiral Collapse), Sub (Orbit Circle), Fog (Wander Drift), Lurk (Wander Wave) · spare: Cellar (Cycle Hypo 5-3) | low, slow, dark |
| **Float** | Aurora (Loop 1-2), Canopy (Cycle Hypo 7-2), Blossom (Flower Petal), Lullaby (Loop Figure 8) · spare: Cloud (Flower Clover) | overhead, slow, smooth |
| **Closing** | Sunset (Flower Rose 4), Farewell (Spiral Collapse), Tide (Wander Wave), Ember (Orbit Ellipse) · spare: Still (Orbit Circle) | descending, slowing, settling |
| **Tribal** | Gallop (Rhythm Gallop), Ping Pong (Rhythm Ping Pong), Clave (Rhythm Clave 2-3), Zigzag (Edge Zigzag) · spare: Echo (Rhythm Echo) | percussive, low, call and answer |
| **Tension** | Siren (Orbit Circle), Vortex (Spiral Vortex), Helix (Spiral Helix), Riser (Spiral Riser) · spare: Collapse (Spiral Collapse) | circling, rising, faster |
| **Acid** | Loop (Loop 3-4), Infinity (Loop Infinity), Epicycle (Cycle Epi 3-1), Pulse (Orbit Pulse) · spare: Hypocycle (Cycle Hypo 5-3) | one figure, slowly turning, hypnotic |
| **Ambient** | Drift (Wander Drift), Wave (Wander Wave), Breath (Spiral Breath), Kepler (Orbit Kepler) · spare: Ellipse (Orbit Ellipse) | overhead, slow, wide |

<!-- QUESTION (maintainer): the Character column comes from the library plan; the clip JSON files carry no mood text of their own. Should they, like the actions' Mood: line? -->

Plus **Default**: no shape. It is what a channel with no clip falls back on,
not something to play.

Some shapes turn up in several phases — Orbit Circle is a calm *Halo* in the
warm-up, a heavy *Sub* in Deep and a *Still* at closing time. The shape is the
path; the clip decides whether it floats overhead or rumbles under the floor.

### Actions (71)

An action changes the clip for as long as its accent lasts, then the clip comes
back to itself (see ACTION). The prefix says what it changes:

- **Move, Lift, Width, Speed, Dub** mostly move the sound: turns, height, spread,
  tempo of the shape, dub tricks in space. Any of them may also touch 3d, filter
  and resonance where the mood calls for it (the mood sets' gestures often do).
- **FX** are the dedicated sound actions — 3d and the filter. Every FX changes the sound.
- **Cue** loads a clip and plays it (see *Across a night* above).

**Mode**: **Hold** acts for as long as the pad is held; **1shot** fires and lets
go. In the tables, *more* moves the room towards energy and openness, *less*
towards calm and weight, and Q1–Q4 is the quarter of the mood meter it heads for.

**Move** — turns, direction, stillness:

| Action | What it does | Mood | Mode |
| :--- | :--- | :--- | :--- |
| Move Spin | the shape turns once every two bars | more — a steady turn; groove (Q1) | Hold |
| Move Spin Fast | a turn every half bar | more — rush; peak energy (Q1) | Hold |
| Move Unwind | the turn runs the other way, slowly | less — release; the turn let go (Q4) | Hold |
| Move Reverse | the shape runs backwards | less — the same idea from behind | Hold |
| Move Bounce | the shape bounces at its ends from here on | more — back and forth; playful (Q1) | 1shot |
| Move Freeze | everything holds still at one height | less — time stops; suspended (Q3/Q4) | Hold |
| Move Tilt | the shape leans forward and rocks | more — the room tips towards you (Q1/Q2) | Hold |
| Move Rock | the shape swings up and down the room | more — a swing; groove (Q1) | Hold |
| Move Mirror | the shape turned half round and run backwards | less — a reflective turn | Hold |
| Move Stomp | the figure stamps round once a bar and leans to the floor | more — percussive, low; tribal (Q1) | Hold |
| Move Call | the figure jumps to the opposite side and answers | a dialogue between channels | 1shot |
| Move Squeeze Sweep | the figure is squeezed and the squeeze sweeps | hypnotic — one figure, kneaded; acid (Q2) | Hold |
| Move Phase Drift | the figure slips a quarter turn and starts drifting | hypnotic — out of phase with the others; acid (Q2) | 1shot |
| Move Wind | a slow turn with a pull downwards | less — wind through the room; ambient (Q3) | Hold |
| Move Siren | the figure circles once a bar, brighter as it goes | more — an alarm; tension (Q2) | Hold |

**Lift** — height:

| Action | What it does | Mood | Mode |
| :--- | :--- | :--- | :--- |
| Lift Up | the shape rises a third of the way to the ceiling | more — lifts gently; bright (Q4 → Q1) | Hold |
| Lift Overhead | the shape snaps to the cap above the listener | more — up and bright (Q1) | 1shot |
| Lift Ear Level | a band at ear height: any clip becomes a ring | less — grounded, steady (Q4) | Hold |
| Lift Down | the shape sinks below ear height | less — weight; darker (Q3) | Hold |
| Lift Floor | the sound goes under the floor | less — heavy, dark (Q3) | Hold |
| Lift Sway | the height sways on the bar | more — a slow swell of height (Q4 → Q1) | Hold |
| Lift Cloud | the figure rises slowly into the ceiling and drifts there | less — weather overhead; ambient (Q3) | Hold |
| Lift Climb | the figure climbs to the ceiling while held | more — rising; tension (Q2) | Hold |

**Width** — spread:

| Action | What it does | Mood | Mode |
| :--- | :--- | :--- | :--- |
| Width Open | the shape spreads half again as wide | more — opens the room (Q1) | Hold |
| Width Full | the shape thrown to the whole sphere | more — everything, everywhere (Q1/Q2) | 1shot |
| Width Close | the shape halves its spread | less — focused, intimate (Q3/Q4) | Hold |
| Width Point | everything pulls in to one point | less — the sound comes close; tension (Q2) | Hold |
| Width Breathe | the spread opens and closes slowly | less — a calm breath (Q4) | Hold |
| Width Squash | pressed flat, springs back when you let go | less — pressure (Q2/Q3) | Hold |
| Width Drum Roll | a fast squeeze sweep, front-back against left-right | more — a roll on the skins; tribal (Q1) | Hold |
| Width Inhale | the spread breathes out and in, the filter with it | hypnotic — slow lungs; acid (Q2) | Hold |
| Width Fog | the figure spreads wide and soft | less — everything blurs; ambient (Q3) | Hold |
| Width Tighten | the figure narrows to a point and pulses | more — the room closes in; tension (Q2) | Hold |

**Speed** — the tempo of the shape:

| Action | What it does | Mood | Mode |
| :--- | :--- | :--- | :--- |
| Speed Double | the shape plays twice as fast | more — energy up, same shape (Q1/Q2) | Hold |
| Speed Half | the shape plays half as fast | less — energy down, same shape (Q4/Q3) | Hold |
| Speed Stutter | the shape chatters at a sixteenth | more — nervous; a stutter edit in space (Q2) | Hold |
| Speed Tape Stop | the shape winds down and stands still | less — the motor stops; the end of a phrase (Q3) | 1shot |
| Speed Halt | everything that moves on its own stops, and the pass ends | less — the reset | 1shot |
| Speed Double Gallop | twice as fast, low and rolling | more — the gallop runs; tribal (Q1) | Hold |
| Speed Double Twist | twice as fast and twisting | more — the line gets busy; acid (Q2) | Hold |
| Speed Slow Tide | half as fast, rising and falling like a tide | less — energy down; ambient (Q3) | Hold |
| Speed Accelerate | four times as fast and turning | more — faster and faster; tension (Q2) | Hold |

**Dub** — the dub desk's moves, played in space instead of on the sound:

| Action | What it does | Mood | Mode |
| :--- | :--- | :--- | :--- |
| Dub Echo Throw | the dub throw: reversed, bouncing, gliding out | less — a repeat that trails away (Q3) | 1shot |
| Dub Bounce Back | a hard swing out and back | more — a throw that returns (Q2) | 1shot |
| Dub Reverse Tape | backwards and slower, like a tape turned over | less — the reverse tape trick (Q3) | Hold |
| Dub Spring | a spring-reverb shake: a fast swell, short | more — a splash (Q2) | 1shot |
| Dub Scatter | somewhere else every time it is put on a button | more — a surprise; playful | 1shot |
| Dub Stitch | the gaps in a take glide shut | less — smooth, calm (Q4) | Hold |

**FX** — the dedicated sound actions:

| Action | What it does | Mood | Mode |
| :--- | :--- | :--- | :--- |
| FX Punch | depth hits, nothing moves | more — weight on the one; driving (Q2) | 1shot |
| FX Sweep | the filter opens over two bars, nothing moves | more — the dub woosh; tension that lifts | Hold |
| FX Resonate | the resonance creeps up | more — slow tension (Q3 → Q2) | Hold |
| FX Riser | four bars of build: spread, spin, filter | more — the build before the drop (Q2 → Q1) | Hold |
| FX Impact | the drop: everything at once, then a long fall | more — the release; impact (Q2 → Q1) | 1shot |
| FX Swell | depth and filter rise together, gently | more — a warm lift (Q4 → Q1) | Hold |
| FX Thunder | the 3d hits full and the filter goes low and dark | more — weight under the drums; tribal (Q1) | Hold |
| FX Resonance Climb | the acid line opens: resonance high, cutoff climbing | more — the squelch; acid (Q2) | Hold |
| FX Rain | a soft wash: some 3d, the cutoff low, a long tail | less — rain on the roof; ambient (Q3) | Hold |
| FX Filter Rise | the filter opens all the way, slowly, resonance high | more — the riser before the drop; tension (Q2) | Hold |

**Cue** — load a clip, play it on the next downbeat:

| Action | Loads | On A6 of |
| :--- | :--- | :--- |
| Cue Groove Four Floor | Groove Four Floor | Warmup |
| Cue Build Riser | Build Riser | Groove |
| Cue Peak Anthem | Peak Anthem | Build |
| Cue Drop Impact | Drop Impact | Peak |
| Cue Break Standstill | Break Standstill | Drop |
| Cue Build Pulse | Build Pulse | Break |
| Cue Deep Undertow | Deep Undertow | Dub |
| Cue Float Aurora | Float Aurora | Deep |
| Cue Closing Sunset | Closing Sunset | Float |
| Cue Warmup Halo | Warmup Halo | Closing |
| Cue Dub Echo | Dub Echo | — the dub escape |
| Cue Closing Still | Closing Still | — the emergency calm |
| Cue Tension Siren | Tension Siren | Tribal |

**README** in the ACTIONS list is not an action but the scripting manual.
Firing it changes nothing.

<!-- GIF: howto-library-assign-cue.gif | region: 0,672,578,352 | recorded 2026-09-29, 7.5 s | steps: On channel 2's ACTION page tap A6, then tap Cue Dub Echo in the list: A6 carries it. | "Channel 2, ACTION" / "Tap A6: the list shows its script" / "Tap Cue Dub Echo: A6 carries it" | A6 set to Cue Drop Impact beforehand, so Cue Dub Echo sits right below it without scrolling -->

![On channel 2's ACTION page tap A6, then tap Cue Dub Echo in the list: A6 carries it.](pics_user/howto-library-assign-cue.gif)

## The research behind it

The research this rests on:

- Russell's circumplex model of affect, and the Mood Meter built on it;
- studies of approaching and receding sound (Tajadura-Jiménez et al., *Embodied auditory
  perception*, 2010);
- the mapping of pitch and height;
- Denis Smalley's *Spectromorphology* (1997);
- Stockhausen's work with rotating sound, which found that past about sixteen rotations a second,
  movement stops being heard as movement at all;
- dub and dance-music production practice.

(motion-under-the-hood)=

## Under the hood

For scripters and technicians. Nothing here is needed to play.

(motion-scripting)=

### Scripting actions

**The FILES editor** edits every kind of file: sets and clips as JSON, shapes
as SVG, actions as scripts.

**What ACTION writes.** Every knob on the ACTION page, the mode, **then** and
every MOTION value changes exactly one line of the chosen button's script
(`~spin = 3;`, `~envelopeMax = 0.5;`, `~then = 3;`); your comments and every
other line stay as you wrote them. A line that was commented out is switched
on, a missing one is added, and a random value (`rrand`) becomes the number
you turned to. **Two taps** on a MOTION value, or on **then**, comment the line
out again.

- **The editor follows.** If FILES shows the same script, its text changes
  with the knob — also while you are typing in it; what you typed stays.
- **Written when the hand stops**, about a third of a second after the last
  turn, and before a set is loaded or FILES saves, renames or deletes.

**A Cue** is a script with one line, `~clip = "Peak Anthem";`. Copy one with
**Save as**, change the name in the quotes, **Save**, and it cues any clip you
like — your own takes included.

**Every shipped action script** carries a `Mood:` line under its title that
says which way it moves the room, and a line that says why. **README** in the
ACTIONS list is the language's manual, written as a script whose every line is
a comment.

(motion-system)=

### A³ Motion and the rest of the system

A³ Motion talks to A³ Core, the A³ Mixer and the beat analyser over OSC. The
full list of messages is in the [OSC reference](../ressources/osc.md).

- **Positions:** each channel's azimuth and elevation go to Core while its
  blob moves. At start-up Core is asked where each sound already is (see
  [When the device comes up](#motion-start-up)).
- **3d** crossfades the channel between its stereo and its multichannel
  encoder in A³ Core; **freq** and **Q** are its filter.
- **CHMIX and MIXER** send the same messages the A³ Mixer sends. Core passes
  on whatever REAPER reports, which is why a hand on the desk or in REAPER
  moves the knobs on the screen too.
- **The meters and the lightning** are the levels Core's audio engine sends
  back: the four channels, the subwoofer and the four speakers.
- **The clock:** in INT the device sends `/beat`; in EXT it follows the
  `/beat` the beat analyser sends; a tap on the beat display or on TAP sends
  `/tap` in every mode.
- **SHIFT + an action pad** plays the action with the messages to Core held
  back, which is why only the screen sees the preview.
- **Hosts, ports and addresses** come from `a3-osc.json`, not from the
  device's own settings. See
  [How to point the device at another Core](#motion-howto-network).

### The squeeze, in numbers

The squeezes `sqzX` and `sqzY` are bipolar, with their middle at zero, and
multiply their axis by 2^value: half at one end, double at the other. X is
front to back, Y is left to right. **The squeeze happens before the turn**, so
the ellipse belongs to the shape and travels with it.

### The panel's electronics

The panel has a microcontroller of its own and connects to the UI computer
over USB. What it is made of, which computers run the UI and how its serial
port is found: {ref}`A³ Motion hardware <moc-hardware>`.
