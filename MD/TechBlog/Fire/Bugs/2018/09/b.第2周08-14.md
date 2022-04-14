1.发生时间2.耗时3.描述4.解决思路5.解决方案 6.反思

# 默认邮箱附件打不开
1. 发生时间:`2017-09-10 10:00:00`  耗时:`xxdxxhxxm`
2. 问题标签 `email`,`content://com.android.email.attachmentprovider`
3. 问题具体描述
默认邮箱 `com.android.email` 中下载的pdf附件，调用第三方应用时提示找不到文件。
4. 错误日志
***日志代码：***
```
 java.io.FileNotFoundException
```

传递Intent中的data `content://com.android.email.attachmentprovider/1/4/RAW `, 根据 `https://android.googlesource.com/platform/packages/apps/Email/+/eclair-release/src/com/android/email/provider/AttachmentProvider.java ` 知道 默认的邮件应用的附件是存储在 私有目录 databases/accountId.db_att 下的，具体位置和账户的id相关，通过Uri无法获取真实的文件地址，只能得到输入输出流
```
AssetFileDescriptor assetFileDescriptor = context.getContentResolver().openAssetFileDescriptor(uri, "rw");
assetFileDescriptor.createOutputStream();
```

针对这种情况，第三方应用能做的只能是通过输入输出流，拷贝源文件到临时文件，然后打开临时文件，对临时文件进行修改，之后再把相关修改写入附件中。

5. 原因分析

6. 解决方案
***解决方案代码:***
```
AssetFileDescriptor assetFileDescriptor = context.getContentResolver().openAssetFileDescriptor(uri, "rw");
assetFileDescriptor.createOutputStream();

```
7. 参考资料
8. 反思和总结