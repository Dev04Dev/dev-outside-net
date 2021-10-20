import data
import functions
import sys
from ui import *
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication

class App(QObject):
    def __init__(self, window:object, app:object) -> None:
        super().__init__()
        
        self.ui = window
        self.qapp = app
        
        self.ui.tool_bar.search.triggered.connect(self.show_search)
        self.ui.tool_bar.list.triggered.connect(self.show_list)
        self.ui.tool_bar.settings.triggered.connect(self.show_config)
    
    def show_search(self):
        self.ui.side_left.do_search()
    
    def show_list(self):
        self.ui.side_left.do_list()
    
    def show_config(self):
        self.ui.side_left.do_config()
        

if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    #qtmodern_styles.dark(app)
    qtmodern_styles.light(app)
    
    win = MainWindow()
    controller = App(win, app)
    
    with open("resources/styles/light.qss") as stylesheet:
        app.setStyleSheet(stylesheet.read())
        win.setStyleSheet(stylesheet.read())
    
    app.exec_()