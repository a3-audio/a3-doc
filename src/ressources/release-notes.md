# Release notes

One version is one tag, set on every repository at once: the devices are built and played
together, so they are released together. Each section lists what changed, grouped by device,
newest version first. Each group names the repository the changes live in.

For how the system got here, the reasoning and the wrong turns included, see
[History](history.md).

## Unreleased

On `main` since `v03.0`, not tagged yet.

### A³ Motion (`a3-motion-ui`)

**One clip per channel, six actions**

- **Each channel holds one clip and six action buttons**, A1–A6, instead of two slots with
  one action each. The panel's eight pads per channel are Play|Pause and PAGE, then A1–A6 in
  two columns. The Stop and Settings pads are gone: SHIFT + Play|Pause stops at once, and
  STOP stays on the screen.
- **PAGE** selects its channel, or on the shown channel steps CLIP → MOTION → ACTION → CHMIX
  → REC (SHIFT: backwards).
- **The ACTION page** shows the six buttons in the panel's arrangement, each with a **1/H**
  badge for its mode, the list to assign from, and the keys EDIT, Hold/1shot and **then**; the
  card has two tabs, **AUDIO** (the accent) and **MOTION** (what the button puts on the clip).
  A field only **chooses** its button; the pads fire, on the panel and the PADS page, and a
  pad press brings up ACTION with that button chosen. A field turns white while its action
  runs, as its pad does.
- **Encoders on ACTION:** 1 chooses A1–A6, 2 walks the list (a press assigns), 3 rings
  EDIT/mode/then (a press presses), 4 switches AUDIO/MOTION, 5–8 turn the card's marked row (a
  press marks the next).
- **What ACTION sets is written into the script** — what you see is what you get. Every knob,
  the mode, **then** and every MOTION value changes one line of the button's script, in place
  (shipped scripts too); comments and the other lines stay. Every button and set using that
  script plays the change. The clip file's own envelope values are no longer used.
- **Then:** `~then = N;` in a script names the button (1–6) that fires when this one's accent
  is over; chains may loop, another press, Play|Pause or Stop ends one.
- **A set only names its scripts.** Sets saved before 2026-09-29 load without the values that
  were turned per button, and **without their then chains** — set those again on ACTION.
- A script is worked out **at the press, against the clip as it is then**. Before, a button
  kept the clip it was assigned on, and after a new clip or a turned knob a press threw the
  channel back to the old values for the length of the accent. The dice of a random action are
  thrown when it is assigned, so every press lands in the same place.
- A second action while the first is still sounding takes over; afterwards the clip comes back
  to itself, not to the first action.
- An action button with nothing on it does nothing, and its pad is dark.
- The PADS page is 2×4 per channel, with a scene column that fires a pad on all four channels
  (see *The keyboard is the panel* below).
- The channel row shows the clip's name instead of a slot number.
- Sets store the six actions per channel. **Sets from before are copied once to
  `pattern/backup-two-slots/`** on the first start, then read with slot 1 as the clip and the
  two slot actions as A1 and A2.
- **The library: 50 shapes, 50 clips, 50 actions, 10 sets**, laid out on the mood meter (energy
  × pleasantness).
  - **Eleven new shapes** from rhythm and electroacoustic motion:
    - Tresillo and Clave 3-2, which jump on their sixteenths;
    - Ping Pong, Riser, Collapse, Vortex, Pulse and Echo;
    - Astroid, Trefoil and Drift.
  - **29 new clips**, named for what they do in a set (Anthem, Hands Up, Tresillo Drive,
    Warehouse, Echo Chamber, Undertow, Aurora, Canopy, …).
  - **24 new actions**:
    - Riser and Impact for the build and the drop;
    - Loom and Recede for approach and retreat;
    - Echo Throw and Tape Stop from dub;
    - Lift, Widen, Stutter, Freeze, Breathe, and more.
  - Every action names its mood.
  - The ten sets are rebuilt from the whole library, one mood each. The six buttons are laid out
    the same way in every set: the left column adds energy and openness, the right takes it away.
  - Cellar now sits low and turns slowly, and Standstill stands still.
- Loading a set makes it the current one on disk at once; a restart straight after a Load came
  back with the set before.

**Recording and clips**

