#!/bin/bash

setxkbmap us -variant dvp

xmodmap -e "keycode 94 = Shift_L Shift_L"
xmodmap -e "keycode 9 = dollar asciitilde Escape Escape"

xmodmap -e "keycode 38 = a A aacute Aacute"
xmodmap -e "keycode 40 = e E eacute Eacute"
xmodmap -e "keycode 42 = i I iacute Iacute"
xmodmap -e "keycode 39 = o O oacute Oacute"
xmodmap -e "keycode 41 = u U uacute Uacute"
xmodmap -e "keycode 46 = n N ntilde Ntilde"
xmodmap -e "keycode 34 = slash question questiondown"

xmodmap -e "keycode 108 = Mode_switch"
