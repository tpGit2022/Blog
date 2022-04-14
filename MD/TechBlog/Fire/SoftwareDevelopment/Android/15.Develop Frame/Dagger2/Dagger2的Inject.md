Inejct用于注解成员变量或者构造方法。

被Injected标注的变量会build/generated/source/apt/debug/被标记变量所在包名下面生成xxxx_MembersInjector类，
被Injected标记过的构造方法会生成xxx_Factory工厂类。
被Component标记过的接口会生成DaggerXXXX类。

普通注入的例子

1. 新建类A
```

public class A {
    @Inject
    public A(){
        System.out.println("A class's Construct is invoke");
    }
}
```

2. 新建类B依赖A
```
public class B {
    @Inject
    protected A a;
    public B(){
        System.out.println("B class's Construct is invoke");
        printBA();
        a=DaggerAC.create().injectA();
        printBA();
    }
    public void printBA(){
        System.out.println(a==null?"B class member a is null":"B class member a is not null");
    }
}
```

3. 新建接口AC
```
@Component
public interface AC {
    A injectA();
    void injectA(MainActivity mainActivity);
}
```

@Injected标记过的构造方法和Module里面@Providers修饰的方法，也就是通过函数的返回值来进行判断。
` A injectA();` 这个方法正常执行后生成一个A的实例。
`void injectA(MainActivity mainActivity);` ,这个方法正常执行后是将`MainActivity`中被Injected标记过的所有变量进行注入(变量的初始化).

> Dagger2获取依赖只有两条途径Module中的Provider标记的方法提供或者是被Inject标记过的构造方法提供。

1. 错误日志
Error:(12, 7) 错误: Members injection methods may only return the injected type or void.
```
Error:(12, 10) 错误: com.leemoaly.daggerstudy.MainActivity has type parameters, cannot members inject the raw type. via:
com.leemoaly.daggerstudy.MainActivity is injected at
com.leemoaly.daggerstudy.di.component.ActivityComponent.inject(mainActivity)
```
2. 原因MainActivity的定义为`public class MainActivity<K extends View> extends BaseActivity<MainPresenter>`,而ActivityComponent中定义的方法`void inject(MainActivity mainActivity);`方法两者不一致导致该错误，要修正该错误移除MainActivity后面的泛型声明`<K extends View>`，如果这部分申明是必要，可以新建
Injected不能正常工作的地方
Interfaces can’t be constructed.
Third-party classes can’t be annotated.
Configurable objects must be configured!

即
1. 被标记的接口类型不能被正常构建
2. 第三方类库不能被@Injected所标记

```
Error:(14, 10) 错误: com.leemoaly.daggerstudy.MainActivity has type parameters, cannot members inject the raw type. via:
com.leemoaly.daggerstudy.MainActivity is injected at
com.leemoaly.daggerstudy.di.component.ActivityComponent.injectAComplex(activity)
```

@Provides的优先级高于Injected，即如果@Provides修饰的方法和@Injected修饰的方法同时都能满足依赖，只调用@Provider修饰的方法而不会调用@Injected修饰的构造方法。

接口只能通过Module的方式来注入，下面是一个接口注入的实例。

1. 编写BasePresenter.java
```
public interface BasePresenter{
    void attachView();
}
```
2. 编写基类BaseActivity.java
***用`@Inject`标记要注入presenter***
```

public abstract class BaseActivity<T extends BasePresenter> extends AppCompatActivity {
    @Inject
    protected T mPresenter;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        initInject();
    }

    /**
     * 初始化依赖
     */
    protected abstract void initInject();
}
```
3. 编写MainPresenter.java
***`@Inject`标记MainPresenter的构造函数以便提供依赖***
```
public class MainPresenter implements BasePresenter {
    @Inject
    public MainPresenter(){

    }
    @Override
    public void attachView() {

    }
    public void getMainData(){

    }
}
```
4. 编写MainActivity.java
***继承基类并指定BasePresenter接口的实现类为MainPresenter类型。
```
public class MainActivity extends BaseActivity<MainPresenter> {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ...
        mPresenter.getMainData();
        ...
    }

    @Override
    protected void initInject() {
        DaggerActivityComponent.create().inject(MainActivity.this);
    }
}
```