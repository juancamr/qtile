from libqtile.widget import Spacer, TextBox, GroupBox, Clock, Systray


def init_colors():
    return [
        ["#2F343F", "#2F343F"],  # color 0
        ["#2F343F", "#2F343F"],  # color 1
        ["#c0c5ce", "#c0c5ce"],  # color 2
        ["#fba922", "#fba922"],  # color 3
        ["#3384d0", "#3384d0"],  # color 4
        ["#f3f4f5", "#f3f4f5"],  # color 5
        ["#cd1f3f", "#cd1f3f"],  # color 6
        ["#62FF00", "#62FF00"],  # color 7
        ["#6790eb", "#6790eb"],  # color 8
        ["#a9a9a9", "#a9a9a9"],
    ]  # color 9


colors = init_colors()


def init_widgets():
    def init_widgets_defaults():
        return dict(font="Noto Sans", fontsize=12, padding=2, background=colors[1])

    widget_defaults = init_widgets_defaults()

    def init_widgets_list():
        spacer = TextBox(text=" ")
        widgets_list = [
            spacer,
            GroupBox(
                font="Noto Sans Bold",
                fontsize=12,
                margin_y=0,
                margin_x=0,
                padding_y=6,
                padding_x=5,
                borderwidth=0,
                disable_drag=True,
                active=colors[9],
                inactive=colors[5],
                rounded=False,
                highlight_method="text",
                this_current_screen_border=colors[8],
                foreground=colors[2],
                background=colors[1],
            ),
            Spacer(),
            Clock(
                foreground=colors[5],
                background=colors[1],
                fontsize=12,
                format="%Y-%m-%d - %H:%M",
            ),
            Systray(background=colors[1], icon_size=20, padding=10),
        ]

        widgets_list.insert(0, spacer)
        widgets_list.append(spacer)

        return widgets_list

    widgets_list = init_widgets_list()

    return widget_defaults, widgets_list
