(motion-howto)=

# How to …

(motion-howto-load)=

## Load a set or a clip

1. Tap **FILES** in the global strip. It opens on top of the sphere.
2. Tap **SETS** for a set, **CLIPS** for a clip. To load a clip, select its
   channel first.
3. Tap a row. **A tap only shows it** in the editor on the right; nothing on
   the device changes yet.
4. Tap **Load**. A set goes onto all four channels, a clip onto the selected
   channel. The shipped sets load standing still: start them with Play\|Pause
   or PADS › **Play all**. A set you saved while clips were playing starts
   those clips again, together, on the next downbeat.
5. Tap **FILES** again (or any tab) to close it.

```{warning}
**Loading a set mid-set** stops all four clips and jumps every channel's 3d,
freq and Q to the set's values. The room hears it.
```

<!-- GIF: howto-files-load-set.gif | region: 0,36,768,664 | recorded 2026-09-29, 9.5 s | steps: In FILES › SETS tap Warmup, tap Load, close FILES: all four channels carry the set, stopped. | "FILES › SETS" / "Tap a set: it only shows" / "Load: all four channels take it" / "Stopped, ready for your ▶" | a shipped set loads stopped, so it ends on "ready for your ▶"; replaced howto-load-a-set.gif -->

![In FILES › SETS tap Warmup, tap Load, close FILES: all four channels carry the set, stopped.](pics_user/howto-files-load-set.gif)

<!-- GIF: howto-files-load-clip.gif | region: 0,0,768,1024 | recorded 2026-10-01, quiet-indigo-2, --fuzz 0 (quantized before optimizing) | steps: Tap channel 2, open FILES › CLIPS, tap a clip, tap Load: channel 2 gets the clip. | "Choose the channel first" / "FILES › CLIPS" / "Tap a clip: it only shows" / "Load puts it on channel 2" -->

![Tap channel 2, open FILES › CLIPS, tap a clip, tap Load: channel 2 gets the clip.](pics_user/howto-files-load-clip.gif)

(motion-howto-play)=

## Play and stop a clip

- **Start:** press the channel's **Play\|Pause** pad, or select the channel
  and tap **▶** in the global strip. It starts on the **next downbeat** and
  blinks while it waits.
- **Stop on the beat:** press **Play\|Pause** again, or tap **❚❚** (the same
  key on the screen). The clip stops on the next downbeat.
- **Stop now:** tap **■** on the screen, or hold **SHIFT** and press
  **Play\|Pause** on the panel.
- **Call off a start that is still waiting:** press Play\|Pause again while
  it blinks.
- **Start all four:** open **PADS** and tap **Play all** in the scene column
  on the left: it starts every clip that is standing still. To stop all four,
  stop each channel (■, or SHIFT + Play\|Pause); there is no Stop all.

Every start begins at the top of the shape. A stop leaves the sound where it
is; it doesn't jump anywhere.

<!-- QUESTION (maintainer): the key is called Play|Pause and shows ❚❚, but in the code a "pause" is a stop: every start begins at position 0 (MotionEngine::startPlaying), so ❚❚, SHIFT + Play|Pause and ■ all end in the same state and differ only in timing. The page describes it that way. Is that the intent (and the label stays), or should ❚❚ resume where it stopped? -->

<!-- GIF: howto-transport-play-pause.gif | region: 0,626,768,398 | recorded 2026-09-29, 9.8 s | steps: Tap ▶: it blinks until the downbeat, then plays. Tap ❚❚: it pauses on the next downbeat. | "Clip stopped" / "▶ blinks: waiting for the downbeat" / "On the one: it plays" / "❚❚ waits for the downbeat too" / "Paused, right on the one" | replaced howto-play-pause.gif -->

![Tap ▶: it blinks until the downbeat, then plays. Tap ❚❚: it pauses on the next downbeat.](pics_user/howto-transport-play-pause.gif)

<!-- GIF: howto-transport-stop.gif | region: 0,626,768,398 | recorded 2026-09-29, 9.0 s | steps: With the clip playing tap ■: it stops at once. Tap ▶: it starts from the top on the downbeat. | "Channel 1 plays" / "■ stops now, no waiting" / "Next ▶ starts from the top" -->

