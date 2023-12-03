import subprocess
from libqtile import hook
from utils import utils, constants as const


@hook.subscribe.client_new
def new_client(window):
    utils.toggle_borders(window, True)


@hook.subscribe.client_killed
def kill_client(window):
    utils.toggle_borders(window, False)


@hook.subscribe.startup_once
def start_once():
    utils.random_wallpaper()
    subprocess.call([const.HOME + const.AUTOSTART_SCRIPT])


@hook.subscribe.client_new
def set_floating(window):
    floating_types = ["notification", "toolbar", "splash", "dialog"]
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True
