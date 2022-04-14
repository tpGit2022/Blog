[TOC]

View System 是 Android 系统的重要组分部分之一，代码位于 `frameworks/base/core/java/android/view/View.java`

# 常用对外方法

public final int getTop()

public final void setTop(int top)

public final int getBottom()

public boolean isDirty()

public final void setBottom(int bottom)

public final int getLeft()

public final void setLeft(int left)

public final int getRight()

public final void setRight(int right)

public float getX()

public void setX(float x)

public float getY()

public void setY(float y)

public float getZ()

public void setZ(float z)

public float getElevation()

public void setElevation(float elevation)

public float getTranslationX()

public void setTranslationX(float translationX)

public float getTranslationY()

public void setTranslationY(float translationY)

public float getTranslationZ()

public void setTranslationZ(float translationZ)

public void scrollTo(int x, int y)

public void scrollBy(int x, int y)

public void invalidate(Rect dirty)

public void invalidate(int l, int t, int r, int b)

public void invalidate()

public void invalidate(boolean invalidateCache)
public void postInvalidate()

public void postInvalidate(int left, int top, int right, int bottom)

public void postInvalidateDelayed(long delayMilliseconds)

public void postInvalidateDelayed(long delayMilliseconds, int left, int top,
            int right, int bottom)

public void postInvalidateOnAnimation()

public void postInvalidateOnAnimation(int left, int top, int right, int bottom)

public void computeScroll()

public void draw(Canvas canvas)
public void layout(int l, int t, int r, int b)
public void setBackgroundColor(@ColorInt int color)

public void setBackgroundResource(@DrawableRes int resid)

public void setBackground(Drawable background)

public void setBackgroundDrawable(Drawable background)

public Drawable getBackground()

public void setBackgroundTintList(@Nullable ColorStateList tint)

public ColorStateList getBackgroundTintList()

public void setBackgroundTintMode(@Nullable PorterDuff.Mode tintMode)

public Drawable getForeground()

public void setForeground(Drawable foreground)

public boolean isForegroundInsidePadding()

public int getForegroundGravity()

public void setForegroundGravity(int gravity)

public void setForegroundTintList(@Nullable ColorStateList tint)

public ColorStateList getForegroundTintList()

public void setForegroundTintMode(@Nullable PorterDuff.Mode tintMode)

public void onDrawForeground(Canvas canvas)

public void setPadding(int left, int top, int right, int bottom)

public void setPaddingRelative(int start, int top, int end, int bottom)

public int getPaddingTop()

public int getPaddingBottom()

public int getPaddingLeft()

public int getPaddingStart()

public int getPaddingRight()

public int getPaddingEnd()

public void requestLayout()

public void forceLayout()

public static int getDefaultSize(int size, int measureSpec)

public int getMinimumHeight()

public void setMinimumHeight(int minHeight)

public int getMinimumWidth()

public void setMinimumWidth(int minWidth)

public Animation getAnimation()

public void startAnimation(Animation animation)

public void clearAnimation()

public void setAnimation(Animation animation)


# 所有对外方法

public View(Context context)

public View(Context context, @Nullable AttributeSet attrs)

public View(Context context, @Nullable AttributeSet attrs, int defStyleAttr)

public View(Context context, @Nullable AttributeSet attrs, int defStyleAttr, int defStyleRes)

public DeclaredOnClickListener(@NonNull View hostView, @NonNull String methodName)

public void onClick(@NonNull View v)

public String toString()

public int getVerticalFadingEdgeLength()

public void setFadingEdgeLength(int length)

public int getHorizontalFadingEdgeLength()

public int getVerticalScrollbarWidth()

public void setVerticalScrollbarPosition(int position)

public int getVerticalScrollbarPosition()

public void setScrollIndicators(@ScrollIndicators int indicators)

public void setScrollIndicators(@ScrollIndicators int indicators, @ScrollIndicators int mask)

public int getScrollIndicators()

public void setOnScrollChangeListener(OnScrollChangeListener l)

public void setOnFocusChangeListener(OnFocusChangeListener l)

public void addOnLayoutChangeListener(OnLayoutChangeListener listener)

public void removeOnLayoutChangeListener(OnLayoutChangeListener listener)

public void addOnAttachStateChangeListener(OnAttachStateChangeListener listener)

public void removeOnAttachStateChangeListener(OnAttachStateChangeListener listener)

public OnFocusChangeListener getOnFocusChangeListener()

public void setOnClickListener(@Nullable OnClickListener l)

public boolean hasOnClickListeners()

public void setOnLongClickListener(@Nullable OnLongClickListener l)

public void setOnContextClickListener(@Nullable OnContextClickListener l)

public void setOnCreateContextMenuListener(OnCreateContextMenuListener l)

