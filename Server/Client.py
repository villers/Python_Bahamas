from Model.RequestModel import RequestModel
from Model.MessageModel import MessageModel
from Room import Room

class Client():
    def __init__(self, QWebSocketClient, ServerInstance):

        self.Login = None

        self.WebSocketClient = QWebSocketClient
        self.ServerObject = ServerInstance
        self.WebSocketClient.textMessageReceived.connect(self.OnProcessTextMessage)
        self.WebSocketClient.disconnected.connect(self.OnSocketDisconnected)

    def OnProcessTextMessage(self,  message):
        RequestDecoded = RequestModel.from_JSON(message)
        self.SwitchRequestMethod(RequestDecoded.request)(RequestDecoded.Message)

    def OnSocketDisconnected(self):
        self.WebSocketClient.deleteLater()
        self.ServerObject.TChatManagementInstance.Clients.remove(self)
        self.WebSocketClient.disconnected.disconnect()
        self.WebSocketClient.textMessageReceived.disconnect()

    def OnLogin(self, Message):
        if not self.ServerObject.TChatManagementInstance.CheckLoginExists(Message):
            print("Login OK")
            self.Login = Message
            self.WebSocketClient.sendTextMessage(MessageModel(200, "", 0).to_JSON())
        else:
            print("Login Error")
            self.WebSocketClient.sendTextMessage(MessageModel(404, "Already use", 0).to_JSON())

    def OnJoinRoom(self, Message):
        if not self.ServerObject.TChatManagementInstance.CheckRoomExists(Message):
            print("Create Room And Join Room OK")
            self.ServerObject.TChatManagementInstance.Rooms.append(Room(Message, self))
        else:
            print("Join Room Okey")
            self.ServerObject.TChatManagementInstance.GetRoomByName(Message).Players.append(self)

    def OnListPlayerFromRoom(self, Message):
        if self.ServerObject.TChatManagementInstance.CheckRoomExists(Message):
            self.ServerObject.TChatManagementInstance.GetRoomByName(Message).Players


    def SwitchRequestMethod(self, x):
        return {
            0: self.OnLogin,
            1: self.OnJoinRoom,
            2: self.OnListPlayerFromRoom
        }[x]