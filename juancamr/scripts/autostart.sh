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

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &

firefox &
# anki-woodrow.anki &
# obsidian &
# todoist &

picom --experimental-backends &
run volumeicon &
sh ~/.config/qtile/juancamr/scripts/keyboard/keyboard.sh
parcellite --no-icon &
nitrogen --restore &
