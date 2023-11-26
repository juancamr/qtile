from libqtile.config import Key
from libqtile.command import lazy
from utils import run_script
from const import MOD, ALT
import const

workspaces_keybindings = ["g", "c", "r", "s"]


def init_custom_keys():
    return [
        Key([MOD], "x", lazy.spawn("archlinux-logout")),
        Key([MOD], "Return", lazy.spawn(const.TERMINAL)),
        Key([MOD], "d", lazy.spawn(const.DMENU)),
        Key([MOD], "b", lazy.spawn(const.BROWSER)),
        Key([MOD], "e", lazy.function(lambda qtile: run_script(qtile, const.PYHASHER))),
    ]


def init_navigate_keys():
    return [
        Key([MOD], "f", lazy.window.toggle_fullscreen()),
        Key([MOD], "q", lazy.window.kill()),
        Key([MOD, "shift"], "q", lazy.window.kill()),
        Key([MOD, "shift"], "i", lazy.restart()),
        Key([MOD], "n", lazy.layout.normalize()),
        Key([MOD], "space", lazy.next_layout()),
        Key([MOD], "Up", lazy.layout.up()),
        Key([MOD], "Down", lazy.layout.down()),
        Key([MOD], "Left", lazy.layout.left()),
        Key([MOD], "Right", lazy.layout.right()),
        Key([MOD], "k", lazy.layout.up()),
        Key([MOD], "j", lazy.layout.down()),
        Key([MOD], "h", lazy.layout.left()),
        Key([MOD], "l", lazy.layout.right()),
        Key(
            [MOD, "control"],
            "l",
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ratio(),
            lazy.layout.delete(),
        ),
        Key(
            [MOD, "control"],
            "Right",
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ratio(),
            lazy.layout.delete(),
        ),
        Key(
            [MOD, "control"],
            "h",
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add(),
        ),
        Key(
            [MOD, "control"],
            "Left",
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add(),
        ),
        Key(
            [MOD, "control"],
            "k",
            lazy.layout.grow_up(),
            lazy.layout.grow(),
            lazy.layout.decrease_nmaster(),
        ),
        Key(
            [MOD, "control"],
            "Up",
            lazy.layout.grow_up(),
            lazy.layout.grow(),
            lazy.layout.decrease_nmaster(),
        ),
        Key(
            [MOD, "control"],
            "j",
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster(),
        ),
        Key(
            [MOD, "control"],
            "Down",
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster(),
        ),
        Key([MOD, "shift"], "f", lazy.layout.flip()),
        Key([MOD, "mod1"], "k", lazy.layout.flip_up()),
        Key([MOD, "mod1"], "j", lazy.layout.flip_down()),
        Key([MOD, "mod1"], "l", lazy.layout.flip_right()),
        Key([MOD, "mod1"], "h", lazy.layout.flip_left()),
        Key([MOD, "shift"], "k", lazy.layout.shuffle_up()),
        Key([MOD, "shift"], "j", lazy.layout.shuffle_down()),
        Key([MOD, "shift"], "h", lazy.layout.shuffle_left()),
        Key([MOD, "shift"], "l", lazy.layout.shuffle_right()),
        Key([MOD, "shift"], "Up", lazy.layout.shuffle_up()),
        Key([MOD, "shift"], "Down", lazy.layout.shuffle_down()),
        Key([MOD, "shift"], "Left", lazy.layout.swap_left()),
        Key([MOD, "shift"], "Right", lazy.layout.swap_right()),
        Key([MOD, "shift"], "space", lazy.window.toggle_floating()),
    ]


def add_workespaces_keys(groups, keys):
    keys = []
    for i in groups:
        keys.extend(
            [
                Key([MOD], i.name, lazy.group[i.name].toscreen()),
                Key([MOD], "Tab", lazy.screen.next_group()),
                Key([MOD, "shift"], "Tab", lazy.screen.prev_group()),
                Key([ALT], "Tab", lazy.screen.next_group()),
                Key([ALT, "shift"], "Tab", lazy.screen.prev_group()),
                Key(
                    [MOD, "shift"],
                    i.name,
                    lazy.window.togroup(i.name),
                    lazy.group[i.name].toscreen(),
                ),
            ]
        )
    return keys
