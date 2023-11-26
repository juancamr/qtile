from libqtile import hook, qtile
from utils import constants as const
import subprocess


@hook.subscribe.client_new
def new_client(window):
    if window.name == "ArchLinux Logout":
        qtile.hide_show_bar()


# shows the top bar when the archlinux-logout widget is closed
@hook.subscribe.client_killed
def logout_killed(window):
    if window.name == "ArchLinux Logout":
        qtile.hide_show_bar()


@hook.subscribe.startup_once
def start_once():
    subprocess.call([const.HOME + const.AUTOSTART_SCRIPT])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


@hook.subscribe.client_new
def set_floating(window):
    floating_types = ["notification", "toolbar", "splash", "dialog"]
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True