public void addFrameMetricsListener(Window window,
            Window.OnFrameMetricsAvailableListener listener,
            Handler handler)

public void removeFrameMetricsListener(
            Window.OnFrameMetricsAvailableListener listener)

public void setNotifyAutofillManagerOnClick(boolean notify)

public boolean performClick()

public boolean callOnClick()

public boolean performLongClick()

public boolean performLongClick(float x, float y)

public boolean performContextClick(float x, float y)

public boolean performContextClick()

public boolean showContextMenu()

public boolean showContextMenu(float x, float y)

public ActionMode startActionMode(ActionMode.Callback callback)

public ActionMode startActionMode(ActionMode.Callback callback, int type)

public void startActivityForResult(Intent intent, int requestCode)

public boolean dispatchActivityResult(
            String who, int requestCode, int resultCode, Intent data)

public void onActivityResult(int requestCode, int resultCode, Intent data)

public void setOnKeyListener(OnKeyListener l)

public void setOnTouchListener(OnTouchListener l)

public void setOnGenericMotionListener(OnGenericMotionListener l)

public void setOnHoverListener(OnHoverListener l)

public void setOnDragListener(OnDragListener l)

public final void setRevealOnFocusHint(boolean revealOnFocus)

public final boolean getRevealOnFocusHint()

public void getHotspotBounds(Rect outRect)

public boolean requestRectangleOnScreen(Rect rectangle)

public boolean requestRectangleOnScreen(Rect rectangle, boolean immediate)

public void clearFocus()

public boolean hasFocus()

public boolean hasFocusable()

public boolean hasExplicitFocusable()

public void notifyEnterOrExitForAutoFillIfNeeded(boolean enter)

public void setAccessibilityPaneTitle(@Nullable CharSequence accessibilityPaneTitle)

public CharSequence getAccessibilityPaneTitle()

public void sendAccessibilityEvent(int eventType)

public void announceForAccessibility(CharSequence text)

public void sendAccessibilityEventInternal(int eventType)

public void sendAccessibilityEventUnchecked(AccessibilityEvent event)

public void sendAccessibilityEventUncheckedInternal(AccessibilityEvent event)

public boolean dispatchPopulateAccessibilityEvent(AccessibilityEvent event)

public boolean dispatchPopulateAccessibilityEventInternal(AccessibilityEvent event)

public void onPopulateAccessibilityEvent(AccessibilityEvent event)

public void onPopulateAccessibilityEvent(AccessibilityEvent event)

public void onPopulateAccessibilityEventInternal(AccessibilityEvent event)

public void onInitializeAccessibilityEvent(AccessibilityEvent event)

public void onInitializeAccessibilityEvent(AccessibilityEvent event)

public void onInitializeAccessibilityEventInternal(AccessibilityEvent event)

public AccessibilityNodeInfo createAccessibilityNodeInfo()

public AccessibilityNodeInfo createAccessibilityNodeInfoInternal()

public void onInitializeAccessibilityNodeInfo(AccessibilityNodeInfo info)

public void getBoundsOnScreen(Rect outRect)

public void getBoundsOnScreen(Rect outRect, boolean clipToParent)

public void mapRectFromViewToScreenCoords(RectF rect, boolean clipToParent)

public CharSequence getAccessibilityClassName()

public void onProvideStructure(ViewStructure structure)

public void onProvideAutofillStructure(ViewStructure structure, @AutofillFlags int flags)

public void onProvideVirtualStructure(ViewStructure structure)

public void onProvideAutofillVirtualStructure(ViewStructure structure, int flags)

public void autofill(AutofillValue value)

public final AutofillId getAutofillId()

public void setAutofillId(@Nullable AutofillId id)

public @AutofillType int getAutofillType()

public String[] getAutofillHints()

public boolean isAutofilled()

public AutofillValue getAutofillValue()

public @AutofillImportance int getImportantForAutofill()

public void setImportantForAutofill(@AutofillImportance int mode)

public final boolean isImportantForAutofill()

public boolean canNotifyAutofillEnterExitEvent()

public void dispatchProvideStructure(ViewStructure structure)

public void dispatchProvideAutofillStructure(@NonNull ViewStructure structure,
            @AutofillFlags int flags)

public void onInitializeAccessibilityNodeInfoInternal(AccessibilityNodeInfo info)

public void addExtraDataToAccessibilityNodeInfo(
            @NonNull AccessibilityNodeInfo info, @NonNull String extraDataKey,
            @Nullable Bundle arguments)

public boolean isVisibleToUserForAutofill(int virtualId)

public boolean isVisibleToUser()

public AccessibilityDelegate getAccessibilityDelegate()

public void setAccessibilityDelegate(@Nullable AccessibilityDelegate delegate)

public AccessibilityNodeProvider getAccessibilityNodeProvider()

public int getAccessibilityViewId()

