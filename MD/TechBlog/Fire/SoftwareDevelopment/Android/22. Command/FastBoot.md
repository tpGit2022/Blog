D:\huawei>fastboot help
usage: fastboot [OPTION...] COMMAND...

flashing:
 update ZIP                 Flash all partitions from an update.zip package.
 flashall                   Flash all partitions from $ANDROID_PRODUCT_OUT.
                            On A/B devices, flashed slot is set as active.
                            Secondary images may be flashed to inactive slot.
 flash PARTITION [FILENAME] Flash given partition, using the image from
                            $ANDROID_PRODUCT_OUT if no filename is given.

basics:
 devices [-l]               List devices in bootloader (-l: with device paths).
 getvar NAME                Display given bootloader variable.
 reboot [bootloader]        Reboot device.

locking/unlocking:
 flashing lock|unlock       Lock/unlock partitions for flashing
 flashing lock_critical|unlock_critical
                            Lock/unlock 'critical' bootloader partitions.
 flashing get_unlock_ability
                            Check whether unlocking is allowed (1) or not(0).

advanced:
 erase PARTITION            Erase a flash partition.
 format[:FS_TYPE[:SIZE]] PARTITION
                            Format a flash partition.
 set_active SLOT            Set the active slot.
 oem [COMMAND...]           Execute OEM-specific command.

boot image:
 boot KERNEL [RAMDISK [SECOND]]
                            Download and boot kernel from RAM.
 flash:raw PARTITION KERNEL [RAMDISK [SECOND]]
                            Create boot image and flash it.
 --cmdline CMDLINE          Override kernel command line.
 --base ADDRESS             Set kernel base address (default: 0x10000000).
 --kernel-offset            Set kernel offset (default: 0x00008000).
 --ramdisk-offset           Set ramdisk offset (default: 0x01000000).
 --tags-offset              Set tags offset (default: 0x00000100).
 --page-size BYTES          Set flash page size (default: 2048).
 --header-version VERSION   Set boot image header version.
 --os-version MAJOR[.MINOR[.PATCH]]
                            Set boot image OS version (default: 0.0.0).
 --os-patch-level YYYY-MM-DD
                            Set boot image OS security patch level.

Android Things:
 stage IN_FILE              Sends given file to stage for the next command.
 get_staged OUT_FILE        Writes data staged by the last command to a file.

options:
 -w                         Wipe userdata.
 -s SERIAL                  Specify a USB device.
 -s tcp|udp:HOST[:PORT]     Specify a network device.
 -S SIZE[K|M|G]             Break into sparse files no larger than SIZE.
 --slot SLOT                Use SLOT; 'all' for both slots, 'other' for
                            non-current slot (default: current active slot).
 --set-active[=SLOT]        Sets the active slot before rebooting.
 --skip-secondary           Don't flash secondary slots in flashall/update.
 --skip-reboot              Don't reboot device after flashing.
 --disable-verity           Sets disable-verity when flashing vbmeta.
 --disable-verification     Sets disable-verification when flashing vbmeta.
 --unbuffered               Don't buffer input or output.
 --verbose, -v              Verbose output.
 --version                  Display version.
 --help, -h                 Show this message.
