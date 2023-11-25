from libqtile.config import Screen
from topbar import init_widgets
from libqtile import bar

widgets_list = init_widgets()[1]

def init_widgets_screen1():
    widgets_screen1 = widgets_list
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = widgets_list
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26, opacity=0.8)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26, opacity=0.8))]