- A take is as long as the clip on show.
- **● arms, ▶ starts.** ● puts the shown slot in REC PAUSE: the bar jumps to the REC page and
  the clip keeps playing while length, recmode, fade and bias are set. ▶ starts the take on
  the next downbeat; ● or ■ while armed takes it back and writes nothing. The panel's REC +
  Play|Pause pad still starts a take directly.
- **Pots are recorded.** The twelve Motion and Elevation knobs (rot, spin, reach, swell,
  sqzX, strX, sqzY, strY, clip-bot, clip-top, sway, elv) are written in a take by the same
  recmode as the path: TOUCH while a hand is on the knob, LATCH to the end of that lap, WRITE
  the whole pass. A finger counts from the touch to the lift, an encoder step for 400 ms.
  While the take writes a knob, its arc and pointer are the REC key's red. On playback the
  recorded knob turns by itself with a small red dot beside it; a hand on it wins, and picks
  it up where it stands. SAVE keeps the lanes in the clip file (`"lanes"`); clips without
  any are unchanged.
- **A take overdubs the slot's clip.** It starts from that clip's settings, path and knob
  lanes, so TOUCH and LATCH change only what is touched -- turning pots alone over an old
  figure is a take. WRITE still replaces everything; a take on an empty slot starts empty.
- A double tap on a knob with a recorded lane clears that lane and keeps the value; on a knob
  without one it still resets to the middle. A cleared lane marks the clip as changed, and
  FILES-Save writes it.
- A take is the last lap that was finished, and a hand held still is no longer read as a fold.
- Save writes back to the clip a slot came from, and the list marks a clip that has unsaved
  changes.
- In developer mode, Save may write over the factory clips.
- New recordings no longer come back with a second clip (`… 2`) after a restart.
- **A take waits for SAVE or DISCARD.** It is no longer written to disk the moment it ends:
  it keeps playing, marked with a red dot on its pad, while REC reads SAVE (a tick) and ACT
  reads DISCARD (a cross, tapped twice). Anything that replaces it -- a new take, a shape, a
  set, a restart -- drops it. A set only ever names what is on disk.
- Fast strokes no longer come back from the file in pieces: a step counts as a jump only
  when it is far larger than the movement around it.
- The touch screen no longer freezes for seconds after a long take: a take's path data is
  read in one pass.

**Sets and files**

- Save as for a set writes the new set where the list reads it. It shows up straight away and
  no longer overwrites an older set that has the same name.
- A set carries the four speed keys; loading it brings them back. Sets written before this
  leave the keys alone. The mixer is deliberately not part of a set.
- The browser keeps your place, keeps the row you chose, and a set is loaded with a key.
- A clip chosen for a slot -- in the clip field or from FILES -- is saved in the set at once,
  not only the next time something else saved it.

**Controls**

- **The workspace switch**, at the right end of the status bar: **STEMDECK** goes to StemDeck
  on the Core's screen, **▾** lists the rig's workspaces as i3 reports them (those with a
  window on them), the current one highlighted; a tap beside the list closes it. It stands
  exactly where StemDeck's MOTION key stands, so the key under the finger stays put, and it
  is drawn in StemDeck's look rather than the skin's. CLEAN, KEYS and MENU now stand before it.

- **New layout of the bar.**
  - **The channel row:** across the whole width, between the sphere and the bar, one field per
    channel in its colour. Each field shows the channel's VU, its 3D, FREQ and Q pots, and a bar
    its clip's progress fills from the left, with the slot number at its start. A touch anywhere
    on the field selects the clip, and a second tap on the shown field flips its slot. Touching
    a pot selects the channel without flipping. The playhead marks in the tick indicator and
    the signal dot moved into these bars.
  - **Tabs:** CLIP · MOTION · ACTION · CHMIX · REC. FILES, MAINMIX and PADS stand at the top
    of the global strip, over the elevation picture and the 2×2 transport.
  - **CLIP:** one area of eight equal fields, in the encoders' 4×2 arrangement: clip, dir and
    two lengths over the shape, end and two lengths.
  - **MOTION:** one area, rows as the encoders turn them: spin swell strX strY / rot reach
    sqzX sqzY / sway clip-top / elv clip-bottom.
  - **REC:** eight equal fields like CLIP, with recmode over fade|bias instead of dir over end.
  - **CHMIX:** GAIN HIGH MID LOW over SEND 3D FREQ Q.
  - MAINMIX shows the big mixer like a tab.
