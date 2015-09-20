from Model.ClientModel import ClientModel

class Room:
    def __init__(self, name, client):
        self.Name = name
        self.Players = []
        self.Players.append(client)

    def remove_player(self, player):
        if (player in self.Players):
            self.Players.remove(player)

    def GetAllPlayersName(self):
        result = []
        for item in self.Players:
            if item.WebSocketClient.localAddress().toString() == "::1":
                ip = "127.0.0.1"
            else:
                ip = item.WebSocketClient.localAddress().toString()
            result.append(ClientModel(item.Login, ip))
        return result

    def PlayerExists(self, player):
        return (player in self.Players)