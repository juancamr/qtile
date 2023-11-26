import subprocess
import os


def open_pyhasher(qtile, command):
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/pyhasher/pyhasher.sh"])
