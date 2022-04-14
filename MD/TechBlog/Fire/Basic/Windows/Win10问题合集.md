[TOC]

# 假死

win10 版本 1709 OS内部版本 16299.371

随机性假死，时间不定，频率不定。没有任何头绪目前所知的只有键盘出了 Fn+F5 可以开关键盘灯外，其他键盘鼠标操作均无相应，不强制关机的情况下唯一可行的操作时拔插电源，只要拔插电源一次，电脑就能正常响应。

根据 eventvmr 的日志显示 假死时间 15:03 ~ 15:09 频繁出现同一个错误

驱动程序在 \Device\Harddisk3\DR3 上检测到控制器错误。

```
- <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
- <System>
  <Provider Name="Disk" /> 
  <EventID Qualifiers="49156">11</EventID> 
  <Level>2</Level> 
  <Task>0</Task> 
  <Keywords>0x80000000000000</Keywords> 
  <TimeCreated SystemTime="2019-12-11T07:04:01.341329800Z" /> 
  <EventRecordID>69608</EventRecordID> 
  <Channel>System</Channel> 
  <Computer>seeksky</Computer> 
  <Security /> 
  </System>
- <EventData>
  <Data>\Device\Harddisk3\DR3</Data> 
  <Binary>0F00800001000000000000000B0004C00301000000000000000000001600000000000000000000008E7C4C0100000000FFFFFFFF0600000058000005000000000000061228090800000000000A0000000000000000000000C0CF0D318EB2FFFF000000000000000060312B328EB2FFFF000000000000000000000000000000001B010000000000000000000000000000000000000000000000000000000000000000000000000000</Binary> 
  </EventData>
  </Event>
```


https://answers.microsoft.com/zh-hans/windows/forum/windows_10-performance/win10/b85c3c68-e42d-4a59-b501-8240d4b28c0b?tm=1576684556732

https://support.microsoft.com/zh-cn/help/929833/use-the-system-file-checker-tool-to-repair-missing-or-corrupted-system