[TOC]

***初始问题：如何从RAW8得到看图软件可打开的BMP，JPG，JPEG或者PNG***


# RAW Image概述

Sensor 输出的原始图像称之为RAW图。 由于工艺和成本的原因 在 Sensor 之前放置了CFA(Color Filter Arrays) 过滤不同波长的光线，Sensor 上每一个感光点接受到的经过CFA过滤后的光线，也就是说CFA的排序顺序决定了 Sensor输出的一维数组的结构，按照 Bayer 阵列输出图片的一维数组图像有

* RG/GB
* BG/GR
* GR/BG
* BG/RG

RAW8:  8bit表示一个像素点  
RAW10：10bit表示一个像素点，实际中需要用到 2byte也就是16bit，所以高6位无用  
RAW12：12bit表示一个像素点，实际中也需要 2byte来表示 所以高4位无用

![RAW8和RAW10的Hex比较](../Pictures/RAW8和RAW10的比较.png)

上图是同一张图 RAW8 和 RAW10 格式的 Hex 值对比，根据RAW图的定义 `41 00` 和 `10` 其实代表的同一个像素点

RAW10 转 RAW8 以上图为例

```
41 00  ---> 0100 0001 0000 0000
低位 0100 0001 --> 右移两位 0001 0000 取后六位
高位 0000 0000 --> 左移六位 0000 0000 取前两位

组成 0001 0000 --> 即十六进制 10
```

疑问：RAW10高位丢掉高位的六位丢掉可以理解毕竟是无效数据，但是地位的低两位丢掉不会有影响吗？

**数据丢失是必然的，特别是RAW10到RAW8**  

低位丢掉两位最大值是 `11` 也就是3，误差属于较小可忽略




# RAW解析


## Java 代码实现

RAW10 转 RAW8 的Java代码实现

```
code java
public void convertRaw10TRaw8(File source) {
        if (source == null || !source.exists()) return;
        //TODO 暂时固定为 2592*1944
        int width = 2592; int height = 1944;
        System.out.println(String.format("%d*%d byte:%dbyte --> word:%dbyte", width, height, width*height, 2*width*height));

        System.out.println(String.format("RAW10:%s fileLength:%d", source.getName(), source.length()));
        try {
            byte[] buffer =  FileUtils.readFileToByteArray(source);
            System.out.println(String.format("buffer size:%d", buffer.length));

            // convert to RAW8
            byte[] buffer_raw8 = new byte[width * height];
            for (int r = 0; r < height; r++) {
                for (int c = 0; c < width; c++) {
                    byte  low = buffer[2 * r * width + 2 * c];
                    byte high = buffer[2 * r * width + 2 * c + 1];
                    // Java 中 byte 的取值范围是-128-127，地位右移需要高位需要补0而不是1 故需要无符号数位移
                    byte convert_low = (byte) ((low >>> 2) & 0x3f);
                    byte convert_high = (byte) ((high << 6) & 0xc0);
//                    System.out.println(String.format("r:%d width:%d c:%d Index=%d size=%d", r, width, c, r * width + c, buffer_raw8.length));
                    buffer_raw8[r * width + c] = (byte) (convert_high + convert_low);
                }
            }

            //TODO 轉化存在問題 待處理  RAW10兩個字節那個　那个属于高位　那个属于地位？　处理时是否存在溢出的情况　
            String fileRaw8Name= source.getName().replaceAll("RAW10", "RAW8");
            String baseDir = "C:\\Users\\xxxx\\Desktop\\OutPut\\";
            File desFile = new File(baseDir, "/" + fileRaw8Name);
            if (desFile.exists())  {
                System.out.println(String.format("已存在文件%s，准备删除", desFile.getAbsolutePath()));
                if (!desFile.delete()) {
                    System.out.println("删除失败!");
                }
            }
            if (!desFile.getParentFile().exists()) {
                if (!desFile.getParentFile().mkdirs()) {
                    System.out.println("创建父目录失败！");
                }
            }
            if (!desFile.createNewFile()) {
                System.out.println("创建文件失败");
            }
            FileUtils.writeByteArrayToFile(desFile, buffer_raw8);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
```


# RAW图与RGB

光线经过CFA过滤后被Sensor的感应到，此时Sensor输出的RAW图只是数组，数组中的数据实际描述的光照的强度，要想得到符合人眼看到的彩色图片，需要进行插值, 也就是从原始的数组得到R,G,B三个数组，数据量在原来的三倍


![RAW图插值](../Pictures/RAW图插值.png)


# 图片格式

图片格式遵循固定的格式 最开始的文件头也称之为文件魔数


# 参考资料

1. [一文读懂rawRGB、RGB和YUV数据格式与转换](https://blog.csdn.net/qq_29575685/article/details/103954096)
2. [RAW、YUV、RGB、JPEG格式简介](https://blog.csdn.net/yaoming168/article/details/120434807)
3. [【VS开发】【图像处理】RGB各种格式](https://www.cnblogs.com/huty/p/8518412.html)
4. [raw文件格式详解 ](https://developer.orbbec.com.cn/forum_plate_module_details.html?id=721)
5. [RAW图像数据到RGB](https://blog.csdn.net/peng864534630/article/details/78177211)