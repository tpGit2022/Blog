硬盘SSD+HDD，UEFI+GPT。

要想在在UEFI模式下显示启动盘，必须创建UEFI模式的启动盘，利用以往方式创建的启动盘将无法在UEFI模式下识别，

根据Ubuntu的官方文档使用Rufus创建Ubuntu的启动盘，分区方案和目标文件系统类型(Partition scheme and target system type)选择第二项，然后制作Ubuntu启动盘。制作好后就可以开始安装了。关闭BIOS的Secure Boot功能(个人猜测可能跟Ubuntu安装时的选项安装第三方驱动的选项有关)启动U盘里面的Ubuntu开始安装。
重点来了在分区的时候，因为是UEFI的模式所以是不需要boot分区的，又因为要实现Win10和Ubuntu的并存启动，所以最下方的`Device for boot loader installation`选择`Windows Boot Manager`,让Win10和Ubuntu公用一个efi分区。
个人的分区方案
/ 根目录 15G
swap(交换空间) 8G
/home   所有剩余的空间

> 关于分区这个启动首先UEFI模式下/boot分区肯定是没有必要的，不同的是有人会创建一个efi系统分区，而我没有创建因为已经有了这样的分区，我需要Win10和Ubuntu共用该efi分区，再者就是最下方的安装启动引导器的设备一定要选择对，理论上efi系统引导分区在哪你就指向哪儿。

关于如果安装完Ubuntu，重启机器直接进入了win10没有显示Grub的双引导界面，考虑为win10被设定为第一启动项了，进入BIOS修改UEFI模式下的启动顺序，将Ubuntu设置为第一启动项，

UEFI Boot Order-OS Boot Manager 选择Ubuntu的启动项为第一启动项



# tip
1. grub引导文件不要修改`/boot/grub2/grub.cfg`,该文件明确提示了不要修改它，该文件是由其他文件产生的。需要修改的是`/etc/grub.d`下面的某个文件，win10是`/etc/grub.d/40_custom`,更新重新生成启动引导配置命令
`grub2-mkconfig -o /boot/grub2/grub.cfg`

2. Ubuntu更新Root密码首次设置Root密码`sudo passwd`,二次设置Root密码`sudo passwd root`

3. Windows下利用`bcdedit`可以查看具体的启动项`bcdedit /enum`
`bcdedit /set {bootmgr} path xxxx`,如果修改不成功产生关闭secure boot重新修改。

4. 中间由于重启机器一直显示win10没有Ubuntu的启动界面，当时没有考虑到BIOS的设置问题，尝试过将EFI分区下面的Ubuntu启动引导项重命名为windows下的引导项结果是成功进入了grub，结果在grub下面点击windows的引导却一直进入grub，想想因为也简单，因为windows的引导被替换了所以会出现这种情况。

5. 修改Win10为第一启动项，进入Ubuntu ，修改`/etc/default/grub`文件，要修改的东西有两项一是启动的等待时间，二是启动项。根据grub启动界面上的顺序找到win10启动项所在的位置(注意序号从0开始算起)，然后修改为win10启动项的序号。

# 参考资料
1. [如何在UEFI模式下Win8与Ubuntu多系统的安装？](https://www.zhihu.com/question/22502670)
2. [Windows多启动数据配置工具bcdedit命令详解](http://blog.sina.com.cn/s/blog_632bf2e50102uzh4.html)
3. [Win10+Ubuntu16.04双系统(UEFI+GPT, SDD+HDD)解决方案](http://www.jishux.com/plus/view-603131-1.html)
4. [UEFI+GPT与BIOS+MBR各自有什么优缺点？](https://www.zhihu.com/question/28471913)
5. 
