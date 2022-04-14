# 模拟右键点击

绑定的快捷键F4，按下后点击右键120次

```
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
$F4::
count := 1
Loop 120
{
    Click right ;
    Sleep 350   ;
}
```


# 模拟区域内扫击

模拟射击游戏鼠标移动射击目标

```
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
space::
MouseGetPos,xpos,ypos
addX := 0
addY := 0
Loop 20000000
{
    if WinActive("Typing of the Dead Overkill")
    {
        Click   ;
        x := xpos+addX  ;
        y := ypos+addY  ;
        MouseMove, %x%, %y% ;
        addX += 3
        if (addX > 600)
        {
            addX = 0    ;
            addY += 25  ;
            if (addY > 200)
                addY = 0    ;
        }
    }
}
```