import os, sys
import platform
from pathlib import Path

PLATFORM = platform.system()
SYS_NAME=PLATFORM.lower()

SYS_SEP="/"

if SYS_NAME == "windows":
    SYS_SEP="\\"

if getattr(sys, 'frozen', False):
    BASE_PATH = os.path.dirname(sys.executable)
    os.chdir(BASE_PATH)

BASE_PATH = os.getcwd()

sys.path.append(BASE_PATH+f"{SYS_SEP}content")
sys.path.append(BASE_PATH)

def end(code = 0):
    os._exit(code)