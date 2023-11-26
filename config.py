import keymap, layout, topbar, screens, set, functions
from libqtile import hook, qtile

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
) = set.get_settings()

new_client = functions.new_client
logout_killed = functions.logout_killed
start_once = functions.start_once
start_always = functions.start_always
set_floating = functions.set_floating
