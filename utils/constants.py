from utils.theme import theme
from utils.colors import only
import os

TERMINAL = "alacritty"
BROWSER = "firefox"
OBSIDIAN = "obsidian"
HOME = os.path.expanduser("~")
DMENU = f"dmenu_run -i -nb '{only(theme.panel_background)}' -nf '{only(theme.window_name)}' -sb '{only(theme.window_name)}' -sf '{only(theme.panel_background)}' -fn 'ProductSans:bold:pixelsize=14'"
ICONS_PATH = [f"{HOME}/.config/qtile/assets/icons"]
PYTHON_ICON = "~/.config/qtile/assets/icons/python.png"
FONT_AWESOME = "FontAwesome"
UBUNTU_FONT = "Ubuntu"
UBUNTU_BOLD_FONT = "Ubuntu Bold"
PRODUCT_SANS_FONT = "Product Sans"
PRODUCT_SANS_BOLD_FONT = "Product Sans Bold"
PAVUCONTROL = "pavucontrol"
LOGOUT_COMMAND = "archlinux-logout"

SCRIPT_PATH = "/.config/qtile/assets/scripts"
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
