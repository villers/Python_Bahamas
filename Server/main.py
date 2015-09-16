import sys
from PyQt5 import QtCore,QtNetwork, QtWebSockets
from Server import Server

def main():
    app = QtCore.QCoreApplication(sys.argv)
    Server(3334)
    app.exec()
    return 1

if __name__ == "__main__":
    sys.exit(main())