![With the clip playing tap ■: it stops at once. Tap ▶: it starts from the top on the downbeat.](pics_user/howto-transport-stop.gif)

<!-- GIF: howto-pads-scene.gif | region: 0,36,768,590 | steps: PADS; Play all; downbeat; 2 s | "The scene column plays all four" / "Play all: in on the downbeat" | round 1, no. 7; Stop all is gone since 2026-09-30 -->

<!-- GIF: howto-pads-shift-now.gif | region: pads 0,36,768,590 | steps: clip playing; hold SHIFT on PADS; tap the channel's Play|Pause | "SHIFT + Play|Pause: stop now" | blocked: needs two pointers, xdotool has one -->

(motion-howto-drag)=

## Move a sound by hand

1. Put a finger **on** a channel's blob on the sphere and drag. The finger has
   to land on the blob (or right beside it): a drag that starts on empty
   sphere moves nothing. The sound goes where your finger goes. **A drag is
   live and doesn't wait for the beat**: the room hears every centimetre.
2. Let go. A playing clip takes the sound back onto its shape; a stopped one
   leaves it where you let go.

Two fingers take two blobs. The top of the sphere is the front of the room.

**Steer round the other blobs.** A dragged blob pushes every blob it comes
close to out of its way, and their sound moves with them. Drag straight
through a crowd and you carry the others along.

<!-- QUESTION (maintainer): MotionComponent::disoccludeBlobs pushes every blob near a held one aside and writes the new position to the engine (setChannel3DPosition), so the pushed channels move in the room too. In the recording one drag gathered three other blobs and carried them. Is moving the other channels' sound intended, or should the push be screen-only? -->

<!-- QUESTION (maintainer): which way is "front" in a venue? The osc reference says 0° azimuth is the front of the room; the page now says the top of the sphere is the front. A DJ needs to know where that is before dragging: the booth side, the stage, or wherever Core was set up? -->

To look at the room from another angle **without moving anything**, use
camera mode: tap the small sphere in the global strip, drag up on the sphere
to lean the view towards the horizon (down brings it back), drag sideways to
walk round, and double tap to go back to straight above. In camera mode no
finger can move a sound.

<!-- GIF: howto-sphere-drag-blob.gif | region: 0,36,768,620 | recorded 2026-09-29, 9.0 s | steps: With channel 1 playing, drag its blob across the sphere and let go: the clip takes it back. | "Channel 1 plays its clip" / "Drag a blob: the sound follows" / "Let go: the clip takes it back" | the drag path goes round the other blobs, which a dragged blob pushes aside -->

![With channel 1 playing, drag its blob across the sphere and let go: the clip takes it back.](pics_user/howto-sphere-drag-blob.gif)

<!-- GIF: howto-sphere-camera-mode.gif | region: 0,36,768,988 | recorded 2026-09-29, 10.2 s | steps: Tap the small sphere, drag up, drag sideways, double tap, tap the small sphere again: camera on, lean, turn, reset, off. | "Tap the small sphere: camera" / "Drag up: lean to the horizon" / "Drag sideways: walk round" / "Double tap: straight above" / "Small sphere again: camera off" | from straight above only a drag UP leans the view; a drag down does nothing -->

![Tap the small sphere, drag up, drag sideways, double tap, tap the small sphere again: camera on, lean, turn, reset, off.](pics_user/howto-sphere-camera-mode.gif)

<!-- GIF: howto-sphere-zoom.gif | region: 0,36,768,624 | recorded 2026-10-01, quiet-indigo-2, --fuzz 0 (quantized before optimizing), 12.2 s | steps: In camera mode turn the mouse wheel in and out, then double tap: back to normal. | "Camera mode on" / "Mouse wheel (or pinch): zoom in" / "...and out" / "Double tap: back to normal" | mouse wheel (xdotool click 4/5), so no finger ring on the zoom -->

![In camera mode turn the mouse wheel in and out, then double tap: back to normal.](pics_user/howto-sphere-zoom.gif)

(motion-howto-clip)=

## Change the shape, the speed and the direction

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

