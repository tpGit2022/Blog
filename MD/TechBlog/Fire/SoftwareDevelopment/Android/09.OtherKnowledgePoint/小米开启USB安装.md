com.miui.guardprovider

GuardProvider.apk


INSTALL_FAILED_USER_RESTRICTED


小米手机开个USB安装又是要插卡又是要登录小米账号的实在太烦，这里提供一个解决方案前提是你手机已经Root了。




* 确认手机上有


提取 SecurityCenter.apk， Settings.apk 两个APK。

```
mFocusedActivity: ActivityRecord{4211eab8 u0 com.android.settings/.SubSettings t10}
```

查询到 具体的页面  DevelopmentSettings

 ```
 public class DevelopmentSettings extends RestrictedSettingsFragment implements OnClickListener, OnDismissListener, OnPreferenceChangeListener
 ```

 在 oncreate方法中 
 
 ```
public void onCreate(Bundle bundle) {
    ...
     this.Ho = aK("adb_install");
        this.Hp = aK("adb_input");
        if (FeatureParser.getBoolean("is_pad", false)) {
            preferenceGroup = (PreferenceGroup) findPreference("debug_debugging_category");
            preferenceGroup.removePreference(this.Ho);
            preferenceGroup.removePreference(this.Hp);
        } else {
            this.Ho.setChecked(a.am(getActivity()));
            this.Hp.setChecked(a.isInputEnabled());
        }
    ...
}
 ```

CheckBox类型的变量Ho代表的就是 "USB安装"，进一步看 `a.am()方法`

```
/* compiled from: AdbUtils */
public class a {
    private static Bundle a(Context context, String str, Bundle bundle) {
        return context.getContentResolver().call(Uri.parse("content://com.miui.securitycenter.remoteprovider"), "callPreference", str, bundle);
    }

    public static void c(Context context, String str, boolean z) {
        Bundle bundle = new Bundle();
        bundle.putInt("type", 1);
        bundle.putString("key", str);
        bundle.putBoolean("value", z);
        a(context, "SET", bundle);
    }

    public static boolean d(Context context, String str, boolean z) {
        Bundle bundle = new Bundle();
        bundle.putInt("type", 1);
        bundle.putString("key", str);
        bundle.putBoolean("default", z);
        bundle = a(context, "GET", bundle);
        return bundle == null ? z : bundle.getBoolean(str, z);
    }

    public static boolean am(Context context) {
        return d(context, "security_adb_install_enable", false);
    }

    public static void f(Context context, boolean z) {
        c(context, "security_adb_install_enable", z);
    }

    public static boolean isInputEnabled() {
        return SystemProperties.getBoolean("persist.security.adbinput", false);
    }

    public static void ae(boolean z) {
        SystemProperties.set("persist.security.adbinput", z ? "1" : "0");
    }
}
```

有上述代码可知在查询 com.miui.securitycenter.remoteprovider 这个 ContentProvider

com.miui.securitycenter 是SecurityCenter.apk 的包名，于是 Jadx 打开 apk，由 AndroidManifest 可知对应的类文件是 `com.miui.common.persistence.RemoteProvider`

```
<provider android:name="com.miui.common.persistence.RemoteProvider" android:permission="com.miui.securitycenter.permission.ACCESS_SECURITY_CENTER_PROVIDER" android:exported="true" android:process="com.miui.securitycenter.remote" android:authorities="com.miui.securitycenter.remoteprovider"/>
```

简单看了下代码可以知道这个 ContentProvider并没有以数据库的方式存放数据，而是选择了 SharedPrefs。

一路跟踪 call 方法

call --> a --> b --> j --> d.a


```
public Bundle call(String str, String str2, Bundle bundle) {
        if ("callPreference".equals(str)) {
            return a(str2, bundle);
        }
        return null;
}
private Bundle a(String str, Bundle bundle) {
        if (bundle.containsKey(ShowSmsDetailActivity.TYPE)) {
            switch (bundle.getInt(ShowSmsDetailActivity.TYPE)) {
                case 0:
                    return c(str, bundle);
                case 1://USB安装
                    return b(str, bundle);
                case 2:
                    return d(str, bundle);
                case 3:
                    return g(str, bundle);
                case 4:
                    return f(str, bundle);
                case 5:
                    return e(str, bundle);
            }
        }
        return null;
    }

private Bundle b(String str, Bundle bundle) {
        String string = bundle.getString("key");
        if (string != null) {
            if ("SET".equals(str)) {
                boolean z = bundle.getBoolean("value");
                j(string, z);
                this.XI.edit().putBoolean(string, z).apply();
                return null;
            } else if ("GET".equals(str)) {
                boolean z2 = bundle.getBoolean(SimUserInfo.DEFAULT_NULL_IMSI);
                bundle.clear();
                bundle.putBoolean(string, this.XI.getBoolean(string, z2));
                return bundle;
            }
        }
        return null;
    }


private void j(String str, boolean z) {
        if ("security_adb_install_enable".equals(str) && z) {
            int callingPid = Binder.getCallingPid();
            Context context = getContext();
            try {
                String str2 = (String) d.a((SecurityManager) context.getSystemService("security"), "getPackageNameByPid", new Class[]{Integer.TYPE}, Integer.valueOf(callingPid));
                if (context.getPackageName().equals(str2) || "com.miui.klo.bugreport".equals(str2)) {
                    return;
                }
            } catch (Throwable e) {
                Log.e("RemoteProvider", "getPackageNameByPid error", e);
            }
            throw new SecurityException("set security_adb_install_enable permssion denied");
        }
    }

```


d.a 的方法是反射修改值，

