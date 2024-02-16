from libqtile.layout import MonadTall, MonadWide, Matrix, Bsp, Floating, RatioTile, Max
from libqtile.config import Screen
from libqtile import bar
from libqtile import qtile, widget
from libqtile.config import Group, Match
from libqtile.config import Key
from libqtile import hook
from libqtile.config import Drag
from libqtile.command import lazy
import subprocess
import os

# Constants -----------------------------------------------------------------

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

TERMINAL = "alacritty"
BROWSER = "firefox"
OBSIDIAN = "obsidian"
THUNAR = "thunar"
CODE = "code"
HOME = os.path.expanduser("~")
# DMENU = f"dmenu_run -i -nb '{theme["panel_background"][1]}' -nf '{theme["window_name"][1]}' -sb '{theme["window_name"][1]}' -sf '{theme["panel_background"][1]}' -fn 'ProductSans:bold:pixelsize=14'"
DMENU = "dmenu_run"
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

PYHASHER = f"python {HOME}/pyhasher/main.py &"
OPEN_SETTINGS = f"cd {HOME}/.config/qtile; nvim ."
AUTOSTART_SCRIPT = "/.config/qtile/autostart.sh"
CHANGE_OUTPUT = "/.config/qtile/audio.sh"

# icons
CORNER_ICON = ""
VOLUME_ICON = " "
MEMORY_ICON = ""

# super keys
MOD = "mod4"
ALT = "mod1"
SHIFT = "shift"
CONTROL = "control"

WITH_MARGIN = True
MARGIN = 0

# Settings -----------------------------------------------------------------

mod = "mod4"
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod],
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
        # Run the utility of `xprop` to see the wm class and name of an X client.
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

# Keybindings ---------------------------------------------------------------

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

# groups keymaps
workspaces_keybindings = ["h", "t", "n", "s", "c", "r"]


def init_groups() -> list:
    """initialize groups"""
    firefox_match = Match(wm_class="firefox")
    obsidian_match = Match(wm_class="obsidian")
    anki_match = Match(wm_class="anki")

    groups = []
    group_names = workspaces_keybindings
    group_labels = workspaces_keybindings
    group_layouts = ["bsp" for _ in range(6)]
    group_matches = [[firefox_match], [obsidian_match], [anki_match], [], [], []]

    for name, layout_c, label, matches in zip(
        group_names, group_layouts, group_labels, group_matches
    ):
        groups.append(
            Group(
                name=name,
                layout=layout_c.lower(),
                label=label,
                matches=matches,
            )
        )

    return groups


groups = init_groups()


@lazy.function
def toggle_borders_before_change_group(qtile):
    """verifica si en el actual group queda unicaemnte una ventana"""
    toggle_borders(qtile.current_group, False, is_for_migrate=True)


def toggle_borders_after_change_group(qtile, group_name, groups_dict: dict):
    """despues de cambiar entre grupos verifica el estado
    de esta contando la cantidad de ventanas actuales"""
    index_group = groups_dict[group_name]
    group = qtile.groups[index_group]
    if len(group.windows) == 1:
        toggle_borders(group, False)
    else:
        toggle_borders(group, True)


workspaces = enumerate(workspaces_keybindings)


groups_dict = {keybind: index for (index, keybind) in workspaces}


def add_workespaces_keys(groups, keys) -> list:
    keys = []
    for i in groups:
        keys.extend(
            [
                Key([MOD], i.name, lazy.group[i.name].toscreen()),
                Key(
                    [MOD, CONTROL],
                    i.name,
                    toggle_borders_before_change_group,
                    lazy.window.togroup(i.name),
                    lazy.function(
                        lambda qtile,
                        group_name=i.name: toggle_borders_after_change_group(
                            qtile, group_name, groups_dict
                        )
                    ),
                ),
                Key(
                    [MOD, SHIFT],
                    i.name,
                    toggle_borders_before_change_group,
                    lazy.window.togroup(i.name),
                    lazy.group[i.name].toscreen(),
                    lazy.function(
                        lambda qtile,
                        group_name=i.name: toggle_borders_after_change_group(
                            qtile, group_name, groups_dict
                        )
                    ),
                ),
            ]
        )
    return keys


SCREENSHOT_PATH = "/tmp/temp_capture.png"
SHUTTER_COMMAND = f"shutter -s -e -o {SCREENSHOT_PATH} && xclip -selection clipboard -target image/png -i {SCREENSHOT_PATH}"


