

Paint 对外的方法如下：

构造方法：


public Paint()

public Paint(int flags)

public Paint(Paint paint)

public void reset()

public void set(Paint src)

public boolean hasEqualAttributes(@NonNull Paint other)

public void setCompatibilityScaling(float factor)

public long getNativeInstance()

public int getBidiFlags()

public void setBidiFlags(int flags)

public int getFlags()

public void setFlags(int flags)

public int getHinting()

public void setHinting(int mode)

public final boolean isAntiAlias()

public void setAntiAlias(boolean aa)

public final boolean isDither()

public void setDither(boolean dither)

public final boolean isLinearText()

public void setLinearText(boolean linearText)

public final boolean isSubpixelText()

public void setSubpixelText(boolean subpixelText)

public final boolean isUnderlineText()

public float getUnderlinePosition()

public float getUnderlineThickness()

public void setUnderlineText(boolean underlineText)

public final boolean isStrikeThruText()

public float getStrikeThruPosition()

public float getStrikeThruThickness()

public void setStrikeThruText(boolean strikeThruText)

public final boolean isFakeBoldText()

public void setFakeBoldText(boolean fakeBoldText)

public final boolean isFilterBitmap()

public void setFilterBitmap(boolean filter)

public Style getStyle()

public void setStyle(Style style)

public int getColor()

public void setColor(@ColorInt int color)

public int getAlpha()

public void setAlpha(int a)

public void setARGB(int a, int r, int g, int b)

public float getStrokeWidth()

public void setStrokeWidth(float width)

public float getStrokeMiter()

public void setStrokeMiter(float miter)

public Cap getStrokeCap()

public void setStrokeCap(Cap cap)

public Join getStrokeJoin()

public void setStrokeJoin(Join join)

public boolean getFillPath(Path src, Path dst)

public Shader getShader()

public Shader setShader(Shader shader)

public ColorFilter getColorFilter()

public ColorFilter setColorFilter(ColorFilter filter)

public Xfermode getXfermode()

public Xfermode setXfermode(Xfermode xfermode)

public PathEffect getPathEffect()

public PathEffect setPathEffect(PathEffect effect)

public MaskFilter getMaskFilter()

public MaskFilter setMaskFilter(MaskFilter maskfilter)

public Typeface getTypeface()

public Typeface setTypeface(Typeface typeface)

public Rasterizer getRasterizer()

public Rasterizer setRasterizer(Rasterizer rasterizer)

public void setShadowLayer(float radius, float dx, float dy, int shadowColor)

public void clearShadowLayer()

public boolean hasShadowLayer()

public Align getTextAlign()

public void setTextAlign(Align align)

public Locale getTextLocale()

public LocaleList getTextLocales()

public void setTextLocale(@NonNull Locale locale)

public boolean isElegantTextHeight()

public void setElegantTextHeight(boolean elegant)

public float getTextSize()

public void setTextSize(float textSize)

public float getTextScaleX()

public void setTextScaleX(float scaleX)

public float getTextSkewX()

public void setTextSkewX(float skewX)

public float getLetterSpacing()

public void setLetterSpacing(float letterSpacing)

public float getWordSpacing()

public void setWordSpacing(float wordSpacing)

public String getFontFeatureSettings()

public void setFontFeatureSettings(String settings)

public String getFontVariationSettings()

public boolean setFontVariationSettings(String fontVariationSettings)

public int getHyphenEdit()

public void setHyphenEdit(int hyphen)

public float ascent()

public float descent()

public float getFontMetrics(FontMetrics metrics)

public FontMetrics getFontMetrics()

public String toString()

public int getFontMetricsInt(FontMetricsInt fmi)

public FontMetricsInt getFontMetricsInt()

public float getFontSpacing()

public float measureText(char[] text, int index, int count)

public float measureText(String text, int start, int end)

public float measureText(String text)

public float measureText(CharSequence text, int start, int end)

public int breakText(char[] text, int index, int count,
                                float maxWidth, float[] measuredWidth)

public int breakText(CharSequence text, int start, int end,
                         boolean measureForwards,
                         float maxWidth, float[] measuredWidth)

public int breakText(String text, boolean measureForwards,
                                float maxWidth, float[] measuredWidth)

public int getTextWidths(char[] text, int index, int count,
                             float[] widths)

public int getTextWidths(CharSequence text, int start, int end,
                             float[] widths)

public int getTextWidths(String text, int start, int end, float[] widths)

public int getTextWidths(String text, float[] widths)

public float getTextRunAdvances(char[] chars, int index, int count,
            int contextIndex, int contextCount, boolean isRtl, float[] advances,
            int advancesIndex)

public float getTextRunAdvances(CharSequence text, int start, int end,
            int contextStart, int contextEnd, boolean isRtl, float[] advances,
            int advancesIndex)

public float getTextRunAdvances(String text, int start, int end, int contextStart,
            int contextEnd, boolean isRtl, float[] advances, int advancesIndex)

public int getTextRunCursor(char[] text, int contextStart, int contextLength,
            int dir, int offset, int cursorOpt)

public int getTextRunCursor(CharSequence text, int contextStart,
           int contextEnd, int dir, int offset, int cursorOpt)

public int getTextRunCursor(String text, int contextStart, int contextEnd,
            int dir, int offset, int cursorOpt)

public void getTextPath(char[] text, int index, int count,
                            float x, float y, Path path)

public void getTextPath(String text, int start, int end,
                            float x, float y, Path path)

public void getTextBounds(String text, int start, int end, Rect bounds)

public void getTextBounds(CharSequence text, int start, int end, Rect bounds)

public void getTextBounds(char[] text, int index, int count, Rect bounds)

public boolean hasGlyph(String string)

public float getRunAdvance(char[] text, int start, int end, int contextStart, int contextEnd,
            boolean isRtl, int offset)

public float getRunAdvance(CharSequence text, int start, int end, int contextStart,
            int contextEnd, boolean isRtl, int offset)

public int getOffsetForAdvance(char[] text, int start, int end, int contextStart,
            int contextEnd, boolean isRtl, float advance)

public int getOffsetForAdvance(CharSequence text, int start, int end, int contextStart,
            int contextEnd, boolean isRtl, float advance)

public boolean equalsForTextMeasurement(@NonNull Paint other)
