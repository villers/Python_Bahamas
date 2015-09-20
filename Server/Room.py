class Room:
    def __init__(self, name, client):
        self.Name = name
        self.Players = []
        self.Players.append(client)

    def broadcast(self, from_player, msg):
        for player in self.Players:
            print(player, msg)

    def remove_player(self, player):
        self.Players.remove(player)