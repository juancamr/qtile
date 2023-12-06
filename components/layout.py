"""setup layout qtile"""

from libqtile import layout
from libqtile.config import Group, Match
from settings import keymap
from utils.theme import theme

WITH_MARGIN = True
MARGIN = 15


def init_groups() -> list:
    """initialize groups"""

    groups = []
    group_names = keymap.workspaces_keybindings
    group_labels = ["www", "code", "term", "notes", "music", "other"]
    # group_labels = [str(i + 1) for i in range(6)]
    group_layouts = ["bsp" for _ in range(6)]
    group_matches = [[Match(wm_class="firefox")], *[None for _ in range(5)]]

    for name, layout_c, label, matches in zip(
        group_names, group_layouts, group_labels, group_matches
    ):
        groups.append(
            Group(
                name=name,
                layout=layout_c.lower(),
                label=label,
                matches=matches,
            )
        )

    return groups


def init_layouts() -> list:
    """return the default layouts"""

    layout_theme = {
        "margin": MARGIN if WITH_MARGIN else 0,
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
