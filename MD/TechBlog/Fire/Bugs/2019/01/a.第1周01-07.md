
1. JDK 和 Gradle版本不匹配导致编译失败

```
FAILURE: Build failed with an exception.

* What went wrong:
Could not determine java version from '9.0.1'.

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output.

* Get more help at https://help.gradle.org
```

Java9需要Gradle4.3及以上才可以正常编译

https://blog.csdn.net/aiyimo_/article/details/79458609