public int getAutofillViewId()

public int getAccessibilityWindowId()

public CharSequence getContentDescription()

public void setContentDescription(CharSequence contentDescription)

public void setAccessibilityTraversalBefore(int beforeId)

public int getAccessibilityTraversalBefore()

public void setAccessibilityTraversalAfter(int afterId)

public int getAccessibilityTraversalAfter()

public int getLabelFor()

public void setLabelFor(@IdRes int id)

public boolean isFocused()

public View findFocus()

public boolean isScrollContainer()

public void setScrollContainer(boolean isScrollContainer)

public int getDrawingCacheQuality()

public void setDrawingCacheQuality(@DrawingCacheQuality int quality)

public boolean getKeepScreenOn()

public void setKeepScreenOn(boolean keepScreenOn)

public int getNextFocusLeftId()

public void setNextFocusLeftId(int nextFocusLeftId)

public int getNextFocusRightId()

public void setNextFocusRightId(int nextFocusRightId)

public int getNextFocusUpId()

public void setNextFocusUpId(int nextFocusUpId)

public int getNextFocusDownId()

public void setNextFocusDownId(int nextFocusDownId)

public int getNextFocusForwardId()

public void setNextFocusForwardId(int nextFocusForwardId)

public int getNextClusterForwardId()

public void setNextClusterForwardId(int nextClusterForwardId)

public boolean isShown()

public WindowInsets onApplyWindowInsets(WindowInsets insets)

public void setOnApplyWindowInsetsListener(OnApplyWindowInsetsListener listener)

public WindowInsets dispatchApplyWindowInsets(WindowInsets insets)

public WindowInsets getRootWindowInsets()

public WindowInsets computeSystemWindowInsets(WindowInsets in, Rect outLocalInsets)

public void setFitsSystemWindows(boolean fitSystemWindows)

public boolean getFitsSystemWindows()

public boolean fitsSystemWindows()

public void requestFitSystemWindows()

public void requestApplyInsets()

public void makeOptionalFitsSystemWindows()

public void getOutsets(Rect outOutsetRect)

public int getVisibility()

public void setVisibility(@Visibility int visibility)

public boolean isEnabled()

public void setEnabled(boolean enabled)

public void setFocusable(boolean focusable)

public void setFocusable(@Focusable int focusable)

public void setFocusableInTouchMode(boolean focusableInTouchMode)

public void setAutofillHints(@Nullable String... autofillHints)

public void setAutofilled(boolean isAutofilled)

public void setSoundEffectsEnabled(boolean soundEffectsEnabled)

public boolean isSoundEffectsEnabled()

public void setHapticFeedbackEnabled(boolean hapticFeedbackEnabled)

public boolean isHapticFeedbackEnabled()

public int getRawLayoutDirection()

public void setLayoutDirection(@LayoutDir int layoutDirection)

public int getLayoutDirection()

public boolean isLayoutRtl()

public boolean hasTransientState()

public void setHasTransientState(boolean hasTransientState)

public boolean isAttachedToWindow()

public boolean isLaidOut()

public void setWillNotDraw(boolean willNotDraw)

public boolean willNotDraw()

public void setWillNotCacheDrawing(boolean willNotCacheDrawing)

public boolean willNotCacheDrawing()

public boolean isClickable()

public void setClickable(boolean clickable)

public boolean isLongClickable()

public void setLongClickable(boolean longClickable)

public boolean isContextClickable()

public void setContextClickable(boolean contextClickable)

public void setPressed(boolean pressed)

public boolean isPressed()

public boolean isAssistBlocked()

public void setAssistBlocked(boolean enabled)

public boolean isSaveEnabled()

public void setSaveEnabled(boolean enabled)

public boolean getFilterTouchesWhenObscured()

public void setFilterTouchesWhenObscured(boolean enabled)

public boolean isSaveFromParentEnabled()

public void setSaveFromParentEnabled(boolean enabled)

public final boolean isFocusable()

public int getFocusable()

public final boolean isFocusableInTouchMode()

public boolean isScreenReaderFocusable()

public void setScreenReaderFocusable(boolean screenReaderFocusable)

public boolean isAccessibilityHeading()

public void setAccessibilityHeading(boolean isHeading)

public View focusSearch(@FocusRealDirection int direction)

public final boolean isKeyboardNavigationCluster()

public void setKeyboardNavigationCluster(boolean isCluster)

public final void setFocusedInCluster()

public final boolean isFocusedByDefault()

public void setFocusedByDefault(boolean isFocusedByDefault)

public View keyboardNavigationClusterSearch(View currentCluster,
            @FocusDirection int direction)

public boolean dispatchUnhandledMove(View focused, @FocusRealDirection int direction)

public void setDefaultFocusHighlightEnabled(boolean defaultFocusHighlightEnabled)

