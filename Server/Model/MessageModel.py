import json

def object_decoder(obj):
    if 'Status' in obj.keys():
        return MessageModel(obj['Status'], obj['Message'], obj['Request'])
    if 'Ip' in obj.keys():
        return IpClientModel(obj["Ip"], obj["Login"])
    return RoomClientModel(obj["Room"], obj["Clients"])

class MessageModel():
    Status = 0
    Request = 0
    Message = None

    def __init__(self, Status, Message, Request):
        self.Status = Status
        self.Message = Message
        self.Request = Request

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    @staticmethod
    def from_JSON(data):
        return json.loads(data, object_hook=object_decoder)


class IpClientModel():
    Ip = 0
    Login = ""

    def __init__(self, ip, Login):
        self.Ip = ip
        self.Login = Login

class RoomClientModel():
    Room = ""
    Clients = []

    def __init__(self, room, clients):
        self.Room = room
        self.Clients = clients