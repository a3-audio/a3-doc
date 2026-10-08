# Screen and panel

(motion-reference-screen)=

## The screen

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
| **Menu** and its pages | skins, network, LEDs, folders | MENU in the status bar, or MENU on the panel | ‹ (back) or MENU: one level; ✕: all of it |
| a list of values, an edit box | changing one menu value | double tap or ENTER on a menu row | ENTER or a tap on a value (keeps it); back, MENU or Escape (drops it) |
| the colour picker | changing one colour in the Skin Editor | double tap a colour row | **done**, back or MENU. The colour stays either way: it is changed as you drag. Escape does nothing here |
| **Keyboard** | typing names and values | KEYS, status bar; comes up by itself when there is something to type | KEYS again, or HIDE |
| the workspace list | going to another of the Core's screens | ▾, right end of the status bar | a tap on a workspace (goes there), or a tap beside the list |

Only one of FILES, MIXER and PADS is open at a time; each opens on top of the
sphere, and the channel row, the bar and the global strip stay in view under
it. Closing FILES ends a rename without keeping it and cancels an armed
Delete; text typed in the editor stays, marked unsaved.

<!-- GIF: howto-overlays.gif | region: 0,36,768,712 | recorded 2026-10-01, quiet-indigo-2, --fuzz 0 (quantized before optimizing), PADS as the panel | steps: Tap FILES, MIXER, PADS: each lies over the sphere, one at a time. Tap CLIP: it closes. | "FILES, MIXER, PADS: over the sphere" / "FILES" / "MIXER: one at a time" / "PADS" / "A bar tab closes it" -->

![Tap FILES, MIXER, PADS: each lies over the sphere, one at a time. Tap CLIP: it closes.](pics_user/howto-overlays.gif)

### The main screen

![The main screen, here with the ACTION page in the bar: status bar, sphere, channel row, bar and global strip](pics_user/a3-motion-ui-display-one-clip.png)

<!-- The main screen, the channel row and the ACTION page were taken on 2026-09-30 from the rig's running A³ Motion, which runs the skin "custom" (quiet-indigo-2's colours with the maintainer's effect settings), not quiet-indigo-2 itself: the sandbox would have stopped the live service. Re-shoot in quiet-indigo-2 when the sandbox may run. -->

Top to bottom:

1. the **status bar**: clock, tempo, what was last done, the beat, CLEAN,
   KEYS, MENU, and the workspace switch STEMDECK ▾;
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
| **STEMDECK** | shows [StemDeck](stemdeck.md), on the Core's screen. StemDeck has the same key, reading MOTION, at exactly the same place, so a second tap brings you back |
| **▾** | opens the list of the Core's workspaces — MOTION, STEMDECK, REAPER, QJACKCTL, and SCARLETT while the Scarlett mixer runs; only those with a window on them. The one on the screen is highlighted; tap one to go there, beside the list to close it |

