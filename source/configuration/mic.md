# A³ Mix Configuration
## Teensy
- [Flash Teensy Firmware](https://doc.a3-audio.com/development/flashTeensy.html)

## Raspberry Pi 3 Model B
- [Flash Device Image](https://doc.a3-audio.com/development/imaging.html)
- microSD card > 8GB

##  From scratch <-wip
### Install Arch Linux ARMv7
- https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-4

### Find Raspberry PI's ip address
```
nmap -sn 192.168.1.0/24
```

### Login
```
ssh alarm@found_ip_address
password: alarm
root password is "root"
```
  
### Root operations
#### Setup user and hostname
```
nano /etc/hostname

passwd root
useradd -m aaa
passwd aaa

groupadd dialout

usermod -aG dialout aaa
usermod -aG users aaa
usermod -aG tty aaa
usermod -aG uucp aaa

userdel alarm
rm -rf /home/alarm
```

#### Install depencies
```
pacman-key --init
pacman-key --populate archlinuxarm
pacman -Syu 
pacman -S python
pacman -S python-pip
pacman -S git
pacman -S libusb
pacman -S libusb-compat
pacman -S vim
pacman -S gcc
pacman -S teensy_loader_cli
pacman -S bash-completion
```

#### Install python virtualenv and modules in virtualenv as user aaa
```
pip install virtualenv
virtualenv -p python3 ~/.a3python_env
source ~/.a3python_env/bin/activate

pip install wheel
pip install numpy 
pip install setuptools
pip install python-osc
pip install pyserial
pip install python-dev-tools
pip install platformio
pip install board
CFLAGS="-fcommon" pip install rpi.gpio
pip install adafruit-circuitpython-neopixel --force-reinstall adafruit-blinka rpi_ws281x
```

#### Clone repo as user aaa
```
git clone git@github.com:ambisonics-audio-association/Ambijockey.git
```

#### Copy Files as root
```
Ambijockey/Controller_Mixer/software/raspberry
└── etc
    ├── environment
    ├── modprobe.d
    │   └── raspi-blacklist.conf
    ├── ?? pip.conf
    └── systemd
        ├── network
        │   └── eth.network
        └── system
            └── mic.service
```

#### Configure services as root
``` 
systemctl start mic.service
systemctl enable mic.service
```

### Old
```
If 'systemctl enable mic' throws an error 'invalid argument'

cd /etc/systemd/system/multi-user.target.wants
ln -s /etc/systemd/system/mic.service

?? nano /boot/config.txt
??	max_usb_current=1

?? groupadd gpio
?? chown root.gpio /dev/gpiomem
?? chmod g+rw /dev/gpiomem
?? usermod -aG gpio aaa
```