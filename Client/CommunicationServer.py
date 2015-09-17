from PyQt5 import QtWebSockets, QtCore

from Model.RequestModel import RequestModel


class CommunicationServer(QtCore.QObject):

    ErrorConnexion = QtCore.pyqtSignal()

    isConnected = False

    Login = ""

    def __init__(self, address):
        super(CommunicationServer, self).__init__()
        self.Address = address
        self.WebSockets = QtWebSockets.QWebSocket()
        self.WebSockets.connected.connect(self.onConnected)
        self.WebSockets.disconnected.connect(self.onDisconnected)
        self.WebSockets.error.connect(self.onError)

    def Run(self):
        print("Trying to connected on " + self.Address)
        self.WebSockets.open(QtCore.QUrl(self.Address))

    def setAddress(self, address):
        self.Address = address

    def onConnected(self):
        print("Connected to " + self.Address)
        isConnected = True
        self.WebSockets.textMessageReceived.connect(self.onMessage)
        self.sendLoginAuthentification()

    def onDisconnected(self):
        self.isConnected = False

    def onMessage(self, Message):
        #TODO PROXY EMIT MESSAGE
        print(Message)

    def onError(self, SocketError):
        self.ErrorConnexion.emit()

    def ShutdownApplication(self):
        print("Closed Connection")
        if self.isConnected == True:
            self.WebSockets.close()

    def sendLoginAuthentification(self):
        LoginModel = RequestModel(0, self.Login)
        self.WebSockets.sendTextMessage(LoginModel.to_JSON())
