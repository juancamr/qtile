import os
from juancamr.utils.theme import theme
from juancamr.utils.colors import only

TERMINAL = "alacritty"
BROWSER = "firefox"
OBSIDIAN = "obsidian"
THUNAR = "thunar"
CODE = "code"
HOME = os.path.expanduser("~")
DMENU = f"dmenu_run -i -nb '{only(theme.panel_background)}' -nf '{only(theme.window_name)}' -sb '{only(theme.window_name)}' -sf '{only(theme.panel_background)}' -fn 'ProductSans:bold:pixelsize=14'"
ICONS_PATH = [f"{HOME}/.config/qtile/assets/icons"]
ICON_TOPBAR = "~/.config/qtile/assets/icons/arch_indigo.png"
FONT_AWESOME = "FontAwesome"
UBUNTU_FONT = "Ubuntu"
UBUNTU_BOLD_FONT = "Ubuntu Bold"
PRODUCT_SANS_FONT = "Product Sans"
PRODUCT_SANS_BOLD_FONT = "Product Sans Bold"
PAVUCONTROL = "pavucontrol"
LOGOUT_COMMAND = "archlinux-logout"
SCREENSHOT_PATH = "/tmp/temp_capture.png"
SHUTTER_COMMAND = f"shutter -s -e -o {SCREENSHOT_PATH} && xclip -selection clipboard -target image/png -i {SCREENSHOT_PATH}"

SCRIPT_PATH = "/.config/qtile/juancamr/scripts"
PYHASHER = f"python {HOME}/pyhasher/main.py &"
OPEN_SETTINGS = f"cd {HOME}/.config/qtile; nvim ."
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
