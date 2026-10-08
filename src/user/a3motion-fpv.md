(motion-fpv)=

# FPV: play the floor

**FPV** is A³ Motion's second view, for watching and playing a set: the room
and four ships, no editor. **FULL** is everything else on these pages. The
key between them is in the status bar, right of the clock key; it lights
while FPV is up. Switching only changes what you see: the sound does not
move, and the device wakes up in the view it was left in.

<!-- SCREENSHOT: fpv-overview.png | region: full screen 0,0,768,1024 | steps: FPV with ch 1 and ch 2 in ORBIT, ch 3 and ch 4 in CLIP, three groups on the floor (a G, a C, an X) | caption: "FPV: the sphere with its ships and groups, four channel strips below" | not recorded: the rig was in use (2026-10-08) -->

| Part | What it shows |
| :--- | :--- |
| **status bar** | as in FULL, plus **FULL/FPV** and **BREATH** |
| **sphere** (top two thirds) | the room; each playing clip is a **ship**, a dart pointing where it is going. The guest groups lie on its **floor** |
| **strips** (bottom third) | one per channel: `CH n` and **CLIP** (hollow) or **ORBIT** (filled), the clip name with ▶ or ❚❚, the **3D**, **FREQ** and **Q** bars and a meter. In ORBIT the clip row says **PATROL** or **→ G2**. The strips are to read; they take no touch |

(motion-fpv-floor)=

## The floor and the four kinds of people

You tell A³ Motion where people are by **tapping the floor**. Each tap puts a
**group** there, labelled **G1** to **G8** (a number, not a kind). Tap the
group to say what it is; each tap steps to the next kind:

| Kind | On a real floor | Pull | What an ORBIT ship does | Looks like |
| :--- | :--- | :--- | :--- | :--- |
| **G** group | a few people | light (0.5) | leans towards them on the one | a small disc |
| **C** crowd | a dancing crowd | 1 | leans a little more | a bigger disc |
| **H** hotspot | "more of this here" | 1.5, the strongest | leans most | the biggest disc |
| **X** dead zone | "not here": the bar, the booth, a dead corner | pushes away (−2) | keeps out of it, always | red, hatched, with a red ring: the only red thing on the floor |

Tap order: **G → C → H → X → G**. The discs swell on the one and rest on
the other beats.

- **Groups pull only on the one** (beat 1 of each bar), so every lean lands on
  the downbeat. A dead zone's wall works on every beat.
