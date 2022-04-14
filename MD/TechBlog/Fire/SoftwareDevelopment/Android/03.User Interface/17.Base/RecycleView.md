[TOC]

RecyclerView 中需要着重注意的是以下几个内部抽象类

```
Adapter: 用于设置Adapter，装载数据源
LayoutManager： 设置布局管理决定如何显示UI
ItemDecoration：设置分界线
ViewHolder：缓存的View
ItemAnimator： Item的操作动画
```

布局管理器设置
item的动画
间距的设置
响应事件的设置
第三方库的使用
DiffUtil的使用

解决问题：
RecyclerView 的基本使用步骤(数据源的装载，刷新，item事件的响应)





# 对外方法

RecyclerView(Context context)

RecyclerView(Context context, AttributeSet attrs)

RecyclerView(Context context, AttributeSet attrs, int defStyleAttr)

RecyclerViewAccessibilityDelegate getCompatAccessibilityDelegate()

setAccessibilityDelegateCompat()

CharSequence getAccessibilityClassName()

setHasFixedSize()

hasFixedSize()

setClipToPadding()

getClipToPadding()

setScrollingTouchSlop()

swapAdapter()

setAdapter()

Adapter getAdapter()

void setRecyclerListener()

int getBaseline()

addOnChildAttachStateChangeListener()

removeOnChildAttachStateChangeListener()

clearOnChildAttachStateChangeListeners()

setLayoutManager()

setOnFlingListener()

getOnFlingListener()

getLayoutManager()

getRecycledViewPool()

setRecycledViewPool()

setViewCacheExtension()

setItemViewCacheSize()

getScrollState()

addItemDecoration(@NonNull ItemDecoration decor, int index)

addItemDecoration(@NonNull ItemDecoration decor)

getItemDecorationAt()

getItemDecorationCount

removeItemDecorationAt

removeItemDecoration

setChildDrawingOrderCallback

setOnScrollListener

addOnScrollListener

removeOnScrollListener

clearOnScrollListeners

scrollToPosition

smoothScrollToPosition

scrollTo

scrollBy

computeHorizontalScrollOffset

computeHorizontalScrollExtent

computeHorizontalScrollRange

computeVerticalScrollOffset

computeVerticalScrollExtent

computeVerticalScrollRange

suppressLayout

isLayoutSuppressed

setLayoutFrozen

isLayoutFrozen

setLayoutTransition

smoothScrollBy(int,
int)

smoothScrollBy(int,
int,
Interpolator)

smoothScrollBy(int,
int,
Interpolator,
int)

fling

stopScroll

getMinFlingVelocity

getMaxFlingVelocity

setEdgeEffectFactory

getEdgeEffectFactory

focusSearch

requestChildFocus

requestChildRectangleOnScreen

addFocusables

isAttachedToWindow

addOnItemTouchListener

removeOnItemTouchListener

onInterceptTouchEvent

requestDisallowInterceptTouchEvent

onTouchEvent

onGenericMotionEvent

setItemAnimator

isComputingLayout

sendAccessibilityEventUnchecked

dispatchPopulateAccessibilityEvent

getItemAnimator

requestLayout

draw

onDraw

generateLayoutParams(AttributeSet)

isAnimating

invalidateItemDecorations

getPreserveFocusAfterLayout

setPreserveFocusAfterLayout

getChildViewHolder

findContainingItemView

findContainingViewHolder

getChildPosition

getChildAdapterPosition

getChildLayoutPosition

getChildItemId

findViewHolderForPosition(int)

findViewHolderForLayoutPosition

findViewHolderForAdapterPosition

findViewHolderForItemId

findChildViewUnder

drawChild

offsetChildrenVertical

onChildAttachedToWindow

onChildDetachedFromWindow

offsetChildrenHorizontal

getDecoratedBoundsWithMargins

onScrolled

onScrollStateChanged

hasPendingAdapterUpdates

setNestedScrollingEnabled

isNestedScrollingEnabled

startNestedScroll(int)

startNestedScroll(int,
int)

stopNestedScroll()

stopNestedScroll(int)

hasNestedScrollingParent()

hasNestedScrollingParent(int)

dispatchNestedScroll(int,
int,
int,
int,
int[])

dispatchNestedScroll(int,
int,
int,
int,
int[],
int)

dispatchNestedScroll(int,
int,
int,
int,
int[],
int,
int[])

dispatchNestedPreScroll(int,
int,
int[],
int[])

dispatchNestedPreScroll(int,
int,
int[],
int[],
int)

dispatchNestedFling

dispatchNestedPreFling



# 基本使用

# 参考资料
1. [Android-Docs-Reference-RecyclerView](https://developer.android.google.cn/reference/androidx/recyclerview/widget/RecyclerView?hl=en)