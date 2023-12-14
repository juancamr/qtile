"""setting keymaps for qtile"""
import os
from libqtile.config import Key
from libqtile.command import lazy
from utils import utils, constants as const
from utils.constants import MOD, ALT, SHIFT, CONTROL

workspaces_keybindings = ["h", "t", "n", "s", "c", "r"]
workspaces = enumerate(workspaces_keybindings)
groups_dict = {keybind: index for (index, keybind) in workspaces}


def init_custom_keys() -> list:
    """return my custom keymaps"""

    return [
        Key([MOD], "Return", lazy.spawn(const.TERMINAL)),
        Key([MOD, SHIFT], "Return", lazy.spawn(const.THUNAR)),
        Key([MOD], "x", lazy.spawn(const.LOGOUT_COMMAND)),
        Key([MOD], "d", lazy.spawn(const.DMENU)),
        Key([MOD], "b", lazy.spawn(const.BROWSER)),
        Key([MOD], "a", lazy.function(lambda _: os.system(const.PYHASHER))),
        Key([MOD], "o", lazy.spawn(const.OBSIDIAN)),
        Key([MOD], "m", lazy.window.toggle_floating()),
        Key(
            [MOD, ALT],
            "s",
            lazy.function(
                lambda _: utils.run_command_with_terminal(const.OPEN_SETTINGS)
            ),
        ),
        Key([MOD], "p", utils.capture_and_copy),
        Key([MOD], "e", utils.open_code_with_fzf),
    ]


def init_navigate_keys() -> list:
    """return keymaps that use qtile"""
    return [
        Key([MOD, SHIFT], "f", lazy.window.toggle_fullscreen()),
        Key([MOD], "q", lazy.window.kill()),
        Key([MOD, SHIFT], "q", lazy.window.kill()),
        Key([MOD, SHIFT], "i", lazy.restart()),
        Key([MOD], "Up", lazy.layout.up()),
        Key([MOD], "Down", lazy.layout.down()),
        Key([MOD], "Left", lazy.layout.left()),
        Key([MOD], "Right", lazy.layout.right()),
        Key([MOD], "k", lazy.layout.up()),
        Key([MOD], "j", lazy.layout.down()),
        Key([MOD], "g", lazy.layout.left()),
        Key([MOD], "l", lazy.layout.right()),
        Key(
            [MOD, CONTROL],
            "l",
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ratio(),
            lazy.layout.delete(),
        ),
        Key(
            [MOD, CONTROL],
            "Right",
            lazy.layout.grow_right(),
            lazy.layout.grow(),
            lazy.layout.increase_ratio(),
            lazy.layout.delete(),
        ),
        Key(
            [MOD, CONTROL],
            "g",
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add(),
        ),
        Key(
            [MOD, CONTROL],
            "Left",
            lazy.layout.grow_left(),
            lazy.layout.shrink(),
            lazy.layout.decrease_ratio(),
            lazy.layout.add(),
        ),
        Key(
            [MOD, CONTROL],
            "k",
            lazy.layout.grow_up(),
            lazy.layout.grow(),
            lazy.layout.decrease_nmaster(),
        ),
        Key(
            [MOD, CONTROL],
            "Up",
            lazy.layout.grow_up(),
            lazy.layout.grow(),
            lazy.layout.decrease_nmaster(),
        ),
        Key(
            [MOD, CONTROL],
            "j",
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster(),
        ),
        Key(
            [MOD, CONTROL],
            "Down",
            lazy.layout.grow_down(),
            lazy.layout.shrink(),
            lazy.layout.increase_nmaster(),
        ),
        # Key([MOD, SHIFT], "f", lazy.layout.flip()),
        Key([MOD, "mod1"], "k", lazy.layout.flip_up()),
        Key([MOD, "mod1"], "j", lazy.layout.flip_down()),
        Key([MOD, "mod1"], "l", lazy.layout.flip_right()),
        Key([MOD, "mod1"], "g", lazy.layout.flip_left()),
        Key([MOD, SHIFT], "k", lazy.layout.shuffle_up()),
        Key([MOD, SHIFT], "j", lazy.layout.shuffle_down()),
        Key([MOD, SHIFT], "g", lazy.layout.shuffle_left()),
        Key([MOD, SHIFT], "l", lazy.layout.shuffle_right()),
        Key([MOD, SHIFT], "Up", lazy.layout.shuffle_up()),
        Key([MOD, SHIFT], "Down", lazy.layout.shuffle_down()),
        Key([MOD, SHIFT], "Left", lazy.layout.swap_left()),
        Key([MOD, SHIFT], "Right", lazy.layout.swap_right()),
        Key([MOD, SHIFT], "space", lazy.window.toggle_floating()),
    ]


def add_workespaces_keys(groups, keys) -> list:
    """esto es unicamente de prueba bolub"""
    keys = []
    for i in groups:
        keys.extend(
            [
                Key([MOD], i.name, lazy.group[i.name].toscreen()),
                Key(
                    [MOD, CONTROL],
                    i.name,
                    utils.toggle_borders_before_change_group,
                    lazy.window.togroup(i.name),
                    lazy.function(
                        lambda qtile,
                        group_name=i.name: utils.toggle_borders_after_change_group(
                            qtile, group_name, groups_dict
                        )
                    ),
                ),
                Key(
                    [MOD, SHIFT],
                    i.name,
                    utils.toggle_borders_before_change_group,
                    lazy.window.togroup(i.name),
                    lazy.group[i.name].toscreen(),
                    lazy.function(
                        lambda qtile,
                        group_name=i.name: utils.toggle_borders_after_change_group(
                            qtile, group_name, groups_dict
                        )
                    ),
                ),
            ]
        )
    return keys