public final boolean getDefaultFocusHighlightEnabled()

public boolean test(View t)

public ArrayList<View> getFocusables(@FocusDirection int direction)

public void addFocusables(ArrayList<View> views, @FocusDirection int direction)

public void addFocusables(ArrayList<View> views, @FocusDirection int direction,
            @FocusableMode int focusableMode)

public void addKeyboardNavigationClusters(
            @NonNull Collection<View> views,
            int direction)

public void findViewsWithText(ArrayList<View> outViews, CharSequence searched,
            @FindViewFlags int flags)

public ArrayList<View> getTouchables()

public void addTouchables(ArrayList<View> views)

public boolean isAccessibilityFocused()

public boolean requestAccessibilityFocus()

public void clearAccessibilityFocus()

public final boolean requestFocus()

public boolean restoreFocusInCluster(@FocusRealDirection int direction)

public boolean restoreFocusNotInCluster()

public boolean restoreDefaultFocus()

public final boolean requestFocus(int direction)

public boolean requestFocus(int direction, Rect previouslyFocusedRect)

public final boolean requestFocusFromTouch()

public int getImportantForAccessibility()

public void setAccessibilityLiveRegion(int mode)

public int getAccessibilityLiveRegion()

public void setImportantForAccessibility(int mode)

public boolean isImportantForAccessibility()

public ViewParent getParentForAccessibility()

public void addChildrenForAccessibility(ArrayList<View> outChildren)

public boolean includeForAccessibility()

public boolean isActionableForAccessibility()

public void notifyViewAccessibilityStateChangedIfNeeded(int changeType)

public void notifySubtreeAccessibilityStateChangedIfNeeded()

public void setTransitionVisibility(@Visibility int visibility)

public boolean dispatchNestedPrePerformAccessibilityAction(int action, Bundle arguments)

public boolean performAccessibilityAction(int action, Bundle arguments)

public boolean performAccessibilityActionInternal(int action, Bundle arguments)

public CharSequence getIterableTextForAccessibility()

public boolean isAccessibilitySelectionExtendable()

public int getAccessibilitySelectionStart()

public int getAccessibilitySelectionEnd()

public void setAccessibilitySelection(int start, int end)

public TextSegmentIterator getIteratorForGranularity(int granularity)

public final boolean isTemporarilyDetached()

public void dispatchStartTemporaryDetach()

public void onStartTemporaryDetach()

public void dispatchFinishTemporaryDetach()

public void onFinishTemporaryDetach()

public boolean dispatchKeyEventPreIme(KeyEvent event)

public boolean dispatchKeyEvent(KeyEvent event)

public boolean dispatchKeyShortcutEvent(KeyEvent event)

public boolean dispatchTouchEvent(MotionEvent event)

public boolean onFilterTouchEventForSecurity(MotionEvent event)

public boolean dispatchTrackballEvent(MotionEvent event)

public boolean dispatchCapturedPointerEvent(MotionEvent event)

public boolean dispatchGenericMotionEvent(MotionEvent event)

public final boolean dispatchPointerEvent(MotionEvent event)

public void dispatchWindowFocusChanged(boolean hasFocus)

public void onWindowFocusChanged(boolean hasWindowFocus)

public boolean hasWindowFocus()

public void dispatchDisplayHint(@Visibility int hint)

public void dispatchWindowVisibilityChanged(@Visibility int visibility)

public void onVisibilityAggregated(boolean isVisible)

public int getWindowVisibility()

public void getWindowVisibleDisplayFrame(Rect outRect)

public void getWindowDisplayFrame(Rect outRect)

public void dispatchConfigurationChanged(Configuration newConfig)

public boolean isInTouchMode()

public final Context getContext()

public boolean onKeyPreIme(int keyCode, KeyEvent event)

public boolean onKeyDown(int keyCode, KeyEvent event)

public boolean onKeyLongPress(int keyCode, KeyEvent event)

public boolean onKeyUp(int keyCode, KeyEvent event)

public boolean onKeyMultiple(int keyCode, int repeatCount, KeyEvent event)

public boolean onKeyShortcut(int keyCode, KeyEvent event)

public boolean onCheckIsTextEditor()

public InputConnection onCreateInputConnection(EditorInfo outAttrs)

public boolean checkInputConnectionProxy(View view)

public void createContextMenu(ContextMenu menu)

public boolean onTrackballEvent(MotionEvent event)

public boolean onGenericMotionEvent(MotionEvent event)

public boolean onGenericMotionEvent(MotionEvent event)

public boolean onHoverEvent(MotionEvent event)

public boolean isHovered()

public void setHovered(boolean hovered)

public void onHoverChanged(boolean hovered)

public boolean onTouchEvent(MotionEvent event)

public boolean isInScrollingContainer()

