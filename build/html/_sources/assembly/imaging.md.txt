# Imaging

Work in progress snippets to build and restore deviceimages

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