<!-- GIF: howto-clip-length-tap.gif | region: 0,36,768,988 | recorded 2026-09-29, 9.5 s | steps: With the clip playing at LENGTH 16, tap LENGTH 2, then LENGTH 1: the laps get faster. | "LENGTH 16: a lap every four bars" / "Tap 2: the same lap in two beats" / "Tap 1: fewer beats, faster laps" -->

![With the clip playing at LENGTH 16, tap LENGTH 2, then LENGTH 1: the laps get faster.](pics_user/howto-clip-length-tap.gif)

<!-- GIF: howto-clip-choose-shape.gif | region: 0,36,768,988 | recorded 2026-09-29, 9.0 s | steps: With the clip playing, drag the SVG field up three steps: the shape changes, speed and values stay. | "The SVG field: the shape" / "Drag it: a new shape each step" / "Speed and values stay put" -->

![With the clip playing, drag the SVG field up three steps: the shape changes, speed and values stay.](pics_user/howto-clip-choose-shape.gif)

<!-- GIF: howto-clip-choose-clip.gif | region: 0,36,768,988 | recorded 2026-09-29, 9.0 s | steps: With the clip playing, drag the CLIP field up three steps: each step is a new preset with its own shape and speed. | "The CLIP field: a whole preset" / "Drag it: new shape, new values" / "Each clip brings its own speed" -->

![With the clip playing, drag the CLIP field up three steps: each step is a new preset with its own shape and speed.](pics_user/howto-clip-choose-clip.gif)

<!-- GIF: howto-clip-direction.gif | region: 0,36,768,988 | recorded 2026-09-29, 9.8 s | steps: With the clip playing, tap DIRECTION three times: Rev, Bnce, Rnd. | "DIRECTION: Fwd" / "Tap: Rev runs it backwards" / "Bnce: there and back again" / "Rnd: a random start each pass" -->

![With the clip playing, tap DIRECTION three times: Rev, Bnce, Rnd.](pics_user/howto-clip-direction.gif)

<!-- GIF: howto-clip-length-drag.gif | region: 0,672,578,352 | recorded 2026-09-29, 8.4 s | steps: Drag a LENGTH key up: 4 becomes 8, then 16, and the key keeps it. | "A LENGTH key reads 4" / "Drag it up: 8, then 16" / "The key keeps its new length" -->

![Drag a LENGTH key up: 4 becomes 8, then 16, and the key keeps it.](pics_user/howto-clip-length-drag.gif)

<!-- GIF: howto-clip-stop-vs-paus.gif | region: sphere and bar 0,36,768,988 | steps: short LENGTH; END-ACTION on Stop, let a pass run out; then Paus, let a pass run out | "Stop: back to the start" / "Paus: stays where it ends" | round 2; replaces howto-clip-end-action.gif -->

(motion-howto-motion)=

## Shape the movement

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

<!-- QUESTION (maintainer): in the recording (2026-09-29) clip-top dragged 40-60 px after elv changed nothing visible, and a double tap on elv left the shape at the bottom rather than at ear level (its rest is "the middle of the clip band", ClipKnobs.hh elevationKnobSpec). Is that the intended rest, and what does clip-top need to show its ceiling? Needs a look at the device. -->

<!-- GIF: howto-motion-rotation.gif | region: 0,36,768,988 | recorded 2026-10-01, quiet-indigo-2, --fuzz 0 (quantized before optimizing), 12.6 s | steps: On MOTION drag rot: the shape turns. Drag spin: it keeps turning. Double tap spin: it stops. | "MOTION › ROTATION" / "Drag rot: the shape turns" / "Drag spin: it keeps on turning" / "Double tap spin: off again" | channel 1 alone on Break Heartbeat (the notch shows the turn; spin 0 in the clip); spin is dragged far, since its first steps take 32 and 16 bars a turn -->

![On MOTION drag rot: the shape turns. Drag spin: it keeps turning. Double tap spin: it stops.](pics_user/howto-motion-rotation.gif)

<!-- GIF: howto-motion-elevation.gif | region: 0,36,768,988 | recorded 2026-09-29, 6.1 s | steps: On MOTION drag elv up: the small sphere and the sphere show the shape rising. | "The small sphere shows the height" / "Drag elv: the shape rises" | elv only: clip-top showed nothing visible and is missing (see the QUESTION under How to shape the movement) -->

