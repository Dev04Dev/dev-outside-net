import os, sys
import platform
from pathlib import Path
import frameworks.jedit2 as jedit

PLATFORM = platform.system()
SYS_NAME=PLATFORM.lower()
SYS_SEP="/"

if SYS_NAME == "windows":
    SYS_SEP="\\"

if getattr(sys, 'frozen', False):
    BASE_PATH = os.path.dirname(sys.executable)
    os.chdir(BASE_PATH)

BASE_PATH = os.getcwd()

SETTINGS_FILE = f"{BASE_PATH}{SYS_SEP}data{SYS_SEP}launch.json"
API_MAIN_FILE = f"{BASE_PATH}{SYS_SEP}content{SYS_SEP}main.json"

sys.path.append(BASE_PATH+f"{SYS_SEP}content")
sys.path.append(BASE_PATH)

def get_all() -> dict:

    return jedit.load(SETTINGS_FILE)

def get_theme():

    return jedit.load(SETTINGS_FILE)["app-theme"]

def get_icons_theme():

    return jedit.load(SETTINGS_FILE)["icons-theme"]

def get_palette():

    return jedit.load(SETTINGS_FILE)["qt-palette"]

def set_theme(new_value):
    jedit.edit(["app-theme"], new_value, SETTINGS_FILE)

def set_icons_theme(new_value):
    jedit.edit(["icons-theme"], new_value, SETTINGS_FILE)

def set_palette(new_value):
    jedit.edit(["qt-palette"], new_value, SETTINGS_FILE)

class ContentManager(object):
    def __init__(self) -> None:
        pass
    
    def get_data(self):
        return jedit.load(API_MAIN_FILE)

def end(code = 0):
    os._exit(code)