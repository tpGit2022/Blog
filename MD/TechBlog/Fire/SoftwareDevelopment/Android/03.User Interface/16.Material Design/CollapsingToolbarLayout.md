[TOC]

CollapsingToolbarLayout 设计上就是为了包裹 ToolBar 的，一般都是和 AppBarLayout 一起联用，组成合适的效果

CollapsingToolbarLayout 继承至 FrameLayout,

使用 CollapsingToolbarLayout 很多时候需要将 ToolBar 固定到顶端，因此 CollapsingToolbarLayout 常搭配 `app:layout_scrollFlags="scroll|exitUntilCollapsed"` 属性

titleEnabled： 是否启用 CollapsingToolbarLayout 的标题，默认为false

title: 设置 CollapsingToolbarLayout 的标题

collapsedTitleTextAppearance: 收拢时标题的字体

expandedTitleTextAppearance: 展开时标题的字体

contentScrim：收拢时的背景色

expandedTitleMargin：展开时标题的margin

expandedTitleMarginStart：展开时标题的start 方向的margin

expandedTitleMarginEnd：展开时标题的end方向的margin

expandedTitleMarginBottom：展开时标题bottom方向的margin

CollapsingToolbarLayout 的标题和 ToolBar 的标题

statusBarScrim：

scrimAnimationDuration： 颜色变化的持续时间

toolbarId：将对应id的toolbar用于缩放效果

scrimVisibleHeightTrigger:  view的可见高度小于该值时 scrims 可见 否则不可见


layout_collapseMode：取值有 `none,pin,parallax`

`none`:

`pin`: 设置为这个模式时，当CollapsingToolbarLayout完全收缩后，Toolbar还可以保留在屏幕上。

`parallax` 属性需要与 `app:layout_collapseParallaxMultiplier` 一同使用

设置为这个模式时，在内容滚动时， CollapsingToolbarLayout 中的View（比如ImageView)也可以同时滚动，实现视差滚动效果，通常和layout_collapseParallaxMultiplier(设置视差因子)搭配使用。

parallax 称之为视差，collapseParallaxMultiplier又叫视差因子取值在0-1之间，这里的视差指的是 CollapsingToolbarLayout 滑动时，设置 parallax 模式的子View 滑动速度不一样，这样会形成立体的运动效果

> 视差滚动(parallax scroll) 通俗点来讲就是 同样速度旋转的物体 隔的近的会觉得快 隔得远会觉得慢


需要注意的是 CollapsingToolbarLayout 包裹的 ToolBar 是不建议运行时动态新增子View

xml 属性：

```
 * @attr ref com.google.android.material.R.styleable#CollapsingToolbarLayout_collapsedTitleTextAppearance
 * @attr ref com.google.android.material.R.styleable#CollapsingToolbarLayout_expandedTitleTextAppearance
 * @attr ref com.google.android.material.R.styleable#CollapsingToolbarLayout_contentScrim
 * @attr ref com.google.android.material.R.styleable#CollapsingToolbarLayout_expandedTitleMargin
 * @attr ref com.google.android.material.R.styleable#CollapsingToolbarLayout_expandedTitleMarginStart
 * @attr ref com.google.android.material.R.styleable#CollapsingToolbarLayout_expandedTitleMarginEnd
 * @attr ref com.google.android.material.R.styleable#CollapsingToolbarLayout_expandedTitleMarginBottom
 * @attr ref com.google.android.material.R.styleable#CollapsingToolbarLayout_statusBarScrim
 * @attr ref com.google.android.material.R.styleable#CollapsingToolbarLayout_toolbarId
```

可用的 xml 属性如下：

