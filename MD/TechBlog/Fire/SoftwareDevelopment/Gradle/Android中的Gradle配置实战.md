[TOC]

# 分离依赖
提取各类依赖集中于一个地方方便管理。新建`config.gradle`，配置上主要借助全局变量`ext`，例如一个常见的`config.gradle`配置如下：

```
ext.deps = [:]

def addExtraRepos(RepositoryHandler handler) {
    handler.maven { url 'https://jitpack.io' }
}
ext.addExtraRepos = this.&addExtraRepos

def build_versions = [:]
build_versions.min_sdk = 19
build_versions.target_sdk = 28
build_versions.compile_sdk = 28
build_versions.build_tools = "28.0.3"
ext.build_versions = build_versions

def versions = [:]
versions.supportv7 = "26.1.0"
versions.RxJava2 = "2.2.2"
versions.RxAndroid = "2.1.0"

def deps = [:]

def support = [:]
support.app_compat_v7 = "com.android.support:appcompat-v7:${versions.supportv7}"
support.recyclerview = "com.android.support:recyclerview-v7:${versions.supportv7}"
deps.support = support

//declare rx-series
deps.RxJava2 = "io.reactivex.rxjava2:rxjava:${versions.RxJava2}"
deps.RxAndroid = "io.reactivex.rxjava2:rxandroid:${versions.RxAndroid}"

ext.deps = deps
```

在项目的build.gradle中添加 `apply from: "config.gradle"` 使其被应用至各个module，之后在module中引用

```
...
android {
    ...
    compileSdkVersion rootProject.ext.build_versions.compile_sdk
    ...
}
...
dependencies {
    ...
    implementation rootProject.ext.deps.support.app_compat_v7
    implementation rootProject.ext.deps.RxJava2
    ...
}
...

```

`config.gradle`定义了添加额外仓库的方法，在项目build.gradle文件中的repositories节点调用
```
...
repositories {
    google()
    jcenter()
    rootProject.ext.addExtraRepos(repositories)
}
...
```

# 多渠道打包及签名配置
Android中通过项目的`build.gradle`的`signingConfigs`节点配置相关的签名文件。

为了统一配置方便一般把签名文件相关配置同一写到`config.gradle`中，为了避免明文写入gradle文件中，这里`config.gradle`采用环境变量来配置签名参数。新建环境变量(用户变量和系统变量均可)
```
ANDROID_CERTIFIFACTE_ALIAS : 密钥的别名alias
ANDROID_CERTIFIFACTE_ALIAS_PASSWORD : 密钥别名的密码
ANDROID_CERTIFIFACTE_STORE_FILEPATH : 密钥文件所在位置
ANDROID_CERTIFIFACTE_STORE_PASSWORD : 密钥文件密码
```

在`config.gradle`文件中
```
ext {
    ....
    releaseParameter = [
            'keyAlias' : System.getenv("ANDROID_CERTIFIFACTE_ALIAS"),
            'keyPassword' : System.getenv("ANDROID_CERTIFIFACTE_ALIAS_PASSWORD"),
            'storeFilePath' : System.getenv("ANDROID_CERTIFIFACTE_STORE_FILEPATH"),
            'storePassword' : System.getenv("ANDROID_CERTIFIFACTE_STORE_PASSWORD")
    ]
    ....
}
```

同时项目级别的`build.gradle`中添加`config.gradle`的引用，同步下gradle让其对所有子模块生效

```
apply from: 'config.gradle'
```

最后在子模块级别添加release的签名配置

```
apply plugin: 'com.android.application'
def certificateParameters = rootProject.ext.releaseParameter
...
android {
    ...
    signingConfigs {
        release {
            keyAlias certificateParameters["keyAlias"]
            keyPassword certificateParameters["keyPassword"]
            try {
                //try catch this code avoid show error message:'filepath may null or empty' when sync gradle
                storeFile file(certificateParameters["storeFilePath"])
            } catch (Exception e) {
                e.printStackTrace()
                println("keystore file path is invalid")
            }
            storePassword certificateParameters["storePassword"]
        }

        debug {

        }
    }
    ...

    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
            signingConfig signingConfigs.release
        }
    }
}
```

这样就可以通过环境变量中配置的签名文件参数进行apk的release发布。


# 附录


```groovy
/**
 *  deps.gradle 同一管理依赖库
 *  项目的 build.gradle 添加 `apply from: 'deps.gradle'` 引用该文件
 *  同时将原来的 `repositories {....}` 节点 替换为 `addRepos(repositories)`
 */
// add resp remote url
def addRepos(RepositoryHandler handler) {
    // add aliyun resp url to build fast
    handler.maven{ url 'https://maven.aliyun.com/nexus/content/groups/public/'}
    handler.maven { url 'https://maven.aliyun.com/repository/google' }
    handler.maven{ url 'https://maven.aliyun.com/repository/jcenter'}
    handler.maven { url 'https://maven.aliyun.com/repository/central' }
    handler.maven { url "https://maven.aliyun.com/repository/gradle-plugin" }
    // origin resp remote url
    handler.maven { url 'https://jitpack.io' }
    handler.google()
    handler.mavenLocal()
    handler.mavenCentral()
    handler.maven { url 'https://oss.sonatype.org/content/repositories/snapshots' }
    //handler.jcenter()  jcenter自2021.02.28开始停止维护
}
ext.addRepos = this.&addRepos

def deps = [:]

def android_sdk = [:]
android_sdk.minSdkVersion =  21
android_sdk.targetSdkVersion = 29
android_sdk.compileSdkVersion = 29
android_sdk.buildToolsVersion = "29.0.3"

ext.android_sdk = android_sdk

def androidx = [:]
// room
androidx.room = "androidx.room:room-runtime:2.2.5"
androidx.room_apt = "androidx.room:room-compiler:2.2.5"
androidx.room_ktx = "androidx.room:room-ktx:2.2.5"
androidx.room_rxjava2 = "androidx.room:room-rxjava2:2.2.5"
androidx.room_test_helper = "androidx.room:room-testing:2.2.5"
// live data

androidx.viewmodel = "androidx.lifecycle:lifecycle-viewmodel-ktx:2.2.0"
androidx.livedata = "androidx.lifecycle:lifecycle-livedata-ktx:2.2.0"
// lifecycle without ViewModel or LiveData
androidx.lifecycle = "androidx.lifecycle:lifecycle-runtime-ktx:2.2.0"
androidx.lifecycle_apt = "androidx.lifecycle:lifecycle-compiler:2.2.0"

androidx.recyclerview = "androidx.recyclerview:recyclerview:1.1.0"
androidx.cardview = "androidx.cardview:cardview:1.0.0"
androidx.viewpager2 = "androidx.viewpager2:viewpager2:1.0.0"
androidx.material = "com.google.android.material:material:1.2.1"
deps.androidx = androidx

def common_deps = []

ext.common_deps = common_deps

def android_deps = []
ext.common_deps = android_deps


def java_deps = []
ext.common_deps = java_deps

ext.deps = deps
```