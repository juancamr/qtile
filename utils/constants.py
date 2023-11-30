import os

TERMINAL = "alacritty"
BROWSER = "firefox"
OBSIDIAN = "obsidian"
HOME = os.path.expanduser("~")
DMENU = "dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'ProductSans:bold:pixelsize=14'"
ICONS_PATH = [f"{HOME}/.config/qtile/assets/icons"]
FONT_AWESOME = "FontAwesome"
UBUNTU_FONT = "Ubuntu"
UBUNTU_BOLD_FONT = "Ubuntu Bold"
PRODUCT_SANS_FONT = "Product Sans"
PRODUCT_SANS_BOLD_FONT = "Product Sans Bold"
PAVUCONTROL = "pavucontrol"
LOGOUT_COMMAND = "archlinux-logout"


SCRIPT_PATH = "/.config/qtile/assets/scripts"
# scripts
# PYHASHER = f"{SCRIPT_PATH}/pyhasher.sh"
# SETTINGS = f"{SCRIPT_PATH}/settings.sh"
PYHASHER = f"python {HOME}/pyhasher/main.py &"
OPEN_SETTINGS = f"code {HOME}/.config/qtile"
AUTOSTART_SCRIPT = f"{SCRIPT_PATH}/autostart.sh"
CHANGE_OUTPUT = f"{SCRIPT_PATH}/audio.sh"

# icons
CORNER_ICON = ""
VOLUME_ICON = " "
MEMORY_ICON = ""

# super keys
MOD = "mod4"
ALT = "mod1"
SHIFT = "shift"
CONTROL = "control"