```
<declare-styleable name="CollapsingToolbarLayout">
    <!--  Specifies extra space on the start, top, end and bottom
          sides of the the expanded title text. Margin values should be positive. -->
    <attr format="dimension" name="expandedTitleMargin"/>
    <!--  Specifies extra space on the start side of the the expanded title text.
          Margin values should be positive. -->
    <attr format="dimension" name="expandedTitleMarginStart"/>
    <!--  Specifies extra space on the top side of the the expanded title text.
          Margin values should be positive. -->
    <attr format="dimension" name="expandedTitleMarginTop"/>
    <!--  Specifies extra space on the end side of the the expanded title text.
          Margin values should be positive. -->
    <attr format="dimension" name="expandedTitleMarginEnd"/>
    <!--  Spec
    ifies extra space on the bottom side of the the expanded title text.
          Margin values should be positive. -->
    <attr format="dimension" name="expandedTitleMarginBottom"/>
    <!-- The text appearance of the CollapsingToolbarLayout's title when it is fully
         'expanded' -->
    <attr format="reference" name="expandedTitleTextAppearance"/>
    <!-- The text appearance of the CollapsingToolbarLayouts title when it is fully
         'collapsed' -->
    <attr format="reference" name="collapsedTitleTextAppearance"/>
    <!-- The drawable to use as a scrim on top of the CollapsingToolbarLayouts content when
         it has been scrolled sufficiently off screen. -->
    <attr format="color" name="contentScrim"/>
    <!-- The drawable to use as a scrim for the status bar content when the
         CollapsingToolbarLayout has been scrolled sufficiently off screen. Only works on
         Lollipop when used together with android:fitSystemWindows="true". -->
    <attr format="color" name="statusBarScrim"/>
    <!-- The id of the primary Toolbar child that you wish to use for the purpose of collapsing.
         This Toolbar descendant view does not need to be a direct child of the layout.
         If you do not set this, the first direct Toolbar child found will be used. -->
    <attr format="reference" name="toolbarId"/>
    <!-- Specifies the amount of visible height in pixels used to define when to trigger a
         scrim visibility change. -->
    <attr format="dimension" name="scrimVisibleHeightTrigger"/>
    <!-- Specifies the duration used for scrim visibility animations. -->
    <attr format="integer" name="scrimAnimationDuration"/>

    <!-- Specifies how the title should be positioned when collapsed. -->
    <attr name="collapsedTitleGravity">
      <!-- Push title to the top of its container, not changing its size. -->
      <flag name="top" value="0x30"/>
      <!-- Push title to the bottom of its container, not changing its size. -->
      <flag name="bottom" value="0x50"/>
      <!-- Push title to the left of its container, not changing its size. -->
      <flag name="left" value="0x03"/>
      <!-- Push title to the right of its container, not changing its size. -->
      <flag name="right" value="0x05"/>
      <!-- Place title in the vertical center of its container, not changing its size. -->
      <flag name="center_vertical" value="0x10"/>
      <!-- Grow the vertical size of the title if needed so it completely fills its container. -->
      <flag name="fill_vertical" value="0x70"/>
      <!-- Place title in the horizontal center of its container, not changing its size. -->
      <flag name="center_horizontal" value="0x01"/>
      <!-- Place the title in the center of its container in both the vertical and horizontal axis, not changing its size. -->
      <flag name="center" value="0x11"/>
      <!-- Push title to the beginning of its container, not changing its size. -->
      <flag name="start" value="0x00800003"/>
      <!-- Push title to the end of its container, not changing its size. -->
      <flag name="end" value="0x00800005"/>
    </attr>

    <!-- Specifies how the title should be positioned when expanded. -->
    <attr name="expandedTitleGravity">
      <!-- Push title to the top of its container, not changing its size. -->
      <flag name="top" value="0x30"/>
      <!-- Push title to the bottom of its container, not changing its size. -->
      <flag name="bottom" value="0x50"/>
      <!-- Push title to the left of its container, not changing its size. -->
      <flag name="left" value="0x03"/>
      <!-- Push title to the right of its container, not changing its size. -->
      <flag name="right" value="0x05"/>
      <!-- Place title in the vertical center of its container, not changing its size. -->
      <flag name="center_vertical" value="0x10"/>
      <!-- Grow the vertical size of the title if needed so it completely fills its container. -->
      <flag name="fill_vertical" value="0x70"/>
      <!-- Place title in the horizontal center of its container, not changing its size. -->
      <flag name="center_horizontal" value="0x01"/>
      <!-- Place the title in the center of its container in both the vertical and horizontal axis, not changing its size. -->
      <flag name="center" value="0x11"/>
      <!-- Push title to the beginning of its container, not changing its size. -->
      <flag name="start" value="0x00800003"/>
      <!-- Push title to the end of its container, not changing its size. -->
      <flag name="end" value="0x00800005"/>
    </attr>

    <!-- Whether the CollapsingToolbarLayout should draw its own shrinking/growing title. -->
    <attr format="boolean" name="titleEnabled"/>
    <!-- The title to show when titleEnabled is set to true. -->
    <attr name="title"/>
  </declare-styleable>
    <declare-styleable name="CollapsingToolbarLayout_Layout">
    <attr name="layout_collapseMode">
      <!-- The view will act as normal with no collapsing behavior. -->
      <enum name="none" value="0"/>
      <!-- The view will pin in place. -->
      <enum name="pin" value="1"/>
      <!-- The view will scroll in a parallax fashion. See the
           layout_collapseParallaxMultiplier attribute to change the multiplier. -->
      <enum name="parallax" value="2"/>
    </attr>

    <!-- The multiplier used when layout_collapseMode is set to 'parallax'. The value should
         be between 0.0 and 1.0. -->
    <attr format="float" name="layout_collapseParallaxMultiplier"/>
  </declare-styleable>
```