- **The panel's encoders turn the field they stand under** on CLIP, MOTION, REC and CHMIX. A
  press switches between the two things under an encoder: MOTION's rows, and REC's fade and
  bias. A press on a length chooses it. With Shift, and on ACTION, FILES, MAINMIX and PADS,
  each column turns its channel's FREQ and Q as before; 3D stays on the analog pots.
- **The section locks are gone.** A loaded clip lands every value it carries and the figure it
  names.
- **Direction and end are two choices.** `dir` is Fwd, Rev, Bnce or Rnd and `end` is Loop,
  Stop or Paus, in any combination: Bnce + Stop goes out and back once. Old clips with an end
  of bounce or random play as before.
- The elevation line is a knob, `elv`, left of `sway`; the picture takes no touch any more.
- Tapping the elevation picture puts the sphere in camera mode. A finger turns the view,
  from overhead to the horizon and never from below. Two fingers or the wheel zoom, and a
  double tap resets. The view survives a restart.
- The status bar: CLOCK · BPM · the last action · the beat display (touch it to tap) ·
  CLEAN · KEYS · MENU. KEYS is coloured while the on-screen keyboard is up.
- The mixers: 3D, FREQ and Q per channel on CHMIX and in the big mixer; FX FREQ and FX RES
  sit under RET.
- The transport shows what it is doing, and blinks while it waits for the beat.
- Play/Pause on a running clip stops it on the next downbeat, and at once with Shift, the
  way a start works. It used to wait for the end of the lap, which with a long playback
  length could be half a minute and felt like a key that did nothing. Stop is still the
  way out that does not wait.
- Pads: a scene column, feedback on press and on a running action, marks readable on every
  channel colour, and the settings pad opens the clip.
- Menu values change in a mask, and nothing else edits while it is open.
- The main menu is see-through again: the sphere shows through its panel, as it did before
  it turned solid. It has its own skin value for that (`menuPanelOpacity`, under Panels);
  the skin editor and the colour picker stay solid.
- The MIX page: the filter and master pots have a way back to their centre.
- The CLIP knobs show their blue arcs again: where a modulation is carrying `rot`, `reach`,
  `sqzX` and `sqzY` right now. They had gone missing when the knobs were rebuilt, and an arc
  below the knob's setting now runs down from the pointer instead of up from the start of
  the scale.
- The colour picker is JUCE's own colour field.
- A CLEAN key switches to a clean skin and back.
- Every action script names every parameter it takes, with its range.

**The keyboard is the panel**

- **PADS is the panel, key for key:** 44 keys on the panel's ten columns and six rows. On the
  left TAP and clock, then the scene column — Play all, A1, A3 and A5 on every channel; the four
  channels in the middle; the six function keys on the right. The scene block's second column
  (Stop all, and A2, A4, A6 across channels) is gone.
- **The in-app keyboard stands on the same grid**, QWERTY instead of QWERTZ: ESC and 123 in the
  left column's top two keys, DEL and ENTER in the right's, the letters in rows 2–4, SHIFT,
  ◀ ▶, SPACE, ' " and HIDE along the bottom. **123** holds digits and the symbols scripts are
  written with. No umlauts any more. The four rows of twelve on the encoder fields, walked by
  the encoders, are gone.
- **While the keyboard is up, the whole panel types:** each of the 44 buttons is the key in its
  place, and types on press. No clip fires and TAP, REC, MENU and SHIFT do nothing else;
  running clips go on, pots and faders are unchanged. HIDE or ESC gives the panel back, and a
  key pressed while typing keeps its release on the keyboard, so ESC (on TAP) never taps. This
  reverses the earlier rule that the pads keep playing while you type.
- Encoder 1 (channel 1, upper) moves the text cursor; the other encoders keep their jobs.
- While typing, the pad and key LEDs show the keyboard: letters dim, the other keys in the
  skin's accent colour.
- On the screen a key still types on release (slide off to cancel); DEL and the arrows repeat
  while held.

**Clock**