- **The pull is light on purpose.** A group says *where* the sound goes; it
  does not make the movement on its own (see [What to expect](#motion-fpv-expect)).
- **Groups last for the session.** A restart of the device clears the floor.
- **Up to eight.** A ninth tap says `-- 8 GROUPS`.

<!-- GIF: howto-fpv-groups.gif | region: sphere 0,36,768,640 (to be measured in FPV) | steps: tap the floor three times; tap G2 four times (C, H, X, G); drag G1; hold G3 until it goes | "Tap the floor: a group" / "Tap it: crowd, hotspot, dead zone" / "Drag it where the people are" / "Hold it: gone" | not recorded: the rig was in use (2026-10-08) -->

(motion-fpv-orbit)=

## CLIP or ORBIT

In FPV every channel is in one of two modes, shown on its strip:

| Mode | The ship … |
| :--- | :--- |
| **CLIP** | flies the clip, exactly as in FULL. Groups do nothing to it |
| **ORBIT** | leaves the clip and flies **one big ellipse round the room, one lap per four bars**. The groups bend it |

**PAGE** (short press) switches a channel between them. Nothing jumps: into
ORBIT the ship glides off its line from where it is; back to CLIP it glides
onto the clip over one beat, in phase, because the clip kept running
underneath.

- The ellipse turns slowly, once every 32 bars, so even an empty floor is not
  the same circle again and again.
- It is locked to the bar: however far a group pulls the ship, it stays in
  time. At any tempo a lap is four bars.
- The ship stays in its clip's height band. A clip that sits low flies a low
  orbit.
- **ORBIT flies only while the clip plays.** With no clip, or a stopped one,
  the readout says `CH1 ORBIT · no clip` or `CH1 ORBIT · stopped`.
  **Play\|Pause** stops and starts an ORBIT ship as it does a clip.
- ORBIT is the channel's, not the view's: switch to FULL and the ship keeps
  flying its orbit; its blob follows it, and Play\|Pause or PAGE reads
  `CH1 ORBIT`.

<!-- GIF: howto-fpv-orbit.gif | region: full screen 0,0,768,1024 | steps: ch 1 playing in CLIP; short PAGE press on ch 1; 8 bars; short PAGE again | "CLIP: the ship flies its clip" / "PAGE: ORBIT, no jump" / "One lap every four bars" / "PAGE again: back onto the clip, in phase" | not recorded: the rig was in use (2026-10-08) -->

(motion-fpv-escort)=

## Patrol and escort

An ORBIT ship **patrols** by default: it flies the big path and leans
towards groups on the way. You can also send it to **escort** one group: it
leaves the path and circles that group, one turn every two bars. The heavier
the group, the wider the circle (the ring drawn round the group is the
circle it flies). A thin line in the ship's colour joins it to its group.

| To | Do | Strip and readout |
| :--- | :--- | :--- |
| escort a group | **hold** the channel's **PAGE**, **tap** the group | `→ G2`, `CH1 → G2` |
| back to the path | **hold PAGE**, tap **empty floor** | `PATROL`, `CH1 PATROL` |

- Escort switches the channel to ORBIT if it was in CLIP.
- A dead zone cannot be escorted: the ship patrols.
- Removing the group, or making it a dead zone, sends its ship back to
  PATROL, and it stays there.
- While PAGE is held, a tap never removes a group, however long the finger
  stays.

<!-- GIF: howto-fpv-escort.gif | region: full screen 0,0,768,1024 | steps: ch 2 in ORBIT; hold ch 2 PAGE, tap G1; 4 bars; hold PAGE, tap empty floor | "Hold PAGE, tap a group" / "The ship circles it" / "Hold PAGE, tap the floor: patrol" | not recorded: the rig was in use (2026-10-08) -->

(motion-fpv-breath)=

## The breath

With **BREATH** on, every ORBIT ship **stands still on beat 4 of every bar**
and sets off again on the one. The stop on the grid is what keeps the
movement alive: the restart on the one is an event the whole floor hears.
Without it, an orbit soon sounds like it only goes round.

- **On at every start.** **BREATH** in the status bar switches it off or on
  for the session; the readout says `-- BREATH ON` or `-- BREATH OFF`. The
  next start has it on again.
- It works in both views, so the key is in both.
- A stop is never cut short and never starts late: switched during beat 4,
  the change shows from the next bar.
- Escorting ships breathe too and keep their circle. Ships in CLIP don't
  breathe: they fly their clip.
- In a bar of fewer than three beats there is no breath.

(motion-fpv-controls)=

## All controls

### Panel

| Control | In FPV |
| :--- | :--- |
| **PAGE**, short press | that channel CLIP ↔ ORBIT (on release) |
| **PAGE** held + tap a group | that ship escorts it |
| **PAGE** held + tap empty floor | that ship back to PATROL |
| **Play\|Pause** | as in FULL: starts and pauses on the downbeat; SHIFT + it stops now |
| **encoders** | as with SHIFT: upper turns its column's **FREQ**, lower its **Q**. A press does nothing |
| **3d pot** | as in FULL |
| **action pads** | fire as in FULL. They don't switch the page; FULL shows the action next time you look, if ACTION is open |
| **REC** + **Play\|Pause** | switches to **FULL** first and starts the take there, since a take is drawn and kept in FULL. The channel is CLIP afterwards |
| **MENU** | switches to FULL and opens the menu |

### Screen

| Where | Gesture | Does |
| :--- | :--- | :--- |
| floor, empty | tap | a new group (G) |
| a group | tap | next kind: G → C → H → X → G |
| a group | drag | moves it; the view stays put |
| a group | hold (0.6 s) | a red ring fills, then the group goes |
| anywhere but a group | one finger drag | tilts and turns the view; places nothing |
| anywhere on the sphere | pinch | zoom |
| outside the floor | double tap | view straight above, unzoomed. On the floor a double tap places a group and steps its kind |
| status bar | **FULL/FPV** | the other view |
| status bar | **BREATH** | the breath on or off |

**KEYS** and the overlays (FILES, MIXER, PADS) switch to FULL first; going
into FPV closes them. With FILES open, a rename in progress is dropped.

(motion-fpv-playing)=

## Playing a set with FPV

1. **Load and start the set in FULL**, set the clock, check 3d. Then FPV.
2. **Put the floor down**: a crowd where they dance, a hotspot where you want
   more, a dead zone on the bar or the booth. **Few and spread out** beats
   many: each extra group costs the room a little attention.
3. **Two ships move, the rest wait.** Put two channels in ORBIT; leave the
   others in CLIP on a quiet clip, or paused. Four moving ships tire a floor
   fast.
4. **Leave the breath on.** It is the move that carries the set.
5. **Move the top of the mix.** The encoders are FREQ and Q in FPV: a high
   band (around 6–8 kHz) a couple of octaves wide is followed best, or a
   lower one (about 3 kHz) that is wider still. Never narrower than about an
   octave, and nothing down at the bass: under ~250 Hz nobody hears where a
   sound is.
6. **Fly low.** Side to side is heard better than up and down; a clip that
   sits near ear height makes a better orbit than one overhead.
7. **Escort is a gesture, not a routine**: a few bars on the group you want
   to lift, then back to PATROL. Don't feed the biggest group all night.
8. **Change something every few laps.** Move a group, swap which two ships
   fly, drop one back to CLIP. An orbit that never changes is heard, then
   tuned out.

(motion-fpv-expect)=

## What to expect

- **The planets are quiet.** A crowd beside the path moves the ship by a
  small lean on the one, not a swerve you would hear on its own. That is
  decided, not a fault: the groups say *where*, the breath carries the
  motion. Check the lean goes the right way, towards the people.
- **A dead zone is firm.** Its wall works on every beat; a ship keeps clear
  of it.
- **The sound path is the same as FULL.** FPV adds no OSC address; Core sees
  positions as before.
- **Nothing is saved.** Groups, escorts and the breath switch are for the
  session. Only the view itself (FULL or FPV) survives a restart.

| Symptom | Why, and what to do |
| :--- | :--- |
| PAGE switched to ORBIT, the ship stands still | No clip, or it is stopped (`ORBIT · no clip` / `stopped`): load or start one |
| A ship never stops on beat 4 | It is in CLIP, or BREATH is off |
| A group seems to do nothing | Groups only lean on the one, and lightly. Escort it if you want the ship there |
| A drag turned the view instead of moving a group | Start the drag on the group itself |
| A double tap on the floor didn't reset the view | On the floor it places a group; double tap the rim or background |
| The editor is gone | That is FPV. **FULL/FPV** in the status bar |
