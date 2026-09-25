# Release notes

One version is one tag, set on every repository at once: the devices are built and played
together, so they are released together. Each section lists what changed, grouped by device,
newest version first. Each group names the repository the changes live in.

For how the system got here, the reasoning and the wrong turns included, see
[History](history.md).

## Unreleased

On `main` since `v03.0`, not tagged yet.

### A³ Motion (`a3-motion-ui`)

**Recording and clips**

- A take is as long as the clip on show; the separate REC tab is gone.
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
- The colour picker is JUCE's own colour field.
- A CLEAN key switches to a clean skin and back.
- Every action script names every parameter it takes, with its range.

**Clock**

- In EXT and PIO the clock sits on the beats it is sent.
- A beat trace, to measure where the time goes between a beat arriving and a clip moving.

**The sphere**

- Rendered twice as fine and drawn back down, so edges no longer step.
- No lag while recording: the line of a take being played in is drawn from what the hand
  moved to, the take underneath is drawn once, and the listener figure is worked out only
  when the view turns.
- The trajectory, the braid and the speaker bolts are drawn in the shader. A speaker's level
  is how thick its bolts run, and a silent room throws none.
- The far side of a trajectory goes behind the sphere again, and the floor no longer cuts
  the blobs in half.

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

### A³ Mixer (`a3-mixer`)

- The tap keys blink with the beat; the bright key carries the cue, and the dim one taps.
- At start the desk asks what is on, so its lamps are right from the first moment.
- One dark display no longer takes the other five with it, and a crashed display process no
  longer looks like a running service. A display's label stays when its script ends.
- A key with no OSC address is ignored rather than stopping the desk.
- The 3D key is out of service; the PFL lamp is no longer inverted twice.

### A³ Motion controller (`a3-motion`)

- The `v03.2` hardware branch is merged into `main`.

### Beat analyzer (`beat-analyzer`)

- The beat clock takes tempo and phase from BTrack's beats and predicts with the measured
  period. The octave lock moved from the tempo range to the clock: one octave, or no lock.
- The mixer's VU goes to port 7772 (was 7771).
- The example `.env` follows the rig's network.

### Documentation (`a3-doc`)

- The user section explains every control on A³ Motion where a performer looks for it; the
  Mixer, the Core and the welcome page follow the same shape, with current pictures.
- The OSC reference lists every path, with send and receive per device, and one page lists
  every port.
- These release notes.

## v03.0 (2026-09-12)

The first version tagged across all repositories at once. From here on `main` is the
integration branch everywhere and versions are tags. The per-hardware-revision branches
(`v03.2`, `dev/v03`) are merged and kept as history.

What came before is told in [History](history.md).
