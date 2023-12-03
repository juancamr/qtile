from libqtile import layout
from libqtile.config import Group
import settings.keymap as keymap
from utils.theme import theme

with_margin = True
margin = 20


def init_groups() -> list:
    groups = []
    group_names = keymap.workspaces_keybindings
    group_labels = ["www", "code", "term", "notes", "music", "other"]
    # group_labels = [str(i + 1) for i in range(6)]
    group_layouts = ["bsp" for _ in range(6)]
    group_matches = [*[None for _ in range(6)]]

    for i in range(len(group_names)):
        groups.append(
            Group(
                name=group_names[i],
                layout=group_layouts[i].lower(),
                label=group_labels[i],
                matches=group_matches[i],
            )
        )

    return groups


def init_layouts() -> list:
    layout_theme = {
        "margin": margin if with_margin else 0,
        "border_width": 1,
        "border_focus": theme.border_active,
        "border_normal": theme.border_inactive,
    }

    return [
        layout.MonadTall(**layout_theme),
        layout.MonadWide(**layout_theme),
        layout.Matrix(**layout_theme),
        layout.Bsp(**layout_theme),
        layout.Floating(**layout_theme),
        layout.RatioTile(**layout_theme),
        layout.Max(**layout_theme),
    ]
