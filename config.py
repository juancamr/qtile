from libqtile.layout import MonadTall, MonadWide, Matrix, Bsp, Floating, RatioTile, Max
from libqtile.config import Group, Match, Key, Drag, Screen
from libqtile import qtile, widget, bar, hook
from libqtile.command import lazy
import subprocess
import os

# Constants -----------------------------------------------------------------

TERMINAL = "alacritty"
BROWSER = "firefox"
HOME = os.path.expanduser("~")
UBUNTU_FONT = "Ubuntu"
MOD = "mod4"
ALT = "mod1"
SHIFT = "shift"
CONTROL = "control"
PYHASHER = f"python {HOME}/.config/qtile/pyhasher.py &"

ZINC_900 = "18181b"
theme = {
    "first": [ZINC_900, ZINC_900],
    "second": [ZINC_900, ZINC_900],
    "third": [ZINC_900, ZINC_900],
    "fourth": [ZINC_900, ZINC_900],
    "group_selected": ["#1e40af", "#1e40af"],
    "group_inactive": ["#52525b", "#52525b"],
    "window_name": ["#fafafa", "#fafafa"],
    "panel_background": [ZINC_900, ZINC_900],
    "border_active": ["#0c4a6e", "#0c4a6e"],
    "border_inactive": ["#030712", "#030712"],
}

# Settings -----------------------------------------------------------------

mouse = [
    Drag(
        [MOD],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [MOD],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
]
dgroups_key_binder = None
dgroups_app_rules = []
main = None
floating_types = ["notification", "toolbar", "splash", "dialog"]
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = Floating(
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="Arcolinux-welcome-app.py"),
        Match(wm_class="Arcolinux-calamares-tool.py"),
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="Arandr"),
        Match(wm_class="feh"),
        Match(wm_class="Galculator"),
        Match(wm_class="archlinux-logout"),
        Match(wm_class="xfce4-terminal"),
        Match(wm_class="thunar"),
        Match(wm_class="Thunar"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="shutter"),
    ],
    fullscreen_border_width=0,
    border_width=0,
)
auto_fullscreen = True
focus_on_window_activation = "focus"  # or smart
wmname = "LG3D"

# Functions -----------------------------------------------------------------


@lazy.function
def capture_and_copy(_):
    screenshot_path = "/tmp/temp_capture.png"
    shutter_command = f"shutter -s -e -o {screenshot_path} && xclip -selection clipboard -target image/png -i {screenshot_path}"
    subprocess.run(shutter_command, shell=True, check=True)
    os.remove(screenshot_path)


@lazy.function
def volume_up(qtile):
    qtile.cmd_spawn("amixer -D pulse sset Master 5%+")


@lazy.function
def volume_down(qtile):
    qtile.cmd_spawn("amixer -D pulse sset Master 5%-")


def double(color: str) -> list:
    return [color, color]


# Keybindings ---------------------------------------------------------------

workspaces_keybindings = ["h", "t", "n", "s", "c", "r"]

