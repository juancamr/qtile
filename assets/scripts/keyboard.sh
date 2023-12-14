#!/bin/bash

setxkbmap us -variant dvp

# spanish keymaps
xmodmap -e "keycode 38 = a A aacute Aacute"
xmodmap -e "keycode 40 = e E eacute Eacute"
xmodmap -e "keycode 42 = i I iacute Iacute"
xmodmap -e "keycode 39 = o O oacute Oacute"
xmodmap -e "keycode 41 = u U uacute Uacute"
xmodmap -e "keycode 46 = n N ntilde Ntilde"
xmodmap -e "keycode 34 = slash question questiondown"
xmodmap -e "keycode 20 = exclam 8 exclamdown"

# by type of keyboard
xmodmap -e "keycode 94 = Shift_L Shift_L"
xmodmap -e "keycode 9 = dollar asciitilde"
xmodmap -e "keycode 31 = c C Escape"

# navigate keys
xmodmap -e "keycode 54 = j J Down"
xmodmap -e "keycode 55 = k K Up"
xmodmap -e "keycode 44 = h H Left"
xmodmap -e "keycode 33 = l L Right"

# for comfort
xmodmap -e "keycode 59 = w w W W" # para no confundirme con vim xd
xmodmap -e "keycode 26 = period greater greater"
xmodmap -e "keycode 36 = backslash bar" # also depends on the keyboard
xmodmap -e "keycode 18 = plus 4 minus"
xmodmap -e "keycode 48 = Return underscore"

# modifier keys
xmodmap -e "keycode 66 = Mode_switch Caps_Lock"
xmodmap -e "keycode 51 = minus underscore"
