from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from TChatApplicationClient import *

class LoginTchat(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        super(LoginTchat, self).__init__(parent)
        self.setupUIWindow()
        self.SetupUIWidgets()
        self.SetupSignal()

    def setupUIWindow(self):
        self.setWindowTitle("Bahamas Tchat login")
        self.resize(300, 200)
        self.CentralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.CentralWidget)

    def SetupUIWidgets(self):
        self.LoginLineEdit = QtWidgets.QLineEdit(self.centralWidget())
        self.LoginLineEdit.setGeometry(90, 50, 150, 20)
        self.LoginButtonStart = QtWidgets.QPushButton("Login", self.centralWidget())
        self.LoginButtonStart.setGeometry(90, 80, 150, 30)

    def SetupSignal(self):
        self.LoginButtonStart.clicked.connect(self.Handler_Click_Button_Login)

    def Handler_Click_Button_Login(self):
        appPrincipal = TChatApplicationClient(self)
        appPrincipal.show()
        self.hide()


