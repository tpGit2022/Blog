[TOC]

Canvas 即画布或者说图层对象，其默认坐标和View的坐标一致即以View的左上角为原点，向右是X轴正方向，向下是Y轴的正方向。Canvas可以通过其translate,rotate等操作使坐标系的原点以及方向发生变化

在Canvas之外区域绘制内容是无效的，例如画布的区域是(0,0,100,100) 绘制Rect(-100,0,0,100)然后移动画布对象会发现矩形的绘制并没有效果

平移，旋转，缩放，错切影响的是Canvas还是View的坐标系？

个人任何选择，平移，缩放等操作影响的应该是View的坐标系，而非Canvas本身

2020.07.21 感觉操作的应该是画布对象本身而非坐标系

public void translate(float dx, float dy)

# 常见方法

Canvas 的方法大致可以分为两类 drawXXXX 和 画布的操作(旋转，平移，缩放)



移动画布，dx为正代表向当前坐标系X轴的正方向移动dx，为负则表示向X轴的负方向移动dx，dy同理

public void scale(float sx, float sy)

缩放画布， sx,sy是缩放因子。即原来的坐标(x,y)变成 (dx*x,dy*y)


public final void scale(float sx, float sy, float px, float py)

以px，py作为中心点，缩放画布对象，即原来的坐标 (x,y) 转化为 (dx*(x-px),dy*(y-dy))

public void rotate(float degrees)

以当前坐标系的原点旋转degrees，degrees为正顺时针旋转，为负逆时针旋转。  
注意 degress 是角度而非弧度

public final void rotate(float degrees, float px, float py)

~~该方法有点奇葩，先移动再旋转最后在移动，注意移动是基于当前坐标系而言所以其结果与 上一方法并不同~~

以点(px,py)作为中心点，旋转degrees

```
    public final void rotate(float degrees, float px, float py) {
        if (degrees == 0.0f) return;
        translate(px, py);
        rotate(degrees);
        translate(-px, -py);
    }
```


public void skew(float sx, float sy)

错切


# 所有对外方法

Canvas 对外的方法如下:

public long getNativeCanvasWrapper()

public boolean isRecordingFor(Object o)

public Canvas()

public Canvas(@NonNull Bitmap bitmap)

public Canvas(long nativeCanvas)

public boolean isHardwareAccelerated()

public void setBitmap(@Nullable Bitmap bitmap)

public void insertReorderBarrier()

public void insertInorderBarrier()

public boolean isOpaque()

public int getWidth()

public int getHeight()

public int getDensity()

public void setDensity(int density)

public void setScreenDensity(int density)

public int getMaximumBitmapWidth()

public int getMaximumBitmapHeight()

public int save()

public int save(@Saveflags int saveFlags)

public int saveLayer(@Nullable RectF bounds, @Nullable Paint paint, @Saveflags int saveFlags)

public int saveLayer(@Nullable RectF bounds, @Nullable Paint paint)

public int saveUnclippedLayer(int left, int top, int right, int bottom)

public int saveLayer(float left, float top, float right, float bottom, @Nullable Paint paint, @Saveflags int saveFlags)

public int saveLayer(float left, float top, float right, float bottom, @Nullable Paint paint)

public int saveLayerAlpha(@Nullable RectF bounds, int alpha, @Saveflags int saveFlags)

public int saveLayerAlpha(@Nullable RectF bounds, int alpha)

public int saveLayerAlpha(float left, float top, float right, float bottom, int alpha,
            @Saveflags int saveFlags)

public int saveLayerAlpha(float left, float top, float right, float bottom, int alpha)

public void restore()

public int getSaveCount()

public void restoreToCount(int saveCount)

public void translate(float dx, float dy)

public void scale(float sx, float sy)

public final void scale(float sx, float sy, float px, float py)

public void rotate(float degrees)

public final void rotate(float degrees, float px, float py)

public void skew(float sx, float sy)

public void concat(@Nullable Matrix matrix)

public void setMatrix(@Nullable Matrix matrix)

public void getMatrix(@NonNull Matrix ctm)

public final @NonNull Matrix getMatrix()

public boolean clipRect(@NonNull RectF rect, @NonNull Region.Op op)

public boolean clipRect(@NonNull Rect rect, @NonNull Region.Op op)

public boolean clipRectUnion(@NonNull Rect rect)

public boolean clipRect(@NonNull RectF rect)

public boolean clipOutRect(@NonNull RectF rect)

public boolean clipRect(@NonNull Rect rect)

public boolean clipOutRect(@NonNull Rect rect)

public boolean clipRect(float left, float top, float right, float bottom, @NonNull Region.Op op)

public boolean clipRect(float left, float top, float right, float bottom)

public boolean clipOutRect(float left, float top, float right, float bottom)

public boolean clipRect(int left, int top, int right, int bottom)

public boolean clipOutRect(int left, int top, int right, int bottom)

public boolean clipPath(@NonNull Path path, @NonNull Region.Op op)

public boolean clipPath(@NonNull Path path)

public boolean clipOutPath(@NonNull Path path)

