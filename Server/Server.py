from PyQt5 import QtCore, QtNetwork, QtWebSockets

class Server():
    def __init__(self, port):
        self.server = QtWebSockets.QWebSocketServer("Socket1", QtWebSockets.QWebSocketServer.NonSecureMode)

        if self.server.listen(QtNetwork.QHostAddress.Any, port):
            print("listening on port" + str(port))
        return