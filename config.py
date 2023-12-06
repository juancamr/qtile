from settings import keymap, set as myset, functions as fn
from components import layout, topbar, screens

# navigate keys
keys = keymap.init_navigate_keys()
# workspaces keys
groups = layout.init_groups()
keys.extend(keymap.add_workespaces_keys(groups, keys))
# custom keys
keys.extend(keymap.init_custom_keys())
layouts = layout.init_layouts()
widget_defaults, widgets_list = topbar.init_widgets()
screens = screens.init_screens()
# setters
(
    mouse,
    dgroups_key_binder,
    dgroups_app_rules,
    main,
    floating_types,
    follow_mouse_focus,
    bring_front_click,
    cursor_warp,
    floating_layout,
    auto_fullscreen,
    focus_on_window_activation,
    wmname,
) = myset.get_settings()

new_client = fn.new_client
kill_client = fn.kill_client
start_once = fn.start_once
set_floating = fn.set_floating