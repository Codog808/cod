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
- USING FDISK
    - fdisk -l (lists the disks and partitions of a drive)
    - fdisk /dev/<disk>
        - Within fdisk enter 'm' to get a list of commands
            - 't': choose made partition to make the type
            - 'n': make a new partition
            - 'w': write the changes within fdisk to the disk.
        - UEFI with GPT
            - mount: /mnt/boot; partition: /dev/<name>; type: EFI system partition (1); size: 300MiB (+300M)
            - mount: /mnt; partition: /dev/<name>; type: Linux x86_64 (23); size: default (enter 2x)
            - mount: [swap]; partition: /dev/<name>; type: Linux swap (19); size: <=512MiB (+512M)
        - Boot with MBR
            - mount: [swap]; partition: /dev/<name>; type: Linux swap (19); size: <=512MiB (+512M)
            - mount: /mnt; partition: /dev/<name>; type: Linux x86_64 (23); size: default (enter 2x)
format partitions; setting a filesytem to a partition
- mkfs.ext4 /dev/<root partition> 
- mkswap /dev/<swap partition>
- if you are creating a NEW EFI system partition
    - WARNING: mkfs.fat -F 32 /dev/<efi system partition>
mounting file systems
- mount /dev/<root partition> /mnt
- swapon /dev/<swap partition>
- if EFI boot
    - mount --mkdir /dev/efi system partition /mnt/boot; or, mkdir /mnt/boot && <command without --mkdir>
Installation
- pacstrap -K /mnt base linux linux-firmware
    - IF verification of files displays an error, for instance "Leonidas Syncopi is not a trusted author" do teh following
        - pacman-key --init; (grab new keys)
        - pacman-key --populate archlinux; (push new keys to the arch environment, updating the packages)
        - (MAYBE) pacman -Sy archlinux-keyring; if in pacstrap environment then skip
Configure system
- Fstab
    - genfstab -U /mnt >> /mnt/etc/fstab
- Chroot
    - arch-chroot /mnt; enter the linux environment
    --- input more later ---  12/10/23
    *** systemd is not set up during installation process, must ls files containing the information needed. ***
    - Set Time Zone
        - ls /usr/share/zoneinfo/AREA/; substitute America for AREA if you live are in America
        - ln -sf /usr/share/zoneinfo/AREA/TIMEZONE /etc/localtime; TIMEZONE could be Los_Angeles
    --- input more later --- 12/11/23



