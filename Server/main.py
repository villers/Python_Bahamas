import sys
import os

# for webserver
import http.server
import socketserver
from multiprocessing import Process

# for qt
from PyQt5 import QtCore,QtNetwork, QtWebSockets
from Server import Server


def http_server():
    os.chdir(os.path.dirname(os.path.realpath(__file__)) + '/../clientweb')
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("",8080), Handler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass


def main():
    app = QtCore.QCoreApplication(sys.argv)
    threadServer = Server(3334)

    threadhttp = Process(target=http_server, args=())
    threadhttp.start()

    app.exec()
    return 1

if __name__ == "__main__":
    sys.exit(main())
