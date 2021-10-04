# Imaging

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