public void cancelLongPress()

public void setTouchDelegate(TouchDelegate delegate)

public TouchDelegate getTouchDelegate()

public final void requestUnbufferedDispatch(MotionEvent event)

public void bringToFront()

public final ViewParent getParent()

public void setScrollX(int value)

public void setScrollY(int value)

public final int getScrollX()

public final int getScrollY()

public final int getWidth()

public final int getHeight()

public void getDrawingRect(Rect outRect)

public final int getMeasuredWidth()

public final int getMeasuredWidthAndState()

public final int getMeasuredHeight()

public final int getMeasuredHeightAndState()

public final int getMeasuredState()

public Matrix getMatrix()

public final Matrix getInverseMatrix()

public float getCameraDistance()

public void setCameraDistance(float distance)

public float getRotation()

public void setRotation(float rotation)

public float getRotationY()

public void setRotationY(float rotationY)

public float getRotationX()

public void setRotationX(float rotationX)

public float getScaleX()

public void setScaleX(float scaleX)

public float getScaleY()

public void setScaleY(float scaleY)

public float getPivotX()

public void setPivotX(float pivotX)

public float getPivotY()

public void setPivotY(float pivotY)

public boolean isPivotSet()

public void resetPivot()

public float getAlpha()

public void forceHasOverlappingRendering(boolean hasOverlappingRendering)

public final boolean getHasOverlappingRendering()

public boolean hasOverlappingRendering()

public void setTransitionAlpha(float alpha)

public float getTransitionAlpha()

public final int getTop()

public final void setTop(int top)

public final int getBottom()

public boolean isDirty()

public final void setBottom(int bottom)

public final int getLeft()

public final void setLeft(int left)

public final int getRight()

public final void setRight(int right)

public float getX()

public void setX(float x)

public float getY()

public void setY(float y)

public float getZ()

public void setZ(float z)

public float getElevation()

public void setElevation(float elevation)

public float getTranslationX()

public void setTranslationX(float translationX)

public float getTranslationY()

public void setTranslationY(float translationY)

public float getTranslationZ()

public void setTranslationZ(float translationZ)

public void setAnimationMatrix(Matrix matrix)

public StateListAnimator getStateListAnimator()

public void setStateListAnimator(StateListAnimator stateListAnimator)

public final boolean getClipToOutline()

public void setClipToOutline(boolean clipToOutline)

public void setOutlineProvider(ViewOutlineProvider provider)

public ViewOutlineProvider getOutlineProvider()

public void invalidateOutline()

public boolean hasShadow()

public void setOutlineSpotShadowColor(@ColorInt int color)

public @ColorInt int getOutlineSpotShadowColor()

public void setOutlineAmbientShadowColor(@ColorInt int color)

public @ColorInt int getOutlineAmbientShadowColor()

public void setRevealClip(boolean shouldClip, float x, float y, float radius)

public void getHitRect(Rect outRect)

public boolean pointInView(float localX, float localY, float slop)

public void getFocusedRect(Rect r)

public boolean getGlobalVisibleRect(Rect r, Point globalOffset)

public final boolean getGlobalVisibleRect(Rect r)

public final boolean getLocalVisibleRect(Rect r)

public void offsetTopAndBottom(int offset)

public void offsetLeftAndRight(int offset)

public void setLayoutParams(ViewGroup.LayoutParams params)

public void resolveLayoutParams()

public void scrollTo(int x, int y)

public void scrollBy(int x, int y)

public void invalidate(Rect dirty)

public void invalidate(int l, int t, int r, int b)

public void invalidate()

public void invalidate(boolean invalidateCache)

public boolean isOpaque()

public Handler getHandler()

public ViewRootImpl getViewRootImpl()

public ThreadedRenderer getThreadedRenderer()

public boolean post(Runnable action)

public boolean postDelayed(Runnable action, long delayMillis)

public void postOnAnimation(Runnable action)

public void postOnAnimationDelayed(Runnable action, long delayMillis)

public boolean removeCallbacks(Runnable action)

public void postInvalidate()

public void postInvalidate(int left, int top, int right, int bottom)

public void postInvalidateDelayed(long delayMilliseconds)

public void postInvalidateDelayed(long delayMilliseconds, int left, int top,
            int right, int bottom)

public void postInvalidateOnAnimation()

public void postInvalidateOnAnimation(int left, int top, int right, int bottom)

public void computeScroll()

public boolean isHorizontalFadingEdgeEnabled()

public void setHorizontalFadingEdgeEnabled(boolean horizontalFadingEdgeEnabled)

public boolean isVerticalFadingEdgeEnabled()

public void setVerticalFadingEdgeEnabled(boolean verticalFadingEdgeEnabled)

public boolean isHorizontalScrollBarEnabled()