# 对外方法

public CollapsingToolbarLayout(@NonNull Context context)

public CollapsingToolbarLayout(@NonNull Context context, @Nullable AttributeSet attrs)

public CollapsingToolbarLayout(@NonNull Context context, @Nullable AttributeSet attrs, int defStyleAttr)

public WindowInsetsCompat onApplyWindowInsets(
              View v, @NonNull WindowInsetsCompat insets)

public void draw(@NonNull Canvas canvas)

public void setTitle(@Nullable CharSequence title)

public CharSequence getTitle()

public void setTitleEnabled(boolean enabled)

public boolean isTitleEnabled()

public void setScrimsShown(boolean shown)

public void setScrimsShown(boolean shown, boolean animate)

public void onAnimationUpdate(@NonNull ValueAnimator animator)

public void setContentScrim(@Nullable Drawable drawable)

public void setContentScrimColor(@ColorInt int color)

public void setContentScrimResource(@DrawableRes int resId)

public Drawable getContentScrim()

public void setStatusBarScrim(@Nullable Drawable drawable)

public void setVisibility(int visibility)

public void setStatusBarScrimColor(@ColorInt int color)

public void setStatusBarScrimResource(@DrawableRes int resId)

public Drawable getStatusBarScrim()

public void setCollapsedTitleTextAppearance(@StyleRes int resId)

public void setCollapsedTitleTextColor(@ColorInt int color)

public void setCollapsedTitleTextColor(@NonNull ColorStateList colors)

public void setCollapsedTitleGravity(int gravity)

public int getCollapsedTitleGravity()

public void setExpandedTitleTextAppearance(@StyleRes int resId)

public void setExpandedTitleColor(@ColorInt int color)

public void setExpandedTitleTextColor(@NonNull ColorStateList colors)

public void setExpandedTitleGravity(int gravity)

public int getExpandedTitleGravity()

public void setCollapsedTitleTypeface(@Nullable Typeface typeface)

public Typeface getCollapsedTitleTypeface()

public void setExpandedTitleTypeface(@Nullable Typeface typeface)

public Typeface getExpandedTitleTypeface()

public void setExpandedTitleMargin(int start, int top, int end, int bottom)

public int getExpandedTitleMarginStart()

public void setExpandedTitleMarginStart(int margin)

public int getExpandedTitleMarginTop()

public void setExpandedTitleMarginTop(int margin)

public int getExpandedTitleMarginEnd()

public void setExpandedTitleMarginEnd(int margin)

public int getExpandedTitleMarginBottom()

