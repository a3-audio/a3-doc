# Imaging partitions

```
lsblk
e2fsck -f /dev/mmcblk0p2
resize2fs -p /dev/mmcblk0p2 4G

dd if=/dev/mmcblk0 of=test.iso
```