public void setHorizontalScrollBarEnabled(boolean horizontalScrollBarEnabled)

public boolean isVerticalScrollBarEnabled()

public void setVerticalScrollBarEnabled(boolean verticalScrollBarEnabled)

public void setScrollbarFadingEnabled(boolean fadeScrollbars)

public boolean isScrollbarFadingEnabled()

public int getScrollBarDefaultDelayBeforeFade()

public void setScrollBarDefaultDelayBeforeFade(int scrollBarDefaultDelayBeforeFade)

public int getScrollBarFadeDuration()

public void setScrollBarFadeDuration(int scrollBarFadeDuration)

public int getScrollBarSize()

public void setScrollBarSize(int scrollBarSize)

public void setScrollBarStyle(@ScrollBarStyle int style)

public int getScrollBarStyle()

public boolean canScrollHorizontally(int direction)

public boolean canScrollVertically(int direction)

public boolean resolveRtlPropertiesIfNeeded()

public void resetRtlProperties()

public void onScreenStateChanged(int screenState)

public void onMovedToDisplay(int displayId, Configuration config)

public void onRtlPropertiesChanged(@ResolvedLayoutDir int layoutDirection)

public boolean resolveLayoutDirection()

public boolean canResolveLayoutDirection()

public void resetResolvedLayoutDirection()

public boolean isLayoutDirectionInherited()

public boolean isLayoutDirectionResolved()

public void resolvePadding()

public void resetResolvedPadding()

public IBinder getWindowToken()

public WindowId getWindowId()

public IBinder getApplicationWindowToken()

public Display getDisplay()

public final void cancelPendingInputEvents()

public void onCancelPendingInputEvents()

public void saveHierarchyState(SparseArray<Parcelable> container)

public void restoreHierarchyState(SparseArray<Parcelable> container)

public long getDrawingTime()

public void setDuplicateParentStateEnabled(boolean enabled)

public boolean isDuplicateParentStateEnabled()

public void setLayerType(int layerType, @Nullable Paint paint)

public void setLayerPaint(@Nullable Paint paint)

public int getLayerType()

public void buildLayer()

public void setDrawingCacheEnabled(boolean enabled)

public boolean isDrawingCacheEnabled()

public void outputDirtyFlags(String indent, boolean clear, int clearMask)

public boolean canHaveDisplayList()

public RenderNode updateDisplayListIfDirty()

public Bitmap getDrawingCache()

public Bitmap getDrawingCache(boolean autoScale)

public void destroyDrawingCache()

public void setDrawingCacheBackgroundColor(@ColorInt int color)

public int getDrawingCacheBackgroundColor()

public void buildDrawingCache()

public void buildDrawingCache(boolean autoScale)

public Bitmap createSnapshot(ViewDebug.CanvasProvider canvasProvider, boolean skipChildren)

public boolean isInEditMode()

public boolean isHardwareAccelerated()

public void setClipBounds(Rect clipBounds)

public Rect getClipBounds()

public boolean getClipBounds(Rect outRect)

public void draw(Canvas canvas)

public ViewOverlay getOverlay()

public int getSolidColor()

public boolean isLayoutRequested()

public static boolean isLayoutModeOptical(Object o)

public void layout(int l, int t, int r, int b)

public void setLeftTopRightBottom(int left, int top, int right, int bottom)

public Resources getResources()

public void invalidateDrawable(@NonNull Drawable drawable)

public void scheduleDrawable(@NonNull Drawable who, @NonNull Runnable what, long when)

public void unscheduleDrawable(@NonNull Drawable who, @NonNull Runnable what)

public void unscheduleDrawable(Drawable who)

public void onResolveDrawables(@ResolvedLayoutDir int layoutDirection)

public void drawableHotspotChanged(float x, float y)

public void dispatchDrawableHotspotChanged(float x, float y)

public void refreshDrawableState()

public boolean isDefaultFocusHighlightNeeded(Drawable background, Drawable foreground)

public final int[] getDrawableState()

public void jumpDrawablesToCurrentState()

public void setBackgroundColor(@ColorInt int color)

public void setBackgroundResource(@DrawableRes int resid)

public void setBackground(Drawable background)

public void setBackgroundDrawable(Drawable background)

public Drawable getBackground()

public void setBackgroundTintList(@Nullable ColorStateList tint)

public ColorStateList getBackgroundTintList()

public void setBackgroundTintMode(@Nullable PorterDuff.Mode tintMode)

public Drawable getForeground()

public void setForeground(Drawable foreground)

public boolean isForegroundInsidePadding()

public int getForegroundGravity()

public void setForegroundGravity(int gravity)

public void setForegroundTintList(@Nullable ColorStateList tint)

public ColorStateList getForegroundTintList()

public void setForegroundTintMode(@Nullable PorterDuff.Mode tintMode)