- In EXT and PIO the clock sits on the beats it is sent.
- **EXT follows smoothly.** Half or double the tempo counts as the same tempo; a real change
  needs four beats in agreement (an octave jump sixteen) and glides in. The phase is pulled
  in small steps, and a stray beat is ignored, so the motion no longer stutters on a
  doubtful beat.
- A beat trace, to measure where the time goes between a beat arriving and a clip moving.

**The sphere**

- **What is drawn:** on the sphere and in the elevation picture alike, every playing clip, plus
  the selected clip as a preview even when it is not playing, drawn over the others. The
  elevation picture shows every playing clip, each in its channel's colour.
- **Previews are visible again.** Since the lines moved to the GPU, a preview (the selected
  clip, the Shift+ACT listen) was drawn in software less than a pixel wide. It goes through the
  GPU like a playing line now.
- **Shapes made of dots show their dots** (Cross, Corner, Bounce) on the sphere, in the
  elevation picture and in the shape field. They had vanished: the sphere drew their dots about
  a pixel wide, a turned knob replaced them with an empty line, and the shape field's picture
  measured them as a single point.
- Rendered twice as fine and drawn back down, so edges no longer step.
- No lag while recording: the line of a take being played in is drawn from what the hand
  moved to, the take underneath is drawn once, and the listener figure is worked out only
  when the view turns.
- The trajectory, the braid and the speaker bolts are drawn in the shader. A speaker's level
  is how thick its bolts run, and a silent room throws none.
- The far side of a trajectory goes behind the sphere again, and the floor no longer cuts
  the blobs in half.
- **No lag with several clips playing.** The glow, cord and braid of every playing trajectory
  are painted on the graphics card; they were drawn by the processor every frame, which with
  four clips running held the picture at about 8 frames a second. Now about 40, and the touch
  screen answers at once. The picture itself is unchanged.

**Start-up and build**

- The app waits until the screen is really there, and refuses to start without a display
  instead of crashing.
- A speaker test (pink noise at −40 dBFS), in builds with `A3_AUDIO_ENGINE_ENABLED`.
- Each build directory gets its own generated config; `test.sh` builds before it runs and
  says when the runner was built.

### A³ Core (`a3-core`)

- **Total recall:** Core writes the evening down and plays it back on the next start. At
  start it asks REAPER to report everything, so the order the services start in no longer
  matters, and it plays the evening back only once REAPER has finished reporting —
  earlier, REAPER's own report could overwrite it. A value set at the desk or on Motion is
  written down even while REAPER is silent.
- The OSC window has a key that asks REAPER to report everything again.
- **No more lag from Core:** one loop reads each OSC port. It used to start a thread per
  message, and under load those piled up until the mixer and Motion stopped reaching
  REAPER. Core also no longer shares its processor core with Motion's screen.
- REAPER is told only the OSC addresses Core uses, which shortens its report at start from
  23 to 14 seconds.
- An update no longer reinstalls REAPER and its plugins under a running REAPER (which
  crashed it); they are installed only when missing.
- What one mixer sets, every other screen shows.
- The OSC window shows data rates per device and overall, and both tables sort by any
  column. Messages that arrive and find no receiver are written down.
- Installing: an update keeps configuration somebody edited, a re-install neither fails
  nor overwrites the `.env`, and the package installs the programs its services run.
  REAPER's config ships as plain files with the current project, and the plugin paths are
  set without shipping `reaper.ini`.
- New tools: `--install`, and a report of what the machine runs that the repository does
  not carry.
- The macOS tree and the MIDI clock are gone.
- The package installs on the network the ports page states (`192.168.8.10`), and takes the
  interface away from the DHCP setup that raced it. Core sends to the Mixer and to Motion at
  their documented addresses by default.
- The dummy screen for a Core without a monitor is asked for during the install (default
  no) instead of being installed on every machine, where it left a monitor black.
- **Both network sockets can be bridged.** The install asks which second socket to bridge
  with the first (pre-filled with the other wired one); with it, both become one segment,
  `br0`, which carries Core's address, with spanning tree on. Router in one socket, mixer
  in the other, all on `192.168.8.0/24`. It takes effect at the next boot, and answering
  with nothing takes the bridge away again. Core then sits between router and mixer: with
  Core off, the mixer has no network.
- The install asks for the address, gateway and DNS every time, pre-filled with what is
  stored. An answer still on the retired `192.168.43.x` network is replaced by the
  documented default before it is offered.
