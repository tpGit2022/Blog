public Path()

public Path(Path src)

public void reset()

public void rewind()

public void set(@NonNull Path src)

public boolean op(Path path, Op op)

public boolean op(Path path1, Path path2, Op op)

public boolean isConvex()

public FillType getFillType()

public void setFillType(FillType ft)

public boolean isInverseFillType()

public void toggleInverseFillType()

public boolean isEmpty()

public boolean isRect(@Nullable  RectF rect)

public void computeBounds(RectF bounds, boolean exact)

public void incReserve(int extraPtCount)

public void moveTo(float x, float y)

public void rMoveTo(float dx, float dy)

Path 绘制辅助类，对外方法如下：

public void lineTo(float x, float y)

public void rLineTo(float dx, float dy)

public void quadTo(float x1, float y1, float x2, float y2)

public void rQuadTo(float dx1, float dy1, float dx2, float dy2)

public void cubicTo(float x1, float y1, float x2, float y2,
                        float x3, float y3)

public void rCubicTo(float x1, float y1, float x2, float y2,
                         float x3, float y3)

public void arcTo(RectF oval, float startAngle, float sweepAngle,
                      boolean forceMoveTo)

public void arcTo(RectF oval, float startAngle, float sweepAngle)

public void arcTo(float left, float top, float right, float bottom, float startAngle,
            float sweepAngle, boolean forceMoveTo)

public void close()

public void addRect(RectF rect, Direction dir)

public void addRect(float left, float top, float right, float bottom, Direction dir)

public void addOval(RectF oval, Direction dir)

public void addOval(float left, float top, float right, float bottom, Direction dir)

public void addCircle(float x, float y, float radius, Direction dir)

public void addArc(RectF oval, float startAngle, float sweepAngle)

public void addArc(float left, float top, float right, float bottom, float startAngle,
            float sweepAngle)

public void addRoundRect(RectF rect, float rx, float ry, Direction dir)

public void addRoundRect(float left, float top, float right, float bottom, float rx, float ry,
            Direction dir)

public void addRoundRect(RectF rect, float[] radii, Direction dir)

public void addRoundRect(float left, float top, float right, float bottom, float[] radii,
            Direction dir)

public void addPath(Path src, float dx, float dy)

public void addPath(Path src)

public void addPath(Path src, Matrix matrix)

public void offset(float dx, float dy, @Nullable Path dst)

public void offset(float dx, float dy)

public void setLastPoint(float dx, float dy)

public void transform(Matrix matrix, Path dst)

public void transform(Matrix matrix)

public final long readOnlyNI()
