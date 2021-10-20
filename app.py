import data
import functions
import sys
from ui import *
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication

class App(QObject):
    def __init__(self, window:object, app:object) -> None:
        super().__init__()
        
        self.content_api = data.ContentManager()
        
        self.ui = window
        self.qapp = app
        self.search = self.ui.side_left.search
        
        self.ui.index.btn_start.clicked.connect(self.get_start)
        self.ui.tool_bar.search.triggered.connect(self.show_search)
        self.ui.tool_bar.list.triggered.connect(self.show_list)
        self.ui.tool_bar.settings.triggered.connect(self.show_config)
        self.search.input.returnPressed.connect(self.search_topic)
        self.search.input.textChanged.connect(self.live_search_topic)
    
    def get_start(self):
        if not self.ui.side_left.isVisible():
            self.show_search()
        self.search.input.setFocus()
        self.search.input.setText("Python")
    
    def live_search_topic(self, query):
        print(query)
        print(self.content_api.get_data())
    
    def search_topic(self):
        query = self.search.input.text()
        print(query)
    
    def show_search(self):
        self.ui.side_left.do_search()
    
    def show_list(self):
        self.ui.side_left.do_list()
    
    def show_config(self):
        self.ui.side_left.do_config()
        

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setWindowIcon(functions.get_icons()["app_icon"])
    
    win = MainWindow()
    functions.styler(app, win)
    
    controller = App(win, app)
    
    app.exec_()