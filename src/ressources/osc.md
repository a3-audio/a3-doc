# OSC communication
## A³ Core

| RECEIVE | SEND | DATA TYPE | DATA | DESCRIPTION
| :---| :--- | :--- | :--- | :---
| - | /vu/[0-11] | float (peak), float (rms) | [0-1], [0-1] | Peak and rms vu meter
| - | /channel/pfl/led/[0-3] | bool | [0 or 1] | pfl status
| - | /channel/fx/led/[0-3] | bool | [0 or 1] | fx status
| - | /channel/3d/led/[0-3] | bool | [0 or 1] | 3d status
| - | /fx/led | string | [high_pass, low_pass] | fx mode status
| /channel/[0-3]/gain | - | float | [0-1] | Channel gain
| /channel/[0-3]/eq/high | - | float | [0-1] | Channel eq high
| /channel/[0-3]/eq/mid | - | float | [0-1] | Channel eq mid
| /channel/[0-3]/eq/low | - | float | [0-1] | Channel eq low
| /channel/[0-3]/volume | - | float | [0-1] | Channel volume
| /channel/[0-3]/reverb | - | float | [0-1] | Channel reverb
| /channel/[0-3]/pfl | - | bool | [0 or 1] | Channel pfl
| /channel/[0-3]/fx | - | bool | [0 or 1] | Channel fx
| /channel/[0-3]/3d | - | bool | [0 or 1] | Channel 3d
| /channel/[0-3]/azimuth | - | float | [-180-180] | ambisonic azimuth
| /channel/[0-3]/elevation | - | float | [0-1] | ambisonic elevation
| /channel/[0-3]/width | - | float | [0-1] | ambisonic stereo width
| /channel/[0-3]/order | - | float | [0-1] | ambisonic order
| /master/volume | - | float | [0-1] | Master volume
| /master/booth | - | float | [0-1] | Booth volume
| /master/phones_mix | - | float | [0-1] | Phones mix
| /master/phones_volume | - | float | [0-1] | Phones volume
| /fx/mode | - | string | [high_pass, low_pass] | Global fx mode
| /fx/frequency | - | float | [0-1] | fx filter frequency
| /fx/resonance | - | float | [0-1] | fx filter resonance

## A³ Motion

A³ Motion listens on three UDP ports (configurable in the UI's `config/config.json`,
`oscReceiver`): the main port (default 7771), a separate VU port (default 7772), and an energy
port (default 7777), so neither the high-rate VU stream nor the energy grid shares a socket with
the beat clock. All three are served by the same handler, so the split is a convention, not a
restriction.

| RECEIVE | SEND | DATA TYPE | DATA | DESCRIPTION
| :---| :--- | :--- | :--- | :---
| /vu/[0-3] | - | float (peak), float (rms) | [0-1], [0-1] | Audio channels 1-4 — drives the corona around each channel blob
| /vu/4 | - | float (peak), float (rms) | [0-1], [0-1] | Subwoofer — drives the sphere glow
| /vu/[5-8] | - | float (peak), float (rms) | [0-1], [0-1] | Speakers 1-4 — drives the speaker spotlights
| /vu/[9-11] | - | float (peak), float (rms) | [0-1], [0-1] | Received but unused — silently discarded
| /EnergyVisualizer/RMS | - | 426 × float | [0-1] each | Energy arriving from each direction, one value per point of the IEM EnergyVisualizer's sphere — lights the sphere itself. Port 7777.
| - | /channel/[0-3]/3d | float | [0-1] | How far the channel is spread into the 3D field, from its pot. Core crossfades the channel's stereo and multi encoder on it. |
| /beat | - | int (beat), int (bar), int (bpm) | [1-4], [-], [-] | External beat clock. Always updates the status bar readout; in EXT/PIO clock mode it also syncs playback tempo and phase. Float arguments are accepted and truncated to int.

