(core-services)=

# A³ Core services

## How they hang together

`systemd --user` units under the umbrella **`a3-main.service`** (oneshot,
`/bin/true`, `RemainAfterExit=yes`). It *wants* the components; each is
`PartOf=a3-main.service`.

- **Start** `a3-main`: starts `a3-engine`, `a3-core`, `a3-core-window`,
  `beat-analyzer`, `a3-motion`, StemDeck's deck A. (`qjackctl` and `a3-reaper`
  were in the list until REAPER and the patchbay were removed, {ref}`see below <core-engine-units>`.)
- **Stop/restart** `a3-main`: stops/restarts all its parts. The audio server is not one of them: PipeWire belongs to the user session and runs whether `a3-main` does or not.
- **One component** can stop or fail alone: `Wants=`, not `Requires=` (which
  made `stop a3-core` take the others down too).
- `a3-motion` is not shipped here; where Motion has its own machine the name
  matches nothing, harmlessly.

```text
pipewire + wireplumber  (the user session's audio server, JACK via libjack)
 ├─ a3-core          (the core role of the a3-core program)
 ├─ a3-engine        (the engine role; waits until JACK accepts clients)
 ├─ beat-analyzer    (the beat clock only)
 └─ a3-aes67         (only with an audio socket)
```

```sh
systemctl --user start a3-main          # the whole group
systemctl --user restart a3-engine      # one component
systemctl --user status a3-core
journalctl --user -u a3-core -f
```

(core-units-one-place)=

## Where the units live

Every A³ user unit ships in a package under **`/usr/lib/systemd/user/`**, each
unit once. **`~/.config/systemd/user/` holds only this machine's own
drop-ins.** (Until 2026-10-31 the deployment copied its units into `~/.config`,
where they hid the packaged ones.)

| Unit or drop-in | Package | Enabled by |
| :--- | :--- | :--- |
| `a3-engine.service` | `a3-core-app` | the postinst, for every user |
| `a3-core.service` | `a3-core-app` | nothing: `a3-main` wants it |
| `a3-core-window.service` | `a3-core-app` | nothing: `a3-main` wants it |
| `a3-clock.service` | `a3-core-app` | the postinst, with an audio socket |
| `a3-main.service` | `a3-core` | the postinst |
| `a3-bar-per-workspace.service` | `a3-core` | the postinst |
| `a3-aes67.service` | `a3-core` | the postinst, with an audio socket |
| `a3-screencast.service` | `a3-core` | each machine by hand |
| `beat-analyzer.service.d/a3-core.conf` | `a3-core` | drop-in on the analyzer's own unit |
| `stemdeck.service.d/a3-core.conf`, `two-deck-off.conf` | `a3-core` | drop-ins on StemDeck's own unit |

An update replaces the files in `/usr/lib`; don't edit them.

### Changing one line on this machine

Write a drop-in with only that line, then reload:

```sh
systemctl --user edit a3-core      # opens ~/.config/systemd/user/a3-core.service.d/override.conf
systemctl --user daemon-reload     # when you wrote the file by hand instead
systemctl --user cat a3-core       # what runs: the unit, then every drop-in
```

```ini
# ~/.config/systemd/user/a3-core.service.d/bench.conf
[Service]
ExecStart=
ExecStart=/usr/bin/a3-core --role core --print-osc
```

- `ExecStart=` needs the empty line first; most other settings simply replace
  the unit's value.
- Drop-ins apply in file-name order, from `/usr/lib` and `~/.config` together.
  One in `~/.config` with **the same file name** as a packaged one replaces it.
- Never copy a whole unit into `~/.config`: it hides every later change the
  package makes to it.

### What the upgrade does with old copies

The postinst (step 9 of {ref}`the installation <core-postinst>`) looks at
every unit and drop-in in `~/.config/systemd/user/` that an earlier version
put there:

- **unchanged** (its checksum is one the package once shipped) → renamed to
  `<name>.before-one-place`, never deleted; a `default.target.wants` link that
  pointed at it now points at `/usr/lib/systemd/user/<name>`, so what was
  enabled stays enabled;
