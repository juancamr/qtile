from libqtile.command import lazy
from libqtile import qtile
from colors import Colors
from libqtile import widget
import const

my_colors = Colors()


def init_widgets():
    black = my_colors.duplicate_colors(my_colors.GRAY_900)

    def init_widgets_defaults():
        return dict(font=const.NOTO_SANS_FONT, fontsize=12, padding=2, background=black)

    widget_defaults = init_widgets_defaults()
    white = my_colors.duplicate_colors(my_colors.ZINC_050)
    panel_background = ["#292d3e", "#292d3e"]
    python_icon = "~/.config/qtile/icons/python.png"

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
                margin=4,
                background=panel_background,
                mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(const.TERMINAL)},
            ),
            widget.Sep(
                linewidth=0,
                padding=5,
                background=panel_background,
            ),
            widget.GroupBox(
                font=const.UBUNTU_BOLD_FONT,
                fontsize=12,
                margin_y=2,
                margin_x=0,
                padding_y=5,
                padding_x=3,
                borderwidth=3,
                active=white,
                inactive=my_colors.duplicate_colors(my_colors.GRAY_600),
                # rounded=True,
                rounded=False,
                # highlight_color=colors[9],
                # highlight_method="line",
                highlight_method="block",
                urgent_alert_method="block",
                # urgent_border=colors[9],
                this_current_screen_border=my_colors.duplicate_colors(
                    my_colors.BLUE_500
                ),
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
                foreground=my_colors.duplicate_colors(my_colors.INDIGO_300),
                background=panel_background,
                padding=0,
            ),
            widget.Systray(background=panel_background, padding=5),
            spacer,
            widget.TextBox(
                text=const.CORNER_ICON,
                font=const.FONT_AWESOME,
                background=panel_background,
                foreground=my_colors.duplicate_colors(my_colors.YELLOW_500),
                padding=0,
                fontsize=48.9,
            ),
            widget.TextBox(
                text=const.MEMORY_ICON,
                font=const.FONT_AWESOME,
                foreground=black,
                background=my_colors.duplicate_colors(my_colors.YELLOW_500),
                padding=0,
                fontsize=14,
            ),
            widget.Memory(
                foreground=black,
                background=my_colors.duplicate_colors(my_colors.YELLOW_500),
                font=const.NOTO_SANS_BOLD_FONT,
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn(const.TERMINAL + " -e htop")
                },
                padding=5,
            ),
            widget.TextBox(
                text=const.CORNER_ICON,
                font=const.FONT_AWESOME,
                background=my_colors.duplicate_colors(my_colors.YELLOW_500),
                foreground=my_colors.duplicate_colors(my_colors.ORANGE_500),
                padding=0,
                fontsize=48.9,
            ),
            widget.TextBox(
                text=const.VOLUME_ICON,
                fontsize=23,
                font=const.FONT_AWESOME,
                foreground=black,
                background=my_colors.duplicate_colors(my_colors.ORANGE_500),
                padding=0,
                mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(const.PAVUCONTROL)},
            ),
            widget.Volume(
                foreground=black,
                background=my_colors.duplicate_colors(my_colors.ORANGE_500),
                padding=5,
            ),
            widget.TextBox(
                text=const.CORNER_ICON,
                font=const.FONT_AWESOME,
                background=my_colors.duplicate_colors(my_colors.ORANGE_500),
                foreground=my_colors.duplicate_colors(my_colors.RED_500),
                padding=0,
                fontsize=48.9,
            ),
            widget.CurrentLayoutIcon(
                custom_icon_paths=const.ICONS_PATH,
                foreground=black,
                background=my_colors.duplicate_colors(my_colors.RED_500),
                padding=0,
                scale=0.7,
            ),
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=black,
                background=my_colors.duplicate_colors(my_colors.RED_500),
            ),
            widget.CurrentLayout(
                foreground=black,
                background=my_colors.duplicate_colors(my_colors.RED_500),
                padding=5,
                font=const.NOTO_SANS_BOLD_FONT,
            ),
            widget.TextBox(
                text=const.CORNER_ICON,
                font=const.FONT_AWESOME,
                background=my_colors.duplicate_colors(my_colors.RED_500),
                foreground=my_colors.duplicate_colors(my_colors.INDIGO_500),
                padding=0,
                fontsize=48.9,
            ),
            widget.Clock(
                foreground=black,
                background=my_colors.duplicate_colors(my_colors.INDIGO_500),
                font=const.NOTO_SANS_BOLD_FONT,
                format="%B %d  [ %H:%M ]",
            ),
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=black,
                background=my_colors.duplicate_colors(my_colors.INDIGO_500),
            ),
        ]

        return widgets_list

    widgets_list = init_widgets_list()

    return widget_defaults, widgets_list
