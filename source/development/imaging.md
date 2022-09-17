# A³ Device Images
## Download images
- [device images](https://cloud.a3-audio.com/d/744da83d0f994de9bc76)

## Unpack image on linux
```
tar -xf path/to/...img.tar.gz
```

## Find device on linux
- Find the device name you want to apply the image on. Note that the name could be different on your system. In this example my sdcard is shown:
```
lsblk

NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
mmcblk0     179:0    0  59.6G  0 disk
```

## Flash image to SD-Card on linux
- Make shure to identify the right device. This command overwrite targeting data:
```
sudo dd BS=4M if=path/to/extracted/...img of=/dev/mmcblk0
```

## mount image to loop device
```
sudo modprobe loop
sudo losetup -f
sudo losetup /dev/loop0 myimage.img
sudo partprobe /dev/loop0
```
Release loop device:
```
sudo losetup -d /dev/loop0
```

## Show image info
```
fdisk -l path_to_image.img

Disk /home/aaa/a3motion_aarch64.img: 59.63 GiB, 64021856256 bytes, 125042688 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x030c2c18

Device                             Start    End      Sectors  Size Id Type
/home/aaa/a3motion_aarch64.img1    2048     411647   409600   200M  c W95 FAT32 (LBA)
/home/aaa/a3motion_aarch64.img2    411648   8800255  8388608  4G  	83 Linux
```

## Resize partition on image
```
as root:

losetup /dev/loop10 path_to_image.img
gparted /dev/loop10p2
 ```

## crop empty space in images
```
truncate --size=$[(8800255+1)*512] myimage.img
```

## compress image
```
tar -czvf name-of-archive.tar.gz /path/to/directory-or-file
```