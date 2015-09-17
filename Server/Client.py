from Model.RequestModel import RequestModel
class Client():
    def __init__(self, QWebSocketClient, ServerInstance):
        self.WebSocketClient = QWebSocketClient
        self.ServerObject = ServerInstance
        self.WebSocketClient.textMessageReceived.connect(self.OnProcessTextMessage)
        self.WebSocketClient.disconnected.connect(self.OnSocketDisconnected)

    def OnProcessTextMessage(self,  message):
        RequestDecoded = RequestModel.from_JSON(message)
        self.SwitchRequestMethod(RequestDecoded.request)(RequestDecoded.Message)

    def OnSocketDisconnected(self):
        self.WebSocketClient.deleteLater()
        self.ServerObject.removeClientOnDisconnect(self)

    def OnLogin(self, Message):
        print(Message)

    def SwitchRequestMethod(self, x):
        return {
            0: self.OnLogin
        }[x]