from libqtile import qtile, widget
from utils.colors import colors, double, purple_combination
from utils import constants as const, utils


def init_widgets():
    black = double(colors.GRAY_900)

    def init_widgets_defaults():
        return dict(
            font=const.PRODUCT_SANS_FONT, fontsize=12, padding=2, background=black
        )

    widget_defaults = init_widgets_defaults()
    white = double(colors.ZINC_050)
    panel_background = ["#292d3e", "#292d3e"]

    (
        ram_background,
        volume_background,
        layout_background,
        date_background,
    ) = purple_combination

    python_icon = "~/.config/qtile/assets/icons/python.png"

    def init_widgets_list():
        spacer = widget.TextBox(text=" ", background=panel_background)
        return [
            widget.Sep(
                linewidth=0,
                padding=6,
                background=panel_background,
            ),
            widget.Image(
                filename=python_icon,
                margin=1,
                background=panel_background,
                # mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(const.TERMINAL)},
                mouse_callbacks={"Button1": utils.random_wallpaper},
            ),
            widget.Sep(
                linewidth=0,
                padding=5,
                background=panel_background,
            ),
            widget.GroupBox(
                font=const.PRODUCT_SANS_BOLD_FONT,
                fontsize=12,
                margin_y=2,
                margin_x=0,
                padding_y=5,
                padding_x=3,
                borderwidth=3,
                active=white,
                inactive=double(colors.GRAY_600),
                rounded=False,
                highlight_method="block",  # block
                urgent_alert_method="block",
                this_current_screen_border=double(colors.BLUE_600),
                this_screen_border=panel_background,
                other_current_screen_border=panel_background,
                other_screen_border=panel_background,
                foreground=white,
                background=panel_background,
                disable_drag=True,
            ),
            widget.Sep(
                linewidth=0,
                padding=40,
                background=panel_background,
            ),
            widget.WindowName(
                foreground=double(colors.YELLOW_500),
                font=const.PRODUCT_SANS_BOLD_FONT,
                background=panel_background,
                fontsize=13,
                padding=0,
            ),
            widget.Systray(background=panel_background, padding=5),
            spacer,
            widget.TextBox(
                text=const.CORNER_ICON,
                font=const.FONT_AWESOME,
                background=panel_background,
                foreground=ram_background,
                padding=0,
                fontsize=48.9,
            ),
            widget.TextBox(
                text=const.MEMORY_ICON,
                font=const.FONT_AWESOME,
                foreground=black,
                background=ram_background,
                padding=0,
                fontsize=14,
            ),
            widget.Memory(
                foreground=black,
                background=ram_background,
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
                background=ram_background,
                foreground=volume_background,
                padding=0,
                fontsize=48.9,
            ),
            widget.TextBox(
                text=const.VOLUME_ICON,
                fontsize=23,
                font=const.FONT_AWESOME,
                foreground=black,
                background=volume_background,
                padding=0,
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn(
                        f"{const.HOME}{const.CHANGE_OUTPUT}"
                    )
                },
            ),
            widget.Volume(
                font=const.PRODUCT_SANS_BOLD_FONT,
                foreground=black,
                background=volume_background,
                padding=5,
                fontsize=13,
            ),
            widget.TextBox(
                text=const.CORNER_ICON,
                font=const.FONT_AWESOME,
                background=volume_background,
                foreground=layout_background,
                padding=0,
                fontsize=48.9,
            ),
            widget.CurrentLayoutIcon(
                custom_icon_paths=const.ICONS_PATH,
                foreground=black,
                background=layout_background,
                padding=0,
                scale=0.7,
            ),
            widget.Sep(
                linewidth=0,
                padding=5,
                foreground=black,
                background=layout_background,
            ),
            widget.CurrentLayout(
                foreground=black,
                fontsize=13,
                background=layout_background,
                padding=5,
                font=const.PRODUCT_SANS_BOLD_FONT,
            ),
            widget.TextBox(
                text=const.CORNER_ICON,
                font=const.FONT_AWESOME,
                background=layout_background,
                foreground=date_background,
                padding=0,
                fontsize=48.9,
            ),
            widget.Clock(
                foreground=black,
                background=date_background,
                font=const.PRODUCT_SANS_BOLD_FONT,
                fontsize=13,
                format="%B %d - %H:%M",
            ),
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=black,
                background=date_background,
            ),
        ]

    widgets_list = init_widgets_list()

    return widget_defaults, widgets_list
