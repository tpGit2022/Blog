
1. Fresco 4.x系统加载图片问题

错误日志：
```
W/ImagesAndroidWrapper: com.facebook.imagepipeline.memory.BasePool$PoolSizeViolationException: Pool hard cap violation? Hard cap = 4194304 Used size = 0 Free size = 131072 Request size = 4324834
at com.facebook.imagepipeline.memory.BasePool.get(BasePool.java:236)
at com.facebook.imagepipeline.memory.FlexByteArrayPool.get(FlexByteArrayPool.java:47)
at com.facebook.imagepipeline.platform.KitKatPurgeableDecoder.decodeByteArrayAsPurgeable(KitKatPurgeableDecoder.java:49)
at com.facebook.imagepipeline.platform.DalvikPurgeableDecoder.decodeFromEncodedImage(DalvikPurgeableDecoder.java:61)
at com.facebook.imagepipeline.platform.KitKatPurgeableDecoder.decodeFromEncodedImage(KitKatPurgeableDecoder.java:28)
```

加载4M图出现问题

Fresco 图片解码根据系统有所变化。5.0以上使用ArtDecoder没有java内存限制，5.0以下非webp图片使用`KitKatPurgeableDecoder`加载，由于使用java内存有内存限制默认大小是4M*处理器的数量，如果需要加载更大图片需要手动配置参数。
具体逻辑见 Fresco 源码中的 `ImagePipelineFactory.java`
```
public static PlatformDecoder buildPlatformDecoder(
      PoolFactory poolFactory,
      boolean directWebpDirectDecodingEnabled) {
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
      int maxNumThreads = poolFactory.getFlexByteArrayPoolMaxNumThreads();
      return new ArtDecoder(
          poolFactory.getBitmapPool(),
          maxNumThreads,
          new Pools.SynchronizedPool<>(maxNumThreads));
    } else {
      if (directWebpDirectDecodingEnabled
          && Build.VERSION.SDK_INT < Build.VERSION_CODES.KITKAT) {
        return new GingerbreadPurgeableDecoder();
      } else {
        return new KitKatPurgeableDecoder(poolFactory.getFlexByteArrayPool());
      }
    }
  }
```



调整为加载12m图
```
private void initFresco() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            Fresco.initialize(this);
        } else {
            // we found 4.4 system can not load big image like 4M, so we need to manual config ImagePipelineConfig
            // base on Fresco code comment Fresco use ArtDecoder to decode on LOLLIPOP system or up,  use PurgeableDecoder for 4.x
            int MIN_BYTE_ARRAY_SIZE = 128 * ByteConstants.KB;
            int MAX_ARRAY_SIZE = 12 * ByteConstants.MB;
            int MAX_NUM_THREADS = Runtime.getRuntime().availableProcessors();
            //construction with full parameters to set maxNumThreads
            PoolParams poolParams = new PoolParams(MAX_ARRAY_SIZE, MAX_ARRAY_SIZE * MAX_NUM_THREADS,
                    DefaultFlexByteArrayPoolParams.generateBuckets(MIN_BYTE_ARRAY_SIZE, MAX_ARRAY_SIZE,
                            MAX_NUM_THREADS),MIN_BYTE_ARRAY_SIZE ,MAX_ARRAY_SIZE,MAX_NUM_THREADS);
            PoolConfig poolConfig = PoolConfig.newBuilder().setFlexByteArrayPoolParams(poolParams).build();
            PoolFactory poolFactory = new PoolFactory(poolConfig);
            ImagePipelineConfig imagePipelineConfig = ImagePipelineConfig.newBuilder(this).setPoolFactory(poolFactory).build();
            Fresco.initialize(this, imagePipelineConfig);
        }
    }
```

> 注意必须使用 PoolParams 的全参构造方法来设置最大线程数量，否则会引发非法参数异常


# 参考资料
1. [Fresco - Docs](https://www.fresco-cn.org/docs/)
2. [fresco初始化过程](https://guolei1130.github.io/2016/12/12/fresco初始化过程/)
3. [使用Fresco加载图片](https://blog.csdn.net/mockingbirds/article/details/50658846)