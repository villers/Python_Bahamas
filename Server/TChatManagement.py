
class TChatManagement():

    Clients = []
    Rooms = []

    def CheckLoginExists(self, name):
        for item in self.Clients:
            if item.Login is not None and item.Login == name:
                return True
        return False

    def CheckRoomExists(self, name):
        for item in self.Rooms:
            if item.Name is not None and item.Name == name:
                return True
        return False

    def GetRoomByName(self, name):
        for item in self.Rooms:
            if item.Name is not None and item.Name == name:
                return item
        return False