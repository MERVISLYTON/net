from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
import socket


class Client(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.mMesaage  = ""
        self.messaerServer_address = ""
        self.messaerServer_port = 0
        self.messaerServer_feedback = ""

    @pyqtSlot(str)
    def setMessageServerAddress(self, newaddr: str):
        self.messaerServer_address = newaddr
        print(f"server address has set to: {self.getMessageServerAddress()}")

    @pyqtSlot(result=str)
    def getMessageServerAddress(self):
        return self.messaerServer_address
    
    @pyqtSlot(int)
    def setMessageServerPort(self, newServerPort: int):
        self.messaerServer_port = newServerPort
        print(f"the server port has been set to: {self.getMessageServerPort()}")

    @pyqtSlot(result=int)
    def getMessageServerPort(self):
        return self.messaerServer_port
    
    @pyqtSlot(str)
    def setMessageServerMessage(self, newMessage):
        self.mMesaage = newMessage
        print(f"the server message is: {self.getMessageServerMessage()}")

    @pyqtSlot(result=str)
    def getMessageServerMessage(self):
        return  self.mMesaage
    
    @pyqtSlot()
    def connect_to_server(self):

        if self.messaerServer_port == 0 or self.messaerServer_address == "": 
            return
        try:
            print("connecting to server")
            client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
            client_socket.connect((self.getMessageServerAddress(),self.getMessageServerPort()))
            client_socket.send(self.getMessageServerMessage().encode("utf-8"))
            self.messaerServer_feedback = client_socket.recv(1024).decode("utf-8")
        except Exception as error:
            print("")

    @pyqtSlot(result=str)
    def getmessageServerFeedback(self):
        return self.messaerServer_feedback


    



