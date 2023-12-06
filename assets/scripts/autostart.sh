#!/bin/bash
function run {
	if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null; then
		$@ &
	fi
}

#run sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &
run nm-applet &
run pamac-tray &
run xfce4-power-manager &

numlockx on &
blueberry-tray &

picom --config $HOME/.config/qtile/assets/scripts/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &

run volumeicon &
sh ~/.config/qtile/assets/scripts/keyboard.sh &
parcellite --no-icon &

firefox &
#sh ~/.config/qtile/assets/scripts/hide_mouse.sh &
#python ~/.config/qtile/assets/scripts/change_wallpaper.py
