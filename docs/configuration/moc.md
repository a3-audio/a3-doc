# A³ Motion Configuration
## Teensy
- [Flash Teensy Firmware](https://doc.a3-audio.com/development/flashTeensy.html) 

## Raspberry Pi 3 Model B
- [Flash Device Image](https://doc.a3-audio.com/development/imaging.html)
- microSD card > 4GB

##  From scratch <-wip
### install AArch64
- https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-3

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

### Root operations on raspberry
#### User and hostname
```
nano /etc/hostname

passwd root
useradd -m aaa
passwd aaa

groupadd dialout
usermod -aG wheel aaa
usermod -aG dialout aaa
usermod -aG users aaa
usermod -aG tty aaa
usermod -aG uucp aaa
usermod -aG video aaa
usermod -aG input aaa

userdel alarm
rm -rf /home/alarm
```

#### Install depencies:
```
pacman-key --init
pacman-key --populate archlinuxarm
pacman -Syu
pacman -S sudo
pacman -S git
pacman -S qt6-tools
pacman -S python-opengl
pacman -S qt6-svg
pacman -S pyside6
pacman -S xorg-xinit
pacman -S xorg-server
pacman -S xorg-xrandr
pacman -S xorg-xinput
pacman -S ttf-dejavu
pacman -S bash-completion
pacman -S python-pip 
pacman -S tree vim i3-wm dmenu sudo
pacman -S teensy_loader_cli
``` 

### User aaa operations
#### Clone repo
```
su aaa
cd /home/aaa
git clone git@github.com:ambisonics-audio-association/Ambijockey.git
cd Ambijockey/Controller_Motion/software/
git clone git@github.com:ambisonics-audio-association/MotionControllerUI.git
``` 

#### Python
```
cd Ambijockey/Controller_Motion/software/MotionControllerUI/
python -m pip install -r requirements.txt
```

### Root operations
#### Copy files
```
/ControllerMotion/software/raspberry

|-- boot
|   |-- cmdline.txt
|   `-- config.txt
|-- etc
|   |-- X11
|   |   `-- Xwrapper.config
|   |-- sudoers
|   `-- systemd
|       |-- getty@tty2.service.d
|       |   `-- override.conf
|       |-- network
|       |   `-- eth0.network
|       `-- system
|           `-- moc.service
|-- home
|   `-- aaa
|       `-- .xinitrc
`-- moc_splash.png
```

#### Enable services:
``` 
systemctl enable getty@tty2
systemctl enable moc
```
