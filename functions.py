import json
import pathlib
import os
import os.path
import locale
import re
import ast
import codecs
import itertools
from PyQt5.QtGui import QIcon

import frameworks.qtmodern.styles as qtmodern_styles
import frameworks.qtmodern.windows as qtmodern_windows

import data

def get_icons() -> dict:
    res_path = f"{data.BASE_PATH}{data.SYS_SEP}resources{data.SYS_SEP}"
    logos_path = f"{data.BASE_PATH}{data.SYS_SEP}resources{data.SYS_SEP}logo{data.SYS_SEP}"
    icons_path = f"{res_path}icons{data.SYS_SEP}"
    icons_with_theme_path = f"{icons_path}{data.get_icons_theme()}{data.SYS_SEP}"

    return {
        "index":f"{icons_path}index.svg",
        "app_icon":QIcon(f"{logos_path}logo.svg"),
        "logo_small":QIcon(f"{logos_path}logo_small.png"),
        "search":QIcon(f"{icons_with_theme_path}search.png"),
        "list":QIcon(f"{icons_with_theme_path}list.png"),
        "config":QIcon(f"{icons_with_theme_path}settings.png"),
        "light":QIcon(f"{icons_with_theme_path}sun.png"),
        "dark":QIcon(f"{icons_with_theme_path}moon.png"),
    }

def styler(app, win):
    palette = data.get_palette()
    theme = data.get_theme()
    theme_path_obj = pathlib.Path(f"resources/styles/{theme}.qss")
    
    if theme_path_obj.exists():
        stylesheet = theme_path_obj.read_text()
    else:
        stylesheet = f"resources/styles/dark.qss"
    
    if palette == "light":
        qtmodern_styles.light(app)
    else:
        qtmodern_styles.dark(app)
    
    
    app.setStyleSheet(stylesheet)
    win.setStyleSheet(stylesheet)

def find_files_with_text(search_text, search_dir, case_sensitive=False, search_subdirs=True, break_on_find=False):
        
        path=pathlib.Path(search_dir)
        if not path.is_dir():
            return False
        
        text_file_list = []
        
        if search_subdirs == True:
            walk_tree = os.walk(search_dir)
        else:
            walk_tree = [next(os.walk(search_dir))]
        for root, subFolders, files in walk_tree:

            for file in files:

                full_with_path = os.path.join(root, file)
                if self.test_text_file(full_with_path) != None:

                    full_with_path = full_with_path.replace("\\",  "/")
                    text_file_list.append(full_with_path)

        return_file_list = []
        for file in text_file_list:
            try:
                file_text = self.read_file_to_string(file)
                
                if case_sensitive == False:
                    compare_file_text = file_text.lower()
                    compare_search_text = search_text.lower()
                else:
                    compare_file_text = file_text
                    compare_search_text = search_text
                
                if compare_search_text in compare_file_text:
                    return_file_list.append(file)
                    
                    if break_on_find == True:
                        break
            except Exception as e:
                continue
                
        return return_file_list