- **changed by hand** → left in place and named in the output
  (`kept the hand-changed …`). It still hides the package's unit: move it aside
  and put the one changed line into a drop-in;
- a drop-in in `a3-core.service.d/` that still starts the old Core script
  `a3-core.py` → moved to `~/.config/a3-replaced/<date_time>/`.

Everything else in `~/.config/systemd/user/` is left alone.

## User units at a glance

RT = `CPUSchedulingPolicy=rr` at that priority; CPUs 1–3 =
`CPUAffinity=1 2 3`, keeping CPU 0 free.

CPU 0 is where the screen lives: x11vnc (`x11vnc.service.d/cpu.conf`) and Xorg
(`~/.xserverrc`, installed by the package, runs the server under `taskset -c 0`)
are pinned there. With a VNC client connected Xorg took most of CPU 1 on the rig
(2026-10-17). Only the X server is pinned, not the login session, so i3 and the
programs it starts keep their own CPUs.

| Unit | Starts | Part of `a3-main` | After | Restarts | Scheduling |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `a3-main` | the umbrella | — | `graphical.target` | — | — |
| `a3-engine` | `a3-core --role engine` | yes | PipeWire | on failure, 1 s (5 in 60 s) | normal, CPUs 1–3; audio threads RT by the preload below |
| `a3-core` | `a3-core --role core` | yes | PipeWire | no | normal, every CPU |
| `beat-analyzer` | the beat clock | yes | PipeWire | no | RT 65, CPUs 1–3 |
| `a3-screencast` | `a3-core --role screencast-fanout` and ffmpeg | no (each machine opts in) | `graphical.target` | always, 2 s | encoder niced, one core |
| `a3-aes67` | AES67 sender, PTP clock reading | no | PipeWire | always, 2 s | PipeWire's own |
| `a3-bar-per-workspace` | `a3-core --role i3-bar`: i3bar on/off | no | `graphical.target` | always, 2 s | normal |

`a3-main`, `a3-aes67` and `a3-bar-per-workspace` are enabled by the postinst
and start at login; `a3-screencast` waits until a machine enables it. The window
(`a3-core-window`, the `a3-core` program with a screen) has no `[Install]`:
`a3-main` wants it.

## PipeWire — the audio server

`jackd` and `a3-jack.service` are gone (2026-10-14): **PipeWire** with
wireplumber is the audio server, and JACK programs use PipeWire's `libjack`,
system-wide through `/etc/ld.so.conf.d/pipewire-jack-x86_64-linux-gnu.conf`.
The Scarlett (pro-audio profile) drives the graph. Shipped settings under
`~/.config/pipewire/`:

- `pipewire.conf.d/10-a3-rate.conf`: 44.1 kHz only, quantum 128 (2.9 ms),
  never lower: the AES67 nodes would otherwise pull the graph down to 32
  samples.
- `jack.conf.d/10-a3.conf`: the default device answers as the JACK client
  `system`, so the engine's `system:playback_N` and `system:capture_N` stay.

Look at it with `wpctl status` and `pw-top`; the JACK tools
(`jack_lsp`, `jack_connect`) talk to PipeWire.

(core-engine-units)=

## `a3-engine.service` — the audio engine

The engine ({doc}`user page <../user/audio-engine>`) makes the sound. The unit
keeps the name of the role: `a3-engine.service` is shipped in
`/usr/lib/systemd/user/` and runs `/usr/bin/a3-core --role engine` after
`jack_wait -w`. Its JACK client is `a3-engine` too.

- **No `Conflicts=` and no condition.** The engine always starts; there is no
  fallback. It restarts after 1 s on failure, five times in a minute, then stops
  visibly.
- **The old two-deck StemDeck stays off through a drop-in**:
  `stemdeck.service.d/two-deck-off.conf` has `ExecCondition=/bin/false`. A
  failing `ExecCondition` only *skips* a unit, it is not a failure. (No
  `Conflicts=`: a conflict dropped start jobs.) `stemdeck@.service`, the
  B-format decks, runs unconditioned.
