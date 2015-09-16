from PyQt5 import QtCore, QtNetwork, QtWebSockets

class Server():
    def __init__(self, port):
        self.clients = []
        self.connection = None
        self.server = QtWebSockets.QWebSocketServer("Socket1", QtWebSockets.QWebSocketServer.NonSecureMode)

        if self.server.listen(QtNetwork.QHostAddress.Any, port):
            print("listening on port" + str(port))
            self.server.newConnection.connect(self.onNewConnection)
        else:
            print('error')

    def onNewConnection(self):
        print("new user")
        self.connection = self.server.nextPendingConnection()
        self.connection.textMessageReceived.connect(self.processTextMessage)
        self.connection.disconnected.connect(self.socketDisconnected)

        self.clients.append(self.connection)

    def processTextMessage(self,  message):
        if (self.connection):
            self.connection.sendTextMessage(message)

    def processBinaryMessage(self,  message):
        if (self.connection):
            self.connection.sendBinaryMessage(message)

    def socketDisconnected(self):
        if (self.connection):
            self.clients.remove(self.connection)
            self.connection.deleteLater()