public void setExpandedTitleMarginBottom(int margin)

public int getScrimVisibleHeightTrigger()

public long getScrimAnimationDuration()

public LayoutParams(Context c, AttributeSet attrs)

public LayoutParams(int width, int height)

public LayoutParams(int width, int height, int gravity)

public LayoutParams(@NonNull ViewGroup.LayoutParams p)

public LayoutParams(@NonNull MarginLayoutParams source)

public LayoutParams(@NonNull FrameLayout.LayoutParams source)

public void setCollapseMode(@CollapseMode int collapseMode)

public int getCollapseMode()

public void setParallaxMultiplier(float multiplier)

public float getParallaxMultiplier()

public void onOffsetChanged(AppBarLayout layout, int verticalOffset)

public CollapsingToolbarLayout(@NonNull Context context)

public CollapsingToolbarLayout(@NonNull Context context, @Nullable AttributeSet attrs)

public CollapsingToolbarLayout(@NonNull Context context, @Nullable AttributeSet attrs, int defStyleAttr)

public WindowInsetsCompat onApplyWindowInsets(
              View v, @NonNull WindowInsetsCompat insets)

public void draw(@NonNull Canvas canvas)

public void setTitle(@Nullable CharSequence title)

public CharSequence getTitle()

public void setTitleEnabled(boolean enabled)

public boolean isTitleEnabled()

public void setScrimsShown(boolean shown)

public void setScrimsShown(boolean shown, boolean animate)

public void onAnimationUpdate(@NonNull ValueAnimator animator)

public void setContentScrim(@Nullable Drawable drawable)

public void setContentScrimColor(@ColorInt int color)

public void setContentScrimResource(@DrawableRes int resId)

public Drawable getContentScrim()

public void setStatusBarScrim(@Nullable Drawable drawable)

public void setVisibility(int visibility)

public void setStatusBarScrimColor(@ColorInt int color)

public void setStatusBarScrimResource(@DrawableRes int resId)

public Drawable getStatusBarScrim()

public void setCollapsedTitleTextAppearance(@StyleRes int resId)

public void setCollapsedTitleTextColor(@ColorInt int color)

public void setCollapsedTitleTextColor(@NonNull ColorStateList colors)

public void setCollapsedTitleGravity(int gravity)

public int getCollapsedTitleGravity()

public void setExpandedTitleTextAppearance(@StyleRes int resId)

public void setExpandedTitleColor(@ColorInt int color)

public void setExpandedTitleTextColor(@NonNull ColorStateList colors)

public void setExpandedTitleGravity(int gravity)

public int getExpandedTitleGravity()

public void setCollapsedTitleTypeface(@Nullable Typeface typeface)

public Typeface getCollapsedTitleTypeface()

public void setExpandedTitleTypeface(@Nullable Typeface typeface)

public Typeface getExpandedTitleTypeface()

public void setExpandedTitleMargin(int start, int top, int end, int bottom)

public int getExpandedTitleMarginStart()

public void setExpandedTitleMarginStart(int margin)

public int getExpandedTitleMarginTop()

public void setExpandedTitleMarginTop(int margin)

public int getExpandedTitleMarginEnd()

public void setExpandedTitleMarginEnd(int margin)

public int getExpandedTitleMarginBottom()

public void setExpandedTitleMarginBottom(int margin)

public int getScrimVisibleHeightTrigger()

public long getScrimAnimationDuration()

public LayoutParams(Context c, AttributeSet attrs)

public LayoutParams(int width, int height)

public LayoutParams(int width, int height, int gravity)

public LayoutParams(@NonNull ViewGroup.LayoutParams p)

public LayoutParams(@NonNull MarginLayoutParams source)

public LayoutParams(@NonNull FrameLayout.LayoutParams source)

public void setCollapseMode(@CollapseMode int collapseMode)

public int getCollapseMode()

public void setParallaxMultiplier(float multiplier)

public float getParallaxMultiplier()

public void onOffsetChanged(AppBarLayout layout, int verticalOffset)


# 参考资料