from Model.RequestModel import RequestModel
from Model.MessageModel import MessageModel
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

    def OnLogin(self, Message):
        if self.ServerObject.TChatManagementInstance.CheckLoginExists(Message) == False:
            self.Login = Message
            self.WebSocketClient.sendTextMessage(MessageModel(200, "").to_JSON())
        else:
            self.WebSocketClient.sendTextMessage(MessageModel(404, "Already use").to_JSON())

    def SwitchRequestMethod(self, x):
        return {
            0: self.OnLogin
        }[x]