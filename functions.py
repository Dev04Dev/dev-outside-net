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
        try:
            stylesheet = open("resources/styles/dark.qss", "r").read()
        except Exception as e:
            print(e)
            stylesheet = ""
    
    stylesheet = stylesheet.replace(
        "<get_app_icons_path>",
        f"{data.BASE_PATH}{data.SYS_SEP}resources{data.SYS_SEP}icons{data.SYS_SEP}{data.get_icons_theme()}{data.SYS_SEP}")
    
    if palette == "light":
        qtmodern_styles.light(app)
    else:
        qtmodern_styles.dark(app)
    
    app.setStyleSheet(stylesheet)
    win.setStyleSheet(stylesheet)

class Search:
    def __init__(self):
        pass
    
    def find_files_with_text(self, search_text, search_dir, case_sensitive=False, search_subdirs=True, break_on_find=False):
        
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

    def find_files_by_name(self, search_filename, search_dir, case_sensitive=False, search_subdirs=True):
        path=pathlib.Path(search_dir)

        if not path.is_dir():
            return False
    
        found_file_list = []
        
        if search_subdirs == True:
            walk_tree = os.walk(search_dir)
        else:
            
            walk_tree = [next(os.walk(search_dir))]
        for root, subFolders, files in walk_tree:
            for file in files:
                
                full_with_path = os.path.join(root, file)
                
                if case_sensitive == False:
                    compare_actual_filename = file.lower()
                    compare_search_filename = search_filename.lower()
                else:
                    compare_actual_filename = file
                    compare_search_filename = search_filename
                
                if compare_search_filename in compare_actual_filename:
                    
                    full_with_path = full_with_path.replace("\\",  "/")
                    found_file_list.append(full_with_path)
        
        return found_file_list

    def test_text_file(self, file_with_path):
        try:
            file = open(file_with_path, "r", encoding=locale.getpreferredencoding(), errors="strict")
            for line in itertools.islice(file, 10):
                line = line
            file.readlines()
            file.close()
            
            return locale.getpreferredencoding()
        except:
            test_encodings = ["utf-8", "ascii", "utf-16", "utf-32", "iso-8859-1", "latin-1"]
            for current_encoding in test_encodings:
                try:
                    file = open(file_with_path, "r", encoding=current_encoding, errors="strict")
                    
                    for line in itertools.islice(file, 10):
                        line = line
                    
                    file.close()
                    
                    return current_encoding
                except:
                    continue
        return None

        
    def test_binary_file(self, file_with_path):
        file = open(file_with_path, "rb")
        
        binary_text = None
        for line in itertools.islice(file, 20):
            if b"\x00" in line:
            
                file.seek(0)

                binary_text = file.read()
                break
        file.close()
        return binary_text

    def read_file_to_list(self, file_with_path):
        text = self.read_file_to_string(file_with_path)
        if text != None:
            return text.split("\n")
        else:
            return None

    
    def read_file_to_string(self, file_with_path):
        """Read contents of a text file to a single string"""
        binary_text = self.test_binary_file(file_with_path)
        if binary_text != None:
            cleaned_binary_text = binary_text.replace(b"\x00",b"")
            return cleaned_binary_text.decode(encoding="utf-8", errors="replace")
        else:
            test_encodings = ["utf-8", "cp1250", "ascii", "utf-16", "utf-32", "iso-8859-1", "latin-1"]
            for current_encoding in test_encodings:
                try:
                    
                    with open(file_with_path, "r", encoding=current_encoding, errors="strict") as file:
                    
                        text = file.read()
                    
                        file.close()
                    
                    return text
                except:
                    
                    continue
        
        return None

    def read_binary_file_as_generator(self, file_object, chunk_size=1024):
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data

    def read_file_to_list(self, file_with_path):
        text = self.read_file_to_string(file_with_path)
        if text != None:
            return text.split("\n")
        else:
            return None

    
    def read_file(self, file):
        return self.read_file_to_string(file)
    
    def write_to_file(self, text, file_with_path, encoding="utf-8"):
        try:
            if encoding != "utf-8":
                byte_string = bytearray(text, encoding=encoding, errors="replace")
                text = codecs.decode(byte_string, encoding, "replace")

            with open(file_with_path, "w", newline="", encoding=encoding) as file:
                file.write(text)                
                file.close()
            
            return True
        except Exception as ex:
            return ex

searchfn = Search()