public void onDrawForeground(Canvas canvas)

public void setPadding(int left, int top, int right, int bottom)

public void setPaddingRelative(int start, int top, int end, int bottom)

public int getPaddingTop()

public int getPaddingBottom()

public int getPaddingLeft()

public int getPaddingStart()

public int getPaddingRight()

public int getPaddingEnd()

public boolean isPaddingRelative()

public void resetPaddingToInitialValues()

public Insets getOpticalInsets()

public void setOpticalInsets(Insets insets)

public void setSelected(boolean selected)

public boolean isSelected()

public void setActivated(boolean activated)

public boolean isActivated()

public ViewTreeObserver getViewTreeObserver()

public View getRootView()

public boolean toGlobalMotionEvent(MotionEvent ev)

public boolean toLocalMotionEvent(MotionEvent ev)

public void transformMatrixToGlobal(Matrix m)

public void transformMatrixToLocal(Matrix m)

public int[] getLocationOnScreen()

public final <T extends View> T findViewById(@IdRes int id)

public final <T extends View> T requireViewById(@IdRes int id)

public <T extends View> T findViewByAccessibilityIdTraversal(int accessibilityId)

public <T extends View> T findViewByAutofillIdTraversal(int autofillId)

public final <T extends View> T findViewWithTag(Object tag)

public final <T extends View> T findViewByPredicate(Predicate<View> predicate)

public final <T extends View> T findViewByPredicateInsideOut(
            View start, Predicate<View> predicate)

public void setId(@IdRes int id)

public void setIsRootNamespace(boolean isRoot)

public boolean isRootNamespace()

public int getId()

public Object getTag()

public void setTag(final Object tag)

public Object getTag(int key)

public void setTag(int key, final Object tag)

public void setTagInternal(int key, Object tag)

public void debug()

public int getBaseline()

public boolean isInLayout()

public void requestLayout()

public void forceLayout()

public final void measure(int widthMeasureSpec, int heightMeasureSpec)

public static int combineMeasuredStates(int curState, int newState)

public static int resolveSize(int size, int measureSpec)

public static int resolveSizeAndState(int size, int measureSpec, int childMeasuredState)

public static int getDefaultSize(int size, int measureSpec)

public int getMinimumHeight()

public void setMinimumHeight(int minHeight)

public int getMinimumWidth()

public void setMinimumWidth(int minWidth)

public Animation getAnimation()

public void startAnimation(Animation animation)

public void clearAnimation()

public void setAnimation(Animation animation)

public boolean gatherTransparentRegion(Region region)

public void playSoundEffect(int soundConstant)

public boolean performHapticFeedback(int feedbackConstant)

public boolean performHapticFeedback(int feedbackConstant, int flags)

public void setSystemUiVisibility(int visibility)

public int getSystemUiVisibility()

public int getWindowSystemUiVisibility()

public void onWindowSystemUiVisibilityChanged(int visible)

public void dispatchWindowSystemUiVisiblityChanged(int visible)

public void setOnSystemUiVisibilityChangeListener(OnSystemUiVisibilityChangeListener l)

public void dispatchSystemUiVisibilityChanged(int visibility)

public void setDisabledSystemUiVisibility(int flags)

public DragShadowBuilder(View view)

public DragShadowBuilder()

public View getView()

public void onProvideShadowMetrics(Point outShadowSize, Point outShadowTouchPoint)

public void onDrawShadow(Canvas canvas)

public final boolean startDrag(ClipData data, DragShadowBuilder shadowBuilder,
                                   Object myLocalState, int flags)

public final boolean startDragAndDrop(ClipData data, DragShadowBuilder shadowBuilder,
            Object myLocalState, int flags)

public final void cancelDragAndDrop()

public final void updateDragShadow(DragShadowBuilder shadowBuilder)

public final boolean startMovingTask(float startX, float startY)

public boolean onDragEvent(DragEvent event)

public boolean dispatchDragEvent(DragEvent event)

public void onCloseSystemDialogs(String reason)

public void applyDrawableToTransparentRegion(Drawable dr, Region region)

public static View inflate(Context context, @LayoutRes int resource, ViewGroup root)

public int getOverScrollMode()

public void setOverScrollMode(int overScrollMode)

public void setNestedScrollingEnabled(boolean enabled)

public boolean isNestedScrollingEnabled()

public boolean startNestedScroll(int axes)

public void stopNestedScroll()

public boolean hasNestedScrollingParent()

public boolean dispatchNestedFling(float velocityX, float velocityY, boolean consumed)

public boolean dispatchNestedPreFling(float velocityX, float velocityY)

public int getRawTextDirection()

public void setTextDirection(int textDirection)

public int getTextDirection()

public boolean resolveTextDirection()

public boolean canResolveTextDirection()

public void resetResolvedTextDirection()

