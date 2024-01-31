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

## crop empty space in images
```
fdisk -l myimage.img

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
```
truncate --size=$[(8800255+1)*512] myimage.img
```

## compress image
```
tar -czvf name-of-archive.tar.gz /path/to/directory-or-file
```

## Flash image to SD-Card on linux
- Make shure to identify the right device. This command overwrite targeting data:
```
sudo dd BS=4M if=path/to/extracted/...img of=/dev/mmcblk0
```

## Resize device images <- wip
```
lsblk
mkdir /mnt/tmp
sudo mount /dev/mmcblk0p2 /mnt/tmp/

df
	/dev/mmcblk0p2  15052456  2033968  12374740  15% /mnt/tmp

sudo umount /mnt/tmp/
e2fsck -f /dev/mmcblk0p2
sudo resize2fs /dev/mmcblk0p2 4G

wip ...

hint:
	
 for part in /dev/loop0p*; do
    mount $part /mnt
    dd if=/dev/zero of=/mnt/filler conv=fsync bs=1M
    rm /mnt/filler
    umount /mnt
 done

```

```
 dd bs=4M if=/dev/mmcblk0 of=/home/ra/images/a3_mic_debian.img
```

```
truncate -s64M file # no need to fill it with zeros, just make it sparse
```

```
N1ete
wenn du ein img hast dann würde ich das mounten mit losetup

und dann würde ich das loop image mit fstrim auf das nötigste minimum shrinken

also irgendwie so:
1.
losetup --find --partscan file.img
2.
lsblk gibt dir dann die partitionen aus vom image

also zum beispiel

loop0       7:0    0   4096M  0 loop 
├─loop0p1 259:0    0   2048M  0 loop 
└─loop0p2 259:1    0   2048M  0 loop 
dann das trimming von ungenutztem platz von allen partitionen

for part in /dev/loop0p*; do
    mount $part /mnt
    fstrim -v /mnt
    umount /mnt
  done
18:04



am ende wieder unmounten mit

losetup --detach /dev/loop0




 for part in /dev/loop0p*; do
    mount $part /mnt
    dd if=/dev/zero of=/mnt/filler conv=fsync bs=1M
    rm /mnt/filler
    umount /mnt
 done
 ```