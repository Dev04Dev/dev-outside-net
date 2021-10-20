import frameworks.qtmodern.styles as qtmodern_styles
import frameworks.qtmodern.windows as qtmodern_windows
from PyQt5.QtWidgets import (QComboBox, QFormLayout, QHBoxLayout, QLabel, QLineEdit, QListWidget, QMainWindow, QPushButton, QSizePolicy, QSplitter, QStackedLayout, QTabWidget, QTreeWidget, QWidget,
                            QVBoxLayout, QFrame,
                            QDesktopWidget, QStatusBar,
                            QToolBar, QSizePolicy,
                            QAction)
import functions

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtSvg import QSvgWidget

class StatusBar(QStatusBar):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setObjectName("status-bar")
        
        self.up=parent
        
        self.zoom_in = QPushButton("+")
        self.zoom_out = QPushButton("-")
        
        self.addPermanentWidget(self.zoom_out)
        self.addPermanentWidget(self.zoom_in)

class ToolBar(QToolBar):
    def __init__(self, parent:object) -> None:
        super().__init__(parent=parent)
        self.setObjectName("tool-bar")
        self.up=parent
        self.actions_list = []
        self.icons = functions.get_icons()
        self.init_ui()
    
    def init_ui(self) -> None:
        self.setFloatable(False)
        self.setMovable(False)
        self.setOrientation(Qt.Vertical)
        
        self.spacing=QWidget(self)
        self.spacing.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        
        self.search=QAction(self.icons["search"] , "Search", self)
        self.search.setToolTip("Pesquisar")
        self.addAction(self.search)
        
        self.list=QAction(self.icons["list"] , "Search", self)
        self.list.setToolTip("Tópicos")
        self.addAction(self.list)
        
        self.addWidget(self.spacing)
        
        self.settings=QAction(self.icons["config"] , "Search", self)
        self.settings.setToolTip("Configurações")
        self.addAction(self.settings)

