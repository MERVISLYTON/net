import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class LocalBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.server_url = "http://localhost:8085"
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Local Server Browser")
        self.setGeometry(100, 100, 1024, 768)
        
        self.web = QWebEngineView()
        self.url_input = QLineEdit()
        self.search_input = QLineEdit()
        go_btn = QPushButton("Go")
        
        top_bar = QHBoxLayout()
        top_bar.addWidget(self.url_input)
        top_bar.addWidget(go_btn)
        
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_bar)
        main_layout.addWidget(QLabel("Quick Search:"))
        main_layout.addWidget(self.search_input)
        main_layout.addWidget(self.web)
        
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
        
        go_btn.clicked.connect(self.load_page)
        self.url_input.returnPressed.connect(self.load_page)
        self.search_input.returnPressed.connect(self.handle_search)
        
        self.url_input.setText(self.server_url)
        self.web.load(QUrl(self.server_url))
        
    def load_page(self):
        url = self.url_input.text()
        if not url.startswith("http"):
            url = f"http://{url}"
        self.web.load(QUrl(url))
        
    def handle_search(self):
        query = self.search_input.text().strip()
        if not query:
            return
            
        local_path = f"{self.server_url}/{query}"
        self.url_input.setText(local_path)
        self.web.load(QUrl(local_path))
        
        self.web.loadFinished.connect(lambda ok: self.check_local_page(ok, query))
        
    def check_local_page(self, loaded, query):
        if not loaded:
            self.show_search_alternatives(query)
            
    def show_search_alternatives(self, query):
        google_url = f"https://www.google.com/search?q={query}"
        error_html = f"""
        <div style='padding:40px; text-align:center; font-family:Arial'>
            <h2>Local Page Not Found</h2>
            <p>No page found for: <strong>{query}</strong></p>
            <p>Try searching online:</p>
            <a href='{google_url}' 
               style='display:inline-block; 
                      padding:10px 20px; 
                      background:#4285f4; 
                      color:white; 
                      text-decoration:none;
                      border-radius:5px;'>
                Search Google
            </a>
        </div>
        """
        self.web.setHtml(error_html)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LocalBrowser()
    window.show()
    sys.exit(app.exec_())