import json

def object_decoder(obj):
    return MessageModel(obj['Status'], obj['Message'])

class MessageModel():
    Status = 0
    Message = None

    def __init__(self, Status, Message):
        self.Status = Status
        self.Message = Message

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    @staticmethod
    def from_JSON(data):
        return json.loads(data, object_hook=object_decoder)