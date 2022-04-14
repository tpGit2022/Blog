```
cd /d E:\MyCode\JavaCode\IntellijCode\JNIDemo>

javah -classpath out\production\classes -d src\main\jni com.huachao.java.HelloJNI


gcc -D __int64="long long"  -c -I "%JAVA_HOME%\include" -I "%Java_home%\include\win32" src\main\jni\com.huachao.java.HelloJNI.c


gcc -D __int64="long long" -Wl,--add-stdcall-alias -I "%JAVA_HOME%\include" -I "%Java_home%\include\win32" -shared -o src\main\libs\hello.dll src\main\jni\com.huachao.java.HelloJNI.c

gcc -D __int64="long long" -Wl,--add-stdcall-alias -I "%JAVA_HOME%\include" -I "%Java_home%\include\win32" -shared -o src\main\libs\hello.dll src\main\jni\com.huachao.java.HelloJNI.c
```