# navigate keys
keys = [
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


def init_groups() -> list:
    firefox_match = Match(wm_class="firefox")
    obsidian_match = Match(wm_class="obsidian")
    anki_match = Match(wm_class="anki")

    groups = []
    group_names = workspaces_keybindings
    group_layouts = ["bsp" for _ in range(6)]
    group_matches = [[firefox_match], [obsidian_match], [anki_match], [], [], []]

    for name, layout_c, matches in zip(group_names, group_layouts, group_matches):
        groups.append(
            Group(
                name=name,
                layout=layout_c.lower(),
                label=name,
                matches=matches,
            )
        )

    return groups


def add_workspaces_keys(groups, keys) -> list:
    keys = []
    for i in groups:
        keys.extend(
            [
                Key([MOD], i.name, lazy.group[i.name].toscreen()),
                Key(
                    [MOD, CONTROL],
                    i.name,
                    lazy.window.togroup(i.name),
                ),
                Key(
                    [MOD, SHIFT],
                    i.name,
                    lazy.window.togroup(i.name),
                    lazy.group[i.name].toscreen(),
                ),
            ]
        )
    return keys


groups = init_groups()
workspaces = enumerate(workspaces_keybindings)
groups_dict = {keybind: index for (index, keybind) in workspaces}
keys.extend(add_workspaces_keys(groups, keys))
# custom keymaps
keys.extend(
    [
        Key([MOD], "Return", lazy.spawn(TERMINAL)),
        Key([MOD], "x", lazy.spawn("archlinut-logout")),
        Key([MOD], "d", lazy.spawn("dmenu_run")),
        Key([MOD], "b", lazy.spawn("browser")),
        Key([MOD], "a", lazy.function(lambda _: os.system(PYHASHER))),
        Key([MOD], "m", lazy.window.toggle_floating()),
        Key([MOD], "p", capture_and_copy),
        Key([MOD], "e", lazy.spawn("thunar")),
        Key([MOD], "v", volume_up),
        Key([MOD, SHIFT], "v", volume_down),
    ]
)


# Layouts ---------------------------------------------------------------------

layout_theme = {
    "margin": 0,
    "border_width": 1,
    "border_focus": theme["border_active"],
    "border_normal": theme["border_inactive"],
}
layouts = [
    MonadTall(**layout_theme),
    MonadWide(**layout_theme),
    Matrix(**layout_theme),
    Bsp(**layout_theme),
    Floating(**layout_theme),
    RatioTile(**layout_theme),
    Max(**layout_theme),
]


# topbar
def init_widgets():
    widget_defaults = dict(
        font=UBUNTU_FONT,
        fontsize=12,
        padding=2,
        background=theme["panel_background"],
    )
    font_size = 13

    spacer = widget.Sep(linewidth=0, padding=5, background=theme["panel_background"])
    white_double = double("#fafafa")

    def init_widgets_list():
        return [
            widget.GroupBox(
                font=UBUNTU_FONT,
                fontsize=font_size,
                margin_y=2,
                margin_x=0,
                padding_y=5,
                padding_x=3,
                borderwidth=3,
                active=white_double,
                inactive=theme["group_inactive"],
                rounded=False,
                highlight_method="block",  # block
                urgent_alert_method="block",
                this_current_screen_border=theme["group_selected"],
                this_screen_border=theme["panel_background"],
                other_current_screen_border=theme["panel_background"],
                other_screen_border=theme["panel_background"],
                foreground=white_double,
                background=theme["panel_background"],
                disable_drag=True,
            ),
            widget.Sep(
                linewidth=0,
                padding=40,
                background=theme["panel_background"],
            ),
            widget.WindowName(
                foreground=theme["window_name"],
                font=UBUNTU_FONT,
                background=theme["panel_background"],
                fontsize=font_size,
                padding=0,
            ),
            widget.Systray(
                background=theme["panel_background"],
            ),
            spacer,
            widget.TextBox(
                text="RAM:",
                font=UBUNTU_FONT,
                foreground=white_double,
                background=theme["first"],
                padding=0,
                fontsize=12,
            ),
            widget.Memory(
                foreground=white_double,
                background=theme["first"],
                font=UBUNTU_FONT,
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn(TERMINAL + " -e htop")
                },
                padding=5,
                fontsize=font_size,
            ),
            spacer,
            widget.TextBox(
                text="VOL:",
                fontsize=12,
                font=UBUNTU_FONT,
                foreground=white_double,
                background=theme["second"],
                padding=0,
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn(
                        f"{HOME}{ '/.config/qtile/audio.sh'}"
                    )
                },
            ),
            widget.Volume(
                font=UBUNTU_FONT,
                foreground=white_double,
                background=theme["second"],
                padding=5,
                fontsize=font_size,
            ),
            widget.CurrentLayout(
                foreground=white_double,
                fontsize=font_size,
                background=theme["third"],
                padding=5,
                font=UBUNTU_FONT,
            ),
            widget.Clock(
                foreground=white_double,
                background=theme["fourth"],
                font=UBUNTU_FONT,
                fontsize=font_size,
                format="%B %d - %H:%M",
            ),
            spacer,
        ]

    widgets_list = init_widgets_list()

    return widget_defaults, widgets_list


# Screens ---------------------------------------------------------------------

widgets_list = init_widgets()[1]
screens = [
    Screen(bottom=bar.Bar(widgets=widgets_list, size=20, opacity=1)),
]

# Events ---------------------------------------------------------------------


@hook.subscribe.startup_once
def start_once():
    autostart_script = "/.config/qtile/autostart.sh"
    subprocess.call([HOME + autostart_script])


@hook.subscribe.client_new
def set_floating(window):
    floating_types = ["notification", "toolbar", "splash", "dialog"]
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True
