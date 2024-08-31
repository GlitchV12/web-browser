from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngine import *
from PyQt5.QtWebEngineWidgets import QWebEngineView


class MyWebBrowser(QMainWindow):

    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle("WebBrowser")
        self.window.setWindowIcon(QIcon('assets/browserIcon.png'))
        self.window.setFont(QFont("poppins"))

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(40)
        self.url_bar.setPlaceholderText("Enter a URL")

# Search button code
        self.go_btn = QPushButton()
        self.go_btn.setMinimumHeight(40)
        self.go_btn.setIcon(QIcon('assets/searchicon.svg'))
        self.go_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                color: white;
                font-size: 16px;
                padding: 10px;
            }
            QPushButton:hover {
                background: rgba(0, 0, 0, 0.2);
            }
            QPushButton:pressed {
                background: rgba(0, 0, 0, 0.4);
            }
        """)

# back button code
        self.back_btn = QPushButton()
        self.back_btn.setIcon(QIcon('assets/back.png'))
        self.back_btn.setMinimumHeight(40)
        self.back_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                color: white;
                font-size: 16px;
                padding: 10px;
            }
            QPushButton:hover {
                background: rgba(0, 0, 0, 0.2);
            }
            QPushButton:pressed {
                background: rgba(0, 0, 0, 0.4);
            }
        """)

#next buttton code
        self.forward_btn = QPushButton()
        self.forward_btn.setMinimumHeight(40)
        self.forward_btn.setIcon(QIcon('assets/next.png'))
        self.forward_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                color: white;
                font-size: 16px;
                padding: 10px;
            }
            QPushButton:hover {
                background: rgba(0, 0, 0, 0.2);
            }
            QPushButton:pressed {
                background: rgba(0, 0, 0, 0.4);
            }
        """)

#settings button code
        self.settings = QPushButton()
        self.settings.setMinimumHeight(40)
        self.settings.setIcon(QIcon('assets/settings.png'))
        self.settings.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                color: white;
                font-size: 16px;
                padding: 10px;
            }
            QPushButton:hover {
                background: rgba(0, 0, 0, 0.2);
            }
            QPushButton:pressed {
                background: rgba(0, 0, 0, 0.4);
            }
        """)

#home button code
        self.home = QPushButton()
        self.home.setMinimumHeight(40)
        self.home.setIcon(QIcon('assets/home.png'))
        self.home.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                color: white;
                font-size: 16px;
                padding: 10px;
            }
            QPushButton:hover {
                background: rgba(0, 0, 0, 0.2);
            }
            QPushButton:pressed {
                background: rgba(0, 0, 0, 0.4);
            }
        """)


# adding all the widgets to the layout
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.home)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.settings)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        
        

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()


    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))


app = QApplication([])
window = MyWebBrowser()
app.exec_()


