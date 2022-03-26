# A³ Motion Configuration
## Teensy
- [Flash Teensy Firmware](https://doc.a3-audio.com/development/flashTeensy.html) 

## Raspberry Pi 3 Model B
- [Flash Device Image](https://doc.a3-audio.com/development/imaging.html)
- microSD card > 4GB

##  Install Raspberry PI from scratch <-wip
### install aarch64
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
```
nano /etc/hostname

pacman -Syu

groupadd dialout

usermod -aG dialout aaa
usermod -aG users aaa
usermod -aG tty aaa
usermod -aG uucp aaa
usermod -aG video aaa
usermod -aG input aaa
passwd root
useradd -m aaa
passwd aaa

reboot and log in as aaa
su
userdel alarm
```

#### Install depencies:
```
pacman-key --init
pacman-key --populate archlinuxarm
pacman -Syu
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

#### Copy files to corresponding system-folder:
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
sudo systemctl enable getty@tty2
sudo systemctl enable moc
``` 

#### Setup static ip-address:
``` 
vim /etc/systemd/network/eth0.config
``` 

#### Edit the Raspberry config-file
```
nano /boot/config.txt
display_rotate=1
dtoverlay=pi3-disable-bt
```