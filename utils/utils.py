import os, random, subprocess
from utils.constants import HOME
from libqtile.lazy import lazy


@lazy.function
def open_code_with_fzf(_):
    subprocess.Popen(["alacritty", "-e", "bash", "-i", "-c", "code_in_path"])


@lazy.function
def capture_and_copy(_):
    screenshot_path = "/tmp/temp_capture.png"
    capture_command = f"shutter -s -e -o {screenshot_path} && xclip -selection clipboard -target image/png -i {screenshot_path}"
    subprocess.run(capture_command, shell=True)
    os.remove(screenshot_path)


def random_wallpaper():
    wallpaper_directory = f"{HOME}/Pictures/wallpapers/"
    image_formats = (".png", ".jpg", ".jpeg")
    image_files = [
        file
        for file in os.listdir(wallpaper_directory)
        if file.lower().endswith(image_formats)
    ]
    if not image_files:
        return
    selected_image = random.choice(image_files)
    image_path = os.path.join(wallpaper_directory, selected_image)
    os.system(f"feh --bg-fill {image_path}")


def toggle_borders(window: object, is_empty: bool):
    len_windows = len(window.qtile.current_group.windows)
    count_windows = 0 if is_empty else 1
    window.qtile.current_group.use_layout(3 if len_windows == count_windows else 0)


# def send_window_to_group(window: object, workspace: int):
#     group = keymap.workspaces_keybindings[workspace]
#     window.togroup(group)
#     lazy.group[group].toscreen()
