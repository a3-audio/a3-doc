# A³ Mix Configuration
## Teensy
- [Flash Teensy Firmware](https://doc.a3-audio.com/development/flashTeensy.html)

## Raspberry Pi 4
- [Flash Device Image](https://doc.a3-audio.com/development/imaging.html)
- microSD card > 4GB

##  Install Raspberry PI from scratch <-wip
### Install Arch Linux Arm
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
  
### Root operations on the Raspberry: 
#### Setup user and hostname
```
nano /etc/hostname

useradd -m aaa
passwd aaa

groupadd dialout

groupadd gpio
chown root.gpio /dev/gpiochip0
chmod g+rw /dev/gpiochip0

usermod -aG gpio aaa
usermod -aG dialout aaa
usermod -aG users aaa
usermod -aG tty aaa
usermod -aG uucp aaa


passwd root
passwd aaa
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

pacman -S gpio-utils
```
#### Copy Files
```
Controller_Mixer/software/raspberry
└── etc
    ├── environment
    ├── modprobe.d
    │   └── raspi-blacklist.conf
    ├── pip.conf
    └── systemd
        ├── network
        │   └── eth.network
        └── system
            └── mic.service
```

### As user aaa
#### Install python
```
pip install numpy 
pip install setuptools
pip install python-osc
pip install pyserial
pip install wheel
pip install python-dev-tools
pip install platformio
pip install board

CFLAGS="-fcommon" pip install rpi.gpio
pip install adafruit-circuitpython-neopixel --force-reinstall adafruit-blinka rpi_ws281x 

?? process
```

#### Clone repo
```
git clone git@github.com:ambisonics-audio-association/Ambijockey.git
```

### As user root
#### Configure services
``` 
?? nano /boot/config.txt
??	max_usb_current=1

systemctl start mic.service
systemctl enable mic.service
  if 'systemctl enable mic.service' throws an error 'invalid argument'
    cd /etc/systemd/system/multi-user.target.wants
    ln -s /etc/systemd/system/mic.service

Edit /etc/dhcpcd.conf
  interface eth0
  static ip_address=192.168.43.51/24
  static routers=192.168.43.1
  static domain_name_servers=192.168.43.1 8.8.8.8
```

## Early versions
### 2020-2021
### Raspbian
[Install Raspbian](https://www.raspberrypi.org/documentation/computers/getting-started.html)

1. put an empty file 'ssh' on Raspbian boot-partition, this enables ssh
2. search for your Raspberry ip-address ie: nmap -sn 192.168.1.0/24
3. ssh pi@192.168.1.x (pass= raspberry) 

#### Root operations on the Raspberry: 
```
apt update
apt upgrade

useradd -m aaa
passwd aaa

usermod -aG dialout aaa
usermod -aG users aaa
usermod -aG tty aaa
usermod -aG uucp aaa
```
#### Install depencies
```
apt install python python-osc python-pip git python3-numpy

pip install numpy process pyserial python-osc rpi_ws281x adafruit-circuitpython-neopixel --force-reinstall adafruit-blinka

apt purge bluez pi-bluetooth

exit

ssh aaa@192.168.1.x
userdel pi

```
#### Clone repository:
```
cd /home/aaa
git clone git@github.com:ambisonics-audio-association/Ambijockey.git
```
#### Copy files to corresponding system-folder:
```
ControllerMixer/software/raspberry
   └── config
       └── etc
           ├── dhcpcd.conf
           └── systemd
               └── system
                   └── mic.service
```
#### Configure the Raspberry:
``` 
raspi-config
	3 Interface Options > P8 Remote GPIO > yes

nano /boot/config.txt
	max_usb_current=1

nano /boot/cmdline.txt
	logo.nologo (to the end of line)

nano .bashrc
	export PATH="/home/aaa/.local/bin:$PATH"

``` 
#### Setup service:
``` 
systemctl start mic.service
systemctl enable mic.service
  if 'systemctl enable mic.service' throws an error 'invalid argument'
    cd /etc/systemd/system/multi-user.target.wants
    sudo ln -s /etc/systemd/system/mic.service
``` 
#### Setup static ip-address
``` 
mv /etc/dhcpcd.conf /etc/dhcpcd.conf.bck
touch /etc/dhcpcd.conf
Edit /etc/dhcpcd.conf
  interface eth0
  static ip_address=192.168.43.51/24
  static routers=192.168.43.1
  static domain_name_servers=192.168.43.1 8.8.8.8
```
#### Not sure if we still need "fix for Raspberry random hold":
```
nano /etc/sysctl.conf
    vm.dirty_background_ratio = 5
    vm.dirty_ratio = 10
```
