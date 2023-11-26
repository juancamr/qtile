import subprocess
import os


def run_script(command: str):
    home = os.path.expanduser("~")
    subprocess.call([home + command])