@lazy.function
def capture_and_copy(_):
    """funcion que realiza una seleccion para capturar
    la pantalla para posteriormente copiarla al portapapeles"""
    capture_command = SHUTTER_COMMAND
    subprocess.run(capture_command, shell=True, check=True)
    os.remove(SCREENSHOT_PATH)


@lazy.function
def volume_up(qtile):
    qtile.cmd_spawn("amixer -D pulse sset Master 5%+")


@lazy.function
def volume_down(qtile):
    qtile.cmd_spawn("amixer -D pulse sset Master 5%-")


keys.extend(add_workespaces_keys(groups, keys))

# custom keymaps
keys.extend(
    [
        Key([MOD], "Return", lazy.spawn(TERMINAL)),
        Key([MOD, SHIFT], "Return", lazy.spawn(THUNAR)),
        Key([MOD], "x", lazy.spawn(LOGOUT_COMMAND)),
        Key([MOD], "d", lazy.spawn(DMENU)),
        Key([MOD], "b", lazy.spawn(BROWSER)),
        Key([MOD], "a", lazy.function(lambda _: os.system(PYHASHER))),
        Key([MOD], "o", lazy.spawn(OBSIDIAN)),
        Key([MOD], "m", lazy.window.toggle_floating()),
        Key([MOD], "p", capture_and_copy),
        Key([MOD], "e", lazy.spawn(THUNAR)),
        Key([MOD], "v", volume_up),
        Key([MOD, SHIFT], "v", volume_down),
    ]
)


# Layouts ---------------------------------------------------------------------


def double(color: str) -> list:
    return [color, color]


layout_theme = {
    "margin": MARGIN if WITH_MARGIN else 0,
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


def init_widgets():
    """get the widgets"""
    widget_defaults = dict(
        font=PRODUCT_SANS_FONT,
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
                font=PRODUCT_SANS_FONT,
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
                font=PRODUCT_SANS_FONT,
                background=theme["panel_background"],
                fontsize=font_size,
                padding=0,
            ),
            widget.Systray(),
            spacer,
            widget.TextBox(
                text=MEMORY_ICON,
                font=FONT_AWESOME,
                foreground=white_double,
                background=theme["first"],
                padding=0,
                fontsize=12,
            ),
            widget.Memory(
                foreground=white_double,
                background=theme["first"],
                font=PRODUCT_SANS_FONT,
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn(TERMINAL + " -e htop")
                },
                padding=5,
                fontsize=font_size,
            ),
            spacer,
            widget.TextBox(
                text=VOLUME_ICON,
                fontsize=16,
                font=FONT_AWESOME,
                foreground=white_double,
                background=theme["second"],
                padding=0,
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn(f"{HOME}{CHANGE_OUTPUT}")
                },
            ),
            widget.Volume(
                font=PRODUCT_SANS_FONT,
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
                font=PRODUCT_SANS_FONT,
            ),
            spacer,
            widget.Clock(
                foreground=white_double,
                background=theme["fourth"],
                font=PRODUCT_SANS_FONT,
                fontsize=font_size,
                format="%B %d - %H:%M",
            ),
            spacer,
        ]

    widgets_list = init_widgets_list()

    return widget_defaults, widgets_list


# Screens ---------------------------------------------------------------------

widgets_list = init_widgets()[1]


def init_screens():
    return [
        Screen(bottom=bar.Bar(widgets=widgets_list, size=20, opacity=1)),
        Screen(bottom=bar.Bar(widgets=widgets_list, size=20, opacity=1)),
    ]


screens = init_screens()
follow_mouse_focus = False


# Events ---------------------------------------------------------------------


def toggle_borders(group, is_for_open: bool, is_for_migrate=False):
    len_windows = len(group.windows)
    count_windows = 0 if is_for_open else 2 if is_for_migrate else 1
    group.use_layout(3 if len_windows == count_windows else 0)


@hook.subscribe.client_new
def new_client(window):
    toggle_borders(window.qtile.current_group, True)


@hook.subscribe.client_killed
def kill_client(window):
    toggle_borders(window.qtile.current_group, False)


@hook.subscribe.startup_once
def start_once():
    subprocess.call([HOME + AUTOSTART_SCRIPT])


@hook.subscribe.client_new
def set_floating(window):
    floating_types = ["notification", "toolbar", "splash", "dialog"]
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True
