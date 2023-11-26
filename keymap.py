from libqtile.config import Key
from libqtile.command import lazy
import subprocess
import os

mod = "mod4"
alt = "mod1"
my_terminal = "alacritty"
dmenu_command = "dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'"
workspaces_keybindings = ["g", "c", "r", "s"]
browser = "firefox"


def open_pyhasher(qtile):
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/pyhasher/pyhasher.sh"])


def init_custom_keys():
    return [
        Key([mod], "x", lazy.spawn("archlinux-logout")),
        Key([mod], "Return", lazy.spawn(my_terminal)),
        Key([mod], "d", lazy.spawn(dmenu_command)),
        Key([mod], "b", lazy.spawn(browser)),
        Key([mod], "e", lazy.function(open_pyhasher)),
    ]


def init_navigate_keys():
    return [
        Key([mod], "f", lazy.window.toggle_fullscreen()),
        Key([mod], "q", lazy.window.kill()),
        Key([mod, "shift"], "q", lazy.window.kill()),
        Key([mod, "shift"], "i", lazy.restart()),
        Key([mod], "n", lazy.layout.normalize()),
        Key([mod], "space", lazy.next_layout()),
        Key([mod], "Up", lazy.layout.up()),
        Key([mod], "Down", lazy.layout.down()),
        Key([mod], "Left", lazy.layout.left()),
        Key([mod], "Right", lazy.layout.right()),
        Key([mod], "k", lazy.layout.up()),
        Key([mod], "j", lazy.layout.down()),
        Key([mod], "h", lazy.layout.left()),
        Key([mod], "l", lazy.layout.right()),
        Key(
            [mod, "control"],
            "l",
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ratio(),
            lazy.layout.delete(),
        ),
        Key(
            [mod, "control"],
            "Right",
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ratio(),
            lazy.layout.delete(),
        ),
        Key(
            [mod, "control"],
            "h",
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add(),
        ),
        Key(
            [mod, "control"],
            "Left",
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add(),
        ),
        Key(
            [mod, "control"],
            "k",
            lazy.layout.grow_up(),
            lazy.layout.grow(),
            lazy.layout.decrease_nmaster(),
        ),
        Key(
            [mod, "control"],
            "Up",
            lazy.layout.grow_up(),
            lazy.layout.grow(),
            lazy.layout.decrease_nmaster(),
        ),
        Key(
            [mod, "control"],
            "j",
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster(),
        ),
        Key(
            [mod, "control"],
            "Down",
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster(),
        ),
        Key([mod, "shift"], "f", lazy.layout.flip()),
        Key([mod, "mod1"], "k", lazy.layout.flip_up()),
        Key([mod, "mod1"], "j", lazy.layout.flip_down()),
        Key([mod, "mod1"], "l", lazy.layout.flip_right()),
        Key([mod, "mod1"], "h", lazy.layout.flip_left()),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
        Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
        Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
        Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
        Key([mod, "shift"], "Left", lazy.layout.swap_left()),
        Key([mod, "shift"], "Right", lazy.layout.swap_right()),
        Key([mod, "shift"], "space", lazy.window.toggle_floating()),
    ]


def add_workespaces_keys(groups, keys):
    keys = []
    for i in groups:
        keys.extend(
            [
                Key([mod], i.name, lazy.group[i.name].toscreen()),
                Key([mod], "Tab", lazy.screen.next_group()),
                Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
                Key([alt], "Tab", lazy.screen.next_group()),
                Key([alt, "shift"], "Tab", lazy.screen.prev_group()),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name),
                    lazy.group[i.name].toscreen(),
                ),
            ]
        )
    return keys
