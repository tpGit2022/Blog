关键字
权限控制：public,private ,protected,以及没有修饰符默认为友包
线程并发同步关键字：synchronized，volatile
abstract,final,static,
变量
类 class
静态类，抽象类
接口 interface
注解 @interface
枚举 enum



父类的静态变量被所有子类共享

Java中的方法
```
public class Object {
    public static int i =10;
    //静态代码块
    static {
        System.out.println("Object static code is loader");
    }
    //非静态代码块，会在构造方法前面调用而且构造方法每调用一次该代码块调用一次
    {
        System.out.println("Object code without static is run");
    }

    public Object() {
        super();
        System.out.println("Object Construct Method is Invokede");
    }

    public void print(){
        System.out.println("Object is print");
    }
}

```


Java中方法：
抽象方法，接口方法，本地方法，静态方法，成员方法


变量：
类成员变量，方法的局部变量，类的静态变量，