# Java I/O 文件写入重复
1. 发生时间:`2018-10-23 21:30:00`  耗时:`xxdxxhxxm`
2. 问题标签 `buffer`,`I/o`
3. 问题具体描述
编写FileUtils工具用于合并多个txt文件，发现合并后的文件存在冗余内容
4. 错误日志
  思路上遍历文件夹下的file，读取然后写入合并文件中.中间也使用buffer做缓冲 
`byte[] buffer = new byte[1024 * 8]`, 冗余部分都是出现在单个文件的最后考虑可能是buffer的复用，最后一次读取时buffer没有填满，没有填充的部分使用了上一次buffer的数据 `FileOutputStream.write(buffer)` 时写入了上次读取的数据导致了冗余，可行的方案：每次读取有效buffer数据；下一次读取前先清除buffer中的数据;一次性读取file的全部内容.


***日志代码：***
有问题的代码
```
while (fis.read(buffer) != -1) {
    ...
    fos.write(buffer);
    ...
}

```
5. 原因分析
byte 的缓冲数组最后一次并没有被完全复写，保留了旧数据

6. 解决方案
***解决方案代码:***
1. 每次读取有效buffer
```
int readCount = fis.read(buffer) {
    ...
    fos.write(buffer, 0 , readCount);
    readCount = fis.read(buffer);
    ...
}
```

2. 一次读取所有内容，这个考虑到每个txt文件较小也是可行的

```
byte[] buffer = new byte[(int) fileList[i].length()]
```

3. 清除buffer，用这个需要使用nio包中的bytebuffer
```

```


7. 参考资料
8. 反思和总结
