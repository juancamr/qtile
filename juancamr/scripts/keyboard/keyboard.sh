#!/bin/bash

setxkbmap us -variant dvp
xmodmap -e "keycode 108 = Mode_switch"

sh ~/.config/qtile/juancamr/scripts/keyboard/keymaps/spanish_keymaps.sh
sh ~/.config/qtile/juancamr/scripts/keyboard/keymaps/custom_keymaps.sh
