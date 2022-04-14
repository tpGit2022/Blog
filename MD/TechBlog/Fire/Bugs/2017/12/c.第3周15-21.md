[TOC]


# AES+RSA加解密算法异常问题
1. 发生时间:`2017-12-15 10:00:00`  耗时:`00d03h00m`
2. 问题标签 ` java.security.NoSuchProviderException`,`no such provider: Crypto`
3. 问题具体描述
在Android 7.0的系统上面原本使用的好好的加解密算法抛出异常了。
4. 错误日志
***日志代码：***
```
java.security.NoSuchProviderException: no such provider: Crypto
```
5. 原因分析
Android N即Android 7.0弃用了`Crypto provider` ,需要自己实现CryptoProvider
6. 解决方案
***解决方案代码:***
    1. 新增CryptoProvider
```
import java.security.Provider;

/**
 * Created by tyw on 2017/12/15.
 */

public final class CryptoProvider extends Provider {
    /**
     * Creates a Provider and puts parameters
     */
    public CryptoProvider() {
        super("Crypto", 1.0, "HARMONY (SHA1 digest; SecureRandom; SHA1withDSA signature)");
        put("SecureRandom.SHA1PRNG",
                "org.apache.harmony.security.provider.crypto.SHA1PRNG_SecureRandomImpl");
        put("SecureRandom.SHA1PRNG ImplementedIn", "Software");
    }
}
```
    2. 修改原有代码
    ```
    SecureRandom sr = SecureRandom.getInstance("SHA1PRNG", "Crypto");
    ```
    为
    ```
    SecureRandom sr=SecureRandom.getInstance("SHA1PRNG",new CryptoProvider());
    ```
7. 参考资料
    1. [Security "Crypto" provider deprecated in Android N](https://android-developers.googleblog.com/2016/06/security-crypto-provider-deprecated-in.html)
    2. [Security “Crypto” provider deprecated in Android N
](https://stackoverflow.com/questions/39097099/security-crypto-provider-deprecated-in-android-n/42337802#42337802)
8. 反思和总结