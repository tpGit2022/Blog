
1. ntfs error
```
Error mounting /dev/sda3 at /media/dms/286A099C6A0967C0: Command-line `mount -t "ntfs" -o "uhelper=udisks2,nodev,nosuid,uid=1000,gid=1000,dmask=0077,fmask=0177" "/dev/sda3" "/media/dms/286A099C6A0967C0"' exited with non-zero exit status 14: The disk contains an unclean file system (0, 0).

Metadata kept in Windows cache, refused to mount.

Failed to mount '/dev/sda3': Operation not permitted

The NTFS partition is in an unsafe state. Please resume and shutdown

Windows fully (no hibernation or fast restarting), or mount the volume

read-only with the 'ro' mount option.
```

resolve method:
sudo ntfsfix /dev/sda3


2. aosp repo tool
mkdir ~/bin
PATH=~/bin:$PATH
curl http://php.webtutor.pl/en/wp-content/uploads/2011/09/repo> ~/bin/repo
chmod a+x ~/bin/repo

last in aosp dir,
repo sync


3. temp disable touchpad
`sudo modprobe -r psmouse`
to enable
`sudo modprobe psmouse`

4. set proxy to chrome
in terminal input code `google-chrome --proxy-server="socks5://localhost:1080"`


5. AOSP problem
1. .git/config error ,配置了git依旧出现该问题，后面重新解压了aosp.tar文件显示正常了。
2. bad version 删除了manifest之后 执行 `repo init -u git://mirrors.ustc.edu.cn/aosp/platform/manifest` 和`repo sync`后终于同步完了代码 不容易啊

执行`repo sync`后，在与.repo同级的目录下可以看到
```
46766804	./.repo
74982	./art
29050	./bionic
21411	./bootable
13554	./build
3222	./compatibility
601826	./cts
24926	./dalvik
376350	./developers
114652	./development
653941	./device
5909524	./external
1571297	./frameworks
148429	./hardware
667	./kernel
82604	./libcore
380	./libnativehelper
489684	./packages
747	./pdk
2665	./platform_testing
18276371	./prebuilts
25494	./sdk
472258	./system
63497	./test
316542	./toolchain
2738112	./tools
78778987	.

```

6. remote useless kernel 
   1. list all kernel 
      `dpkg --list | grep linux-image`
   2. copy the kernel name you want to remove
      `sudo apt-get purge linux-image-xxxxx-generic`
   3. maybe you need to update grub manual or not
      `sudo update-grub`
7. get net ip 
   `curl ip.gs`
8.zip and unzip
  package dir `zip -r desfilename.zip srcdirname`
  unpackage `unzip srcfilename.zip -d desdirname`
9. unzip filename.tar.bz2
   `bzip2 -d filename.tar.bz2
    tar -xvf filename.tar
   `
10. Syntax error: "(" unexpected,
     `./mountdisk.sh` occuered error,but `bash ./mountdisk.sh` is ok ,
      run `ls -al /bin/sh` we can know the current linux shell version is dash,we can run `sudo dpkg-reconfigure dash`,and choose no,and confirm ,so we can set the shell current version to be bash.
11. creat android-studio lancher.
    step 1: create lancher config. cd to `/usr/share/applications`,new file named `android-studio.desktop`,input content like this:
```
[Desktop Entry]
Version=1.0
Name=Android-Studio
Exec=/opt/android-studio/android-studio/bin/studio.sh
Terminal=false
Icon=/opt/android-studio/android-studio/bin/studio.png
Type=Application
Categories=Development
```
   step 2: grant run permision
   ` sudo chmod u+x /usr/share/applications/android-studio.desktop`,after this ,you can search in lanchers ,you can find android-studio lancher icon

  ```
  参数说明：

Name ：指定快捷方式名称。

Exec ：应用程序可执行文件的绝对路径

Icon ：图标的绝对路径

Terminal ：指定 Exec 键中的命令是否在终端窗口中运行。 如果此值为 true，则该命令在终端窗口中运行。对于并不创建窗口以在其中运行的命令，此键的值必须为 true。

Type : 指定菜单项的类型。 此值应为以下选项之一：

Application： 对于启动应用程序的菜单项，应输入此选项。
Link: 对于链接到文件、文件夹或 FTP 站点的菜单项，应输入此选项。
  ```

12. i use copy windows ssh key to linux ,want to reuse it ,it's occured `Bad owner or permissions on .ssh/config`,to reslove it, change the permission.
`sudo chmod 600 .ssh/config`


13. to mount disk auto.
step 1: `sudo blkid` to see the disk part info.
step 2: edit the file `/etc/fstab`, add content to this file.the content like this.
```
UUID＝344C12354C11F1FA    /media/E   ntfs defaults 0 0  
```
it has six args.
1. 分区设备文件名或UUID
2. 挂载点
3. 文件系统名称
4. 挂载参数，挂载权限
5. 指定分区是否被dump备份，0代表不备份，1代表每天备份，2代表不定期备份。
6. 指定分区是否被fsck检测，0代表不检测，其他数字代表检测的优先级，比如1的优先级比2高。根目录所在的分区的优先级为1，其他分区的优先级为大于或等于2

step 3:`reboot` the system

14. list file absoule path in dir
`ls -R | sed "s:^:`pwd`/:"`

