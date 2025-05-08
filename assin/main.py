import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from client_handler import Client

client = Client()

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("client_backend", client)
    engine.quit.connect(app.quit)
    engine.load("main.qml")
    sys.exit(app.exec())
