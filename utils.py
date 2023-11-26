from libqtile.command import lazy
import subprocess
import os

def run_script(qtile, command):
    home = os.path.expanduser("~")
    subprocess.call([home + command])