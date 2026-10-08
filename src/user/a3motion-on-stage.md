(motion-panic)=

# On stage

(motion-stop-now)=

## Stop the movement, now

| You want | Do this |
| :--- | :--- |
| one channel to stand still, now | select it and tap **■**; on the panel, hold **SHIFT** and press its **Play\|Pause** |
| all four to stand still, now | on the panel, SHIFT + Play\|Pause on each channel; on the screen, select each channel and tap **■**. There is no Stop all |
| a channel back to plain stereo | turn its **3d** pot down. The track stays in the mix, just no longer in the room |
| a chain of actions to end | press Play\|Pause, ■ or another action pad on that channel |
| a take gone wrong to go away | **■** ends it, **DISCARD** twice puts back what was there, stopped |

After a stop the sound stays where it was; it doesn't jump home. And
restarting the device doesn't move the room either: it asks A³ Core where
every sound is before it says anything itself.

(motion-not-mid-set)=

## Not in the middle of a set

These are fine in soundcheck and loud in front of a crowd:

- **Loading a set** stops all four clips and jumps each channel's **3d, freq
  and Q** to the set's values. A shipped set then stands still until you press
  Play.
- **Turning values on ACTION** rewrites that action for every channel and
  every set that uses it. See the warning in
  [How to fire and assign actions](#motion-howto-action).
- **Developer Mode** (in the menu) lets Save write over the shipped files.
  Leave it off on a gig.

And the ones people worry about that are safe: deleting a file (whatever is
loaded keeps playing), scrolling through the menu (a value only changes in
its edit box), and pressing Escape on a keyboard (it never quits the app).

(motion-before-the-gig)=

## Before the gig

- The clock key reads what the booth has: **PIO** for CDJs on a link, **EXT**
  for the beat analyser, **INT** otherwise — and the BPM matches the deck.
- Developer Mode is off.
- The sets you plan to use are loaded once and saved as your own
  (**Save as**), so a tweak on the night can't touch the shipped ones.
- You know where front is on the sphere for this room.

(motion-troubleshooting)=

## Troubleshooting

| Symptom | What to do |
| :--- | :--- |
| The blob moves, the sound doesn't | Turn **3d** up. At 0 the channel is plain stereo |
| A drag on the sphere moves nothing | Start the drag on the blob itself. Or camera mode is on: tap the small sphere to switch it off |
| A drag on a meter moves nothing | Grab the handle, not the meter |
| The channel meters don't move and the speakers throw no lightning | Nothing is coming back from A³ Core. Check the network cable and that Core is running |
| ▶ blinks for a moment before it starts | That's the wait for the next downbeat, up to a bar. Press again to call the start off |
| The clips run off the beat, or the BPM is wrong | Check the clock key. INT: tap the tempo. EXT or PIO: check the source; if its beats stop, A³ Motion carries on at the last tempo it had |
| An action pad does nothing | The button is empty: grey on ACTION, dark on PADS. Put an action on it |
| An action plays differently from yesterday | Someone turned its values on ACTION, and that is saved in the script. Open it with **EDIT** to see what it says now |
| You tapped a set or a clip in FILES and nothing changed | A tap only shows it. **Load** puts it on the device |
| You loaded a set and nothing moves | The shipped sets load standing still. Press Play\|Pause, or PADS › **Play all** |
| **Save** is dark | It's a shipped file. Use **Save as** |
| FILES won't change row and says `-- SAVE OR CANCEL` | The editor has unsaved text. Save it or Cancel it |
| Your drawn shape parks in one spot halfway through the take | The rec mode is **Latch**. Draw in **Touch** |
| A Cue says `-- NO SUCH CLIP` | Its clip was deleted or renamed |
| A Cue says `-- SAVE THE TAKE FIRST` | Tap SAVE or DISCARD on the take |
| **CLEAN** is greyed out | The device has no clean skin installed |
| A double tap on **3D** does nothing | The panel is attached, and its pot decides. Turn the pot |
| The mixer's hardware control and the screen disagree | The A³ Mixer has no motor faders. Touch the hardware control and it takes over |
| You changed an OSC address and nothing reacts | The other side must use the same one. Put it back, or change both |
| The rig is silent after a start | Core is not up, or REAPER was restarted without it. Restart `a3-main`; the journal (`journalctl --user -u a3-core`) has `gate:` lines saying what was opened and what stayed shut. See {ref}`the silent start <core-silent-start>` |
| The screen is frozen | Restart the device. The room doesn't move: it asks Core where every sound is |

<!-- QUESTION (maintainer): "restart the device" in the last row: what is the DJ-safe way on the rig, pulling the network cable (PoE)? And how long until it is back? -->

