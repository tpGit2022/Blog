先配置Gradle的环境
Gradle的配置 
先配置Gradle 
新建环境变量GRADLE_HOME 值为Android Studio中的gradle位置
一般为你的Android Studio的安装目录\gradle\gradle-x.x-x-x

配置GRADLE_USER_HOME，这个用于指向.gradle文件所在的位置

在path中添加%GRADLE_HOME%\bin

Gradle ，Android gradle plugin的概念。

xxxx/.gradle

纯命令行编译时需要管Android gradle plugin

* 使用本地aar
```
repositories {
    flatDir {
        dirs 'libs'
    }
}
//dependencies 
compile(name:'xxx', ext:'aar')//xxx为lib名
```