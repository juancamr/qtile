from libqtile import widget, qtile
from utils import constants as const
from utils.colors import double

text_size = 13
corner_size = 48.9
white = double("#fafafa")
black = double("#030712")


def groups_widget(
    active_background: str, inactive_foreground: str, panel_background: str
) -> object:
    return (
        widget.GroupBox(
            font=const.PRODUCT_SANS_BOLD_FONT,
            fontsize=12,
            margin_y=2,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=white,
            inactive=double(inactive_foreground),
            rounded=False,
            highlight_method="block",
            urgent_alert_method="block",
            this_current_screen_border=double(active_background),
            this_screen_border=black,
            other_current_screen_border=double(panel_background),
            other_screen_border=double(panel_background),
            foreground=white,
            background=double(panel_background),
            disable_drag=True,
        ),
    )


def ram_widget(background: str, foreground: str, next_color: str) -> list:
    return [
        widget.TextBox(
            text=const.CORNER_ICON,
            font=const.FONT_AWESOME,
            background=double(next_color),
            foreground=double(background),
            padding=0,
            fontsize=corner_size,
        ),
        widget.TextBox(
            text=const.MEMORY_ICON,
            font=const.FONT_AWESOME,
            foreground=double(foreground),
            background=double(background),
            padding=0,
            fontsize=14,
        ),
        widget.Memory(
            foreground=double(foreground),
            background=double(background),
            font=const.PRODUCT_SANS_BOLD_FONT,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn(const.TERMINAL + " -e htop")
            },
            padding=5,
            fontsize=14,
        ),
    ]


def volume_widget(background: str, foreground: str, next_color: str) -> list:
    return [
        widget.TextBox(
            text=const.CORNER_ICON,
            font=const.FONT_AWESOME,
            background=double(next_color),
            foreground=double(background),
            padding=0,
            fontsize=corner_size,
        ),
        widget.TextBox(
            text=const.VOLUME_ICON,
            fontsize=23,
            font=const.FONT_AWESOME,
            foreground=double(foreground),
            background=double(background),
            padding=0,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(const.PAVUCONTROL)},
        ),
        widget.Volume(
            font=const.PRODUCT_SANS_BOLD_FONT,
            foreground=double(foreground),
            background=double(background),
            padding=5,
            fontsize=text_size,
        ),
    ]


def layout_widget(background: str, foreground: str, next_color: str) -> list:
    return [
        widget.TextBox(
            text=const.CORNER_ICON,
            font=const.FONT_AWESOME,
            background=double(next_color),
            foreground=double(background),
            padding=0,
            fontsize=corner_size,
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=const.ICONS_PATH,
            foreground=double(foreground),
            background=double(background),
            padding=0,
            scale=0.7,
        ),
        widget.Sep(
            linewidth=0,
            padding=5,
            foreground=double(foreground),
            background=double(background),
        ),
        widget.CurrentLayout(
            foreground=double(foreground),
            fontsize=text_size,
            background=double(background),
            padding=5,
            font=const.PRODUCT_SANS_BOLD_FONT,
        ),
    ]


def date_widget(background: str, foreground: str, next_color: str) -> list:
    return [
        widget.TextBox(
            text=const.CORNER_ICON,
            font=const.FONT_AWESOME,
            background=double(next_color),
            foreground=double(background),
            padding=0,
            fontsize=corner_size,
        ),
        widget.Clock(
            foreground=double(foreground),
            background=double(background),
            font=const.PRODUCT_SANS_BOLD_FONT,
            fontsize=text_size,
            format="%B %d  [ %H:%M ]",
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=double(foreground),
            background=double(background),
        ),
    ]


def systray(background: str, foreground: str, next_color: str) -> list:
    return [
        widget.TextBox(
            text=const.CORNER_ICON,
            font=const.FONT_AWESOME,
            background=double(next_color),
            foreground=double(background),
            fontsize=corner_size,
            padding=0,
        ),
        widget.Systray(background=double(background)),
    ]