```
String str2 = (String) d.a((SecurityManager) context.getSystemService("security"), "getPackageNameByPid", new Class[]{Integer.TYPE}, Integer.valueOf(callingPid));
```

从上面的分析可以看到和 adb 安装的只有 `security_adb_install_enable` 这个值，于是手动修改 `/data/data/com.miui.securitycenter/shared_prefs/remote_provider_preferences.xml`, 新增 

```
<boolean name="security_adb_install_enable" value="true"/>
```

发现依旧不能直接 adb 安装 apk 依旧提示 INSTALL_FAILED_USER_RESTRICTED，只能进一步分析继续查看 Settings.apk， 在
onActivityResult 中看到启动了新的Activity

```
protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
    ....
     else if (preference == this.Ho) {
            if (a.am(getActivity())) {
                a.f(getActivity(), false);
            } else {
                startActivityForResult(new Intent("com.miui.securitycenter.action.ADB_INSTALL_VERIFY"), 11);
            }
    ....
}
```

依旧在 SecurityCenter.apk 的清单文件中查询 Action 得知相应的Activity 是 AdbInstallVerifyActivity。

```
<activity android:theme="0x100d0033" android:name="com.miui.permcenter.install.AdbInstallVerifyActivity" android:exported="false" android:launchMode="singleTop" android:screenOrientation="portrait">
            <intent-filter>
                <action android:name="com.miui.securitycenter.action.ADB_INSTALL_VERIFY"/>
                <category android:name="android.intent.category.DEFAULT"/>
            </intent-filter>
        </activity>

```

一路跟踪 AdbInstallVerifyActivity 的启动过程

OnCreate --> hk --> np --> nq -->  new n(this).executeOnExecutor

```
protected void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        this.Hn = s.eW(this);
        hk();
    }

    protected void hk() {
        this.Ho = getIntent().getBooleanExtra("is_input", false);
        if (this.Ho || !TextUtils.isEmpty(this.Hn)) {
            np();
            return;
        }
        Toast.makeText(this, R.string.adb_login_xiaomi_account, 1).show();
        s.a(this, new Bundle());
        finish();
    }

    protected void np() {
        e(View.inflate(this, R.layout.adb_install_progress, null));
        setupAlert();
        nq();
    }

 private void nq() {
        NetworkInfo activeNetworkInfo = ((ConnectivityManager) getSystemService("connectivity")).getActiveNetworkInfo();
        if (activeNetworkInfo == null || !activeNetworkInfo.isConnected()) {
            Toast.makeText(getApplicationContext(), R.string.adb_install_no_network, 1).show();
            finish();
            return;
        }
        new n(this).executeOnExecutor(AsyncTask.THREAD_POOL_EXECUTOR, new Void[0]);
    }

```

可以看到启动了一个异步任务 n, 粗略的看了下 doInBackground 的内容确认是在发送POST请求，那么着重看下 onPostExecute，网络请求之后的处理 

```
protected void onPostExecute(String str) {
        if (str == null) {
            this.Zp.hl();
        } else if (!TextUtils.isEmpty(str)) {
            Toast.makeText(this.Zp.getApplicationContext(), str, 1).show();
        }
        this.Zp.finish();
}
```

进一步查看 Zp.hl 方法

```
protected void hl() {
        if (this.Ho) {
            // adb input 
            AdbInputApplyActivity.setEnabled(true);
        } else {
            //adb install
            setEnabled(true);
        }
    }

```

这里只关心 adb install，于是进一步查看 setEnabled 方法

```
private void setEnabled(boolean z) {
        a.b(this).c(z);
}

public void c(boolean z) {
        com.miui.common.persistence.a.d("security_adb_install_enable", z);
        com.miui.b.f.a.set("persist.security.adbinstall", z ? "1" : "0");
}

public static void set(String str, String str2) {
        try {
            d.a(Av(), String.class, "set", new Class[]{String.class, String.class}, str, str2);
        } catch (Exception e) {
            e.printStackTrace();
        }
}
private static Class Av() {
        return Class.forName("android.os.SystemProperties");
}
```

d.a 依旧是反射调用，传递的 Set 的参数是 persist.security.adbinstall 和 1。  

android.os.SystemProperties 是系统属性，persist 前缀代表会持久保存，也就是说不会因为开关机而重置。那么问题就简单了，直接修改属性即可

```
su
setprop persist.security.adbinstall 1
reboot
```

重启后继续执行 `adb install xxx.apk`

安全中心也就是 com.miui.securitycenter 会查询 `com.miui.guardprovider`, 如果不存在该 apk 会报错，也会导致安装失败

```
01-02 09:08:58.519 4299-4299/? E/AndroidRuntime: FATAL EXCEPTION: main
    Process: com.miui.securitycenter, PID: 4299
    java.lang.RuntimeException: Unable to start activity ComponentInfo{com.miui.securitycenter/com.miui.permcenter.install.AdbInstallActivity}: java.lang.IllegalArgumentException: Unknown URI content://guard
        at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2200)
        at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2249)
        at android.app.ActivityThread.access$800(ActivityThread.java:141)
        at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1212)
        at android.os.Handler.dispatchMessage(Handler.java:102)
        at android.os.Looper.loop(Looper.java:136)
        at android.app.ActivityThread.main(ActivityThread.java:5052)
        at java.lang.reflect.Method.invokeNative(Native Method)
        at java.lang.reflect.Method.invoke(Method.java:515)
        at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:796)
        at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:612)
        at dalvik.system.NativeStart.main(Native Method)
     Caused by: java.lang.IllegalArgumentException: Unknown URI content://guard
```