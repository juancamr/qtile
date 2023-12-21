#!/bin/bash

setxkbmap us -variant dvp
xmodmap -e "keycode 108 = Mode_switch"

sh ~/.config/qtile/assets/scripts/keymaps/spanish_keymaps.sh
sh ~/.config/qtile/assets/scripts/keymaps/custom_keymaps.sh

# custom mappings
# xmodmap -e "keycode 31 = c C Up"
# xmodmap -e "keycode 45 = t T Down"
# xmodmap -e "keycode 44 = h H Left"
# xmodmap -e "keycode 46 = n N Right"

# xmodmap -e "keycode 30 = g G Home"
# xmodmap -e "keycode 32 = r R End"
