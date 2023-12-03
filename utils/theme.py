from utils.colors import double, Colors


class Theme:
    def __init__(
        self,
        first,
        second,
        third,
        fourth,
        group_selected,
        group_inactive,
        window_name,
        panel_background,
        border_active,
        border_inactive,
    ):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.group_selected = group_selected
        self.group_inactive = group_inactive
        self.window_name = window_name
        self.panel_background = panel_background
        self.border_active = border_active
        self.border_inactive = border_inactive


colors = Colors()
black_double = double(colors.GRAY_900)
white_double = double(colors.ZINC_050)

tokio = Theme(
    first=double(colors.BLUE_600),
    second=double(colors.INDIGO_600),
    third=double(colors.VIOLET_600),
    fourth=double(colors.PURPLE_600),
    group_selected=double(colors.BLUE_600),
    group_inactive=double(colors.GRAY_600),
    window_name=double(colors.YELLOW_500),
    panel_background=double(colors.GRAY_800),
    border_active=colors.BLUE_700,
    border_inactive=colors.BLUE_950,
)

yellow = Theme(
    first=double(colors.YELLOW_600),
    second=double(colors.AMBER_600),
    third=double(colors.ORANGE_600),
    fourth=double(colors.RED_600),
    group_selected=double(colors.BLUE_600),
    group_inactive=double(colors.GRAY_600),
    window_name=double(colors.YELLOW_500),
    panel_background=double(colors.GRAY_800),
    border_active=colors.YELLOW_600,
    border_inactive=colors.YELLOW_950,
)

theme = tokio
