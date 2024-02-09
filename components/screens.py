from libqtile.config import Screen
from components.topbar import init_widgets
from libqtile import bar

widgets_list = init_widgets()[1]


def init_widgets_screen1() -> list:
    return widgets_list


def init_widgets_screen2() -> list:
    return widgets_list


widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [
        Screen(bottom=bar.Bar(widgets=init_widgets_screen1(), size=20, opacity=1)),
        Screen(bottom=bar.Bar(widgets=init_widgets_screen2(), size=20, opacity=1)),
    ]