![On MOTION drag elv up: the small sphere and the sphere show the shape rising.](pics_user/howto-motion-elevation.gif)

<!-- GIF: howto-motion-tilt-roll.gif | region: 0,36,768,988 | recorded 2026-10-01, quiet-indigo-2, --fuzz 0 (quantized before optimizing), 12.7 s | steps: With the camera leant, drag tilt up, drag roll up, double tap both: the shape's plane leans and comes back flat. | "Camera leant, MOTION tab" / "tilt leans the plane forward" / "roll leans it sideways" / "Double tap both: flat again" | channel 1 alone on Break Heartbeat; the double taps go tilt first, then roll -->

![With the camera leant, drag tilt up, drag roll up, double tap both: the shape's plane leans and comes back flat.](pics_user/howto-motion-tilt-roll.gif)

(motion-howto-action)=

## Fire and assign actions

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
**Turning a value on ACTION changes the action everywhere**: every channel and
every set that uses it, shipped sets included. To experiment, copy it first:
**EDIT**, change any character in FILES (a comment will do; **Save as** stays
dark until the text differs), then **Save as**. The copy goes onto the button
you came from.
```

<!-- GIF: howto-action-fire.gif | region: 0,36,768,988 | recorded 2026-09-29, 9.8 s | steps: With channel 1 playing, open ACTION, tap A1, hold A in the global strip: the action moves the clip; let go and the clip comes back. | "Channel 1 plays its clip" / "ACTION: tap A1 to choose it" / "Hold A: Move Spin takes over" / "Let go: the clip is itself again" -->

![With channel 1 playing, open ACTION, tap A1, hold A in the global strip: the action moves the clip; let go and the clip comes back.](pics_user/howto-action-fire.gif)

<!-- GIF: howto-action-assign.gif | region: 0,672,578,352 | recorded 2026-09-29, 9.9 s | steps: Tap A2, tap a script in the list: A2 carries it. Drag the list back to the top and tap "no action": A2 is empty again. | "Six buttons, one list" / "Tap a button to choose it" / "Tap a script: now it's on it" / "Drag the list back to the top" / ""no action" clears the button" | the list glides on after a drag, so pick the row from a still frame; replaced howto-assign-an-action.gif -->

![Tap A2, tap a script in the list: A2 carries it. Drag the list back to the top and tap "no action": A2 is empty again.](pics_user/howto-action-assign.gif)

<!-- GIF: howto-action-audio.gif | region: 0,626,578,398 | recorded 2026-09-29, 9.8 s | steps: Tap A3, drag the 3d max knob up, hold A: the arc on the channel's 3D pot fills in and falls back when you let go. | "AUDIO: the button's accent" / "Choose A3" / "max: how far the 3d accent goes" / "Hold A: the 3D arc fills in" / "Let go: the accent falls" | recorded with A3 (Width Breathe, Hold): with A1 (Lift Overhead, 1shot) no arc showed; the arc is faint on a ~12 px pot -->

![Tap A3, drag the 3d max knob up, hold A: the arc on the channel's 3D pot fills in and falls back when you let go.](pics_user/howto-action-audio.gif)

<!-- GIF: howto-action-writes-script.gif | region: 0,36,768,988 | recorded 2026-09-29, 9.8 s | steps: Tap A1, open the card's MOTION tab, turn spin, tap EDIT: FILES shows the script with ~spin = 4. | "ACTION, the card's MOTION tab" / "Choose A1" / "Turn spin on the card" / "EDIT: the script says ~spin = 4" / "Every set using it hears it too" -->

![Tap A1, open the card's MOTION tab, turn spin, tap EDIT: FILES shows the script with ~spin = 4.](pics_user/howto-action-writes-script.gif)

<!-- GIF: howto-action-then.gif | region: 0,672,578,352 | recorded 2026-09-29, 9.0 s | steps: Tap A1, tap the then key three times: then A1, then A2, then A3. | "then: what fires next" / "Choose A1" / "Tap then: A1, round again" / "Tap again: A2" / "A1, then A3" -->

![Tap A1, tap the then key three times: then A1, then A2, then A3.](pics_user/howto-action-then.gif)

<!-- GIF: howto-action-mode.gif | region: 0,672,768,352 | recorded 2026-09-29, 10.2 s | steps: Tap A3, tap the mode key: 1shot, a short A runs it through. Tap the mode again: Hold, the action ends when A is released. | "Under EDIT: the mode" / "Choose A3" / "Tap: 1shot, the badge says 1" / "A quick A: it runs its course" / "Tap again: Hold, badge H" / "Hold: over when you let go" -->

![Tap A3, tap the mode key: 1shot, a short A runs it through. Tap the mode again: Hold, the action ends when A is released.](pics_user/howto-action-mode.gif)

(motion-howto-take)=

## Record a take, and keep it or throw it away

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
   the channel held before — stopped. Press Play to hear it again.

**A take is live**: the room hears what you draw. To practise without the
room, turn the channel's 3d down first.

Nothing is lost while you decide. The take keeps playing, marked unsaved,
until you tap SAVE or DISCARD, or something replaces it: a new take, a shape
or a set loaded, a restart.

**On the panel:** hold **REC** and press the channel's **Play\|Pause** pad.
That skips arming; the take starts on the next downbeat. Press REC again to
end it.

<!-- GIF: howto-rec-take.gif | region: 0,36,768,988 | recorded 2026-09-29, 10.2 s | steps: With the clip playing tap ●, tap ▶, draw circles on the sphere from the downbeat, tap ●: the last full lap is the take. | "Channel 1 plays" / "● arms the take" / "▶ starts it on the downbeat" / "Draw on the sphere, lap after lap" / "● ends it: the last full lap stays" -->

![With the clip playing tap ●, tap ▶, draw circles on the sphere from the downbeat, tap ●: the last full lap is the take.](pics_user/howto-rec-take.gif)

<!-- GIF: howto-rec-save-discard.gif | region: 0,626,768,398 | recorded 2026-09-29, 9.0 s | steps: After a take tap DISCARD once (it asks), then tap SAVE: the take is kept. | "The take waits: ✕ DISCARD, ✓ SAVE" / "DISCARD asks twice, on purpose" / "Changed your mind? SAVE keeps it" -->

![After a take tap DISCARD once (it asks), then tap SAVE: the take is kept.](pics_user/howto-rec-save-discard.gif)

<!-- GIF: howto-rec-setup.gif | region: 0,672,578,352 | recorded 2026-09-29, 7.0 s | steps: On REC tap LENGTH 4, then LENGTH 2: the lit key is the take's length. | "The lit LENGTH is the take length" / "Tap 4: a take of four beats" / "Tap 2: two beats, quick laps" -->

![On REC tap LENGTH 4, then LENGTH 2: the lit key is the take's length.](pics_user/howto-rec-setup.gif)

(motion-howto-lanes)=

## Record knob moves

● opens REC, and the knobs are on MOTION: after ●, tap **MOTION** again,
then ▶. (On REC the same spot is the CLIP field, and a drag there steps
through clips mid-take.)

During a take, turn any knob on MOTION. It is written into a **lane**, drawn
in red while it writes, with the same rec mode as the shape. On playback the
lane turns the knob by itself; your hand on the knob wins while it holds.
Double tap a knob to clear its lane; the other lanes stay.

<!-- GIF: howto-rec-knob-lane.gif | region: 0,36,768,988 | recorded 2026-09-29, 10.2 s | steps: On MOTION tap ●, tap MOTION again, tap ▶, turn rot during the take, tap ●: rot plays back as a lane. Double tap rot: the lane is cleared. | "MOTION, channel 2" / "● arms: REC opens" / "Back to MOTION, then ▶" / "Turn rot while the take runs" / "● ends it: rot plays a lane" / "Double tap rot: lane cleared" | ● switches the bar to REC, so MOTION is tapped again before ▶; the take is left unsaved -->

![On MOTION tap ●, tap MOTION again, tap ▶, turn rot during the take, tap ●: rot plays back as a lane. Double tap rot: the lane is cleared.](pics_user/howto-rec-knob-lane.gif)

(motion-howto-save)=

## Keep a tweak and save your set

- **Keep a clip you changed.** A warning-coloured **drift dot** on the CLIP
  field means its values have been turned since it was loaded. Open FILES ›
  **CLIPS**, tap **from clip**, then **Save as**. Your copy lands in your own
  files, named after the original ("Warmup Halo 2"). The channel keeps playing
  the original, drift dot and all: **Load** the copy to play it.
- **Keep tonight's set.** FILES › **SETS**, tap **from set**, then
  **Save as**. The copy is named after the row the editor showed; with no row
  shown it is called "Action". Give it a name (below).
- **Give it a name.** Tap the row, tap **Rename**, type, and tap **Keep** (or
  ENTER).
- **Clear out the library.** Tap the row, tap **Delete**, and tap it again
  when it asks **Sure?**. Delete removes the file, not the music: whatever is
  loaded keeps playing.

<!-- QUESTION (maintainer): Save as names a copy after the file the editor shows (copyBaseFor(_panelFile)); with no file shown it falls back to "Action" on every tab, so SETS › from set › Save as straight after opening SETS wrote a set called "Action" (recorded 2026-09-29). Should a set copy be named after the loaded set instead? -->

<!-- GIF: howto-files-keep-tweak.gif | region: 0,36,768,988 | recorded 2026-10-01, quiet-indigo-2, --fuzz 0 (quantized before optimizing), 12.2 s | steps: The CLIP field shows the drift dot. Open FILES › CLIPS, tap from clip, tap Save as: the tweak is a new clip. | "The dot: this clip was changed" / "FILES › CLIPS" / "from clip: the device as text" / "Save as: your tweak, a new clip" | the channel keeps the original clip; the copy has to be loaded -->

![The CLIP field shows the drift dot. Open FILES › CLIPS, tap from clip, tap Save as: the tweak is a new clip.](pics_user/howto-files-keep-tweak.gif)

<!-- GIF: howto-files-save-set.gif | region: 0,36,768,620 | recorded 2026-09-29, 9.0 s | steps: In FILES › SETS tap from set, then Save as: the device's set is kept as a new set of your own. | "FILES › SETS" / "from set: the device as text" / "Save as: kept as your own set" | no row shown before from set, so the copy was named "Action" -->

![In FILES › SETS tap from set, then Save as: the device's set is kept as a new set of your own.](pics_user/howto-files-save-set.gif)

<!-- GIF: howto-keyboard-rename.gif | region: 0,0,768,1024 | recorded 2026-09-30, quiet-indigo-2, the panel keyboard | steps: In FILES tap your own file, tap Rename: the keyboard comes up; DEL back to "Speed ", type Riff, ENTER. | "Rename: the keyboard comes up" / "DEL takes the old name back" / "Type the new one" / "ENTER keeps the name" -->

![In FILES tap your own file, tap Rename: the keyboard comes up; DEL back to "Speed ", type Riff, ENTER.](pics_user/howto-keyboard-rename.gif)

<!-- GIF: howto-files-delete.gif | region: 0,36,768,620 | recorded 2026-09-29, 8.4 s | steps: In FILES › CLIPS tap one of your own clips, tap Delete (it asks Sure?), tap Delete again: the row is gone. | "Your own clips can go" / "Tap the row" / "Delete asks: Sure?" / "Press again: gone" -->

![In FILES › CLIPS tap one of your own clips, tap Delete (it asks Sure?), tap Delete again: the row is gone.](pics_user/howto-files-delete.gif)

<!-- GIF: howto-files-edit-save.gif | region: 0,0,768,1024 | recorded 2026-09-30, quiet-indigo-2, the panel keyboard | steps: In FILES › ACTIONS tap your own copy, type in the editor, tap another row (refused), tap Save. | "FILES › ACTIONS, your own copy" / "Tap in the editor and type" / "Another row? Save or Cancel first" / "Save: written, keyboard gone" -->

![In FILES › ACTIONS tap your own copy, type in the editor, tap another row (refused), tap Save.](pics_user/howto-files-edit-save.gif)

(motion-howto-mix)=

## Mix from the screen

- **One channel:** select it and open the **CHMIX** tab — its gain, EQ,
  send, CUE, FX and volume.
- **All four and the master:** tap **MIXER** in the global strip.
- **Volume:** the meter *is* the VOL fader, and the handle on it is the fader
  cap. Grab the **handle** and drag, one to one. A drag that starts anywhere
  else on the meter does nothing, so a finger landing low on a loud channel
  can't pull it down.
- **Back to a default:** double tap a knob (EQ flat, SEND off, volume full).
  The master fader has no double tap, on purpose.

These are the A³ Mixer's own controls, and the two follow each other. The A³
Mixer has no motor faders, though: turn something on the screen and the
hardware control stays where it is. The next time you touch it, the level
jumps to wherever the hardware control sits.

<!-- GIF: howto-chmix-volume.gif | region: 0,672,578,352 | recorded 2026-09-29, 9.9 s | steps: On CHMIX drag the handle on the meter down and up, then double tap the meter: full volume. | "The meter is the VOL fader" / "Drag the handle, one to one" / "Double tap: full volume" -->

![On CHMIX drag the handle on the meter down and up, then double tap the meter: full volume.](pics_user/howto-chmix-volume.gif)

<!-- GIF: howto-chmix-knobs.gif | region: 0,700,390,320 | recorded 2026-09-29, 9.8 s | steps: On CHMIX drag HIGH up, double tap it: flat. Drag SEND up, double tap it: off. | "CHMIX: drag a knob to turn it" / "HIGH up" / "Double tap: EQ flat" / "SEND up" / "Double tap: SEND off" -->

![On CHMIX drag HIGH up, double tap it: flat. Drag SEND up, double tap it: off.](pics_user/howto-chmix-knobs.gif)

<!-- GIF: howto-mixer-master.gif | region: 0,36,768,624 | recorded 2026-09-29, 9.5 s | steps: In MIXER drag the master handle down and back up, then drag PHN up. | "The master column, far right" / "Drag its handle: master volume" / "PHN beside it: the headphones" -->

![In MIXER drag the master handle down and back up, then drag PHN up.](pics_user/howto-mixer-master.gif)

<!-- GIF: howto-mixer-filter.gif | region: 0,36,768,624 | recorded 2026-09-29, 9.5 s | steps: In MIXER tap FX MODE twice (HPF, LPF), drag FX FREQ up, double tap it: back to the middle. | "One filter for all four" / "FX MODE: HPF or LPF" / "FX FREQ: where it cuts" / "Double tap: FREQ to the middle" -->

![In MIXER tap FX MODE twice (HPF, LPF), drag FX FREQ up, double tap it: back to the middle.](pics_user/howto-mixer-filter.gif)

(motion-howto-tempo)=

## Set the tempo by hand

1. Tap the clock key (top left) until it reads **INT**.
2. Tap the beat display — the four cells beside the readout — in time with
   the music, or press **TAP** on the panel. The first tap after a pause is
   the one; the BPM follows your taps.

In EXT and PIO the tempo comes from outside, and your taps are passed on to
the beat analyser.

**Stepping the clock key all the way round loses your taps.** Back on INT,
the tempo is the one INT had the first time you left it, not the one you
tapped since. Tap it in again.

<!-- QUESTION (maintainer): A3MotionUIComponent::applyClockMode saves _internalBPM only when it is still 0 (the first time INT is left) and taps never update it, so INT → EXT → PIO → INT restores a stale tempo (recorded: 116 BPM tapped, 60 BPM after the round trip). Bug? The page describes it as it is. -->

<!-- GIF: howto-statusbar-tap.gif | region: 0,0,500,36 | recorded 2026-10-01, quiet-indigo-2, --fuzz 0 (quantized before optimizing), --width 500 (the strip at its own size) | steps: Tap the clock key to INT, tap the beat display eight times: the BPM follows. | "The clock key says whose tempo" / "INT: the tempo is yours" / "Tap the beat display in time" / "The BPM follows your taps" -->

![Tap the clock key to INT, tap the beat display eight times: the BPM follows.](pics_user/howto-statusbar-tap.gif)

(motion-howto-look)=

## Change the look

- **Calm the screen down:** tap **CLEAN** in the status bar. Thin lines,
  plain blobs, no effects: easier to read in a dark booth, and lighter on the
  machine. Tap again for your skin. The shipped default skin *is* the clean
  look, so on it CLEAN changes nothing you can see; it matters once you have
  chosen a richer skin.
- **Another skin:** MENU, then double tap **Skin**. Browse with the arrow keys
  ↑ ↓: each skin previews on the sphere, ENTER keeps it, and Escape or back
  keeps the one you had. **A tap on a skin chooses it at once** and keeps it,
  no preview — dragging the list only scrolls it.
- **Your own colours and sizes:** MENU › **Skin Editor**. Opening it on the
  shipped default skin makes a copy called **custom** as you leave, even if you
  changed nothing, and switches to it.

<!-- QUESTION (maintainer): CLEAN on the shipped default: clean.json and default.json are byte-identical since 648628d, so the key lights and nothing else changes (howto-statusbar-clean.gif could not be recorded). Intended, or should one of the two differ? -->

<!-- QUESTION (maintainer): closing the Skin Editor always saves (closeSkinEditor → saveEditedSkin), and on "default" that means writing custom.json and switching to "custom" (skinNameToWriteTo) even when nothing was changed -- recorded 2026-09-29, a look was enough. Should an unchanged editor leave the skin alone? -->

<!-- GIF: howto-statusbar-clean.gif | region: 0,0,768,626 | steps: tap CLEAN; 3 s; tap CLEAN | "CLEAN: lines and blobs only" / "Tap again: your skin is back" | round 1, no. 23 -->

<!-- GIF: howto-menu-skin.gif | region: 0,0,768,1024 | recorded 2026-10-01, quiet-indigo-2, --fuzz 0 (quantized before optimizing), --fps 6 to stay under 3 MB | steps: In MENU double tap Skin, step down three skins with the arrow key (each previews), press Escape: the old skin stays. | "MENU › Skin: double tap" / "Browse: each skin previews" / "Back: the old one stays" | arrow keys (xdotool key Down x3, Escape), so no finger ring on the browse; a tap would choose and save a skin -->

![In MENU double tap Skin, step down three skins with the arrow key (each previews), press Escape: the old skin stays.](pics_user/howto-menu-skin.gif)

<!-- GIF: howto-menu-skin-editor-value.gif | region: 0,0,768,1024 | recorded 2026-10-01, quiet-indigo-2, --fuzz 0 (quantized before optimizing), the panel keyboard | steps: In the Skin Editor (All values and skin actions) double tap netGain, tap + three times, press Escape: the value is back. | "Skin Editor: double tap a value" / "+ steps it: 0.55, 0.605, 0.665" / "Esc: back to 0.500, nothing kept" | the edit box covers the sphere, so only the number shows the step; Escape (the panel keyboard's ESC), not Enter, keeps the sandbox skin as it was -->

![In the Skin Editor double tap netGain, tap + three times, press Escape: the value is back.](pics_user/howto-menu-skin-editor-value.gif)

<!-- GIF: howto-menu-skin-editor-colour.gif | region: 0,36,768,624 | recorded 2026-10-01, quiet-indigo-2, --fuzz 0 (quantized before optimizing), 12.2 s | steps: In the Skin Editor (All values and skin actions) double tap channel 1's colour, drag across the picker and the hue strip, tap done. | "Double tap a colour: the picker" / "Drag: channel 1 recolours live" / "The hue strip for another hue" / "done keeps it" | Escape does not close the picker, only done; recorded on quiet-indigo-2, whose name the editor keeps (the sandbox's copy of the skin) -->

![In the Skin Editor double tap channel 1's colour, drag across the picker and the hue strip, tap done.](pics_user/howto-menu-skin-editor-colour.gif)

## Type on the device

You rarely have to ask: the [on-screen keyboard](#motion-keyboard) comes up by
itself when there is something to type — a Rename in FILES, the FILES editor,
a value in the menu — and goes away when you're done. **KEYS** in the status
bar shows or hides it by hand.

(motion-howto-network)=

## Point the device at another Core

**Not on the device.** A³ Motion takes every host, port and OSC address from
Core's `a3-osc.json`, and there is no Network page in its menu. It is pointed
at another Core by changing that file on the Core, which moves every other
device with it. What happens on the screen when it changes is in
{ref}`Following Core <osc-follow>`; how to change it, in
{ref}`Where addresses and ports live <osc-truth>`.

