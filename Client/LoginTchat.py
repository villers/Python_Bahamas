from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from TChatApplicationClient import *
from CommunicationServer import *

class LoginTchat(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        super(LoginTchat, self).__init__(parent)
        self.ShowErrorLabel = None
        self.WSServer = None
        self.setupUIWindow()
        self.SetupUIWidgets()
        self.SetupSignal()

    def setupUIWindow(self):
        self.setWindowTitle("Bahamas Tchat login")
        self.resize(300, 200)
        self.CentralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.CentralWidget)

    def SetupUIWidgets(self):
        self.AddrLabel = QtWidgets.QLabel("Adresse", self.CentralWidget)
        self.AddrLabel.setGeometry(30, 20, 50, 20)
        self.AddrLineEdit = QtWidgets.QLineEdit(self.centralWidget())
        self.AddrLineEdit.setGeometry(90, 20, 150, 20)
        self.AddrLabel = QtWidgets.QLabel("Login", self.CentralWidget)
        self.AddrLabel.setGeometry(30, 50, 50, 20)
        self.LoginLineEdit = QtWidgets.QLineEdit(self.centralWidget())
        self.LoginLineEdit.setGeometry(90, 50, 150, 20)
        self.LoginButtonStart = QtWidgets.QPushButton("Connection", self.centralWidget())
        self.LoginButtonStart.setGeometry(90, 80, 150, 30)

    def SetupSignal(self):
        self.LoginButtonStart.clicked.connect(self.Handler_Click_Button_Login)

    def Handler_Click_Button_Login(self):
        if self.ShowErrorLabel is not None:
            self.ShowErrorLabel.hide()
        if self.WSServer is None:
            self.WSServer = CommunicationServer()
            self.WSServer.ErrorConnexion.connect(self.ShowErrorConnextion)
            self.WSServer.ErrorLogin.connect(self.OnLoginError)
            self.WSServer.GoodLogin.connect(self.OnLoginGood)
        self.WSServer.Login = self.LoginLineEdit.text()
        if (self.WSServer.Address != self.AddrLineEdit.text()):
            self.WSServer.closeConnexion()
        self.WSServer.setAddress(self.AddrLineEdit.text())
        if self.WSServer.isConnected == False:
            self.WSServer.Run()
        else:
            self.WSServer.sendLoginAuthentification()


    def ShowErrorConnextion(self):
        if self.ShowErrorLabel is None :
            self.ShowErrorLabel = QtWidgets.QLabel("Error Connexion", self.CentralWidget)
            self.ShowErrorLabel.setGeometry(90, 100, 150, 30)
        self.ShowErrorLabel.setText("Error Connexion")
        if self.ShowErrorLabel.isHidden() == True :
            self.ShowErrorLabel.show()

    def OnLoginGood(self):
        self.WSServer.ErrorConnexion.disconnect()
        self.WSServer.ErrorLogin.disconnect()
        self.WSServer.GoodLogin.disconnect()
        appPrincipal = TChatApplicationClient(self)
        appPrincipal.show()
        self.hide()

    def OnLoginError(self):
        if self.ShowErrorLabel is None :
            self.ShowErrorLabel = QtWidgets.QLabel("Error Connexion", self.CentralWidget)
            self.ShowErrorLabel.setGeometry(90, 100, 150, 30)
        self.ShowErrorLabel.setText("Error Login")
        if self.ShowErrorLabel.isHidden() == True :
            self.ShowErrorLabel.show()





