### Android Studio和Eclipse的目录结构很不一致。
![20170108115850.png](../../../Pictures\20170108\20170108115850.png)

### Android Studio 设置某个特定模块使用代理设置
在该模块的build.gradle文件中设置代理
```
apply plugin: 'com.android.application'

android {
    ...

    defaultConfig {
        ...
        systemProp.http.proxyHost=proxy.company.com
        systemProp.http.proxyPort=443
        systemProp.http.proxyUser=userid
        systemProp.http.proxyPassword=password
        systemProp.http.auth.ntlm.domain=domain
    }
    ...
}
```

为整个工程启用代理设置
在gradle/gradle.properties文件中编辑代理设置
```
systemProp.http.proxyHost=proxy.company.com
systemProp.http.proxyPort=443
systemProp.http.proxyUser=username
systemProp.http.proxyPassword=password
systemProp.http.auth.ntlm.domain=domain

systemProp.https.proxyHost=proxy.company.com
systemProp.https.proxyPort=443
systemProp.https.proxyUser=username
systemProp.https.proxyPassword=password
systemProp.https.auth.ntlm.domain=domain
```

### 设置护眼色调整代码编辑区的字体大小

1. 设置护眼色
File-Setting-Editor-Colors & Fonts-General-Text-Default Text-BackGround 写入十六进制颜色数据#CCEED0
2. 设置代码编辑区的字体大小
File-Setting-Editor-Colors & Fonts-Font-size 16 -apply