public boolean isTextDirectionInherited()

public boolean isTextDirectionResolved()

public int getRawTextAlignment()

public void setTextAlignment(@TextAlignment int textAlignment)

public int getTextAlignment()

public boolean resolveTextAlignment()

public boolean canResolveTextAlignment()

public void resetResolvedTextAlignment()

public boolean isTextAlignmentInherited()

public boolean isTextAlignmentResolved()

public static int generateViewId()

public void captureTransitioningViews(List<View> transitioningViews)

public void findNamedViews(Map<String, View> namedElements)

public PointerIcon onResolvePointerIcon(MotionEvent event, int pointerIndex)

public void setPointerIcon(PointerIcon pointerIcon)

public PointerIcon getPointerIcon()

public boolean hasPointerCapture()

public void requestPointerCapture()

public void releasePointerCapture()

public void onPointerCaptureChange(boolean hasCapture)

public void dispatchPointerCaptureChanged(boolean hasCapture)

public boolean onCapturedPointerEvent(MotionEvent event)

public void setOnCapturedPointerListener(OnCapturedPointerListener l)

public void setValue(View object, float value)

public Float get(View object)

public void setValue(View object, float value)

public Float get(View object)

public void setValue(View object, float value)

public Float get(View object)

public void setValue(View object, float value)

public Float get(View object)

public void setValue(View object, float value)

public Float get(View object)

public void setValue(View object, float value)

public Float get(View object)

public void setValue(View object, float value)

public Float get(View object)

public void setValue(View object, float value)

public Float get(View object)

public void setValue(View object, float value)

public Float get(View object)

public void setValue(View object, float value)

public Float get(View object)

public void setValue(View object, float value)

public Float get(View object)

public void setValue(View object, float value)

public Float get(View object)

public static int makeSafeMeasureSpec(int size, int mode)

public static int getMode(int measureSpec)

public static int getSize(int measureSpec)

public static String toString(int measureSpec)

public void run()

public void setAnchor(float x, float y)

public void rememberWindowAttachCount()

public void rememberPressedState()

public void run()

public void run()

public ViewPropertyAnimator animate()

public final void setTransitionName(String transitionName)

public String getTransitionName()

public void requestKeyboardShortcuts(List<KeyboardShortcutGroup> data, int deviceId)

public void onSystemUiVisibilityChange(int visibility)

public void onViewAttachedToWindow(View v)

public void onViewDetachedFromWindow(View v)

public WindowInsets onApplyWindowInsets(View v, WindowInsets insets)

public void run()

public void handleMessage(Message msg)

public BaseSavedState(Parcel source)

public BaseSavedState(Parcel source, ClassLoader loader)

public BaseSavedState(Parcelable superState)

public void writeToParcel(Parcel out, int flags)

public BaseSavedState createFromParcel(Parcel in)

public BaseSavedState createFromParcel(Parcel in, ClassLoader loader)

public BaseSavedState[] newArray(int size)

public static InvalidateInfo obtain()

public void recycle()

public ScrollabilityCache(ViewConfiguration configuration, View host)

public void setFadeColor(int color)

public void run()

public void post(int dx, int dy)

public void run()

public void sendAccessibilityEvent(View host, int eventType)

public boolean performAccessibilityAction(View host, int action, Bundle args)

public void sendAccessibilityEventUnchecked(View host, AccessibilityEvent event)

public boolean dispatchPopulateAccessibilityEvent(View host, AccessibilityEvent event)

public void onPopulateAccessibilityEvent(View host, AccessibilityEvent event)

public void onInitializeAccessibilityEvent(View host, AccessibilityEvent event)

public void onInitializeAccessibilityNodeInfo(View host, AccessibilityNodeInfo info)

public void addExtraDataToAccessibilityNodeInfo(@NonNull View host,
                @NonNull AccessibilityNodeInfo info, @NonNull String extraDataKey,
                @Nullable Bundle arguments)

public boolean onRequestSendAccessibilityEvent(ViewGroup host, View child,
                AccessibilityEvent event)

public AccessibilityNodeProvider getAccessibilityNodeProvider(View host)

public AccessibilityNodeInfo createAccessibilityNodeInfo(View host)

public boolean test(View view)

public boolean test(View view)

public void encode(@NonNull ViewHierarchyEncoder stream)

public void setTooltipText(@Nullable CharSequence tooltipText)

public void setTooltip(@Nullable CharSequence tooltipText)

public CharSequence getTooltipText()

public CharSequence getTooltip()

public View getTooltipView()

public static boolean isDefaultFocusHighlightEnabled()

public void addOnUnhandledKeyEventListener(OnUnhandledKeyEventListener listener)

public void removeOnUnhandledKeyEventListener(OnUnhandledKeyEventListener listener)


# 参考资料