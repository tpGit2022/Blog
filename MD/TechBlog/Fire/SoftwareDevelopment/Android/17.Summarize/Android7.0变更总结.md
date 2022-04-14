FileProvider
和RSA算法变更。
Android7.0(Nought)简称N
https://developer.android.google.cn/about/versions/nougat/android-7.0-changes.html


Android7.0中Google不允许Intent携带`file://`隐式调用。要在应用中共享文件需要发送`content://URI`并授予URI临时访问权限这需要借助FileProvider类。
intent.setFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);

http://blog.csdn.net/u013243573/article/details/54426063