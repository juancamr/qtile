from libqtile import hook, qtile, layout
from utils import constants as const, utils
from libqtile.log_utils import logger
import subprocess


@hook.subscribe.client_new
def new_client(window):
    if window.name == "ArchLinux Logout":
        qtile.hide_show_bar()


# @hook.subscribe.client_new
# def toggle_borders(window):
#     group = window.qtile.current_group
#     if len(group.windows) == 0:
#         # use bsp layout
#         window.qtile.current_group.use_layout(3)
#     else:
#         # use monadtall layout
#         window.qtile.current_group.use_layout(0)


# shows the top bar when the archlinux-logout widget is closed
@hook.subscribe.client_killed
def logout_killed(window):
    if window.name == "ArchLinux Logout":
        qtile.hide_show_bar()


@hook.subscribe.client_killed
def focus_last(window):
    window.qtile.current_group.windows[-1].focus()


@hook.subscribe.startup_once
def start_once():
    utils.random_wallpaper()
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
