# 添加依赖：

需要用到RxJava和RxAndroid的模块(app和库)中的build.gradle文件中添加如下依赖：
```
    compile 'io.reactivex.rxjava2:rxandroid:2.0.1'
    // Because RxAndroid releases are few and far between, it is recommended you also
    // explicitly depend on RxJava's latest version for bug fixes and new features.
    compile 'io.reactivex.rxjava2:rxjava:2.1.0'
```

# 基本使用 

要使用RxJava，首先你需要创建Observable（它们发射数据序列），使用Observable操作符变换那些Observables，获取严格符合你要求的数据，然后观察并处理对这些数据序列（通过实现观察者或订阅者，然后订阅变换后的Observable）。

下面看一段常见的流式调用链代码：
```
  Observable.create(new ObservableOnSubscribe<Integer>() {
            @Override
            public void subscribe(@NonNull ObservableEmitter<Integer> e) throws Exception {
                e.onNext(1);
                e.onNext(2);
                e.onComplete();
            }
        }).subscribeOn(Schedulers.io()).
                observeOn(AndroidSchedulers.mainThread()).subscribe(new Observer<Integer>() {
            @Override
            public void onSubscribe(@NonNull Disposable d) {

            }

            @Override
            public void onNext(@NonNull Integer integer) {

            }

            @Override
            public void onError(@NonNull Throwable e) {

            }

            @Override
            public void onComplete() {

            }
        });
```

上述代码是RxJava使用的基本流程。

1. 通过Observable.create方法创建一个被观察者，调用onNext发送事件
2. subscribeOn()指定被观察者发送事件的线程(可选)
3. observeOn()指定观察者处理事件的线程(可选)。
4. 观察者处理事件
  
> 通过各种方式得到一个被观察者，被观察者发送事件，观察者接受事件，观察者处理事件。



# 操作符

RxJava的操作符很多且1.0和2.0的操作符存在差异，操作符用途如下：

1. 直接创建一个Observable（创建操作）
2. 组合多个Observable（组合操作）
3. 对Observable发射的数据执行变换操作（变换操作）
4. 从Observable发射的数据中取特定的值（过滤操作）
5. 转发Observable的部分值（条件/布尔/过滤操作）
6. 对Observable发射的数据序列求值（算术/聚合操作）

RxJava是ReactiveX在JVM上的实现，原本ReactiveX上的操作符可能在RxJava上对应着不同的名称。总的来说通过强大的操作符，RxJava可能让我们很轻松的完成事件处理，线程调度。让代码逻辑更加清晰。