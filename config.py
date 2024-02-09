from juancamr import keymaps, set, events
from components import layout, topbar, screens

# navigate keys
keys = keymaps.init_navigate_keys()
groups = layout.init_groups()
keys.extend(keymaps.add_workespaces_keys(groups, keys))

# custom keys
keys.extend(keymaps.init_custom_keys())
layouts = layout.init_layouts()
widget_defaults, widgets_list = topbar.init_widgets()

# screens
screens = screens.init_screens()
follow_mouse_focus = False
