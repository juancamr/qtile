"""module for get the topbar widgets"""
from libqtile import qtile, widget
from utils import constants as const, utils
from utils.theme import theme, white_double, black_double


def init_widgets():
    """get the widgets"""
    widget_defaults = dict(
        font=const.PRODUCT_SANS_FONT,
        fontsize=12,
        padding=2,
        background=theme.panel_background,
    )

    def init_widgets_list():
        return [
            widget.Sep(
                linewidth=0,
                padding=6,
                background=theme.panel_background,
            ),
            widget.Image(
                filename=const.ICON_TOPBAR,
                margin=4,
                background=theme.panel_background,
                mouse_callbacks={"Button1": utils.random_wallpaper},
            ),
            widget.Sep(
                linewidth=0,
                padding=5,
                background=theme.panel_background,
            ),
            widget.GroupBox(
                font=const.PRODUCT_SANS_BOLD_FONT,
                fontsize=12,
                margin_y=2,
                margin_x=0,
                padding_y=5,
                padding_x=3,
                borderwidth=3,
                active=white_double,
                inactive=theme.group_inactive,
                rounded=False,
                highlight_method="block",  # block
                urgent_alert_method="block",
                this_current_screen_border=theme.group_selected,
                this_screen_border=theme.panel_background,
                other_current_screen_border=theme.panel_background,
                other_screen_border=theme.panel_background,
                foreground=white_double,
                background=theme.panel_background,
                disable_drag=True,
            ),
            widget.Sep(
                linewidth=0,
                padding=40,
                background=theme.panel_background,
            ),
            widget.WindowName(
                foreground=theme.window_name,
                font=const.PRODUCT_SANS_BOLD_FONT,
                background=theme.panel_background,
                fontsize=13,
                padding=0,
            ),
            widget.TextBox(
                text=const.CORNER_ICON,
                font=const.FONT_AWESOME,
                background=theme.panel_background,
                foreground=theme.first,
                padding=0,
                fontsize=48.9,
            ),
            widget.TextBox(
                text=const.MEMORY_ICON,
                font=const.FONT_AWESOME,
                foreground=black_double,
                background=theme.first,
                padding=0,
                fontsize=14,
            ),
            widget.Memory(
                foreground=black_double,
                background=theme.first,
                font=const.PRODUCT_SANS_BOLD_FONT,
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn(const.TERMINAL + " -e htop")
                },
                padding=5,
                fontsize=13,
            ),
            widget.TextBox(
                text=const.CORNER_ICON,
                font=const.FONT_AWESOME,
                background=theme.first,
                foreground=theme.second,
                padding=0,
                fontsize=48.9,
            ),
            widget.TextBox(
                text=const.VOLUME_ICON,
                fontsize=23,
                font=const.FONT_AWESOME,
                foreground=black_double,
                background=theme.second,
                padding=0,
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn(
                        f"{const.HOME}{const.CHANGE_OUTPUT}"
                    )
                },
            ),
            widget.Volume(
                font=const.PRODUCT_SANS_BOLD_FONT,
                foreground=black_double,
                background=theme.second,
                padding=5,
                fontsize=13,
            ),
            widget.TextBox(
                text=const.CORNER_ICON,
                font=const.FONT_AWESOME,
                background=theme.second,
                foreground=theme.third,
                padding=0,
                fontsize=48.9,
            ),
            widget.CurrentLayoutIcon(
                custom_icon_paths=const.ICONS_PATH,
                foreground=black_double,
                background=theme.third,
                padding=0,
                scale=0.7,
            ),
            widget.Sep(
                linewidth=0,
                padding=5,
                foreground=black_double,
                background=theme.third,
            ),
            widget.CurrentLayout(
                foreground=black_double,
                fontsize=13,
                background=theme.third,
                padding=5,
                font=const.PRODUCT_SANS_BOLD_FONT,
            ),
            widget.TextBox(
                text=const.CORNER_ICON,
                font=const.FONT_AWESOME,
                background=theme.third,
                foreground=theme.fourth,
                padding=0,
                fontsize=48.9,
            ),
            widget.Clock(
                foreground=black_double,
                background=theme.fourth,
                font=const.PRODUCT_SANS_BOLD_FONT,
                fontsize=13,
                format="%B %d - %H:%M",
            ),
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=black_double,
                background=theme.fourth,
            ),
        ]

    widgets_list = init_widgets_list()

    return widget_defaults, widgets_list