- Package updates reach the rigs: the package version is the last tag plus the commits
  since it (`03.0+71`, say) instead of a fixed `1.0.0` that apt never saw change.
- **Named workspaces:** `1:MOTION`, `2:STEMDECK`, `3:REAPER`, `4:QJACKCTL`, `5:SCARLETT`, and
  every program's window is moved to its own by an i3 rule. StemDeck's main window fills its
  workspace without a border (i3's full screen ended with every dialog it opened); its other
  windows float.
- **An i3bar at the top** on workspace 3 and up, the way back from REAPER, QjackCtl and the
  Scarlett mixer, with the workspace names shown without numbers. It is hidden on the two
  touch screens; `a3-bar-per-workspace.service` switches it.
- The package also depends on `x11-utils`, `x11-xserver-utils` and `i3status`.

### A³ Mixer (`a3-mixer`)

- The tap keys blink with the beat; the bright key carries the cue, and the dim one taps.
- At start the desk asks what is on, so its lamps are right from the first moment.
- One dark display no longer takes the other five with it, and a crashed display process no
  longer looks like a running service. A display's label stays when its script ends.
- A key with no OSC address is ignored rather than stopping the desk.
- The 3D key is out of service; the PFL lamp is no longer inverted twice.

### A³ Motion controller (`a3-motion`)

- The `v03.2` hardware branch is merged into `main`.
- **The key LEDs stay within what USB can supply.** The 44 LEDs under the keys run on the
  controller's USB power, and nothing limited them: full white on every key would draw far more
  than a USB 2.0 port gives, and the result is the controller dropping out, not dim keys. The
  firmware now dims all keys together, and only when their estimated draw goes over a budget
  set just above the brightest picture the app shows in normal use — so playing is never
  dimmed. A³ Motion keeps the same estimate and says in its log if a skin or colour rule would
  go over it. The firmware has host tests now (`pio test -e native`).

### Beat analyzer (`beat-analyzer`)

- The beat clock takes tempo and phase from BTrack's beats and predicts with the measured
  period. The octave lock moved from the tempo range to the clock: one octave, or no lock.
- The mixer's VU goes to port 7772 (was 7771).
- The example `.env` follows the rig's network.
- The octave choice has hysteresis: near the edge of the tempo range the clock no longer flips
  between a tempo and its double.

### StemDeck (`stemdeck`)

- **StemDeck joins the system.** The stem player — two decks of four stems, each stem on its
  own output bus, any of them switchable to aux — is carried by the a3-system repository as a
  submodule since 2026-09-29, and versioned with the rest.
- **Always running on the Core**, as `stemdeck.service`, on workspace 2. A (re)start no
  longer takes the screen: `tools/rig-keep-the-screen.sh` puts back the workspace that was
  showing. A restart still costs a burst of JACK xruns from the graph change — not mid-set.
- **MOTION and ▾** at the right end of the top bar: over to A³ Motion, or to any of the rig's
  workspaces, at the same place as A³ Motion's STEMDECK key. The list is drawn inside
  StemDeck's own window; a separate popup window came up black on the rig.

### Documentation (`a3-doc`)

- **A page for the beat analyzer:** what it does in the system, its three clock modes and
  which of A³ Motion's clock keys selects which, what each mode needs, its `.env`, the
  meters and troubleshooting.
- **A page for StemDeck:** stem sets, the screen, the audio outputs, and building and
  starting it.
- The OSC reference has a section for the beat-analyzer's own messages, lists the A³ Mixer on
  its VU port 7772, and no longer lists address mismatches that have been fixed.
- The user section explains every control on A³ Motion where a performer looks for it; the
  Mixer, the Core and the welcome page follow the same shape, with current pictures.
- The OSC reference lists every path, with send and receive per device, and one page lists
  every port.
- These release notes.
- The Core's screen: its workspaces and the bar (user and configuration pages), the workspace
  switch in StemDeck and A³ Motion, and StemDeck on workspace 2 instead of 4.

## v03.0 (2026-09-12)

The first version tagged across all repositories at once. From here on `main` is the
integration branch everywhere and versions are tags. The per-hardware-revision branches
(`v03.2`, `dev/v03`) are merged and kept as history.

What came before is told in [History](history.md).
