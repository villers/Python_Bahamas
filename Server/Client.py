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
        self.ServerObject.TChatManagementInstance.RemoveUserFromAllRoom(self)
        self.WebSocketClient.deleteLater()
        self.ServerObject.TChatManagementInstance.Clients.remove(self)
        self.WebSocketClient.disconnected.disconnect()
        self.WebSocketClient.textMessageReceived.disconnect()

    def OnLogin(self, Message):
        if not self.ServerObject.TChatManagementInstance.CheckLoginExists(Message):
            print("Login OK : " + str(Message))
            self.Login = Message
            self.WebSocketClient.sendTextMessage(MessageModel(200, "", 0).to_JSON())
        else:
            print("Login Error")
            self.WebSocketClient.sendTextMessage(MessageModel(404, "Already use", 0).to_JSON())

    def OnListAvailableRoom(self, Message):
        print("List Available Room: " + str(self.ServerObject.TChatManagementInstance.Rooms))
        self.WebSocketClient.sendTextMessage(MessageModel(200, self.ServerObject.TChatManagementInstance.GetAllRoomName(), 1).to_JSON())

    def OnJoinRoom(self, Message):
        if not self.ServerObject.TChatManagementInstance.CheckRoomExists(Message):
            print("Create Room And Join Room OK")
            self.ServerObject.TChatManagementInstance.Rooms.append(Room(Message, self))
        elif(self.ServerObject.TChatManagementInstance.GetRoomByName(Message).PlayerExists(self) == False):
            print("Join Room Okey")
            self.ServerObject.TChatManagementInstance.GetRoomByName(Message).Players.append(self)
        self.WebSocketClient.sendTextMessage(MessageModel(200, "", 2).to_JSON())

    def OnLeaveRoom(self, Message):
        if self.ServerObject.TChatManagementInstance.CheckRoomExists(Message):
            print("Leave Room Okey")
            self.ServerObject.TChatManagementInstance.GetRoomByName(Message).remove_player(self)
            self.WebSocketClient.sendTextMessage(MessageModel(200, "", 4).to_JSON())
        else:
            print("Leave Room Ko")
            self.WebSocketClient.sendTextMessage(MessageModel(404, "Does not exist", 4).to_JSON())

    def OnListClientRoom(self, Message):
        if self.ServerObject.TChatManagementInstance.CheckRoomExists(Message):
            print("List Client from "+ str(Message) +": " + str(self.ServerObject.TChatManagementInstance.GetRoomByName(Message).GetAllPlayersName()))
            self.WebSocketClient.sendTextMessage(MessageModel(200, self.ServerObject.TChatManagementInstance.GetRoomByName(Message).GetAllPlayersName(), 3).to_JSON())
        else:
            print(str(Message) + " does not exist")
            self.WebSocketClient.sendTextMessage(MessageModel(404, "Does not exist", 3).to_JSON())


    def SwitchRequestMethod(self, x):
        return {
            0: self.OnLogin,
            1: self.OnListAvailableRoom,
            2: self.OnJoinRoom,
            3: self.OnListClientRoom,
            4: self.OnLeaveRoom
        }[x]