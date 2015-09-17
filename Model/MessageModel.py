import json

def object_decoder(obj):
    return MessageModel(obj['Status'], obj['Message'], obj['Request'])

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