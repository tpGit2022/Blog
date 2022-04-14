1. `cannot be provided without an @Provides- or @Produces-annotated method`
```
Error:(10, 10) 错误: @com.leemoaly.androidstudy.dagger2study.DogQualifier("C") com.leemoaly.androidstudy.dagger2study.Dog cannot be provided without an @Provides- or @Produces-annotated method.
@com.leemoaly.androidstudy.dagger2study.DogQualifier("C") com.leemoaly.androidstudy.dagger2study.Dog is injected at
com.leemoaly.androidstudy.dagger2study.Dagger2Activity.dog
com.leemoaly.androidstudy.dagger2study.Dagger2Activity is injected at
com.leemoaly.androidstudy.dagger2study.CatComponent.injectCat(dagger2Activity)
```
出现这种情况是由于没有提供或者说没有提供全面注入标记即injected和provider注解。