```{note}
Every address in this section is a **default**, not a fixed part of the protocol. A³ Motion reads
them from the `oscAddresses` block of its `config/config.json`, and they can be edited on the
device under Menu → Network. `{ch}` there stands for the channel number.

The block is grouped into `out` (to Core and IEM), `in` (VU and energy) and `beatclock`. The beat
clock is neither: `beat` is *sent* in INT clock mode and *received* in EXT, one address either way.

Changing one changes only A³ Motion's side of the conversation — the peer has to be changed to
match. A mismatch does not report itself: the message is sent correctly, to an address nobody is
listening for.
```

The index ranges above exist only in A³ Motion — senders do not carry that meaning. The
`beat-analyzer`, for instance, simply emits `NUM_VU_CHANNELS` (default 12) meters, one per JACK
input, in port order. Which physical signal ends up on which index is decided by the JACK patching
alone, and changing that wiring changes what the UI shows with nothing to warn you.

Note the base mismatch when patching: the analyzer's JACK ports are 1-based (`vu_1` … `vu_12`)
while the OSC addresses are 0-based, so **`vu_N` arrives as `/vu/(N-1)`**. In the A³ setup the
speakers therefore sit on ports `vu_6`..`vu_9`, not `vu_5`..`vu_8`:

| JACK port | OSC address | Signal |
| :--- | :--- | :--- |
| vu_1 .. vu_4 | /vu/0 .. /vu/3 | Mixer channels 1-4 |
| vu_5 | /vu/4 | Subwoofer |
| vu_6 .. vu_9 | /vu/5 .. /vu/8 | Speakers 1-4 |
| vu_10 .. vu_12 | /vu/9 .. /vu/11 | currently unused |

Levels may still arrive on the unused indices if something is patched to those ports; that is not
a sign they are being evaluated.

### /channel/[0-3]/3d

A third per-channel value beside `pot_1` and `pot_2`, sent whenever the channel's potentiometer
moves. In `a3-core.py` it crossfades the channel between its stereo encoder and its multi encoder
(REAPER FX 1, parameters 1 and 15 on one, parameter 1 on the other).

**This address used to be a toggle**, flipping `toggle_3d` on the value 1 and reporting an LED
state back to A³ Mixer. That boolean now lives on `/channel/[0-3]/4d`. The Mixer button that sent
it is gone in hardware v3.2, so nothing sends the boolean today.

### /EnergyVisualizer/RMS

Sent by the [IEM EnergyVisualizer](https://plugins.iem.at/docs/energyvisualizergrid/) from version
1.0.0 on, once its "OSC send" is switched on in the lower left of the plug-in. One message carries
**426 float32 arguments**, one per point of the plug-in's own sphere grid, in the plug-in's order —
roughly 9 messages a second. Values are linear, not dB.

Which direction each index stands for comes from the plug-in's coordinate file, mirrored in the
A³ Motion UI as `resources/EnergyVisualizerGrid.json`. A message of any other length is discarded
rather than partly applied, because a short one would leave the rest of the map holding energy that
is no longer there.

Unlike the VU meters, this carries **elevation** as well as azimuth: it is the ambisonic field
itself rather than a per-loudspeaker level.

## IP and Port

Ports are configurable per device; these are the defaults that ship.

| Component | Listens on | Sends to |
| :--- | :--- | :--- |
| A³ Core | 9000 | REAPER `127.0.0.1:9001`, IEM plugins `127.0.0.1:1337+n` |
| A³ Mixer | 7771 | A³ Core `:9000` |
| A³ Motion | 7771 control, 7772 VU, 7777 energy grid | A³ Core `:9000`, beat-analyzer `:7775` |
| Beat-Analyzer | 7775, Pioneer Pro DJ Link 50000-50002 | A³ Core, A³ Motion, A³ Mixer |

### Known inconsistencies

Worth knowing before chasing a silent link. These are recorded rather than fixed
because each needs a decision about which end is right:

- `a3-core.py` addresses its peers by **hardcoded IP** (`192.168.43.54`, `.55`), and
  `a3-mixer.py` does the same for the core (`192.168.43.50`). A system on a different
  subnet has those links dead with nothing to indicate it.
- `a3-core.py` sends to A³ Motion on port **8700**, while the A³ Motion UI listens on
  **7771**.
- `beat-analyzer` is configured to reach the mixer on **7773/7774**, while
  `a3-mixer.py` listens on **7771**.
