from libqtile.config import Group
from libqtile import layout
import keymap


def init_groups():
    groups = []
    group_names = keymap.workspaces_keybindings
    group_labels = ["Web", "Code", "Notes", "Term"]
    group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall"]

    for i in range(len(group_names)):
        groups.append(
            Group(
                name=group_names[i],
                layout=group_layouts[i].lower(),
                label=group_labels[i],
            )
        )

    return groups


def init_layouts():
    def init_layout_theme():
        return {
            "margin": 10,
            "border_width": 2,
            "border_focus": "#6F00FF",
            "border_normal": "#32127A",
        }

    layout_theme = init_layout_theme()

    return [
        layout.MonadTall(**layout_theme),
        layout.MonadWide(**layout_theme),
        layout.Matrix(**layout_theme),
        layout.Bsp(**layout_theme),
        layout.Floating(**layout_theme),
        layout.RatioTile(**layout_theme),
        layout.Max(**layout_theme),
    ]
