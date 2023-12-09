# Installation guide
localectl list-keymaps
- loadkeys us (defaulted to that)
cat /sys/firmware/efi/fw_platform_size
- 64 (booted in uefi mode, 64 bit x64)
- 32 (32 bit version IA32)
ip link
- displays if your connection to the internet is up
- ping archlinux.org (check if dns up and connection up is true)
timedatectl
- make sure that the clock is true
fdisk -l
- disks are assigned to blocked devices
     - /dev/sda, /dev/nvme0n1, /dev/mmcblk0
- results ending in rom, loop, or airoot to be ignored
     - mmcblk* devices ending in rpbm, boot0, and boot1 can be ignored
- required partitions
    - / (root directory)
    - EFI system partition (boot directory)
