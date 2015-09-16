import json
class RequestModel():
    request = 0
    Message = None

    def __init__(self, Request, Message):
        self.request = Request
        self.Message = Message

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)