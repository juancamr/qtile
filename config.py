from settings import keymap, set, functions as fn
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
) = set.get_settings()

# fn
new_client = fn.new_client
logout_killed = fn.logout_killed
start_once = fn.start_once
start_always = fn.start_always
set_floating = fn.set_floating

border_args = dict(
    border_normal="#000000",
    border_focus="#535d6c",
    border_width=2,
    margin=0,
    single_border_width=0,
    single_margin=0,
    radius=10,  # Ajusta este valor para cambiar la cantidad de redond
)
