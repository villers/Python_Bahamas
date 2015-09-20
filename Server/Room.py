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
            result.append(item.Login)
        return result