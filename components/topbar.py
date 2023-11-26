from libqtile import qtile, widget
from utils.colors import Colors
from utils import constants as const

colors = Colors()


def init_widgets():
    black = colors.double(colors.GRAY_900)

    def init_widgets_defaults():
        return dict(font=const.NOTO_SANS_FONT, fontsize=12, padding=2, background=black)

    widget_defaults = init_widgets_defaults()
    white = colors.double(colors.ZINC_050)
    panel_background = ["#292d3e", "#292d3e"]
    python_icon = "~/.config/qtile/assets/icons/python.png"

    def init_widgets_list():
        spacer = widget.TextBox(text=" ", background=panel_background)
        widgets_list = [
            widget.Sep(
                linewidth=0,
                padding=6,
                background=panel_background,
            ),
            widget.Image(
                filename=python_icon,
                margin=1,
                background=panel_background,
                mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(const.TERMINAL)},
            ),
            widget.Sep(
                linewidth=0,
                padding=5,
                background=panel_background,
            ),
            widget.GroupBox(
                font=const.NOTO_SANS_BOLD_FONT,
                fontsize=12,
                margin_y=2,
                margin_x=0,
                padding_y=5,
                padding_x=3,
                borderwidth=3,
                active=white,
                inactive=colors.double(colors.GRAY_600),
                rounded=False,
                highlight_method="block",
                urgent_alert_method="block",
                this_current_screen_border=colors.double(colors.BLUE_500),
                this_screen_border=black,
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
                foreground=colors.double(colors.INDIGO_300),
                background=panel_background,
                padding=0,
            ),
            widget.Systray(background=panel_background, padding=5),
            spacer,
            widget.TextBox(
                text=const.CORNER_ICON,
                font=const.FONT_AWESOME,
                background=panel_background,
                foreground=colors.double(colors.YELLOW_500),
                padding=0,
                fontsize=48.9,
            ),
            widget.TextBox(
                text=const.MEMORY_ICON,
                font=const.FONT_AWESOME,
                foreground=black,
                background=colors.double(colors.YELLOW_500),
                padding=0,
                fontsize=14,
            ),
            widget.Memory(
                foreground=black,
                background=colors.double(colors.YELLOW_500),
                font=const.NOTO_SANS_BOLD_FONT,
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn(const.TERMINAL + " -e htop")
                },
                padding=5,
                fontsize=13,
            ),
            widget.TextBox(
                text=const.CORNER_ICON,
                font=const.FONT_AWESOME,
                background=colors.double(colors.YELLOW_500),
                foreground=colors.double(colors.ORANGE_500),
                padding=0,
                fontsize=48.9,
            ),
            widget.TextBox(
                text=const.VOLUME_ICON,
                fontsize=23,
                font=const.FONT_AWESOME,
                foreground=black,
                background=colors.double(colors.ORANGE_500),
                padding=0,
                mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(const.PAVUCONTROL)},
            ),
            widget.Volume(
                font=const.NOTO_SANS_BOLD_FONT,
                foreground=black,
                background=colors.double(colors.ORANGE_500),
                padding=5,
                fontsize=13,
            ),
            widget.TextBox(
                text=const.CORNER_ICON,
                font=const.FONT_AWESOME,
                background=colors.double(colors.ORANGE_500),
                foreground=colors.double(colors.RED_500),
                padding=0,
                fontsize=48.9,
            ),
            widget.CurrentLayoutIcon(
                custom_icon_paths=const.ICONS_PATH,
                foreground=black,
                background=colors.double(colors.RED_500),
                padding=0,
                scale=0.7,
            ),
            widget.Sep(
                linewidth=0,
                padding=5,
                foreground=black,
                background=colors.double(colors.RED_500),
            ),
            widget.CurrentLayout(
                foreground=black,
                fontsize=13,
                background=colors.double(colors.RED_500),
                padding=5,
                font=const.NOTO_SANS_BOLD_FONT,
            ),
            widget.TextBox(
                text=const.CORNER_ICON,
                font=const.FONT_AWESOME,
                background=colors.double(colors.RED_500),
                foreground=colors.double(colors.BLUE_300),
                padding=0,
                fontsize=48.9,
            ),
            widget.Clock(
                foreground=black,
                background=colors.double(colors.BLUE_300),
                font=const.NOTO_SANS_BOLD_FONT,
                fontsize=13,
                format="%B %d  [ %H:%M ]",
            ),
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=black,
                background=colors.double(colors.BLUE_300),
            ),
        ]

        return widgets_list

    widgets_list = init_widgets_list()

    return widget_defaults, widgets_list
