import json

def object_decoder(obj):
    return ClientModel(obj['Login'], obj['Ip'])

class ClientModel():
    Login = None
    Ip = None

    def __init__(self, Login, Ip):
        self.Login = Login
        self.Ip = Ip


    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    @staticmethod
    def from_JSON(data):
        return json.loads(data, object_hook=object_decoder)