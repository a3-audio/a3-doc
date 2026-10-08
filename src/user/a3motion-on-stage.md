(motion-panic)=

# On stage

(motion-stop-now)=

## Stop the movement, now

| You want | Do this |
| :--- | :--- |
| one channel still | **■** (selected channel), or **SHIFT** + its **Play\|Pause** |
| all four still | the same on each channel; there is no Stop all |
| plain stereo | **3d** pot down: still in the mix, no longer in the room |
| a chain to end | Play\|Pause, ■ or another action pad on that channel |
| a bad take gone | **■**, then **DISCARD** twice: the old clip, stopped |

A stop leaves the sound where it is. A restart doesn't move the room either.

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
| Silent after a start | Core not up, or REAPER restarted alone: restart `a3-main`; `gate:` lines in `journalctl --user -u a3-core` ({ref}`silent start <core-silent-start>`) |
| Screen frozen | Restart the device; the room doesn't move |

