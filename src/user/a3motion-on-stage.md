(motion-panic)=

# On stage

(motion-stop-now)=

## Stop the movement, now

| You want | Do this |
| :--- | :--- |
| one channel still | its **Play\|Pause** (pauses on the downbeat, keeps the place), or **SHIFT** + its **Play\|Pause** / **■** (now, back to the top) |
| all four paused | **PLAY all** while something plays: pauses what plays, on the downbeat. There is no Stop all; for a stop now, **SHIFT** + each **Play\|Pause** |
| plain stereo | **3d** pot down: still in the mix, no longer in the room |
| a chain to end | Play\|Pause, ■ or another action pad on that channel |
| a bad take gone | **■**, then **DISCARD** twice: the old clip, stopped |

A stop leaves the sound where it is. A restart doesn't move the room either.

(motion-stage-end-keys)=

## The panel's end keys

The outer columns are the same on both sides ([full table](#motion-end-columns)).
Under the thumbs:

| Key | Does | With **SHIFT** held first |
| :--- | :--- | :--- |
| **TAP** (row 1) | taps the tempo (INT) | **CLOCK** |
| **SHIFT** (row 2) | the modifier | – |
| **PLAY all** (row 3) | pauses what plays, or starts what stands still; double tap: back to the top | **REC** while both are held |
| **A1 / A2** (row 4) | that action on all four channels | **REC MODE** |
| **A3 / A4** (row 5) | that action on all four channels | nothing |
| **A5 / A6** (row 6) | that action on all four channels | **MENU** |

SHIFT first, then the key: a key already down keeps its plain job. Mind the
whole-room actions on stage: A5 and A6 on every channel at once is a lot.

(motion-not-mid-set)=

## Not in the middle of a set

Fine at soundcheck, loud in front of a crowd:

- **Loading a set**: all four stop, 3d/freq/Q jump.
- **Turning values on ACTION**: rewrites the action everywhere
  ([warning](#motion-howto-action)).
- **Developer Mode** on: Save overwrites shipped files.

Safe: deleting a file (loaded material plays on), scrolling the menu, Escape.

(motion-before-the-gig)=

## Before the gig

- Clock key matches the booth (**PIO** CDJs, **EXT** analyser, **INT**
  otherwise); BPM matches the deck.
- Developer Mode off.
- Your sets loaded once and kept with **Save as**, so tweaks can't touch the
  shipped ones.
- You know where front is in this room.

(motion-troubleshooting)=

## Troubleshooting

| Symptom | What to do |
| :--- | :--- |
| The blob moves, the sound doesn't | Turn **3d** up. At 0 the channel is plain stereo |
| A drag on the sphere moves nothing | Start the drag on the blob itself. Or camera mode is on: tap the small sphere to switch it off |
| A drag on a meter moves nothing | Grab the handle, not the meter |
| No bar, no channel row, ships instead of blobs | That is [FPV](#motion-fpv). **FULL/FPV** in the status bar brings FULL back |
| A pad pulses by itself in FPV | **PILOTS** is at HINT: that pad starts the game that fits the music. At FLY the pilots start games on their own; tap **PILOTS** to step it back |
| No meters, no lightning | Nothing from Core: cable, Core running? |
| ▶ blinks before starting | Waiting for the downbeat (up to a bar); press again to cancel |
| Off the beat, wrong BPM | Clock key. INT: tap. EXT/PIO: check the source (no beats: last tempo) |
| An action pad does nothing | Empty button (grey on ACTION, dark on PADS) |
| An action plays differently | Its values were turned on ACTION; **EDIT** shows the script |
| A FILES tap changed nothing | A tap only shows; **Load** |
| A loaded set doesn't move | Shipped sets load stopped: Play\|Pause or **Play all** |
| **Save** is dark | It's a shipped file. Use **Save as** |
| FILES won't change row and says `-- SAVE OR CANCEL` | The editor has unsaved text. Save it or Cancel it |
| Your drawn shape parks in one spot halfway through the take | The rec mode is **Latch**. Draw in **Touch** |
| A Cue says `-- NO SUCH CLIP` | Its clip was deleted or renamed |
| A Cue says `-- SAVE THE TAKE FIRST` | Tap SAVE or DISCARD on the take |
| **CLEAN** is greyed out | The device has no clean skin installed |
| A double tap on **3D** does nothing | The panel is attached, and its pot decides. Turn the pot |
| The mixer's hardware control and the screen disagree | The A³ Mixer has no motor faders. Touch the hardware control and it takes over |
| You changed an OSC address and nothing reacts | The other side must use the same one. Put it back, or change both |
| Silent after a start | Core not up, or the engine restarted alone: restart `a3-main`; `gate:` lines in `journalctl --user -u a3-core` ({ref}`silent start <core-silent-start>`) |
| Screen frozen | Switch the A³ Motion off and on with the **power switch on its back**; the room doesn't move while it is down |

