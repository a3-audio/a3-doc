# A³ Core

- [A³ Core Repository](https://github.com/a3-audio/a3-core)
- A freely configurable audio server
- Runs on Linux audio hardware; VNC remote desktop control

A³ Core is where the sound actually is. It takes the analog signals in,
computes the 3D/ambisonics field, and sends it back out — and it does all of
that under remote control: **it has no interface of its own.** A³ Mixer and A³
Motion tell it what to do over OSC, and so can anything else that speaks the
same addresses.

It also runs the **Beat-Analyzer**, which produces the tempo the whole system
follows and the VU meters the other two devices show.

![A³ Core numbered](pics_user/a3-core-icon_light_numbered.png)

The numbers below refer to that picture.

## The front panel

Four things, and none of them is a control for the audio — that is all
remote.

| № | Element | What it does |
| :--- | :--- | :--- |
| 1 | **POWER** | switches the device on |
| 2 | **RESET** | reboots the server, just in case |
| 3 | **POWER LED** | says whether it is on |
| 4 | **Fan and filter** | clean it regularly |

## Clock sources

The tempo the system runs on can come from three places, chosen on A³
Motion's clock key:

| Mode | Where the tempo comes from |
| :--- | :--- |
| **a3motion** | relayed from A³ Motion's tap key |
| **intern** | the Beat-Analyzer's own FFT/onset detection |
| **pioneer** | the master beat from Pioneer Pro DJ Link |

## The window

A³ Core has no interface of its own — but it does have a window. Point a
browser at **`http://<core>:9080`** from anywhere on the same network and you
can see what the devices are actually saying to each other.

![The window, showing the traffic](pics_user/a3-core-window.png)

Along the top are the peers, each with a dot that says when it was last heard
from. Below that, one row per OSC address: how often it has gone past, how
fast, the last value, and which device it came from or went to.

This is the answer to *"is it the cable, the setting, or me?"*. OSC runs over
UDP, which has no way of reporting that nobody was listening — a control that
does nothing and a control that is not connected look exactly alike. In the
window they do not.

Two things worth knowing:

- The selector on the right switches between **Verkehr** (what has actually
  gone past) and **Register** (every address the system *can* speak, whether
  it has ever been used or not). Tick *nur tote Drähte* in the register view
  and you are looking at everything that exists and has never arrived.
- The list of addresses survives a restart of Core; the running values and the
  history do not. Nothing here changes anything — it is a window, not a
  control surface.