class Index(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setObjectName("index-screen")
        self.up=parent
        self.icons = functions.get_icons()
        
        self.init_ui()
    
    def init_ui(self):
        self.box = QVBoxLayout(self)
        self.box.setContentsMargins(0, 10, 0, 10)
        self.setLayout(self.box)
                
        self.svg_widget = QSvgWidget(self.icons["index"])
        
        self.btn_start = QPushButton("Start", self)
        self.btn_start.setObjectName("start-btn")
        
        self.hello = QLabel(self)
        self.hello.setText("<h2><nobr>Encontra respostas fora da internet</nobr></h2>")
        self.hello.setAlignment(Qt.AlignTop)
        self.hello.setScaledContents(True)
        self.hello.setWordWrap(True)
        
        self.box.addWidget(self.hello)
        self.box.setAlignment(self.hello, Qt.AlignTop|Qt.AlignCenter)
        self.box.addWidget(self.svg_widget)
        self.box.setAlignment(self.svg_widget, Qt.AlignCenter)
        self.box.addWidget(self.btn_start)
        self.box.setAlignment(self.btn_start, Qt.AlignCenter)

class Settings(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setObjectName("settings-frame")
        self.up=parent
        self.icons = functions.get_icons()
        
        self.init_ui()
    
    def init_ui(self):
        self.box = QVBoxLayout(self)
        self.setLayout(self.box)
        self.box.setAlignment(Qt.AlignTop)
        
        self.info = QLabel(self)
        self.info.setText("<small>Settings</small>")
        hbox = QHBoxLayout()
        hbox.addWidget(self.info)
        
        self.form_box = QFormLayout()
        
        combobox_size_policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        self.theme_choice = QComboBox(self)
        self.theme_choice.setSizePolicy(combobox_size_policy)
        self.theme_choice.addItem(self.icons["dark"], "Dark")
        self.theme_choice.addItem(self.icons["light"], "Light")
        
        self.icons_choice = QComboBox(self)
        self.icons_choice.setSizePolicy(combobox_size_policy)
        self.icons_choice.addItem(self.icons["dark"], "Dark")
        self.icons_choice.addItem(self.icons["light"], "Light")
        
        self.qpalette_choice = QComboBox(self)
        self.qpalette_choice.setSizePolicy(combobox_size_policy)
        self.qpalette_choice.addItem(self.icons["dark"], "Dark")
        self.qpalette_choice.addItem(self.icons["light"], "Light")
        
        self.theme_label = QLabel("<h3> Tema <h3>", self)
        
        self.form_box.addRow("Aplicação", self.theme_choice)
        self.form_box.addRow("ícones", self.icons_choice)
        self.form_box.addRow("Qt", self.qpalette_choice)
        
        self.box.addLayout(hbox)
        self.box.addSpacing(20)
        self.box.addWidget(self.theme_label)
        self.box.addLayout(self.form_box)
        

class Search(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setObjectName("search-frame")
        self.up=parent
        self.icons = functions.get_icons()
        
        self.init_ui()
    
    def init_ui(self):
        self.box = QVBoxLayout(self)
        self.setLayout(self.box)
        
        self.info = QLabel(self)
        self.info.setText("<small>Search</small>")
        hbox = QHBoxLayout()
        hbox.addWidget(self.info)
        
        self.input = QLineEdit(self)
        self.output = QListWidget(self)
        
        self.box.addLayout(hbox)
        self.box.addWidget(self.input)
        self.box.addWidget(self.output)

class Topics(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.setObjectName("topics-frame")
        self.up=parent
        self.icons = functions.get_icons()
        
        self.init_ui()
    
    def init_ui(self):
        self.box = QVBoxLayout(self)
        self.setLayout(self.box)
        
        self.info = QLabel(self)
        self.info.setText("<small>Topics</small>")
        hbox = QHBoxLayout()
        hbox.addWidget(self.info)
        
        self.tree = QTreeWidget(self)
        
        self.box.addLayout(hbox)
        self.box.addWidget(self.tree)
    
    def set_topics(self, topics:list):
        if topics:
            self.list.clear()
            
            for topic in topics:
                print(topic)

class SideLeft(QFrame):
    def __init__(self, parent:object) -> None: 
        super().__init__(parent)
        self.up = parent
        self.icons = functions.get_icons()
        
        self.box = QStackedLayout(self)
        self.box.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.box)
        
        self.search = Search(self)
        self.list = Topics(self)
        self.config = Settings(self)
        
        self.box.addWidget(self.search)
        self.box.addWidget(self.list)
        self.box.addWidget(self.config)
        
        self.setVisible(False)
    
    def do_search(self):
        if self.isVisible() and self.box.currentWidget() is self.search:
            self.setVisible(False)
        else:
            self.setVisible(True)
            self.box.setCurrentWidget(self.search)
    
    def do_list(self):
        if self.isVisible() and self.box.currentWidget() is self.list:
            self.setVisible(False)
        else:
            self.setVisible(True)
            self.box.setCurrentWidget(self.list)
    
    def do_config(self):
        if self.isVisible() and self.box.currentWidget() is self.config:
            self.setVisible(False)
        else:
            self.setVisible(True)
            self.box.setCurrentWidget(self.config)
        
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.icons = functions.get_icons()
        
        self.frame = None
        
        self.tool_bar=ToolBar(self)
        self.addToolBar(Qt.LeftToolBarArea, self.tool_bar)
        
        self.status_bar=StatusBar(self)
        self.setStatusBar(self.status_bar)
                
        self.div = QSplitter(Qt.Horizontal, self)
        
        self.side_left = SideLeft(self)
        
        self.index = Index(self)
        
        self.notebook = QTabWidget(self)
        self.notebook.setTabsClosable(True)
        self.notebook.setDocumentMode(True)
        
        a = QLabel("BBBBBBBBBBBBBBBBBBBBBB")
        self.notebook.addTab(a, "Example")
        
        self.div.addWidget(self.side_left)
        self.div.addWidget(self.index)
        self.div.addWidget(self.notebook)
        
        self.div.setSizes([30, 70, 0])
        
        self.setCentralWidget(self.div)
        
        self.make_window()
    
    def make_window(self):
        self.setMinimumSize(100, 100)
        self.setGeometry(0, 0, 1000, 600)
        self.setWindowTitle("Dewithoutnet")
        self.center()
        self.frame = qtmodern_windows.ModernWindow(self)
        self.frame.setMenuIcon(self.icons["logo_small"])
        self.frame.show()
        
    def center(self) -> None:
        app_geo = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        app_geo.moveCenter(screen_center)
        self.move(app_geo.topLeft())
    