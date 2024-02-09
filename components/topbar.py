"""module for get the topbar widgets"""
from libqtile import qtile, widget
from juancamr.utils import constants as const
from juancamr.utils.theme import theme, white_double


def init_widgets():
    """get the widgets"""
    widget_defaults = dict(
        font=const.PRODUCT_SANS_FONT,
        fontsize=12,
        padding=2,
        background=theme.panel_background,
    )
    font_size = 13

    spacer = widget.Sep(linewidth=0, padding=5, background=theme.panel_background)

    def init_widgets_list():
        return [
            widget.GroupBox(
                font=const.PRODUCT_SANS_FONT,
                fontsize=font_size,
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
                font=const.PRODUCT_SANS_FONT,
                background=theme.panel_background,
                fontsize=font_size,
                padding=0,
            ),
            widget.Systray(),
            spacer,
            widget.TextBox(
                text=const.MEMORY_ICON,
                font=const.FONT_AWESOME,
                foreground=white_double,
                background=theme.first,
                padding=0,
                fontsize=12,
            ),
            widget.Memory(
                foreground=white_double,
                background=theme.first,
                font=const.PRODUCT_SANS_FONT,
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn(const.TERMINAL + " -e htop")
                },
                padding=5,
                fontsize=font_size,
            ),
            spacer,
            widget.TextBox(
                text=const.VOLUME_ICON,
                fontsize=16,
                font=const.FONT_AWESOME,
                foreground=white_double,
                background=theme.second,
                padding=0,
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn(
                        f"{const.HOME}{const.CHANGE_OUTPUT}"
                    )
                },
            ),
            widget.Volume(
                font=const.PRODUCT_SANS_FONT,
                foreground=white_double,
                background=theme.second,
                padding=5,
                fontsize=font_size,
            ),
            widget.CurrentLayout(
                foreground=white_double,
                fontsize=font_size,
                background=theme.third,
                padding=5,
                font=const.PRODUCT_SANS_FONT,
            ),
            spacer,
            widget.Clock(
                foreground=white_double,
                background=theme.fourth,
                font=const.PRODUCT_SANS_FONT,
                fontsize=font_size,
                format="%B %d - %H:%M",
            ),
            spacer,
        ]

    widgets_list = init_widgets_list()

    return widget_defaults, widgets_list
