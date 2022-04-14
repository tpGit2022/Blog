使用Retrofit框架解析Xml数据需要SimpleXml的支持，添加依赖。
```
//引入Retrofit的XML的转换器
    compile ('com.squareup.retrofit2:converter-simplexml:2.3.0'){
        exclude group: 'xpp3', module: 'xpp3'
        exclude group: 'stax', module: 'stax-api'
        exclude group: 'stax', module: 'stax'
    }  
```

初始化Retrofit对象时使用SimpleXml的转化器。
```
public static Retrofit getXmlRetrofit(String baseUrl){
        Retrofit.Builder retrofitBuild=new Retrofit.Builder();
        retrofitBuild.addConverterFactory(SimpleXmlConverterFactory.create());
        retrofitBuild.addCallAdapterFactory(RxJava2CallAdapterFactory.create());
        retrofitBuild.baseUrl(baseUrl);
        return retrofitBuild.build();
    }
```
使用Retrofit和SimpleXml解析Xml数据关键在于Xml转成的实体类的编写，Json数据有直接的Gson插件一键转化成实体类工具，而Xml并没有这样的插件，需要自己手动编写相应的实体类，例如服务器返回的xml数据如下：
```

```

SimpleXml中常用注解
```
@Namespace,@Root,@Attribute,@Element,@ElementList
```

@ElementList必要属性例子：
```
 @ElementList(type = ModuleInfo.class,required = true,entry = "ModuleInfo",inline = true)
    List<ModuleInfo> moduleInfoList;
```

多个命名空间，xml如下：
```
<?xml version="1.0" encoding="utf-8"?>
<GroupList_Model xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://www.baidu.org/">
    <GroupList>
        <Group>0</Group>
    </GroupList>
    <GroupList>
        <Group>1</Group>
    </GroupList>
</GroupList_Model>
```
对应的实体类如下：
```
@Root(name = "GroupList_Model")
@NamespaceList({@Namespace(prefix = "xsi", reference = "http://www.w3.org/2001/XMLSchema-instance"),
        @Namespace(prefix = "xsd", reference = "http://www.w3.org/2001/XMLSchema"),
        @Namespace(reference = "http://www.baidu.org/")})
public class GroupListModuleXmlBean {
    @Element(name = "GroupList")
    GroupList groupList;
    //..省略get/setter方法
    @Root(name = "GroupList",strict = false)
    static public class GroupList{
        @Element(name = "Group")
        String Group;
        //..省略get/setter方法
    }
}
```
# 参考资料
1. [SimpleXml官方资料](http://simple.sourceforge.net/download/stream/doc/tutorial/tutorial.php)