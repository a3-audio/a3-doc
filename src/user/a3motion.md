# A³ Motion

(motion-at-a-glance)=

## At a glance

A³ Motion moves up to four channels of your mixer through the room, in time
with the music. Each channel's sound travels along a **shape** — a circle, a
rose, a zigzag, a jump on every beat — past the speakers around the floor and
over the heads of the crowd. It makes no sound of its own: it tells A³ Core
where each channel should be, and Core moves the sound.

Think of each channel as a deck. It has one **clip** loaded (a shape, plus how
fast, how wide and how high it runs) and six **action pads** for the accents
you play by hand. A **set** loads all four channels in one go.

Everything runs on a beat clock, so a shape that takes four bars keeps taking
four bars when the tempo changes.

- [A³ Motion Repository](https://github.com/a3-audio/a3-motion)
- Standalone OSC controller: a panel of encoders, pots and pads beside a
  7" full-colour multi-touch screen

![A³ Motion](pics_user/a3-motion-icon_light.png)

<!-- GIF: howto-hero-sphere.gif | region: sphere 0,36,768,590 | steps: a set playing on all four channels; no interaction, 5 to 6 s | "Four channels, one room" | bonus, not counted in round 1 -->

<!-- The screenshots and GIFs on this page are to be (re)made in the skin
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
4. **Turn 3d up** on the channel your track is on: the pot at the top of that
   channel's column on the panel, or **3D** in its field in the channel row.
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
[Get me out of here](#motion-panic). The [how-to](#motion-howto) tasks below
cover everything else you will want to do; the reference after them lists
every control.

(motion-howto)=

## How to …

(motion-howto-load)=

### How to load a set or a clip

1. Tap **FILES** in the global strip. It opens on top of the sphere.
2. Tap **SETS** for a set, **CLIPS** for a clip. To load a clip, select its
   channel first.
3. Tap a row. **A tap only shows it** in the editor on the right; nothing on
   the device changes yet.
4. Tap **Load**. A set goes onto all four channels and starts on the next
   downbeat; a clip goes onto the selected channel.
5. Tap **FILES** again (or any tab) to close it.

```{warning}
**Loading a set mid-set** stops all four clips, jumps every channel's 3d, freq
and Q to the set's values — the room hears it — and starts the set's clips
together on the next downbeat.
```

<!-- GIF: howto-files-load-set.gif | region: 0,36,768,636 (overlay plus the channel row, where the names change) | steps: FILES; SETS; tap Warmup; Load; wait for the downbeat | "Tap a set: it only shows" / "Load: all four channels" / "They start on the downbeat" | round 1, no. 1; re-record replaces howto-load-a-set.gif -->

![How to load a set](pics_user/howto-load-a-set.gif)

<!-- GIF: howto-files-load-clip.gif | region: full screen 0,0,768,1024 | steps: tap face 2; FILES; CLIPS; tap a row; Load | "Choose the channel first" / "Load puts the clip on it" | round 2 -->

(motion-howto-play)=

### How to play and stop a clip

- **Start:** press the channel's **Play\|Pause** pad, or select the channel
  and tap **▶** in the global strip. It starts on the **next downbeat** and
  blinks while it waits.
- **Stop on the beat:** press **Play\|Pause** again, or tap **❚❚** (the same
  key on the screen). The clip stops on the next downbeat.
- **Stop now:** tap **■** on the screen, or hold **SHIFT** and press
  **Play\|Pause** on the panel.
- **Call off a start that is still waiting:** press Play\|Pause again while
  it blinks.
- **Start or stop all four:** open **PADS** and use the grey block on the
  left: **Play all** starts every clip that is standing still, **Stop all**
  stops all four at once.

Every start begins at the top of the shape. A stop leaves the sound where it
is; it doesn't jump anywhere.

<!-- QUESTION (maintainer): the key is called Play|Pause and shows ❚❚, but in the code a "pause" is a stop: every start begins at position 0 (MotionEngine::startPlaying), so ❚❚, SHIFT + Play|Pause and ■ all end in the same state and differ only in timing. The page describes it that way. Is that the intent (and the label stays), or should ❚❚ resume where it stopped? -->

<!-- GIF: howto-transport-play-pause.gif | region: 0,626,768,398 (the progress bar shows the start) | steps: tap ▶; wait for the downbeat; 2 s; tap ❚❚ | "▶ waits for the next downbeat" / "Blinking means waiting, not broken" / "❚❚ lands on the downbeat too" | round 1, no. 2; re-record replaces howto-play-pause.gif -->

![How to play and pause a clip](pics_user/howto-play-pause.gif)

<!-- GIF: howto-transport-stop.gif | region: 0,626,768,398 | steps: clip playing; tap ■; tap ▶ | "■ stops now, no waiting" / "Next ▶ starts from the top" | round 1, no. 21 -->

<!-- GIF: howto-pads-scene.gif | region: 0,36,768,590 | steps: PADS; Play all; downbeat; 2 s; Stop all | "The grey block plays all four" / "Play all: in on the downbeat" / "Stop all: all four, right now" | round 1, no. 7 -->

<!-- GIF: howto-pads-shift-now.gif | region: pads 0,36,768,590 | steps: clip playing; hold SHIFT on PADS; tap the channel's Play|Pause | "SHIFT + Play|Pause: stop now" | blocked: needs two pointers, xdotool has one -->

(motion-howto-drag)=

### How to move a sound by hand

1. Put a finger on a channel's blob on the sphere and drag. The sound goes
   where your finger goes. **A drag is live and doesn't wait for the beat**:
   the room hears every centimetre.
2. Let go. A playing clip takes the sound back onto its shape; a stopped one
   leaves it where you let go.

Two fingers take two blobs. The top of the sphere is the front of the room.

<!-- QUESTION (maintainer): which way is "front" in a venue? The osc reference says 0° azimuth is the front of the room; the page now says the top of the sphere is the front. A DJ needs to know where that is before dragging: the booth side, the stage, or wherever Core was set up? -->

To look at the room from another angle **without moving anything**, use
camera mode: tap the small sphere in the global strip, drag on the sphere to
lean and turn the view, and double tap to go back to straight above. In camera
mode no finger can move a sound.

<!-- GIF: howto-sphere-drag-blob.gif | region: 0,36,768,590 | steps: clip playing; drag ch1 blob in an arc; hold 2 s; release | "Drag a blob: the sound follows" / "Let go: the clip takes it back" | round 1, no. 3; record with the clip playing -->

<!-- GIF: howto-sphere-camera-mode.gif | region: 0,36,768,988 | steps: tap the elevation picture; drag down; drag sideways; double tap | "Small sphere: camera mode" / "Drag to lean and turn the view" / "Double tap: back to above" | round 1, no. 22 -->

<!-- GIF: howto-sphere-zoom.gif | region: sphere 0,36,768,590 | steps: camera mode on; mouse wheel up 5 notches (xdotool click 4), then down 5 (click 5); double tap | "Camera mode: zoom in and out" / "Double tap resets the zoom" | round 2; the wheel leaves no finger ring, so the caption must not say pinch -->

(motion-howto-clip)=

### How to change the shape, the speed and the direction

On the **CLIP** tab, for the selected channel:

- **Another shape, same values:** drag the **SVG** field with a thumb. Each
  step is a new shape; speed, height and everything else stay put.
- **Another clip, shape and values together:** drag the **CLIP** field.
- **Faster or slower:** tap one of the four **LENGTH** keys. The number is how
  many beats one pass takes: fewer beats, faster laps. Drag a key up or down to
  give it another length; the key keeps it.
- **Direction:** tap **DIRECTION** to step forwards, backwards, there and
  back, or a random start each pass.
- **What happens at the end of a pass:** tap **END-ACTION** to step Loop,
  Stop, or Paus (pause).

CLIP and SVG are separate on purpose, so browsing shapes never sneaks someone
else's preset onto your channel mid-set.

<!-- GIF: howto-clip-length-tap.gif | region: 0,36,768,988 | steps: playing; tap a long LENGTH, 3 s; tap a short one, 3 s | "Tap a LENGTH to play at it" / "Fewer beats, faster laps" | round 1, no. 8 -->

<!-- GIF: howto-clip-choose-shape.gif | region: 0,36,768,988 | steps: playing; drag SVG up 3 steps | "Drag SVG: a new shape" / "Your values stay put" | round 1, no. 9 -->

<!-- GIF: howto-clip-choose-clip.gif | region: 0,36,768,988 (the effect is on the sphere) | steps: playing; drag CLIP up 3 steps | "Drag CLIP: a whole new preset" / "New shape, new values" | round 1, no. 10 -->

<!-- GIF: howto-clip-direction.gif | region: 0,36,768,988 | steps: playing; tap DIRECTION x3, 2 s apart | "Tap DIRECTION to step it" / "Bnce: there and back again" | round 1, no. 15 -->

<!-- GIF: howto-clip-length-drag.gif | region: bar 0,672,578,352 | steps: drag LENGTH (494,800) up 36 px (3 steps), release | "Drag a LENGTH key" / "The key keeps the new length" | round 2 -->

<!-- GIF: howto-clip-stop-vs-paus.gif | region: sphere and bar 0,36,768,988 | steps: short LENGTH; END-ACTION on Stop, let a pass run out; then Paus, let a pass run out | "Stop: back to the start" / "Paus: stays where it ends" | round 2; replaces howto-clip-end-action.gif -->

(motion-howto-motion)=

### How to shape the movement

On the **MOTION** tab every field has two knobs: **the right knob sets a
value, the left knob moves it** in time with the bars.

- **Point the shape somewhere else:** `rot`. **Keep it turning:** `spin` —
  one way or the other.
- **Wider or tighter:** `reach`. **Breathing in and out:** `swell`.
- **Higher or lower:** `elv`. **Rising and falling:** `sway`.
- **A ceiling and a floor** the sound can't pass: `clip-top` and `clip-bot`
  (the one field where both knobs set a value).
- **Squash it** front to back or side to side: `sqzX`, `sqzY`.
- **Lean it** forward or back: `tilt`. **Sideways:** `roll`.
- **Back to rest:** double tap the knob.

Whatever moves on its own counts in bars, never seconds, so it comes back to
where it started on a bar line.

<!-- GIF: howto-motion-rotation.gif | region: 0,36,768,988 | steps: MOTION; drag rot; drag spin 2 steps; wait 3 s; double tap spin | "rot turns the shape" / "spin keeps it turning" / "Double tap: spin off" | round 1, no. 11; replaces howto-motion-knob.gif and howto-motion-sweep.gif -->

<!-- GIF: howto-motion-elevation.gif | region: 0,36,768,988 | steps: drag elv down; drag clip-top up | "elv: how high the shape sits" / "clip-top: a ceiling it goes round" | round 1, no. 24 -->

<!-- GIF: howto-motion-tilt-roll.gif | region: sphere and bar 0,36,768,988 | steps: camera mode on, lean view 45°; drag tilt up 40 px; drag roll up 40 px; double tap both | "tilt and roll lean the plane" / "Double tap: flat again" | round 2 -->

(motion-howto-action)=

### How to fire and assign actions

**Fire an action:**

- **From the pads:** hold one of the channel's action pads, A1–A6, on the
  panel or on the PADS window. It fires **at once**. The ACTION page comes up
  with that button chosen.
- **From the screen:** on the ACTION tab, tap a button (A1–A6) to choose it —
  a tap only chooses, it doesn't fire — then hold **A** in the global strip.
- **Audition it privately:** hold **SHIFT** and press an action pad. It plays
  on the screen only; the room hears nothing until you let go of the pad.

**Put another action on a button:**

1. Open the ACTION tab and tap the button, A1–A6.
2. Tap a script in the list next to it. It is on the button now.
3. **no action** at the top of the list empties the button.

```{warning}
**Turning a value on ACTION changes the action everywhere.** What you set
there is saved into the action's script — for every channel and every set
that uses that action, shipped sets included. To experiment, make a copy
first: **EDIT**, then **Save as** in FILES, and put the copy on the button.
```

<!-- GIF: howto-action-fire.gif | region: 0,36,768,988 | steps: clip playing; ACTION; tap A1; hold A (global strip) 2 s; release | "Tap A1 to choose it" / "Hold A: the action takes over" / "Let go: the clip is itself again" | round 1, no. 4; fired with the global strip's A, since the fields only choose (2026-09-28); replaces howto-fire-an-action.gif -->

<!-- GIF: howto-action-assign.gif | region: 0,672,578,352 | steps: tap A2; tap list row 3; scroll to top; tap no action | "Tap a button to choose it" / "Tap a script: now it's on it" / "\"no action\" at the top clears it" | round 1, no. 12; re-record replaces howto-assign-an-action.gif -->

![How to put another action on a button](pics_user/howto-assign-an-action.gif)

<!-- GIF: howto-action-audio.gif | region: 0,626,768,398 | steps: tap A1; drag 3d max up; hold A (global strip, 630,978) 1.5 s | "max: how far the 3d accent goes" / "Hold A and watch the 3D arc" | round 1, no. 16 -->

<!-- GIF: howto-action-writes-script.gif | region: 0,36,768,988 | steps: tap A1; MOTION tab of the card; turn spin; EDIT; the ~spin line shows the value | "Turn a value on the card" / "EDIT: the script says the same" / "Every set using it hears it too" | round 1, no. 25 -->

<!-- GIF: howto-action-then.gif | region: bar 0,672,578,352 | steps: tap A1; tap then (370,858) x3 | "then: what fires next" / "A1 then A3" | round 2 -->

<!-- GIF: howto-action-mode.gif | region: bar 0,672,578,352 | steps: tap A3; tap mode x2; fire once in 1shot, then in Hold | "1shot: fire and forget" / "Hold: as long as you hold" | round 2; only worth it if it shows the difference -->

(motion-howto-take)=

### How to record a take, and keep it or throw it away

1. Select the channel in the channel row.
2. Tap **●**. The take is **armed**: REC opens, ● and ▶ light, and the clip
   keeps playing. **■** or **●** again disarms it.
3. On REC, choose the length (the lit **LENGTH** key is how long the take
   will be) and the rec mode — **Touch** to draw a shape.
4. Tap **▶**. The take starts on the **next downbeat**.
5. Drag on the sphere: the first finger down writes the position, wherever it
   lands. The line appears as you draw. Knobs you turn on MOTION are recorded
   too, see [below](#motion-howto-lanes).
6. Tap **●** (or **■**) to end the take. A take is always the **last full
   pass**: stop halfway through one and that half is dropped.
7. Tap **SAVE** (where ● was) to keep it: the shape, and a clip with every
   value it has now. **DISCARD** (where A was) asks twice, then puts back what
   the channel held before.

**A take is live**: the room hears what you draw. To practise without the
room, turn the channel's 3d down first.

Nothing is lost while you decide. The take keeps playing, marked unsaved,
until you tap SAVE or DISCARD, or something replaces it: a new take, a shape
or a set loaded, a restart.

**On the panel:** hold **REC** and press the channel's **Play\|Pause** pad.
That skips arming; the take starts on the next downbeat. Press REC again to
end it.

<!-- GIF: howto-rec-take.gif | region: 0,36,768,988 | steps: LENGTH 4 lit, Touch; ●; ▶; after the downbeat draw one lap; ● | "● arms, ▶ starts on the downbeat" / "Draw one full lap on the sphere" / "● ends the take" | round 1, no. 5; LENGTH 4 keeps it under 10 s at 124 BPM; replaces howto-rec-arm.gif -->

<!-- GIF: howto-rec-save-discard.gif | region: 0,626,768,398 | steps: after a take: tap DISCARD once (asks); tap SAVE | "DISCARD asks twice, on purpose" / "Changed your mind? SAVE keeps it" | round 1, no. 6; replaces howto-rec-save.gif and howto-rec-discard.gif -->

<!-- GIF: howto-rec-setup.gif | region: bar 0,672,578,352 | steps: on REC: tap a LENGTH key; watch it light | "The lit LENGTH is the take length" | round 2; rec mode and fade split off (fade can't be seen on screen) -->

(motion-howto-lanes)=

### How to record knob moves

During a take, turn any knob on MOTION. It is written into a **lane**, drawn
in red while it writes, with the same rec mode as the shape. On playback the
lane turns the knob by itself; your hand on the knob wins while it holds.
Double tap a knob to clear its lane; the other lanes stay.

<!-- GIF: howto-rec-knob-lane.gif | region: sphere and bar 0,36,768,988 | steps: MOTION tab; arm and start a take; drag rot up and down for one pass; end take; wait one pass; double tap rot | "Knobs turned in a take" / "come back as a lane" / "Double tap clears the lane" | round 2 -->

(motion-howto-save)=

### How to keep a tweak and save your set

- **Keep a clip you changed.** A warning-coloured **drift dot** on the CLIP
  field means its values have been turned since it was loaded. Open FILES ›
  **CLIPS**, tap **from clip**, then **Save as**. Your copy lands in your own
  files, named after the original ("Warmup Halo 2").
- **Keep tonight's set.** FILES › **SETS**, tap **from set**, then
  **Save as**.
- **Give it a name.** Tap the row, tap **Rename**, type, and tap **Keep** (or
  ENTER).
- **Clear out the library.** Tap the row, tap **Delete**, and tap it again
  when it asks **Sure?**. Delete removes the file, not the music: whatever is
  loaded keeps playing.

<!-- GIF: howto-files-keep-tweak.gif | region: 0,36,768,988 | steps: (knob turned beforehand) CLIP tab with the drift dot; FILES; CLIPS; from clip; Save as | "The dot: this clip has changed" / "CLIPS › from clip, then Save as" / "Your tweak, kept as a new clip" | round 1, no. 14; replaces howto-files-from-clip.gif -->

<!-- GIF: howto-files-save-set.gif | region: 0,36,768,590 | steps: FILES; SETS; from set; Save as | "SETS › from set: your set as text" / "Save as: keep it for the gig" | round 1, no. 13 -->

<!-- GIF: howto-keyboard-rename.gif | region: full screen 0,0,768,1024 | steps: FILES; Rename; type a name on the keyboard; ENTER | "Rename: the keyboard comes up" / "ENTER keeps the name" | round 2 (reserve); replaces howto-files-rename.gif and howto-statusbar-keys.gif -->

<!-- GIF: howto-files-delete.gif | region: files 0,36,768,590 | steps: tap a user row; tap Delete (65,560); tap Delete again | "Delete asks: Sure?" / "Press again to delete" | round 2 -->

<!-- GIF: howto-files-edit-save.gif | region: files 0,36,768,590 | steps: tap ACTIONS; tap a user row; tap in editor, type a change; tap another row (refused); tap Save (65,601) | "Type in the editor" / "Unsaved text holds the list" / "Save or Cancel" | round 3 -->

(motion-howto-mix)=

### How to mix from the screen

- **One channel:** select it and open the **CHMIX** tab — its gain, EQ,
  send, PFL, FX and volume.
- **All four and the master:** tap **MIXER** in the global strip.
- **Volume:** the meter *is* the VOL fader. Grab it anywhere and drag; it
  moves one to one from where it stood, so it never jumps.
- **Back to a default:** double tap a knob (EQ flat, SEND off, volume full).
  The master fader has no double tap, on purpose.

These are the A³ Mixer's own controls, and the two follow each other. The A³
Mixer has no motor faders, though: turn something on the screen and the
hardware control stays where it is. The next time you touch it, the level
jumps to wherever the hardware control sits.

<!-- GIF: howto-chmix-volume.gif | region: 0,672,578,352 | steps: CHMIX; drag the meter from its middle down, then up | "The meter is the VOL fader" / "Grab it anywhere, it won't jump" | round 1, no. 17; replaces howto-mixer-volume.gif -->

<!-- GIF: howto-chmix-knobs.gif | region: bar 0,672,578,352 | steps: CHMIX tab (400,700); drag HIGH up 30 px; double tap HIGH; drag SEND up 40 px; double tap SEND | "Drag to turn" / "Double tap: EQ flat, SEND off" | round 2; one "double tap resets" GIF for CHMIX and MIXER -->

<!-- GIF: howto-mixer-master.gif | region: mixer 0,36,768,590 | steps: drag the master column down 40 px, back up; drag PHN up 20 px | "The master column is the fader" / "BTH, MIX, PHN, RET beside it" | round 2 -->

<!-- GIF: howto-mixer-filter.gif | region: mixer 0,36,768,590 | steps: tap FX MODE x2; drag FX FREQ up 40 px; double tap FX FREQ | "FX MODE: HPF or LPF" / "One filter for all four" | round 2 -->

(motion-howto-tempo)=

### How to set the tempo by hand

1. Tap the clock key (top left) until it reads **INT**.
2. Tap the beat display — the four cells beside the readout — in time with
   the music, or press **TAP** on the panel. The first tap after a pause is
   the one; the BPM follows your taps.

In EXT and PIO the tempo comes from outside, and your taps are passed on to
the beat analyser.

<!-- GIF: howto-statusbar-tap.gif | region: 0,0,560,36 at --width 560 | steps: clock key to INT; tap the beat display 8x at ~120 BPM | "Clock on INT" / "Tap the beat display in time" / "The BPM follows your taps" | round 1, no. 18; absorbs howto-statusbar-clock.gif -->

(motion-howto-look)=

### How to change the look

- **Calm the screen down:** tap **CLEAN** in the status bar. Thin lines,
  plain blobs, no effects: easier to read in a dark booth, and lighter on the
  machine. Tap again for your skin.
- **Another skin:** MENU › **Skin**. Each skin previews on the sphere as you
  browse; tap one to keep it, or go back to keep the one you had.
- **Your own colours and sizes:** MENU › **Skin Editor**.

<!-- GIF: howto-statusbar-clean.gif | region: 0,0,768,626 | steps: tap CLEAN; 3 s; tap CLEAN | "CLEAN: lines and blobs only" / "Tap again: your skin is back" | round 1, no. 23 -->

<!-- GIF: howto-menu-skin.gif | region: full screen 0,0,768,1024 | steps: double tap Skin; tap 3 skins down the list, 1.5 s each; tap back | "Browse skins: live preview" / "Back keeps the one you had" | round 2 (first reserve) -->

<!-- GIF: howto-menu-skin-editor-value.gif | region: full screen 0,0,768,1024 | steps: double tap Skin Editor; scroll to a sphere value; double tap it; tap + x3; tap Enter | "Double tap a value" / "− and + step it live" | round 2 -->

<!-- GIF: howto-menu-skin-editor-colour.gif | region: menu 0,36,768,590 | steps: in Skin Editor double tap a colour row; drag across the picking surface; tap done | "A colour opens the picker" / "done closes it" | round 3 -->

### How to type on the device

You rarely have to ask: the [on-screen keyboard](#motion-keyboard) comes up by
itself when there is something to type — a Rename in FILES, the FILES editor,
a value in the menu — and goes away when you're done. **KEYS** in the status
bar shows or hides it by hand.

(motion-howto-network)=

### How to point the device at another Core

MENU › **Network**. Double tap a row, type the new host, port or address, and
press ENTER. The page is saved when you leave it.

```{warning}
**An address only changes on this side.** The other device has to send or
listen on the same one. A typo doesn't fail loudly: A³ Motion just sends to
an address nobody listens to.
```

<!-- IMAGE: a screenshot of MENU › Network with its rows, in quiet-indigo-2 (replaces the dropped howto-menu-network.gif) -->

(motion-panic)=

## Get me out of here

(motion-stop-now)=

### Stop the movement, now

| You want | Do this |
| :--- | :--- |
| one channel to stand still, now | select it and tap **■**; on the panel, hold **SHIFT** and press its **Play\|Pause** |
| all four to stand still, now | PADS › **Stop all** (the grey block). Screen only: on the panel, SHIFT + Play\|Pause on each channel |
| a channel back to plain stereo | turn its **3d** pot down. The track stays in the mix, just no longer in the room |
| a chain of actions to end | press Play\|Pause, ■ or another action pad on that channel |
| a take gone wrong to go away | **■** ends it, **DISCARD** twice puts back what was there |

After a stop the sound stays where it was; it doesn't jump home. And
restarting the device doesn't move the room either: it asks A³ Core where
every sound is before it says anything itself.

(motion-not-mid-set)=

### Not in the middle of a set

These are fine in soundcheck and loud in front of a crowd:

- **Loading a set** stops all four clips, jumps each channel's **3d, freq and
  Q** to the set's values, and starts the set's clips together on the next
  downbeat.
- **Turning values on ACTION** rewrites that action for every channel and
  every set that uses it. See the warning in
  [How to fire and assign actions](#motion-howto-action).
- **Developer Mode** (in the menu) lets Save write over the shipped files.
  Leave it off on a gig.
- **Network** settings: a wrong address goes quiet without telling you.

And the ones people worry about that are safe: deleting a file (whatever is
loaded keeps playing), scrolling through the menu (a value only changes in
its edit box), and pressing Escape on a keyboard (it never quits the app).

(motion-before-the-gig)=

### Before the gig

- The clock key reads what the booth has: **PIO** for CDJs on a link, **EXT**
  for the beat analyser, **INT** otherwise — and the BPM matches the deck.
- Developer Mode is off.
- The sets you plan to use are loaded once and saved as your own
  (**Save as**), so a tweak on the night can't touch the shipped ones.
- You know where front is on the sphere for this room.

(motion-troubleshooting)=

### Troubleshooting

| Symptom | What to do |
| :--- | :--- |
| The blob moves, the sound doesn't | Turn **3d** up. At 0 the channel is plain stereo |
| The channel meters don't move and the speakers throw no lightning | Nothing is coming back from A³ Core. Check the network cable and that Core is running |
| ▶ blinks for a moment before it starts | That's the wait for the next downbeat, up to a bar. Press again to call the start off |
| The clips run off the beat, or the BPM is wrong | Check the clock key. INT: tap the tempo. EXT or PIO: check the source; if its beats stop, A³ Motion carries on at the last tempo it had |
| An action pad does nothing | The button is empty: grey on ACTION, dark on PADS. Put an action on it |
| An action plays differently from yesterday | Someone turned its values on ACTION, and that is saved in the script. Open it with **EDIT** to see what it says now |
| You tapped a set or a clip in FILES and nothing changed | A tap only shows it. **Load** puts it on the device |
| **Save** is dark | It's a shipped file. Use **Save as** |
| FILES won't change row and says `-- SAVE OR CANCEL` | The editor has unsaved text. Save it or Cancel it |
| Your drawn shape parks in one spot halfway through the take | The rec mode is **Latch**. Draw in **Touch** |
| A Cue says `-- NO SUCH CLIP` | Its clip was deleted or renamed |
| A Cue says `-- SAVE THE TAKE FIRST` | Tap SAVE or DISCARD on the take |
| **CLEAN** is greyed out | The device has no clean skin installed |
| A double tap on **3D** does nothing | The panel is attached, and its pot decides. Turn the pot |
| The mixer's hardware control and the screen disagree | The A³ Mixer has no motor faders. Touch the hardware control and it takes over |
| You changed an OSC address and nothing reacts | The other side must use the same one. Put it back, or change both |
| The screen is frozen | Restart the device. The room doesn't move: it asks Core where every sound is |

<!-- QUESTION (maintainer): "restart the device" in the last row: what is the DJ-safe way on the rig, pulling the network cable (PoE)? And how long until it is back? -->

(motion-reference-screen)=

## Reference: the screen

### Windows at a glance

Every window opens from a key with its name on it. Here's where each key lives.

| Window | What it's for | Opens with | Closes with |
| :--- | :--- | :--- | :--- |
| **Main screen** | the room, the four channels, the selected clip | always there | — |
| **CLIP** | which clip, which shape, direction, end, lengths | its tab in the bar | another tab |
| **MOTION** | how the shape moves, and how high it sits | its tab in the bar | another tab |
| **ACTION** | the selected channel's six action buttons | its tab in the bar | another tab |
| **CHMIX** | the selected channel's mixer strip | its tab in the bar | another tab |
| **REC** | setting up and making a take | its tab in the bar, or ● | another tab |
| **FILES** | sets, clips, shapes and actions on disk | FILES, top of the global strip | FILES again; MIXER or PADS (swaps it); any tab; MENU; PAGE on the panel |
| **MIXER** | all four mixer strips and the master | MIXER, top of the global strip | the same as FILES |
| **PADS** | the panel's pads on the screen | PADS, top of the global strip | the same as FILES |
| **Menu** and its pages | skins, network, LEDs, folders | MENU, right end of the status bar, or MENU on the panel | ‹ (back) or MENU: one level; ✕: all of it |
| a list of values, an edit box, the colour picker | changing one menu value | double tap or ENTER on a menu row | ENTER, a tap on a value, or **done** (keeps it); back, MENU or Escape (drops it) |
| **Keyboard** | typing names and values | KEYS, status bar; comes up by itself when there is something to type | KEYS again, or HIDE |

Only one of FILES, MIXER and PADS is open at a time; each opens on top of the
sphere, and the channel row, the bar and the global strip stay in view under
it. Closing FILES ends a rename without keeping it and cancels an armed
Delete; text typed in the editor stays, marked unsaved.

<!-- GIF: howto-overlays.gif | region: 0,36,768,690 | steps: FILES; MIXER; PADS; tap CLIP tab | "FILES, MIXER, PADS: over the sphere" / "One at a time; a tab closes it" | round 1, no. 20; replaces howto-files-open-close.gif, howto-mixer-open-close.gif and howto-pads-open-close.gif -->

### The main screen

![The main screen: status bar, sphere, channel row, bar and global strip](pics_user/a3-motion-ui-display-one-clip.png)

Top to bottom:

1. the **status bar**: clock, tempo, what was last done, the beat, CLEAN,
   KEYS, MENU;
2. the **sphere**: the room seen from above;
3. the **channel row**: one field per channel;
4. the **bar**: five tabs and the page they open, on the left three quarters;
5. the **global strip**: FILES, MIXER, PADS, the elevation picture and the
   transport, on the right quarter.

#### Status bar

| Part | What it does |
| :--- | :--- |
| **clock key** (INT / EXT / PIO) | tap to step INT → EXT → PIO. Written in the mode's colour. See [Clock modes](#motion-clock) |
| **BPM** | the tempo, in the clock's colour. Read only |
| **readout** | what was last done, e.g. `-- REC ARMED`, `-- FILES ON`, `CH2 ACTION` |
| **beat display** | four cells, one per beat, filling as the bar runs. **Tap it to tap the tempo**: in INT it sets the tempo; in EXT and PIO the taps go on to the beat analyser |
| **CLEAN** | switches to the clean skin — thin lines, plain blobs, effects off — and back to the skin you had. Greyed out when the device has no clean skin |
| **KEYS** | shows or hides the on-screen keyboard |
| **MENU** | opens the menu; see [The menu](#motion-menu) |

#### The sphere

The room seen from straight above, with you — the listener — in the middle at
ear height. The top of the sphere is the front of the room. Each channel is a
coloured blob sitting where its sound is; it swells and throws sparks with
that channel's input level. A playing clip draws its path as a braid of
plasma, with the blob travelling inside it. Whatever is on the far side of the
sphere from your view is drawn darker: from straight above, that is
everything below ear height.

The four corners are your speakers, each a tower of tops over subs. Lightning
runs from the tops towards the middle — thicker, and more of it, on the
speaker working hardest, and none at all when the room is silent. The subs
throw ball lightning with the bass. No lightning anywhere while music plays?
Nothing is coming back from Core; see [Troubleshooting](#motion-troubleshooting).

| Gesture | What it does |
| :--- | :--- |
| drag a blob | moves that channel's sound, live. The blob jumps under the finger. A playing clip keeps running and takes the blob back when you let go |
| several fingers | each takes its own blob |
| during a take | the first finger writes the take, wherever it lands; see [REC](#motion-rec) |

**Camera mode** turns the view instead. Tap the **elevation picture** in the
global strip (the small sphere with the camera mark) to switch it on or off;
its field lights while it is on.

| Gesture, in camera mode | What it does |
| :--- | :--- |
| drag up / down | leans the view from straight above down to the horizon |
| drag left / right | walks the view round the room |
| pinch with two fingers, or the mouse wheel | zooms |
| double tap | back to straight above, unzoomed |

In camera mode no finger takes a blob. The view is kept over a restart.

#### The channel row

Between the sphere and the bar: one field per channel, in its colour, channel
1 on the left. Left to right in each field:

| Part | What it does |
| :--- | :--- |
| meter | the channel's input level. Read only |
| **3D**, **FREQ**, **Q** | the channel's 3d, filter frequency and filter resonance. Drag to turn |
| progress bar | fills from the left as the clip runs, with the **clip's name** in it |

**Tap a field to select that channel**: the bar and the global strip then
show its clip. Reaching for one of its knobs selects it too. The selected
field is filled and framed thicker.

**On the panel, the pot is the truth.** Without a panel attached, a double
tap puts 3D or FREQ back to twelve o'clock and Q back to closed. With the
panel, the pot's own position decides.

![The channel row: four channels, each with its clip's name](pics_user/a3-motion-ui-channel-row.png)

<!-- GIF: howto-channelrow-select.gif | region: 0,626,768,398 | steps: tap face 2, 1.5 s; face 3, 1.5 s; face 1 | "Tap a channel to work on it" / "The bar follows the channel" | round 1, no. 19 -->

<!-- GIF: howto-channelrow-pots.gif | region: channel row 0,610,768,80 | steps: drag FREQ of ch1 (63,641) up 60 px, down 30 px; drag 3D of ch2 (222,641) up 40 px | "Drag 3D, FREQ or Q" / "The channel is selected too" | round 3; region too thin, mostly for builds without a panel -->

#### The bar

Five tabs, left to right: **CLIP MOTION ACTION CHMIX REC**. A tab shows its
page in the bar; the lit tab is the page you are on. All five show the clip of
the **selected channel**, framed in its colour. A tab also closes FILES, MIXER
or PADS if one of them is open.

**Double tap a knob** in the bar to put it back to its rest: most knobs to the
middle, the moving ones (the sweeps and spin) to off. On a knob that plays a
recorded lane, the double tap clears the lane instead (see
[How to record knob moves](#motion-howto-lanes)). Fields that step on a tap
have no rest.

#### The global strip

The right quarter of the bottom of the screen, beside the bar. It is the same
whichever tab is open.

| Part | What it does |
| :--- | :--- |
| **FILES**, **MIXER**, **PADS** | each opens its window on top of the sphere; tap again to close it. Only one at a time: another key swaps it |
| elevation picture | a small sphere seen from the side, with the channels' positions. Tap it for camera mode |
| **▶ / ❚❚** | the selected clip's Play\|Pause: starts, or stops, on the **next downbeat**, and blinks while it waits. Shows ❚❚ while the clip runs |
| **■** | stops the selected clip **now**, and flashes. During a take it ends the take |
| **A** | fires the selected channel's **chosen action button** — the one last tapped on ACTION — for as long as you hold it |
| **●** | arms a take on the selected clip and opens REC; see [REC](#motion-rec) |

After a take, **●** turns into **SAVE** (a tick) and **A** into **DISCARD** (a
cross) until you decide.

(motion-clip)=

### CLIP

The clip of the selected channel. Eight fields, four by two, laid out like
the encoders.

| Field | What it does |
| :--- | :--- |
| **CLIP** | which clip — the preset of values — is loaded. **Drag it with a thumb** to step through the clips. A warning-coloured **drift dot** says the values have been turned since it was loaded and something is waiting to be saved. `--` is a shape with no clip behind it |
| **SVG** | the shape the sound traces, with its name. **Drag it** to step through the shapes; **swapping the shape keeps the values** |
| **DIRECTION** | tap to step **Fwd → Rev → Bnce → Rnd**: forwards, backwards, there and back, or from a random point each pass |
| **END-ACTION** | tap to step **Loop → Stop → Paus**: what happens when a pass is over |
| **LENGTH** × 4 | how long one pass takes, **in beats**. **Tap** a key to play at that length. **Drag** a key to give it another length out of the whole range, applied straight away. The key keeps it |

**The LENGTH keys scale the clip's own length.** The number on a key is what
it gives this clip: the same key reads 4 on a four-beat shape and 8 on an
eight-beat one, and can read a fraction such as 3/8 on a short one. The lit
key is the one the clip plays at. The four keys belong to the device and are
saved in the set.

**Stop and Paus (pause) are two different ends.** Stop goes back to the
beginning of the shape, whichever way it was running, so the next start is
visibly a start. Paus stays wherever the pass ended. Any direction works with
any end.

(motion-motion)=

### MOTION

What happens to the shape while it plays, and how high it sits. Eight fields,
four by two; each holds **two knobs**: on the left the movement, on the right
the value it moves.

| Field | Left knob (the movement) | Right knob (the value) |
| :--- | :--- | :--- |
| **ROTATION** | `spin`: keeps turning the shape; up for one way, down for the other | `rot`: turns the whole shape around the vertical axis |
| **REACH** | `swell`: sweeps the reach out and back | `reach`: how far down the sphere the shape's outer edge lands |
| **SQUEEZE X** | `strX`: sweeps the squeeze | `sqzX`: squeezes front to back |
| **SQUEEZE Y** | `strY`: sweeps the squeeze | `sqzY`: squeezes left to right |
| **ELEVATION** | `sway`: sweeps the height up and down | `elv`: the height the shape is centred on |
| **ELEVATION CLIP** | `clip-top`: a ceiling | `clip-bot`: a floor |
| **TILT** | `tswp`: sweeps the tilt (tilt sweep) | `tilt`: leans the shape forward or back |
| **ROLL** | `rswp`: sweeps the roll (roll sweep) | `roll`: leans the shape to the side |

Drag a knob to turn it. Everything that moves on its own counts in **bars off
the tempo clock**, never in seconds, so a cycle comes back to where it started
on a bar line. A knob that is being moved shows the movement as a **blue
arc**; its pointer stays where your hand left it.

How the shape sits on the sphere, and why a ceiling makes it travel round
rather than stop, is in [How it thinks](#motion-shape-on-sphere).

(motion-action)=

### ACTION

Each channel has **six action buttons**, A1 to A6, on the panel and on this
page. An action changes the clip for as long as its accent lasts: it throws
the shape wide, lifts it overhead, pulls it under the floor, stops it. When the
accent has fallen, the clip is itself again.

![The ACTION page](pics_user/a3-motion-ui-action.png)

Left to right:

| Part | What it does |
| :--- | :--- |
| **A1–A6** | three rows of two, as the pads sit on the panel. Each shows its number, the name of its action and a badge, **1** (one-shot) or **H** (Hold). **A tap chooses the button**; everything to its right then shows and edits that one. It doesn't fire: the pads fire, on the panel and on PADS, and so does **A** in the global strip |
| the list | the action scripts. A tap puts that script on the chosen button; **no action** at the top clears it |
| **EDIT** | opens the chosen button's script in FILES › ACTIONS |
| **Hold** / **1shot** | the chosen button's mode: hold the clip for as long as the finger is down, or fire and let go. Tap to switch |
| **then** | what fires when this button's accent is over: another button of the channel (`then A3`), or nothing (`then --`). A tap steps it, two taps clear it |
| **AUDIO \| MOTION** | two tabs on top of the card. **AUDIO**: the accent — `atk`, `dec` and `max` for **3d**, for **freq** and for **q**. **MOTION**: what the button puts on the clip — every knob of the MOTION page, and CLIP's speed, direction and end |

A field is in the channel's colour when it carries an action and grey when it
doesn't; the chosen one has the thick outline; and a field turns **white while
its action runs**, the same as its pad. A button with nothing on it does
nothing at all. **Pressing an action pad** — on the panel or on PADS — fires
it and brings up this page with that button chosen; not with SHIFT, and not
while a take is armed or recording.

**The AUDIO tab** sets the accent: `atk` is how long it takes to rise, `dec`
how long to fall, in bars, and `max` how far it goes. The **3d** row raises the
channel's 3d from where you set it towards `max`; the **freq** and **q** rows
do the same for the filter's cutoff and resonance. A `max` of 0 switches that
row off.

<!-- QUESTION (maintainer): do the freq and q accents only ever raise the filter, like the 3d one, or can they lower it? The code says only "0 is off". -->

**The MOTION tab** shows each value as it will land. **Grey**: the action
leaves it to the clip, and the clip's own value is shown as a hint. **In the
channel's colour**: the action sets it. **Two taps** on a MOTION value, or on
**then**, hand it back to the clip (or to nothing after).

```{warning}
**What you set here is saved into the action — for everyone.** The script
file itself changes, a shipped one too. Every button on every channel that
carries the same action plays the change, and so does every set that names
it. To keep the original, make a copy first: **EDIT**, then **Save as** in
FILES.
```

<!-- QUESTION (maintainer): FILES protects shipped files (Save stays dark unless Developer Mode is on, shippedFileMayBeOverwritten), but ACTION writes a turned value into the script in place, shipped or not (decided 2026-09-29, "always in place"). So a DJ with Developer Mode off can change a factory action by turning a knob, but can't save the same change typed in FILES. The page describes both as they are. Which one should give way? -->

How an accent rises and falls, what "the clip as it is now" means, chains and
two actions at once: see [How actions play](#motion-actions-play). How the
script is written: see [Scripting actions](#motion-scripting).

**On the panel** the four upper encoders sit under the page's columns:

| Encoder | Turn | Press |
| :--- | :--- | :--- |
| 1 | chooses A1–A6 | – |
| 2 | walks a highlight through the list; the button doesn't change yet | puts the highlighted script on the chosen button |
| 3 | moves a ring over EDIT, the mode and **then** | does what a tap on the ringed key does |
| 4 | switches AUDIO ↔ MOTION | the same |
| 5–8 | turn the marked row of the card, left to right (AUDIO: atk, dec, max) | mark the next row |

The ring and the row's outline appear once the encoder has been used. With
SHIFT every encoder is its channel's freq or Q, as on every page.

(motion-chmix)=

### CHMIX

The selected channel's strip of the mixer, in the bar: the same controls as
that channel's strip in [MIXER](#motion-mixer), laid out four by two like the
encoders.

| Control | What it does |
| :--- | :--- |
| **GAIN** | input gain. Double tap: full |
| **HIGH**, **MID**, **LOW** | the three EQ bands. Double tap: flat |
| **SEND** | how much of the channel goes to the FX bus, where the delay that follows the beat sits. Double tap: none |
| **PFL** | the channel on the headphones (cue). Tap to switch |
| **FX** | puts the channel through the shared filter (FX FREQ, FX RES, FX MODE in MIXER). Tap to switch |
| meter, on the right | the channel's level, and its **VOL fader**: the handle is the volume. Drag anywhere on the meter to move it, one to one from where it stood. Double tap: full volume |

(motion-rec)=

### REC

Making a take: a new recording of a shape, on the selected channel's clip.
The steps are in [How to record a take](#motion-howto-take).

| Field | What it does |
| :--- | :--- |
| **CLIP**, **SVG** | as on CLIP |
| **RECMODE** | tap to step **Touch → Latch → Write**; see [Touch, Latch, Write](#motion-rec-modes) |
| **LENGTH** × 4 | as on CLIP. **The lit key is how long the take will be** |
| **GAP-CONNECTOR** | two knobs. `fade`: how long the take's closing move lasts, which smooths the join where the end of the take meets its start. `bias`: where a gap the take never wrote leads. If in doubt, leave both alone |

On the panel, **REC** alone does nothing unless a take is running; then it
ends it.

(motion-files)=

### FILES

The library: what is on disk. Tap **FILES** in the global strip; it opens on
top of the sphere until you tap FILES again, a tab, or MENU. **FILES is for
preparing.** During a set you need **Load** and nothing else.

![FILES, with the set "Peak" shown](pics_user/a3-motion-ui-files-sets.png)

On the left, top to bottom: the four tabs **SETS**, **CLIPS**, **SVG** and
**ACTIONS**, two by two; **from set** / **from clip**; the filter; the list;
then the keys. On the right, the **editor** with the chosen file as text.

| Tab | What the list holds |
| :--- | :--- |
| **SETS** | which clip and which six actions each channel has, plus the channels' 3d, freq and Q and the length keys |
| **CLIPS** | clips: a shape with every value it is played with |
| **SVG** | the shapes, and nothing else |
| **ACTIONS** | the action scripts |

**Tapping a row only shows it** in the editor. Nothing on the device changes.
Drag the list to scroll it. When FILES opens, the list points at what the
selected channel holds; on CLIPS that clip's row carries the drift dot when
its values have been turned.

| Key | What it does |
| :--- | :--- |
| **Load** | puts the chosen row on the device: a set on all four channels, a clip or a shape on the selected channel, an action on the chosen action button |
| filter: **All** / **User** / **System** | tap to narrow the list to your own files or the shipped ones. It says what it shows now |
| **Rename** | opens the row for typing, with the keyboard. **Keep** (the same key) or ENTER settles it; Escape or leaving drops it. A name already taken is refused. Renaming a clip carries the new name into every set that uses it |
| **Delete** | says **Sure?**; the second press deletes. Anything else you do cancels it |
| **from set** / **from clip** | writes what is on the device now into the editor as text, unsaved, for Save as to keep |
| **Cancel** | puts the file's own text back |
| **Save** | writes the editor's text over the file, and every channel using that clip, shape or action picks it up at once. A set is only written; loading it stays Load's job |
| **Save as** | writes a copy into your own files, named after the original ("Lift Up 2") |

**Unsaved text holds the list and the tabs**: a row tap, Rename, Delete or
another tab says `-- SAVE OR CANCEL` and flashes the two keys. A set or a shape
that would not load again cannot be saved; a script with an error can, and the
error shows under the editor. **Shipped files can't be written over**: Save
stays dark on them, and Save as is the way out (see Developer Mode in
[the menu](#motion-menu)). What the editor shows for each kind of file is in
[Under the hood](#motion-under-the-hood).

**Delete only removes the file.** Whatever is loaded keeps playing: a set's
file goes and the set stays loaded; a clip's files go and the sets that named
it are left alone. So you can tidy the library mid-set and the room won't
notice.

(motion-mixer)=

### MIXER

A software mixer for the four channels, with the A³ Mixer's own controls.
Anything you turn here, the desk sees too, and the other way round. Tap
**MIXER** in the global strip; it opens on top of the sphere until you tap
MIXER again, a tab, or MENU.

<!-- Screenshot to be re-shot in quiet-indigo-2: the MIXER overlay. The old
a3-motion-ui-mixer-overlay.png shows a VOL knob, an MST knob and a filter row
that are gone. -->

The knobs show what is really set, not what this device last did: a hand on
the desk moves them here too, and a restart mid-evening brings them back as
they are. That holds for the PFL and FX keys as well. The A³ Mixer has no
motor faders: turn a knob here and the hardware one stays put, and the next
touch on it takes over from wherever it sits.

**Four channel strips**, each with its meter on the left and, down the strip:

| Control | What it does |
| :--- | :--- |
| meter | the channel's level and its **VOL fader**: drag anywhere on it, one to one. Double tap: full volume |
| **GAIN** | input gain. Double tap: full |
| **HIGH**, **MID**, **LOW** | the EQ. Double tap: flat |
| **SEND** | to the FX bus. **SEND comes up shut, and a double tap takes it back there** |
| **PFL**, **FX** | cue, and the channel through the shared filter. Tap to switch |

**The master column**, on the right:

| Control | What it does |
| :--- | :--- |
| the column | the **master fader**: drag it, one to one. No double tap: full on the master is the one gesture that makes the whole room loud at once |
| output meters, at its foot | the subwoofer and the four speakers. Read only |
| **BTH** | booth level |
| **MIX** | headphone blend between cue and master. Double tap: the middle |
| **PHN** | headphone level |
| **RET** | the FX bus's return level. Double tap: none |
| **FX FREQ**, **FX RES** | the one filter shared by all four channels. Double tap: FREQ to the middle, RES to none |
| **FX MODE** | tap to switch the filter between **HPF** and **LPF** |

3D, FREQ and Q are not in the mixer: they are in the channel row.

(motion-pads)=

### PADS

Eight pads per channel, in two columns of four — the same on the panel and on
the PADS window, which puts the panel on the screen for a build without one.
Tap **PADS** in the global strip; it opens on top of the sphere until you tap
PADS again, a tab, or MENU.

| | left | right |
| :--- | :--- | :--- |
| row 1 | **Play\|Pause** | **PAGE** |
| row 2 | **A1** | **A2** |
| row 3 | **A3** | **A4** |
| row 4 | **A5** | **A6** |

The window is laid out **as the panel is**: square pads on a grid of six rows,
the channels' pads in the bottom four. The top two rows stay empty, where the
panel has its pots.

**The function keys are on it too**, as on the panel:

- **right**, top to bottom: **TAP**, **clock**, **REC**, **recmode**, **MENU**,
  **SHIFT**;
- **left**, above the grey block: **TAP** and **clock**.

A key on the screen is the panel's key: down while the finger is on it, up
when it lets go. **SHIFT or REC held on the screen** changes what a pad does,
exactly as on the panel, and a key counts as down while either the panel or the
screen holds it. A key's face lights while it is active: SHIFT held, a take
running, the menu open, TAP pressed or on the beat.

![The PADS window](pics_user/a3-motion-ui-pads.png)

- **Play\|Pause** starts or stops the clip on the **next downbeat**.
  **SHIFT + Play\|Pause** does it now, which is also how you stop a running
  clip at once from the panel: there is no Stop pad.
- **PAGE** on another channel selects that channel. On the selected channel it
  steps through CLIP → MOTION → ACTION → CHMIX → REC; with SHIFT, backwards.
  It also closes FILES, MIXER or PADS.
- **A1–A6** fire that channel's action buttons, now.
- Pressing Play\|Pause or an action selects that channel in the bar, so what
  you read is what you just touched.
- The grey **block at the left** fires one pad on **all four channels**: Play
  all (starts only the clips that are standing still), **Stop all** in PAGE's
  place, and each action on every channel that has one. Screen only; the panel
  has no grey block.

What the pads show:

- Play\|Pause shows ▶ or ❚❚ and follows the clip: lit while it plays, blinking
  while it waits for the downbeat.
- An action pad is dim when it carries an action and dark when it doesn't, and
  **white while its action runs**.
- PAGE is lit on the selected channel.

**When it happens:**

| You press | It happens |
| :--- | :--- |
| Play\|Pause | on the **next downbeat**, starting and stopping alike |
| SHIFT + Play\|Pause | **now** |
| ■ on the screen | **now** |
| an action pad | **now** |
| SHIFT + an action pad | now, as a preview only the screen sees, for as long as it is held |
| a Cue | its clip is loaded now and starts on the **next downbeat** |
| SHIFT + a Cue | loaded and started **now** |
| Load a set | all four stop now and start together on the **next downbeat** |
| a drag on the sphere | **now**, all the way |

<!-- GIF: howto-pads-page.gif | region: full screen 0,0,768,1024 | steps: tap ch3 PAGE (572,110); tap ch3 PAGE again | "PAGE on a channel selects it" / "PAGE again closes PADS" | round 2 -->

(motion-menu)=

### The menu

Opened with **MENU** at the right end of the status bar, or MENU on the panel.
It opens on top of the sphere. **Nothing in the menu is needed to play.**

| Page | What it holds |
| :--- | :--- |
| **Skin** | which skin is loaded, as a list; the skin previews as you browse it |
| **Skin Editor** | every value the loaded skin holds, grouped by what it is |
| **Network** | the OSC hosts, ports and addresses |
| **Button LEDs** | the colours of the panel's keys |
| **Pattern Folder** | where clips, shapes, actions and sets are read from |
| **Sphere in Menu** | **on**: the sphere keeps drawing behind the menu; **off**: it rests while the menu is open |
| **Developer Mode** | **on** lets Save write over shipped files |

```{warning}
**Developer Mode: leave it off on a gig.** With it on, Save in FILES writes
over the shipped sets, clips, shapes and actions.
```

**In the menu, a value only changes in its edit box**, never by brushing past
it:

| Gesture | What it does |
| :--- | :--- |
| drag the list, or the empty strips left and right of it | scrolls, the way a phone does |
| tap a row | selects it |
| double tap a row, or ENTER | opens it: a page, a list of its values, an edit box, or the colour picker |
| in a list of values | tap or ENTER chooses; Escape or back leaves without choosing |
| in an edit box | type with the keyboard; ENTER keeps; Escape, back or ✕ undo. A skin number also has **− / +** keys that step it while you watch |

Two fingers scroll as one.

**Getting out:** the **‹** (back) and **✕** (close) keys in the top right, and
MENU itself. Back and MENU close **one level**; ✕ closes all of it at once,
however deep. **Escape never quits the app.** In a booth, one elbow on a
keyboard shouldn't end your set.

<!-- GIF: howto-menu-navigate.gif | region: full screen 0,0,768,1024 | steps: tap MENU (742,17); drag left strip up 100 px; tap a row; double tap Skin Editor; tap back; tap ✕ | "Drag to scroll, double tap opens" / "Back: one level, ✕: all of it" | round 2; replaces howto-menu-open-close.gif and howto-menu-scroll-select.gif -->

#### Skin

Double tap **Skin**: the rows give way to the list of skins. Browsing
previews each one on the sphere; a tap or ENTER chooses, back puts the running
one back.

#### Skin Editor

Every value of the loaded skin, under headings: surfaces, text, states,
channels, sphere, type, touch, then the effects. At the top, five action rows:
**» Save**, **» Save as new**, **» Rename**, **» Delete** (asks "sure?") and
**» Reset** (every value back to the shipped default, keeping the name). They
fire only on a double tap or ENTER.

- A number opens the edit box with − / + to step it live.
- A colour opens the **colour picker**: drag on the picking surface (hue,
  saturation, lightness); the change is live; **done** closes it.
- **Leaving the editor saves the skin.**

#### Network, Button LEDs, Pattern Folder

Each shows only its own part of the device's settings, as rows: Network the
OSC sender, receiver and addresses; Button LEDs the key colours; Pattern Folder
the folder the library is read from. Double tap a row to type a new value, or
to pick a colour. The page is saved when you leave it. For Network, see
[How to point the device at another Core](#motion-howto-network) and its
warning.

#### Sphere in Menu, Developer Mode

Double tap the row, tap **on** or **off**.

(motion-keyboard)=

### The on-screen keyboard

The device has its own keyboard. It takes the **bar's place** — where CLIP,
MOTION, ACTION, CHMIX and REC are — so the sphere, the channel row, the tabs
and the global strip stay in view, and every field you type into sits on top
of the sphere, never under the keys.

- **KEYS** in the status bar shows or hides it; its icon follows.
- It comes up by itself when there is something to type — a Rename in FILES
  (every tab, sets too), a touch in the FILES editor, a name or a value in the
  Skin Editor and the menu — and goes again when that is done.
- **HIDE** puts it away and leaves the field open.

**QWERTZ**, with ä ö ü and ß where a German hand looks for them. Four rows of
twelve, sitting on the bar's eight fields — each field holds two rows of three
keys, so every key sits above exactly one encoder:

| Row | Letters | Symbols (**123**) |
| :--- | :--- | :--- |
| 1 | q w e · r t z · u i o · p ü **DEL** | 1 2 3 · 4 5 6 · 7 8 9 · 0 . **DEL** |
| 2 | a s d · f g h · j k l · ö ä **ENTER** | - / " · : ; = · ~ \ ' · , + **ENTER** |
| 3 | **SHIFT** y x · c v b · n m ß · . - _ | ( ) { · } [ ] · < > * · _ \| ! |
| 4 | **123** ◀ ▶ · **SPACE** · **ESC** **HIDE** | the same, with **ABC** for 123 |

The symbols page holds what scripts, clips and sets are written with.

- **SHIFT** once: the next letter is a capital. Twice: caps lock. A third
  time: off. The panel's SHIFT held while you tap a key also gives a capital.
- **DEL** and the arrows act at once and repeat while held. Every other key
  types when you **let go**: slide off a wrong key and nothing is typed.
- **ENTER** keeps what you typed and closes, in a name; in the FILES editor it
  is a new line, and **ESC** or **HIDE** put the keyboard away. **ESC** in a
  name, and Back or Close in the Skin Editor, undo it.

**From the panel:** an encoder walks the six keys of the field above it — the
upper encoder row the keyboard's rows 1–2, the lower row its rows 3–4; the
first detent only shows the ring. A **press** types the ringed key. SHIFT +
encoder stays freq and Q. Pads, pots, TAP, clock, REC, recmode and MENU do what
they always do.

(motion-reference-panel)=

## Reference: the panel

The hardware beside the screen. Each channel has a column: two encoders, a
pot and eight pads.

| Control | What it does |
| :--- | :--- |
| Encoders, two per channel | turn the field just above them on the screen; see below |
| SHIFT + encoder | upper: that channel's **freq**, lower: that channel's **Q**, whatever page is open |
| Pot, one per channel | **3d**: how much of the channel is in the room. Fully down, it's plain stereo, like any mixer. Turn it up, and the channel follows its blob |
| Pads, eight per channel | Play\|Pause and PAGE, then the six action buttons A1–A6 (see [PADS](#motion-pads)) |
| Function keys, six | TAP, clock, REC, recmode, MENU, SHIFT |
| Touchscreen | everything else |

**The eight encoders sit four by two, and so do the fields of CLIP, MOTION,
REC and CHMIX.** Without SHIFT an encoder turns the field above it:

| Page | Upper row of encoders | Lower row of encoders | A press on an encoder |
| :--- | :--- | :--- | :--- |
| CLIP | clip, direction, two lengths | shape, end, two lengths | on a length: plays at that length |
| MOTION | spin, swell, strX, strY | sway, clip-top, tswp, rswp | swaps to the other knob of the field: rot, reach, sqzX, sqzY / elv, clip-bot, tilt, roll |
| REC | clip, rec mode, two lengths | shape, fade, two lengths | on fade: swaps to bias |
| CHMIX | GAIN, HIGH, MID, LOW | SEND, PFL, FX, VOL | on PFL or FX: switches it |
| ACTION | A1–A6, the list, the key ring, AUDIO/MOTION | the four values of the card's marked row | list: assigns; key ring: presses; lower row: marks the next row; see [ACTION](#motion-action) |

Where an encoder has two knobs to choose from, the bar marks the one it is on.
The choice is remembered.

The six function keys sit as a **vertical column at each end of the panel**,
mirrored so either hand reaches them; a key is down while either side is down.
**clock** and **recmode** step their value on a press, as their screen twins
do. **SHIFT is on the panel and on the PADS window**: the SHIFT gestures on
this page need one of the two.

(motion-how-it-thinks)=

## How it thinks

(motion-clock)=

### Beat clock and clock modes

| Mode | Where the tempo comes from |
| :--- | :--- |
| **INT** | this device. Tap the beat display, or TAP on the panel |
| **EXT** | the beat analyser, listening to the music |
| **PIO** | Pioneer Pro DJ Link: the tempo master on the link |

**Which one?** PIO when you play CDJs on a link; INT and tap for vinyl or a
lone laptop; EXT when the beat analyser is fed the music.

In EXT and PIO, A³ Motion counts on by itself between beats and pulls itself
gently onto each beat that arrives. If the beats stop coming, it carries on at
the last tempo it had: clips keep playing, and slowly drift off the music
until the beats come back.

**The clock lives in one place**: the clock key top left, or **clock** on the
panel. It is not in the menu, and not saved in a set, because every booth is
wired differently. Check it at soundcheck, not at the drop. The rec mode isn't
saved in a set either.

(motion-start-up)=

### When the device comes up

A³ Motion asks A³ Core where each sound already is, and takes the answer
before it says anything itself. So switching the device on, or restarting it
mid-evening, doesn't move the room: the blobs appear where the sound actually
is, and the pots are where they were.

Loading a **set** is the other way round. That is a deliberate act, so the set
wins: it stops what was running, sets each channel's 3d, freq and Q, and
starts what the set says was running again, from the top, on the next
**downbeat**. Four clips starting together is the whole point of a set. Play
all on PADS starts all four.

(motion-shape-on-sphere)=

### How a shape sits on the sphere

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

### Touch, Latch, Write

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

### How actions play

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

### Why the screen is not optional

The screen *is* the instrument. Menus, lists and the bar are driven by touch;
without the screen, the panel can't drive the device. Treat it like your CDJ
screens, and keep the drinks on the other side.

## The library

### Sets and moods

The library ships **50 shapes, 50 clips, 50 actions and 10 sets**, laid out along
**the arc of a night**: from the first half-empty hour, through the build and the
peak, to the last record. Every name starts with a **prefix** that says where it
belongs, so things that belong together sit together in every list in FILES:

| Kind | Prefix | Example |
| :--- | :--- | :--- |
| Sets | the phase of the night — the set *is* the prefix | `Peak` |
| Clips | the phase they are made for | `Peak Anthem` |
| Actions | what they do: **Move**, **Lift**, **Width**, **Speed**, **Dub**, **FX**, **Cue** | `Lift Up`, `FX Riser`, `Cue Peak Anthem` |
| Shapes | the family of the shape | `Flower Rose 5` |

The ten phases, in the order a night usually runs:

`Warmup · Groove · Build · Peak · Drop · Break · Dub · Deep · Float · Closing`

**Only FX changes the sound.** Every other action moves the sound through the
room and leaves the channel's 3d, filter and resonance alone. So a button you
have never pressed before can be pressed in front of a full floor: at worst the
sound ends up somewhere unexpected in the room, while the mix stays as you left it.

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

#### The ten sets

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

<!-- QUESTION (maintainer): the layout rule below says A3 is a strong "more", but Break and Float carry Width Breathe on A3, whose own Mood: line says "less" (library agent, 37b2001). The table shows what ships. Swap the actions, or change the rule? -->

The clip names in the table leave out the phase: channel 1 of *Peak* plays
`Peak Anthem`. All four channels of a set carry the same six actions.

**The six buttons sit the same way in every set**, so the hands learn one
panel rather than ten:

| | left | right |
| :--- | :--- | :--- |
| **top row** (A1 / A2) | a gentle **more** | a gentle **less** |
| **middle row** (A3 / A4) | a strong **more** | a strong **less** |
| **bottom row** (A5 / A6) | **FX** — the one button that changes the sound | **Cue** into the next phase |

*More* moves the room towards energy and openness, *less* towards calm and
weight. Every action script says which it is on its `Mood:` line.

<!-- GIF: howto-library-load-set.gif | region: full screen 0,0,768,1024 | steps: tap FILES (612,700); tap SETS (34,59); tap row "Warmup"; tap Load (106,560); wait for the downbeat, 3 s; tap FILES (612,700) | "SETS: one set per phase" / "Load: four clips, six buttons" / "It starts on the downbeat" -->

#### Across a night

The A6 Cues chain the sets into the arc of a night:

- **The main line:** Warmup → Groove → Build → Peak → Drop → Break, and Break
  cues **Build** again, because after a breakdown comes the next build and the
  next drop. Round that loop as often as the floor asks for it.
- **The side road:** Dub → Deep → Float → Closing, and Closing cues **Warmup**
  for the next night (or the next DJ).
- **Getting onto the side road** is up to you: load the Dub or the Deep set in
  FILES, or put one of the two spare Cues on a button — **Cue Dub Echo**, the dub
  escape, or **Cue Closing Still**, the emergency calm for when the fire alarm
  goes off.

**A Cue works on its own channel.** A6 on channel 2 puts the next phase's clip on
channel 2 and nowhere else, so you can walk the room into the next phase one
channel at a time. The grey block on PADS fires A6 on all four channels at once
— which gives you the same clip four times over. That is a choice, and a loud
one; for all four clips of the next phase, **Load the next set** in FILES.

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

#### Shapes (50)

<!-- QUESTION (maintainer): the contact sheet a3-motion-shapes-50.png is stale (it shows the library before v2), so it is not shown. Regenerate it, or drop the image? -->

<!-- IMAGE: pics_user/a3-motion-shapes-50.png still shows the library before v2 (Random, Lissajous 3-5, Hypo 8-3 ...). Regenerate it from pattern/system/*.svg, then put it back here: ![All fifty shapes; the rhythm figures are points, numbered in the order they are jumped to](pics_user/a3-motion-shapes-50.png) -->

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

#### Clips (50), by phase

A clip is a shape plus everything it is played with: speed, height, width,
spin, the accent. Five per phase, named `<Phase> <Name>`; the first four are
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

<!-- QUESTION (maintainer): the Character column comes from the library plan; the clip JSON files carry no mood text of their own. Should they, like the actions' Mood: line? -->

Plus **Default**: no shape. It is what a channel with no clip falls back on,
not something to play.

Some shapes turn up in several phases — Orbit Circle is a calm *Halo* in the
warm-up, a heavy *Sub* in Deep and a *Still* at closing time. The shape is the
path; the clip decides whether it floats overhead or rumbles under the floor.

#### Actions (50)

An action changes the clip for as long as its accent lasts, then the clip comes
back to itself (see ACTION). The prefix says what it changes:

- **Move, Lift, Width, Speed, Dub** only move the sound: turns, height, spread,
  tempo of the shape, dub tricks in space. 3d, filter and resonance stay where
  you set them.
- **FX** are the only actions that change the sound — 3d and the filter.
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

**Lift** — height:

| Action | What it does | Mood | Mode |
| :--- | :--- | :--- | :--- |
| Lift Up | the shape rises a third of the way to the ceiling | more — lifts gently; bright (Q4 → Q1) | Hold |
| Lift Overhead | the shape snaps to the cap above the listener | more — up and bright (Q1) | 1shot |
| Lift Ear Level | a band at ear height: any clip becomes a ring | less — grounded, steady (Q4) | Hold |
| Lift Down | the shape sinks below ear height | less — weight; darker (Q3) | Hold |
| Lift Floor | the sound goes under the floor | less — heavy, dark (Q3) | Hold |
| Lift Sway | the height sways on the bar | more — a slow swell of height (Q4 → Q1) | Hold |

**Width** — spread:

| Action | What it does | Mood | Mode |
| :--- | :--- | :--- | :--- |
| Width Open | the shape spreads half again as wide | more — opens the room (Q1) | Hold |
| Width Full | the shape thrown to the whole sphere | more — everything, everywhere (Q1/Q2) | 1shot |
| Width Close | the shape halves its spread | less — focused, intimate (Q3/Q4) | Hold |
| Width Point | everything pulls in to one point | less — the sound comes close; tension (Q2) | Hold |
| Width Breathe | the spread opens and closes slowly | less — a calm breath (Q4) | Hold |
| Width Squash | pressed flat, springs back when you let go | less — pressure (Q2/Q3) | Hold |

**Speed** — the tempo of the shape:

| Action | What it does | Mood | Mode |
| :--- | :--- | :--- | :--- |
| Speed Double | the shape plays twice as fast | more — energy up, same shape (Q1/Q2) | Hold |
| Speed Half | the shape plays half as fast | less — energy down, same shape (Q4/Q3) | Hold |
| Speed Stutter | the shape chatters at a sixteenth | more — nervous; a stutter edit in space (Q2) | Hold |
| Speed Tape Stop | the shape winds down and stands still | less — the motor stops; the end of a phrase (Q3) | 1shot |
| Speed Halt | everything that moves on its own stops, and the pass ends | less — the reset | 1shot |

**Dub** — the dub desk's moves, played in space instead of on the sound:

| Action | What it does | Mood | Mode |
| :--- | :--- | :--- | :--- |
| Dub Echo Throw | the dub throw: reversed, bouncing, gliding out | less — a repeat that trails away (Q3) | 1shot |
| Dub Bounce Back | a hard swing out and back | more — a throw that returns (Q2) | 1shot |
| Dub Reverse Tape | backwards and slower, like a tape turned over | less — the reverse tape trick (Q3) | Hold |
| Dub Spring | a spring-reverb shake: a fast swell, short | more — a splash (Q2) | 1shot |
| Dub Scatter | somewhere else every time it is put on a button | more — a surprise; playful | 1shot |
| Dub Stitch | the gaps in a take glide shut | less — smooth, calm (Q4) | Hold |

**FX** — the only ones that change the sound:

| Action | What it does | Mood | Mode |
| :--- | :--- | :--- | :--- |
| FX Punch | depth hits, nothing moves | more — weight on the one; driving (Q2) | 1shot |
| FX Sweep | the filter opens over two bars, nothing moves | more — the dub woosh; tension that lifts | Hold |
| FX Resonate | the resonance creeps up | more — slow tension (Q3 → Q2) | Hold |
| FX Riser | four bars of build: spread, spin, filter | more — the build before the drop (Q2 → Q1) | Hold |
| FX Impact | the drop: everything at once, then a long fall | more — the release; impact (Q2 → Q1) | 1shot |
| FX Swell | depth and filter rise together, gently | more — a warm lift (Q4 → Q1) | Hold |

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

**README** in the ACTIONS list is not an action but the scripting manual.
Firing it changes nothing.

<!-- GIF: howto-library-assign-cue.gif | region: bar 0,672,578,352 | steps: ACTION tab (287,700); tap A6 (124,950); scroll list to "Cue Dub Echo"; tap it | "Put a Cue on a button" / "Cue Dub Echo: the dub escape" -->

### The research behind it

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
- **Network** in the menu holds the hosts, ports and addresses. See
  [How to point the device at another Core](#motion-howto-network).

### The squeeze, in numbers

The squeezes `sqzX` and `sqzY` are bipolar, with their middle at zero, and
multiply their axis by 2^value: half at one end, double at the other. X is
front to back, Y is left to right. **The squeeze happens before the turn**, so
the ellipse belongs to the shape and travels with it.

### The panel's electronics

An ESP32-S3 (`esp32-s3-devkitc-1-n16r8`) reads the panel's buttons, encoders,
pots and LEDs, and talks to the Raspberry Pi over a binary poll-frame protocol
on USB serial.

## Specs

Current revision, V03:

- PoE, 31.5 W max
- Raspberry Pi 5 running the touchscreen UI
- ESP32-S3 for the panel's buttons, encoders, pots and LEDs
- 7" capacitive multi-touch display
- A³ Motion Buttonmatrix PCB V03, A³ Motion Mainboard PCB V03

Earlier revisions are listed under
[Configuration](https://a3-audio.github.io/a3-doc/configuration/moc.html).
