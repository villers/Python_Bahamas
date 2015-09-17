from PyQt5 import QtWebSockets, QtCore

from Model.RequestModel import RequestModel
from Model.MessageModel import MessageModel


class CommunicationServer(QtCore.QObject):

    ErrorConnexion = QtCore.pyqtSignal()

    GoodLogin = QtCore.pyqtSignal()

    ErrorLogin = QtCore.pyqtSignal()

    isConnected = False

    Login = ""

    def __init__(self):
        super(CommunicationServer, self).__init__()
        self.Address = None
        self.WebSockets = QtWebSockets.QWebSocket()
        self.WebSockets.connected.connect(self.onConnected)
        self.WebSockets.disconnected.connect(self.onDisconnected)
        self.WebSockets.error.connect(self.onError)

    def Run(self):
        print("Trying to connected on " + self.Address)
        self.WebSockets.open(QtCore.QUrl(self.Address))

    def setAddress(self, address):
        self.Address = address

    def closeConnexion(self):
        self.isConnected = False
        self.WebSockets.close()

    def onConnected(self):
        print("Connected to " + self.Address)
        self.isConnected = True
        self.WebSockets.textMessageReceived.connect(self.onMessage)
        self.sendLoginAuthentification()

    def onDisconnected(self):
        self.isConnected = False

    def onMessage(self, Message):
        MessageRecv = MessageModel.from_JSON(Message)
        self.SwitchRequestMethod(MessageRecv.Request)(MessageRecv.Status, MessageRecv.Message)

    def onError(self, SocketError):
        self.ErrorConnexion.emit()

    def ShutdownApplication(self):
        print("Closed Connection")
        if self.isConnected == True:
            self.WebSockets.close()

    def sendLoginAuthentification(self):
        LoginModel = RequestModel(0, self.Login)
        self.WebSockets.sendTextMessage(LoginModel.to_JSON())

    def SwitchRequestMethod(self, x):
        return {
            0: self.RecvCheckLogin
        }[x]

    def RecvCheckLogin(self, Status, Message):
        if Status == 200:
            self.GoodLogin.emit()
        else:
            self.ErrorLogin.emit()

