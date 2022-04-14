[TOC]


MotionEvent 是 View System 的事件分发中触控事件信息的封装。MotionEvent常用的对外方法如下:

Android 系统的input事件例如触控事件是可以通过查看 `/dev/input/` 查看所有的输入事件，Android为此提供了 `getevent` 命令，另外一种更简单的方式是打开设备的开发者选项-输入-指针位置 即可看到触控的坐标位置

# 常用对外方法

public final float getX()

返回触控事件的X轴坐标，以当前View的左上角作为坐标原点

public final float getY()

返回触控事件的Y轴坐标，以当前View的左上角作为坐标原点

public final float getPressure()

获取按压的力度大小

public final float getX(int pointerIndex)

针对多点触控的情况，返回 pointerIndex 所指向的触控点的X坐标

public final float getY(int pointerIndex)

public final float getPressure(int pointerIndex)

public final float getRawX()

返回触控事件相对屏幕左上角的X坐标

public final float getRawY()

返回触控事件相对屏幕左上角的Y坐标

# 所有对外方法
public MotionEvent obtain(long downTime, long eventTime,
            int action, int pointerCount, PointerProperties[] pointerProperties,
            PointerCoords[] pointerCoords, int metaState, int buttonState,
            float xPrecision, float yPrecision, int deviceId,
            int edgeFlags, int source, int flags)

public MotionEvent obtain(long downTime, long eventTime,
            int action, int pointerCount, int[] pointerIds, PointerCoords[] pointerCoords,
            int metaState, float xPrecision, float yPrecision, int deviceId,
            int edgeFlags, int source, int flags)

public MotionEvent obtain(long downTime, long eventTime, int action,
            float x, float y, float pressure, float size, int metaState,
            float xPrecision, float yPrecision, int deviceId, int edgeFlags)

public MotionEvent obtain(long downTime, long eventTime, int action,
            int pointerCount, float x, float y, float pressure, float size, int metaState,
            float xPrecision, float yPrecision, int deviceId, int edgeFlags)

public MotionEvent obtain(long downTime, long eventTime, int action,
            float x, float y, int metaState)

public MotionEvent obtain(MotionEvent other)

public MotionEvent obtainNoHistory(MotionEvent other)

public MotionEvent copy()

public final void recycle()

public final void scale(float scale)

public final int getDeviceId()

public final int getSource()

public final void setSource(int source)

public final int getAction()

public final int getActionMasked()

public final int getActionIndex()

public final boolean isTouchEvent()

public final int getFlags()

public final boolean isTainted()

public final void setTainted(boolean tainted)

public final boolean isTargetAccessibilityFocus()

public final void setTargetAccessibilityFocus(boolean targetsFocus)

public final boolean isHoverExitPending()

public void setHoverExitPending(boolean hoverExitPending)

public final long getDownTime()

public final void setDownTime(long downTime)

public final long getEventTime()

public final long getEventTimeNano()

public final float getX()

public final float getY()

public final float getPressure()

public final float getSize()

public final float getTouchMajor()

public final float getTouchMinor()

public final float getToolMajor()

public final float getToolMinor()

public final float getOrientation()

public final float getAxisValue(int axis)

public final int getPointerCount()

public final int getPointerId(int pointerIndex)

public final int getToolType(int pointerIndex)

public final int findPointerIndex(int pointerId)

public final float getX(int pointerIndex)

public final float getY(int pointerIndex)

public final float getPressure(int pointerIndex)

public final float getSize(int pointerIndex)

public final float getTouchMajor(int pointerIndex)

public final float getTouchMinor(int pointerIndex)

public final float getToolMajor(int pointerIndex)

public final float getToolMinor(int pointerIndex)

public final float getOrientation(int pointerIndex)

public final float getAxisValue(int axis, int pointerIndex)

public final void getPointerCoords(int pointerIndex, PointerCoords outPointerCoords)

public final void getPointerProperties(int pointerIndex,
            PointerProperties outPointerProperties)

public final int getMetaState()

public final int getButtonState()

public final void setButtonState(int buttonState)

public final int getActionButton()

public final void setActionButton(int button)

public final float getRawX()

public final float getRawY()

public final float getXPrecision()

public final float getYPrecision()

public final int getHistorySize()

public final long getHistoricalEventTime(int pos)

public final long getHistoricalEventTimeNano(int pos)

public final float getHistoricalX(int pos)

public final float getHistoricalY(int pos)

public final float getHistoricalPressure(int pos)

public final float getHistoricalSize(int pos)

public final float getHistoricalTouchMajor(int pos)

public final float getHistoricalTouchMinor(int pos)

public final float getHistoricalToolMajor(int pos)

public final float getHistoricalToolMinor(int pos)

public final float getHistoricalOrientation(int pos)

public final float getHistoricalAxisValue(int axis, int pos)

public final float getHistoricalX(int pointerIndex, int pos)

public final float getHistoricalY(int pointerIndex, int pos)

public final float getHistoricalPressure(int pointerIndex, int pos)

public final float getHistoricalSize(int pointerIndex, int pos)

public final float getHistoricalTouchMajor(int pointerIndex, int pos)

public final float getHistoricalTouchMinor(int pointerIndex, int pos)

public final float getHistoricalToolMajor(int pointerIndex, int pos)

public final float getHistoricalToolMinor(int pointerIndex, int pos)

public final float getHistoricalOrientation(int pointerIndex, int pos)

public final float getHistoricalAxisValue(int axis, int pointerIndex, int pos)

public final void getHistoricalPointerCoords(int pointerIndex, int pos,
            PointerCoords outPointerCoords)

public final int getEdgeFlags()

public final void setEdgeFlags(int flags)

public final void setAction(int action)

public final void offsetLocation(float deltaX, float deltaY)

public final void setLocation(float x, float y)

public final void transform(Matrix matrix)

public final void addBatch(long eventTime, float x, float y,
            float pressure, float size, int metaState)

public final void addBatch(long eventTime, PointerCoords[] pointerCoords, int metaState)

public final boolean addBatch(MotionEvent event)

public final boolean isWithinBoundsNoHistory(float left, float top,
            float right, float bottom)

public final MotionEvent clampNoHistory(float left, float top, float right, float bottom)

public final int getPointerIdBits()

public final MotionEvent split(int idBits)

public String toString()

public static String actionToString(int action)

public static String axisToString(int axis)

public static int axisFromString(String symbolicName)

public static String buttonStateToString(int buttonState)

public static String toolTypeToString(int toolType)

public final boolean isButtonPressed(int button)

public MotionEvent createFromParcel(Parcel in)

public MotionEvent[] newArray(int size)

public static MotionEvent createFromParcelBody(Parcel in)

public final void cancel()

public void writeToParcel(Parcel out, int flags)

public PointerCoords()

public PointerCoords(PointerCoords other)

public static PointerCoords[] createArray(int size)

public void clear()

public void copyFrom(PointerCoords other)

public float getAxisValue(int axis)

public void setAxisValue(int axis, float value)

public PointerProperties()

public PointerProperties(PointerProperties other)

public static PointerProperties[] createArray(int size)

public void clear()

public void copyFrom(PointerProperties other)

public boolean equals(Object other)

public int hashCode()
