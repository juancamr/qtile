#!/bin/bash

setxkbmap us -variant dvp
xmodmap -e "keycode 108 = Mode_switch"

sh ~/.config/qtile/assets/scripts/keymaps/spanish_keymaps.sh
sh ~/.config/qtile/assets/scripts/keymaps/custom_keymaps.sh
