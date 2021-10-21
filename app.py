import pathlib
import data
import functions
import sys
from ui import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QTextBrowser

class SearchEngine(QObject):
    
    on_results=pyqtSignal(list)

    def __init__(self, parent):
        super().__init__()
        self.parent=parent
    
    def run(self):
        self.parent.on_searched.connect(self.search)
    
    def search(self, query, folder):
        print(folder)
        try:
            results = functions.searchfn.find_files_with_text(query, folder)
            print(results)
            
            self.on_results.emit(results)
        
        except Exception as e:
            print(e)
            return e

class App(QObject):
    
    on_searched=pyqtSignal(str, str)
    
    def __init__(self, window:object, app:object) -> None:
        super().__init__()
        
        self.thread=QThread()
        self.engine=SearchEngine(self)
        self.engine.on_results.connect(self.display_results)
        self.engine.moveToThread(self.thread)
        self.thread.start()
        self.thread.started.connect(self.run)
        
        self.content_api = data.ContentManager()
        self.base_path = f"{data.BASE_PATH}{data.SYS_SEP}content{data.SYS_SEP}"
        
        self.ui = window
        self.qapp = app
        self.search = self.ui.side_left.search
        self.topics = self.ui.side_left.topics
        
        self.topics.tree.clicked.connect(self.tree_clicked)
        self.ui.index.btn_start.clicked.connect(self.get_start)
        self.ui.tool_bar.search.triggered.connect(self.show_search)
        self.ui.tool_bar.list.triggered.connect(self.show_list)
        self.ui.tool_bar.settings.triggered.connect(self.show_config)
        
        self.ui.notebook.tabCloseRequested.connect(self.close_tab)

        self.search.input.returnPressed.connect(self.search_topic)
        self.search.input.textChanged.connect(self.live_search_topic)
        self.search.output.itemActivated.connect(self.result_link_activated)
        
        self.update_topics()
    
    def close_tab(self, idx):
        self.ui.notebook.removeTab(idx)
        if self.ui.notebook.count() < 1:
            self.ui.togle_views(0)
        
    def result_link_activated(self, item):
        if item.item_data is not None:
            
            try:
                file = pathlib.Path(item.item_data["file"])
                name = file.name.split(".")[0]
            
                viewer = QTextBrowser(self.ui.notebook)
            
                viewer.setText(file.read_text())
                
                self.ui.notebook.addTab(viewer, name.capitalize())
                self.ui.togle_views(1)
            
            except Exception as e:
                print(e)
        
    def tree_clicked(self, index):
        item=self.topics.model.itemFromIndex(index)
        if item.item_data is not None:
            
            try:
                file = pathlib.Path(item.item_data["file"])
                name = file.name.split(".")[0]
            
                viewer = QTextBrowser(self.ui.notebook)
            
                viewer.setText(file.read_text())
                
                self.ui.notebook.addTab(viewer, name.capitalize())
                self.ui.togle_views(1)
            
            except Exception as e:
                print(e)
    
    def get_start(self):
        if not self.ui.side_left.isVisible():
            self.show_search()
        self.search.input.setFocus()
        self.search.input.setText("Python")
        self.search_topic()
    
    def live_search_topic(self, query):
        if len(query) > 1:
        
            pages = self.search.output.findItems(query, Qt.MatchContains)
    
            for i in range(self.search.output.count()):
                self.search.output.setRowHidden(i, True)

            for row_item in pages:
                i = self.search.output.row(row_item)
                self.search.output.setRowHidden(i, False)
            
            if len(pages) > 0:
                i = self.search.output.row(pages[0])
                self.search.output.setCurrentRow(i)
        else:
            for i in range(self.search.output.count()):
                self.search.output.setRowHidden(i, False)
    
    def search_topic(self):
        query = self.search.input.text()
        self.on_searched.emit(query, self.base_path)
    
    def display_results(self, res):
        rows = []
        for item in res:
            obj_path=pathlib.Path(item)
            if obj_path.suffix == ".ml":
                name = obj_path.name.split(".")[0]
                row=ListWidgetItem(name.capitalize(), item, {"file":item})
                rows.append(row)
            
        self.ui.side_left.search.set_results(rows)
    
    def update_topics(self):
        
        base_path = f"{data.BASE_PATH}{data.SYS_SEP}content{data.SYS_SEP}"
        
        topics = []
        raw_topics = self.content_api.get_data()
        
        for key in raw_topics.keys():
            names = raw_topics[key]
        
            row_key = StandardItem()
            row_key.setText(key)
            
            for name in names:
                                
                row = StandardItem()
                row.setText(name)
                
                if pathlib.Path(base_path+key).is_dir() and pathlib.Path(base_path+key).exists():
                    file_name = base_path+key+data.SYS_SEP+str(name).lower()+".ml"
                    if pathlib.Path(file_name).is_file() and pathlib.Path(file_name).exists():
                        row.set_data({"file":file_name})
                        row.setToolTip(file_name)
                        row_key.appendRow(row)
        
            topics.append(row_key)
        
        self.ui.side_left.topics.set_topics(topics)
    
    def show_search(self):
        self.ui.side_left.do_search()
    
    def show_list(self):
        self.ui.side_left.do_tree()
    
    def show_config(self):
        self.ui.side_left.do_config()
    
    def run(self):
        self.engine.run()        

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setWindowIcon(functions.get_icons()["app_icon"])
    
    win = MainWindow()
    functions.styler(app, win)
    
    controller = App(win, app)
    
    app.exec_()