- **REAPER, its units and QjackCtl are gone.** The upgrade moves a machine's old
  `a3-reaper`, `qjackctl` and `a3-user-install` units and the patchbay aside
  ({ref}`step 9 <core-postinst>`). The engine makes its own JACK links
  ({ref}`the I/O map <audio-engine-io>`).
- The audio threads get their real-time priority from a preload shim
  (`libjack-rt-priority.so`), not from the unit: raising the whole process would
  put its GUI and OSC threads above JACK's.

```sh
systemctl --user status a3-engine
journalctl --user -u a3-engine -f
a3-core --role engine --check-config      # ok, or the reason
```

(core-silent-start)=

### The silent start

Main, booth and phones are **closed** (exact silence) from the start of the
engine until Core has replayed the evening and sent `/engine/open 1`; then each
output ramps up to its trim over 1 s. This is the engine's gate
({doc}`The audio engine <../user/audio-engine>`).

- **Silent after a start:** Core is not up, or the engine restarted alone and has
  not been told yet. Restarting `a3-core` is enough once the engine runs.
- **Rec stays open**, so the beat analyzer has its input.

```sh
journalctl --user -u a3-core | grep 'gate:'
```

## `a3-core.service` — the core role

`/usr/bin/a3-core --role core`, private `/tmp`. It takes commands on `core.osc`, relays state and the engine's meters to
every subscriber, and serves the HTTP API on `core.web`
({ref}`Core's HTTP API <osc-http>`). **No Python.**

- **One unit for every machine**, `a3-core-app`'s, in `/usr/lib/systemd/user/`.
  The `program.conf` and `cpu.conf` drop-ins that switched the deployment's old
  copy over are gone; the upgrade moves them aside ({ref}`above <core-units-one-place>`).
- **Every CPU**: the unit sets no `CPUAffinity`. Pinned to CPU 0, Core starved
  whenever the Motion UI peaked there, and OSC was dropped.
- **Needs the truth**: `/usr/share/a3/a3-osc.json` (or `$A3_OSC_TRUTH`), joined
  with `network.json`, served on `core.web`, announced every 2 s
  ({ref}`truth <osc-truth>`).
- No `Restart=`; a stop with SIGTERM writes the state files first.

### Its arguments

None by default; a drop-in can point any default elsewhere (useful on a bench).

| Argument | Default / meaning |
| :--- | :--- |
| `--ip`, `--port` | the truth's `any`, `core.osc` |
| `--mixer HOST:PORT`, `--motion HOST:PORT` | their `osc` listeners |
| `--subscriber NAME=HOST:PORT` | another department; repeatable |
| `--web-bind HOST:PORT` | `core.web`, every interface. The API can send OSC with no login; bind locally to keep it to the machine |
| `--no-web` | no HTTP API |
| `--print-osc` | log every message (off: 300,000 lines an hour on one address) |

(core-subscriber)=

### Adding a department

A department is a light or video desk that gets every A³ message exactly as
Mixer and Motion do. What arrives: {doc}`OSC reference <../ressources/osc>`.

**The normal way is the window**: page **DEPARTMENTS**, **ADD**, then name,
host (an IPv4 address or a host name) and port, **SAVE LIST**. Core applies the
list at once, no restart; each row says whether messages go out (how many, the
last how long ago). An entry is checked as you type and Core checks that the
host resolves, so a wrong one is never saved — and never stops Core. The list
is Core's own config, `~/.config/a3/core/departments.json`, outside the
package.

The alternative is a drop-in, one argument each:

```
ExecStart=
ExecStart=/usr/bin/a3-core --role core \
          --subscriber light=HOST:PORT \
          --subscriber video=HOST:PORT
```

These show in the window as *service file, read-only*. **An unparsable
subscriber stops Core from starting** — better than a desk that silently hears
nothing. **A name in both: the drop-in wins**; the window keeps its entry,
marks it *not used*, and Core sends only to the drop-in's address.

### What it keeps across a restart