public boolean clipRegion(@NonNull Region region, @NonNull Region.Op op)

public boolean clipRegion(@NonNull Region region)

public @Nullable DrawFilter getDrawFilter()

public void setDrawFilter(@Nullable DrawFilter filter)

public boolean quickReject(@NonNull RectF rect, @NonNull EdgeType type)

public boolean quickReject(@NonNull Path path, @NonNull EdgeType type)

public boolean quickReject(float left, float top, float right, float bottom,
            @NonNull EdgeType type)

public boolean getClipBounds(@Nullable Rect bounds)

public final @NonNull Rect getClipBounds()

public void drawPicture(@NonNull Picture picture)

public void drawPicture(@NonNull Picture picture, @NonNull RectF dst)

public void drawPicture(@NonNull Picture picture, @NonNull Rect dst)

public void release()

public static void freeCaches()

public static void freeTextLayoutCaches()

public static void setCompatibilityVersion(int apiLevel)

public void drawArc(@NonNull RectF oval, float startAngle, float sweepAngle, boolean useCenter,
            @NonNull Paint paint)

public void drawArc(float left, float top, float right, float bottom, float startAngle,
            float sweepAngle, boolean useCenter, @NonNull Paint paint)

public void drawARGB(int a, int r, int g, int b)

public void drawBitmap(@NonNull Bitmap bitmap, float left, float top, @Nullable Paint paint)

public void drawBitmap(@NonNull Bitmap bitmap, @Nullable Rect src, @NonNull RectF dst,
            @Nullable Paint paint)

public void drawBitmap(@NonNull Bitmap bitmap, @Nullable Rect src, @NonNull Rect dst,
            @Nullable Paint paint)

public void drawBitmap(@NonNull int[] colors, int offset, int stride, float x, float y,
            int width, int height, boolean hasAlpha, @Nullable Paint paint)

public void drawBitmap(@NonNull int[] colors, int offset, int stride, int x, int y,
            int width, int height, boolean hasAlpha, @Nullable Paint paint)

public void drawBitmap(@NonNull Bitmap bitmap, @NonNull Matrix matrix, @Nullable Paint paint)

public void drawBitmapMesh(@NonNull Bitmap bitmap, int meshWidth, int meshHeight,
            @NonNull float[] verts, int vertOffset, @Nullable int[] colors, int colorOffset,
            @Nullable Paint paint)

public void drawCircle(float cx, float cy, float radius, @NonNull Paint paint)

public void drawColor(@ColorInt int color)

public void drawColor(@ColorInt int color, @NonNull PorterDuff.Mode mode)

public void drawLine(float startX, float startY, float stopX, float stopY,
            @NonNull Paint paint)

public void drawOval(@NonNull RectF oval, @NonNull Paint paint)

public void drawOval(float left, float top, float right, float bottom, @NonNull Paint paint)

public void drawPaint(@NonNull Paint paint)

public void drawPatch(@NonNull NinePatch patch, @NonNull Rect dst, @Nullable Paint paint)

public void drawPatch(@NonNull NinePatch patch, @NonNull RectF dst, @Nullable Paint paint)

public void drawPath(@NonNull Path path, @NonNull Paint paint)

public void drawPoint(float x, float y, @NonNull Paint paint)

public void drawRect(@NonNull RectF rect, @NonNull Paint paint)

public void drawRect(@NonNull Rect r, @NonNull Paint paint)

public void drawRect(float left, float top, float right, float bottom, @NonNull Paint paint)

public void drawRGB(int r, int g, int b)

public void drawRoundRect(@NonNull RectF rect, float rx, float ry, @NonNull Paint paint)

public void drawRoundRect(float left, float top, float right, float bottom, float rx, float ry,
            @NonNull Paint paint)

public void drawText(@NonNull char[] text, int index, int count, float x, float y,
            @NonNull Paint paint)

public void drawText(@NonNull String text, float x, float y, @NonNull Paint paint)

public void drawText(@NonNull String text, int start, int end, float x, float y,
            @NonNull Paint paint)

public void drawText(@NonNull CharSequence text, int start, int end, float x, float y,
            @NonNull Paint paint)

public void drawTextOnPath(@NonNull char[] text, int index, int count, @NonNull Path path,
            float hOffset, float vOffset, @NonNull Paint paint)

public void drawTextOnPath(@NonNull String text, @NonNull Path path, float hOffset,
            float vOffset, @NonNull Paint paint)

public void drawTextRun(@NonNull char[] text, int index, int count, int contextIndex,
            int contextCount, float x, float y, boolean isRtl, @NonNull Paint paint)

public void drawTextRun(@NonNull CharSequence text, int start, int end, int contextStart,
            int contextEnd, float x, float y, boolean isRtl, @NonNull Paint paint)

public void drawVertices(@NonNull VertexMode mode, int vertexCount, @NonNull float[] verts,
            int vertOffset, @Nullable float[] texs, int texOffset, @Nullable int[] colors,
            int colorOffset, @Nullable short[] indices, int indexOffset, int indexCount,
            @NonNull Paint paint)
