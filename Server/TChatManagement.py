
class TChatManagement():

    Clients = []

    def CheckLoginExists(self, name):
        for item in self.Clients:
            if item.Login is not None and item.Login == name:
                return True
        return False
