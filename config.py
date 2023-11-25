import os
import subprocess
import keymap
import layout
import topbar
import screens
import set
from libqtile import hook, qtile

mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser("~")
my_terminal = "alacritty"

keys = keymap.init_keys()
groups = layout.init_groups()
keys.extend(keymap.add_workespaces_keys(groups, keys))
layouts = layout.init_layouts()
widget_defaults, widgets_list = topbar.init_widgets()
screens = screens.init_screens()


# MOUSE CONFIGURATION
(
    mouse,
    dgroups_key_binder,
    dgroups_app_rules,
    main,
    floating_types,
    follow_mouse_focus,
    bring_front_click,
    cursor_warp,
    floating_layout,
    auto_fullscreen,
    focus_on_window_activation,
    wmname,
) = set.get_settings()


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
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


@hook.subscribe.client_new
def set_floating(window):
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True
