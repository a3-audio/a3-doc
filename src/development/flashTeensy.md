## Teensy Firmware
https://docs.platformio.org/en/latest/core/installation.html#system-requirements

### On Raspberry PI
### teensy_loader_cli
```
mkdir packages && cd packages
git clone git@github.com:PaulStoffregen/teensy_loader_cli.git
cd teensy_loader_cli
make
sudo cp teensy_loader_cli /usr/bin/
```
### Platformio
```
pip install virtualenv
virtualenv -p python3 ~/.platformio/penv
source ~/.platformio/penv/bin/activate
pip install platformio
pio boards
cd project
pio project init --board teensy41
pio run --target upload
```

