from libqtile.config import Drag, Match
from libqtile.command import lazy
from libqtile import layout

mod = "mod4"


def get_settings():
    mouse = [
        Drag(
            [mod],
            "Button1",
            lazy.window.set_position_floating(),
            start=lazy.window.get_position(),
        ),
        Drag(
            [mod],
            "Button3",
            lazy.window.set_size_floating(),
            start=lazy.window.get_size(),
        ),
    ]
    dgroups_key_binder = None
    dgroups_app_rules = []
    main = None
    floating_types = ["notification", "toolbar", "splash", "dialog"]
    follow_mouse_focus = False
    bring_front_click = False
    cursor_warp = False
    floating_layout = layout.Floating(
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
            Match(wm_class="Arcolinux-welcome-app.py"),
            Match(wm_class="Arcolinux-calamares-tool.py"),
            Match(wm_class="confirm"),
            Match(wm_class="dialog"),
            Match(wm_class="download"),
            Match(wm_class="error"),
            Match(wm_class="file_progress"),
            Match(wm_class="notification"),
            Match(wm_class="splash"),
            Match(wm_class="toolbar"),
            Match(wm_class="Arandr"),
            Match(wm_class="feh"),
            Match(wm_class="Galculator"),
            Match(wm_class="archlinux-logout"),
            Match(wm_class="xfce4-terminal"),
            Match(wm_class="thunar"),
            Match(wm_class="pavucontrol"),
            Match(wm_class="shutter"),
        ],
        fullscreen_border_width=0,
        border_width=2,
    )
    auto_fullscreen = True
    focus_on_window_activation = "focus"  # or smart
    wmname = "LG3D"

    return (
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
    )
