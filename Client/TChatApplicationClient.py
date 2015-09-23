from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from CameraConfig import *
from AudioInputConfig import *
from AudioOutputConfig import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class TChatApplicationClient(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(TChatApplicationClient, self).__init__(parent)
        self.QWidgetRoomList = []
        self.DialogWindowCreateRoom = None
        self.LoginTchatObject = parent
        self.CameraConfigObject = CameraConfig()
        self.AudioInputConfig = AudioInputConfig()
        self.AudioOutputConfig = AudioOutputConfig()
        self.createWindow()
        self.createMenuBar()
        self.createListRoom()
        self.createCameraList()
        self.createAudioInputList()
        self.createAudioOutputList()
        self.SetDataList()
        self.createTabWidgetRoom()
        self.setSignalCommunicationServer()

    def createWindow(self):
        self.setWindowTitle("Bahamas Tchat")
        self.resize(800, 600)
        self.CentralWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.CentralWidget)

    def createMenuBar(self):
        self.MenuBar = QtWidgets.QMenuBar(self)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.CloseApp = QtWidgets.QAction("&Create Channel", self)
        self.CloseApp.triggered.connect(self.onTriggerCreateRoom)
        self.MenuBar.addAction(self.CloseApp)
        self.setMenuBar(self.MenuBar)

    def onTriggerCreateRoom(self):
        nameNewRoom, Ok = QtWidgets.QInputDialog.getText(self, "creation of room", "Room")
        if Ok == True and nameNewRoom != "":
            self.LoginTchatObject.WSServer.sendCreationOfRoom(nameNewRoom)

    def createListRoom(self):
        self.ListRoomLabel = QtWidgets.QLabel("List Room", self.CentralWidget)
        self.ListRoomLabel.setGeometry(QtCore.QRect(650, 20, 251, 22))
        self.ListRoom = QtWidgets.QListWidget(self.CentralWidget)
        self.ListRoom.setGeometry(QtCore.QRect(590, 40, 211, 561))
        self.ListRoom.setObjectName(_fromUtf8("ListRoom"))
        self.ListRoom.itemDoubleClicked.connect(self.onClickDBLItemListRoom)

    def createCameraList(self):
        self.ComboBoxCameraListLabel = QtWidgets.QLabel("Choose Your Camera", self.CentralWidget)
        self.ComboBoxCameraListLabel.setGeometry(QtCore.QRect(150, 20, 251, 22))
        self.ComboBoxCameraList = QtWidgets.QComboBox(self.CentralWidget)
        self.ComboBoxCameraList.setGeometry(QtCore.QRect(150, 40, 251, 22))

    def createAudioInputList(self):
        self.ComboBoxAudioInputLabel = QtWidgets.QLabel("Choose Your input Audio", self.CentralWidget)
        self.ComboBoxAudioInputLabel.setGeometry(QtCore.QRect(150, 60, 251, 22))
        self.ComboBoxAudioInput = QtWidgets.QComboBox(self.CentralWidget)
        self.ComboBoxAudioInput.setGeometry(QtCore.QRect(150, 80, 251, 22))

    def createAudioOutputList(self):
        self.ComboBoxAudioOutputLabel = QtWidgets.QLabel("Choose Your output Audio", self.CentralWidget)
        self.ComboBoxAudioOutputLabel.setGeometry(QtCore.QRect(150, 100, 251, 22))
        self.ComboBoxAudioOutput = QtWidgets.QComboBox(self.CentralWidget)
        self.ComboBoxAudioOutput.setGeometry(QtCore.QRect(150, 120, 251, 22))

    def SetDataList(self):
        self.ComboBoxCameraList.addItems(self.CameraConfigObject.GetCameralistName())
        self.ComboBoxAudioInput.addItems(self.AudioInputConfig.GetAudioInputListName())
        self.ComboBoxAudioOutput.addItems(self.AudioOutputConfig.GetAudioOutputListName())

    def createTabWidgetRoom(self):
        self.TabWidgetRoom = QtWidgets.QTabWidget(self.CentralWidget)
        self.TabWidgetRoom.setGeometry(QtCore.QRect(0, 150, 589, 450))


    def setSignalCommunicationServer(self):
        self.LoginTchatObject.WSServer.OnGetAllRoom.connect(self.onUpdateListRooms)
        self.LoginTchatObject.WSServer.sendRequestRooms()
        self.LoginTchatObject.WSServer.OnCreationRoomSuccess.connect(self.OnUpdateCreationOfRoomwithSuccess)
        self.LoginTchatObject.WSServer.OnJoinRoomSuccess.connect(self.onJoinRoomSuccessViewUpdate)
        self.LoginTchatObject.WSServer.OnUpdateListInRoom.connect(self.OnUpdateListClientInRoom)

    def onUpdateListRooms(self, listRoom):
        self.ListRoom.clear()
        self.ListRoom.addItems(listRoom)

    def onClickDBLItemListRoom(self, itemClicked):
        roomSelected = itemClicked.text()
        self.LoginTchatObject.WSServer.sendRequestJoinRoom(roomSelected)

    def OnUpdateCreationOfRoomwithSuccess(self):
        self.LoginTchatObject.WSServer.sendRequestRooms()

    def onJoinRoomSuccessViewUpdate(self, NameOfRoom):
        newWidgetTab = QtWidgets.QWidget(self.TabWidgetRoom)
        ListWidget = QtWidgets.QListWidget(newWidgetTab)
        ListWidget.setGeometry(QtCore.QRect(190, 130, 191, 241))
        self.QWidgetRoomList.append({"Room": NameOfRoom, "Widget": newWidgetTab, "ListWidget": ListWidget})
        self.TabWidgetRoom.addTab(newWidgetTab, NameOfRoom)
        self.LoginTchatObject.WSServer.sendRequestListInRoom(NameOfRoom)

    def OnUpdateListClientInRoom(self, JSONListClient):
        for item in self.QWidgetRoomList:
            if item["Room"] == JSONListClient.Room:
                for itemClient in JSONListClient.Clients:
                    item["ListWidget"].addItem(itemClient.Login)
            break