`~/.local/state/a3-core/` (or `$XDG_STATE_HOME/a3-core/`): `state.json` (what
only Core knows), `evening.json` (every continuous value passed on) and
`seen.json` (the list of addresses the OSC monitor has seen). Outside the
package; updates don't touch them.

## `beat-analyzer.service` — the beat clock

`~/a3-system/beat-analyzer/build/beat-analyzer`, `Type=idle`, 3 s after start,
configured by `build/.env` (OSC targets in the [rendered block](#core-postinst),
the rest {ref}`its own <beat-analyzer-config>`). Sends `/beat` to Core, the
controllers and `radla`. **It is the beat clock only**: it sends no `/vu`
(the engine measures the meters).

## `a3-screencast.service` — the screen as a stream

`a3-screencast` runs ffmpeg on the CPU (never VAAPI, which hung in a GPU reset
on the rig) niced and on one core the audio units leave free, writing MPEG-TS to
`a3-core --role screencast-fanout`, which copies it to every viewer; the encoder
starts with the first viewer and stops 10 s after the last. No sound (OBS takes it from
AES67). The port is the truth's, from `~/.config/a3/osc.env`; encoder settings
(`A3_SCREENCAST_CPUS`, `_FPS`, `_CRF`) in the optional
`~/.config/a3/screencast.env`. The package does not enable it: each machine
opts in.

(core-aes67)=

## `a3-aes67.service` and `ptp4l` — the audio network

Only on a Core with a second socket ({ref}`install <core-postinst>`,
`audio-port`); otherwise `a3-aes67` has no config and does not start.

- `ptp4l@<socket>.service` (linuxptp, system unit, enabled by the postinst):
  the PTP clock on the second socket. The Core is master unless a better
  clock is on the network.
- `a3-aes67.service` (user unit): a second PipeWire instance running
  `~/.config/pipewire/pipewire-aes67.conf`, rendered by `a3-core --render-truth` from
  the truth's `network.audio_port`. It sends the Core's 12 channels as the
  multicast stream `AES67 <hostname> out` (44.1 kHz, 24 bit, packet time
  0.5 ms), announces it by SAP and receives the streams of other machines.
  The Scarlett drives it, not the PTP clock, so the samples go out
  unconverted. Restarts 2 s after any exit.

Network and streams: {ref}`ports <ports-audio-network>`; the cabling is the
engine's ({ref}`the I/O map <audio-engine-io>`).

## The engine and the realtime priority

pipewire-jack answers a program's question for the audio threads' priority
wrongly. `a3-engine.service` therefore preloads a small shim,
`~/.local/lib/a3/libjack-rt-priority.so` (built by the postinst from
`~/.local/share/a3-core/src/jack-rt-priority.c`). The unit sets no
`CPUScheduling`: raising the whole process puts its GUI and OSC threads above
the audio threads.

## `a3-bar-per-workspace.service` — i3bar on the tool workspaces

`a3-core --role i3-bar` on `:0`, after `/usr/lib/a3-core/a3-wait-for-the-screen`. Shows the
bar on workspace 3 and up, hides it on 1 and 2 ([The screen](#core-config-screen));
restarts whenever it ends (an i3 restart ends the event stream).

(core-system-units)=

## System units

In `/etc/systemd/system/`, dpkg conffiles.

| Unit | What it does | Enabled |
| :--- | :--- | :--- |
| `x11vnc.service` | `x11vnc` as `aaa` on `:0`, 5 s after `graphical.target`, `-shared -forever`, restart on failure; CPU 0 only (`x11vnc.service.d/cpu.conf`); port on its command line, not in `a3-osc.json` | yes |
| `set_irq_prio.service` | at boot, the USB controller's IRQ threads (`irq/…-xhci_hcd`) to FIFO 95, so the sound card comes first | yes |
| `vnc-display.service` | `recipes/vnc-display.sh`: a monitor on HDMI/DP moves `10-headless.conf` aside to `.bak`, none moves it back | no, shipped only |

Debian's own: the postinst
enables `systemd-networkd` (when configuring the network); LightDM logs `aaa`
into i3 ([Under /etc](#core-etc)).