The switch at the right end belongs to the rig, not to your skin: it is the
same key in both apps. The workspaces are on
{ref}`A³ Core's screen <core-workspaces>`.

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
| drag a blob | moves that channel's sound, live. Start the drag **on the blob**: then it jumps under the finger. A drag that starts on empty sphere moves nothing. A playing clip keeps running and takes the blob back when you let go. Other blobs in the way are pushed aside, and their sound moves with them |
| several fingers | each takes its own blob |
| during a take | the first finger writes the take, wherever it lands; see [REC](#motion-rec) |

**Camera mode** turns the view instead. Tap the **elevation picture** in the
global strip (the small sphere with the camera mark) to switch it on or off;
its field lights while it is on.

| Gesture, in camera mode | What it does |
| :--- | :--- |
| drag up | leans the view from straight above down towards the horizon |
| drag down | leans it back up. From straight above there is nowhere higher to go, so a drag down does nothing |
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

<!-- GIF: howto-channelrow-select.gif | region: 0,626,768,398 | recorded 2026-09-29, 8.4 s | steps: Tap channel 2, channel 3, then channel 1 in the channel row: the bar follows the channel and takes its colour. | "Tap a channel to work on it" / "Channel 2: the bar turns blue" / "Channel 3: its clip, its keys" / "Channel 1: back where you were" -->

![Tap channel 2, channel 3, then channel 1 in the channel row: the bar follows the channel and takes its colour.](pics_user/howto-channelrow-select.gif)

<!-- GIF: howto-channelrow-pots.gif | region: 0,626,768,398 | recorded 2026-09-29, 9.5 s | steps: Drag channel 1's FREQ pot up and down, then drag channel 2's 3D pot: channel 2 becomes selected. | "3D, FREQ, Q: right in the row" / "Drag FREQ up, then down" / "3D on channel 2: now selected" -->

![Drag channel 1's FREQ pot up and down, then drag channel 2's 3D pot: channel 2 becomes selected.](pics_user/howto-channelrow-pots.gif)

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
key is the one the clip plays at; when none is lit, the clip plays at a length
none of the four holds, until you tap one. The four keys belong to the device
and are saved in the set.

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
**What you set here is saved into the action's script, for everyone** —
every channel and every set that uses it, shipped ones too. To keep the
original, copy it first: see [Fire and assign actions](#motion-howto-action).
```

<!-- QUESTION (maintainer): Save as is lit only while the editor holds unsaved text (scriptKeysFor: saveAs = unsaved), so an unchanged file can't be copied as it is -- the page now tells the DJ to change a comment first. Should Save as copy an unchanged file? -->

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
| **CUE** | the channel on the headphones (its pre-fader cue send). Tap to switch |
| **FX** | puts the channel through the shared filter (FX FREQ, FX RES, FX MODE in MIXER). Tap to switch |
| meter, on the right | the channel's level, and its **VOL fader**: the handle is the volume. **Grab the handle** and drag, one to one; a drag that starts elsewhere on the meter does nothing. Double tap the meter: full volume |

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
| **Save as** | writes a copy into your own files, named after the file the editor shows ("Lift Up 2"); with no file shown, "Action". Lit only while the editor holds unsaved text — after **from set** / **from clip**, or once you have typed. The copy is not loaded: Load it to play it; a copy of an action made after EDIT goes onto that button |

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

![The MIXER window over the sphere](pics_user/a3-motion-ui-mixer-overlay.png)

The knobs and the CUE and FX keys show what is really set: a hand on the desk
moves them here too, and a restart brings them back as they are. The desk has
no motor faders; see [Mix from the screen](#motion-howto-mix).

**Four channel strips**, each with its meter on the left and, down the strip:

| Control | What it does |
| :--- | :--- |
| meter | the channel's level and its **VOL fader**: grab the handle and drag, one to one; elsewhere on the meter a drag does nothing. Double tap: full volume |
| **GAIN** | input gain. Double tap: full |
| **HIGH**, **MID**, **LOW** | the EQ. Double tap: flat |
| **SEND** | to the FX bus. **SEND comes up shut, and a double tap takes it back there** |
| **CUE**, **FX** | cue, and the channel through the shared filter. Tap to switch |

**The master column**, on the right:

| Control | What it does |
| :--- | :--- |
| the column | the **master fader**: grab its handle and drag, one to one. No double tap: full on the master is the one gesture that makes the whole room loud at once |
| output meters, at its foot | ten: the main sub and tops 1–9. Read only |
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

The window is **the panel, key for key**: 44 square keys on the panel's grid
of ten columns and six rows, each where its button is on the device.

- **the four channels** in the middle, two columns of four each, in the bottom
  four rows. The top two rows stay empty, where the panel has its pots;
- **right**, top to bottom: **TAP**, **clock**, **REC**, **recmode**, **MENU**,
  **SHIFT**;
- **left**, top to bottom: **TAP** and **clock**, then the **scene column**
  (▶ A A A): **Play all**, **A1**, **A3** and **A5** on every channel.

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
- The **scene column** on the left fires one pad on **all four channels**:
  **Play all** starts only the clips that are standing still; **A1**, **A3**
  and **A5** fire that action on every channel that has one. It is screen
  only: on the panel, the left column's lower four buttons are REC, recmode,
  MENU and SHIFT. There is no Stop all and no A2, A4 or A6 across channels any
  more.

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
| Load a set | all four stop **now**; what the set says was playing starts together on the **next downbeat** (a shipped set: nothing) |
| a drag on the sphere | **now**, all the way |

<!-- GIF: howto-pads-page.gif | region: full screen 0,0,768,1024 | steps: tap ch3 PAGE (572,110); tap ch3 PAGE again | "PAGE on a channel selects it" / "PAGE again closes PADS" | round 2 -->

(motion-menu)=

### The menu

Opened with **MENU** in the status bar, left of STEMDECK, or MENU on the panel.
It opens on top of the sphere. **Nothing in the menu is needed to play.**

| Page | What it holds |
| :--- | :--- |
| **Skin** | which skin is loaded, as a list; the skin previews as you browse it with the arrow keys |
| **Skin Editor** | every value the loaded skin holds, grouped by what it is |
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
| tap a row that leads to a page (Skin Editor, Button LEDs, Pattern Folder) | opens that page, at once |
| tap any other row | selects it |
| double tap a row, or ENTER | opens it: a list of its values (Skin, Sphere in Menu, Developer Mode), an edit box, or the colour picker |
| in a list of values | tap or ENTER chooses, and a tap chooses at once; Escape or back leaves without choosing |
| in an edit box | type with the keyboard; ENTER keeps; Escape, back or ✕ undo. A skin number also has **− / +** keys that step it while you watch |

Two fingers scroll as one. Inside a page — the Skin Editor and the
others — a tap selects a row and a double tap opens it, as above. **Mind the
double tap on the main menu's page rows:** the first tap has already opened
the page, and the second lands on whatever row is under your finger there.

**Getting out:** the **‹** (back) and **✕** (close) keys in the top right, and
MENU itself. Back and MENU close **one level**; ✕ closes all of it at once,
however deep. **Escape never quits the app.** In a booth, one elbow on a
keyboard shouldn't end your set.

<!-- GIF: howto-menu-navigate.gif | region: 0,0,768,660 | recorded 2026-09-30 (after the Network page left the menu), quiet-indigo-2, --fuzz 1% | steps: Tap MENU, tap Skin Editor, tap All values, drag the list, tap back, tap ✕. | "MENU opens it over the sphere" / "Tap a row: its page" / "Drag to scroll" / "‹ back: one level up" / "✕ closes all of it" | a page row opens on ONE tap; a double tap lands the second tap inside the page -->

![Tap MENU, tap Skin Editor, open All values, drag the list, tap back, tap ✕.](pics_user/howto-menu-navigate.gif)

#### Skin

Double tap **Skin**: the rows give way to the list of skins. The arrow keys
↑ ↓ walk the list and preview each skin on the sphere; ENTER keeps the one
you are on, Escape or back puts the running one back. **A tap on a skin
chooses it straight away**, with no preview, and writes it into the device's
settings. Dragging the list only scrolls it.

<!-- QUESTION (maintainer): the preview is reachable only by the arrow keys (GlobalSettingsComponent::keyPressed → onPickerBrowsed); a drag scrolls without previewing, a tap applies and writes config.json (applySkin), and the panel's encoders don't reach the menu at all (handleEncoderTurn has no menu case, although previewSkin's comment speaks of "the encoder"). So on the device without a keyboard there is no way to look at a skin before it is chosen. Intended? -->

#### Skin Editor

Every value of the loaded skin, under headings: surfaces, text, states,
channels, sphere, type, touch, then the effects. At the top, five action rows:
**» Save**, **» Save as new**, **» Rename**, **» Delete** (asks "sure?") and
**» Reset** (every value back to the shipped default, keeping the name). They
fire only on a double tap or ENTER.

- A number opens the edit box with − / + to step it live, by a tenth of its
  value each press (whole numbers by one). Escape puts the number back.
- A colour opens the **colour picker**: drag on the picking surface (hue,
  saturation, lightness); the change is live; **done** closes it. There is no
  undo in the picker: whatever you dragged to is kept, and Escape doesn't
  close it. The picker counts channels from zero, so channel 1's colour is
  labelled `channels.0`.
- **Leaving the editor saves the skin**, changed or not. On the shipped
  default skin it saves a copy called **custom** and switches to it, so the
  default itself is never written over.

![The Skin Editor, its sections on the left of the sphere](pics_user/a3-motion-ui-skin-editor.png)

<!-- QUESTION (maintainer): the colour picker has no undo (closeColourPicker keeps what applyPickedColour already wrote into the document) and no Escape, while the edit box undoes the whole document on Escape (_documentBeforeMask). Should the picker undo on back/Escape like the edit box? -->

#### Button LEDs, Pattern Folder

Each shows only its own part of the device's settings, as rows: Button LEDs
the key colours; Pattern Folder the folder the library is read from. Double
tap a row to type a new value, or to pick a colour. The page is saved when you
leave it. Hosts, ports and addresses are not in the menu any more: see
[How to point the device at another Core](#motion-howto-network).

#### Sphere in Menu, Developer Mode

Double tap the row, tap **on** or **off**.

(motion-keyboard)=

### The keyboard

The device has its own keyboard. It takes the **bar's place** — where CLIP,
MOTION, ACTION, CHMIX and REC are — so the sphere, the channel row, the tabs
and the global strip stay in view, and every field you type into sits on top
of the sphere, never under the keys.

- **KEYS** in the status bar shows or hides it; its icon follows.
- It comes up by itself when there is something to type — a Rename in FILES
  (every tab, sets too), a touch in the FILES editor, a name or a value in the
  Skin Editor and the menu — and goes again when that is done.
- **HIDE** puts it away and leaves the field open.

**The keyboard is the panel.** Its 44 keys stand on the same grid as the
panel's 44 buttons and the [PADS](#motion-pads) window — ten columns, six
rows — so every key on the screen is the button in the same place on the
device. The letters are **QWERTY**:

| Row | col 0 | cols 1–8 | col 9 |
| :--- | :--- | :--- | :--- |
| 0 | **ESC** | — | **DEL** |
| 1 | **123** | — | **ENTER** |
| 2 | q | w e r t y u i o | p |
| 3 | a | s d f g h j k l | - |
| 4 | z | x c v b n m , . | / |
| 5 | **SHIFT** | ◀ ▶ **SPACE** (four wide) ' " | **HIDE** |

**123** swaps rows 2–4 for what scripts, clips and sets are written with, and
reads **ABC** there to come back:

| Row | Symbols (**123**) |
| :--- | :--- |
| 2 | 1 2 3 4 5 6 7 8 9 0 |
| 3 | - / : ; ( ) = + _ * |
| 4 | { } [ ] < > \ \| ! ~ |

There are no umlauts and no ß.

![The keyboard in the bar's place](pics_user/a3-motion-ui-keyboard.png)

- **SHIFT** once: the next letter is a capital. Twice: caps lock. A third
  time: off.
- On the screen a key types when you **let go**: slide off a wrong key and
  nothing is typed. **DEL** and the arrows act at once and repeat while held.
- **ENTER** keeps what you typed and closes, in a name; in the FILES editor it
  is a new line, and **ESC** or **HIDE** put the keyboard away. **ESC** in a
  name, and Back or Close in the Skin Editor, undo it.

**From the panel: while the keyboard is up, the whole panel types.** Each of
the 44 buttons is the key drawn in its place — the pads are the letters; on
the left TAP is ESC and SHIFT is SHIFT, on the right TAP is DEL and SHIFT is
HIDE — and it types **as you press** it; DEL
and the arrows repeat while held. The pads and key LEDs show the keyboard: the
letters dim, the other keys in the skin's accent colour.

- **No clip fires and no key does its own job** while you type: no pad
  starts or stops anything, TAP taps no tempo, REC, MENU and SHIFT do nothing
  else. Clips that are running go on.
- **HIDE or ESC gives the panel back.** A key you pressed while typing is
  released to the keyboard too, so letting go of ESC never taps a tempo. A pad
  you were already holding when the keyboard came up lets go as usual.
- **Encoder 1** (channel 1, upper) moves the text cursor. The other encoders,
  SHIFT + encoder (freq and Q), the pots and the faders keep their jobs: the
  mix stays under your hands.

Open the keyboard only when you mean to type, and put it away with HIDE or
ESC before the next clip has to start.

(motion-reference-panel)=

## The panel

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
| CHMIX | GAIN, HIGH, MID, LOW | SEND, CUE, FX, VOL | on CUE or FX: switches it |
| ACTION | A1–A6, the list, the key ring, AUDIO/MOTION | the four values of the card's marked row | list: assigns; key ring: presses; lower row: marks the next row; see [ACTION](#motion-action) |

Where an encoder has two knobs to choose from, the bar marks the one it is on.
The choice is remembered.

The six function keys sit as a **vertical column at each end of the panel**,
mirrored so either hand reaches them; a key is down while either side is down.
**clock** and **recmode** step their value on a press, as their screen twins
do. **SHIFT is on the panel and on the PADS window**: the SHIFT gestures on
this page need one of the two.

**While the keyboard is up, the panel types** and no pad fires; see
[The keyboard](#motion-keyboard).

