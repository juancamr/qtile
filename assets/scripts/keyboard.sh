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

# for comfort
xmodmap -e "keycode 59 = w w W W" # para no confundirme con vim xd
xmodmap -e "keycode 36 = backslash bar" # also depends on the keyboard
xmodmap -e "keycode 26 = period greater greater"
xmodmap -e "keycode 48 = Return underscore NoSymbol NoSymbol"

# modifier keys
xmodmap -e "keycode 66 = Mode_switch"
xmodmap -e "keycode 51 = NoSymbol"

xmodmap -e "keycode 61 = Shift_R Shift_R"
xmodmap -e "keycode 108 = Caps_Lock"
xmodmap -e "keycode 62 = z Z z Z"

# custom mappings
xmodmap -e "keycode 54 = j J Down"
xmodmap -e "keycode 55 = k K Up"
xmodmap -e "keycode 33 = l L Right"
xmodmap -e "keycode 30 = g G Left"
xmodmap -e "keycode 44 = h H Home"
xmodmap -e "keycode 32 = r R End"

xmodmap -e "keycode 45 = t T minus"
xmodmap -e "keycode 31 = c C Escape"
