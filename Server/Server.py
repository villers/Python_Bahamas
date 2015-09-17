from PyQt5 import QtCore, QtNetwork, QtWebSockets
from Client import Client
from TChatManagement import TChatManagement

class Server():

    TChatManagementInstance = TChatManagement()

    def __init__(self, port):
        self.clients = []
        self.connection = None
        self.server = QtWebSockets.QWebSocketServer("Socket1", QtWebSockets.QWebSocketServer.NonSecureMode)

        if self.server.listen(QtNetwork.QHostAddress.Any, port):
            print("listening on port" + str(port))
            self.server.newConnection.connect(self.onNewConnection)
            self.server.serverError.connect(self.OnErrorOnSocket)
        else:
            print('error')

    def onNewConnection(self):
        self.TChatManagementInstance.Clients.append(Client(self.server.nextPendingConnection(), self))

    def OnErrorOnSocket(self, StatusCodeError):
        print(StatusCodeError)