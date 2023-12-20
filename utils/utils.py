"""utils for the entire project"""
import os
import random
import subprocess
from libqtile.lazy import lazy
from utils.constants import HOME, SHUTTER_COMMAND, SCREENSHOT_PATH


def run_command_with_terminal(command: str):
    subprocess.Popen(["alacritty", "-e", "bash", "-i", "-c", command])


@lazy.function
def open_code_with_fzf(_):
    """funcion que permite la apertura de vscode usando fzf"""
    subprocess.Popen(["alacritty", "-e", "bash", "-i", "-c", "code_in_path"])


@lazy.function
def capture_and_copy(_):
    """funcion que realiza una seleccion para capturar
    la pantalla para posteriormente copiarla al portapapeles"""
    capture_command = SHUTTER_COMMAND
    subprocess.run(capture_command, shell=True, check=True)
    os.remove(SCREENSHOT_PATH)


def random_wallpaper():
    """establece un background wallpaper de manera
    aleatoria en la carpeta 'walllpaper_directory'"""
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


def toggle_borders(group, is_for_open: bool, is_for_migrate=False):
    """function to change dynamically from bsp to monadtall"""
    len_windows = len(group.windows)
    count_windows = 0 if is_for_open else 2 if is_for_migrate else 1
    group.use_layout(3 if len_windows == count_windows else 0)


@lazy.function
def toggle_borders_before_change_group(qtile):
    """verifica si en el actual group queda unicaemnte una ventana"""
    toggle_borders(qtile.current_group, False, is_for_migrate=True)


def toggle_borders_after_change_group(qtile, group_name, groups_dict: dict):
    """despues de cambiar entre grupos verifica el estado
    de esta contando la cantidad de ventanas actuales"""
    index_group = groups_dict[group_name]
    group = qtile.groups[index_group]
    if len(group.windows) == 1:
        toggle_borders(group, False)
    else:
        toggle_borders(group, True)


@lazy.function
def volume_up(qtile):
    qtile.cmd_spawn("amixer -D pulse sset Master 5%+")


@lazy.function
def volume_down(qtile):
    qtile.cmd_spawn("amixer -D pulse sset Master 5%-")
