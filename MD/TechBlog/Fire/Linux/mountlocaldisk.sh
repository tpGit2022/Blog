#! /bin/sh
echo begin to mount local disk


function mount_local_disk ( ) {
	echo $1,$2
	## if dir is not exist, create it
	if [ ! -d $2 ]; then
		echo dir is not exist, create it
		mkdir $2
	fi
	    echo dir is exist
	## if $1 is not mount, mount it
	sudo mount $1 $2

}


mount_local_disk /dev/sdb3     /mnt/Software
mount_local_disk /dev/sdb10    /mnt/DiskSdk
mount_local_disk /dev/sdb2     "/mnt/E(Code)"
mount_local_disk /dev/sdb5     "/mnt/Heaven&Hell"
mount_local_disk /dev/sdb4     /mnt/Virtual
mount_local_disk /dev/sdb1     /mnt/D
mount_local_disk /dev/sda3     /mnt/C