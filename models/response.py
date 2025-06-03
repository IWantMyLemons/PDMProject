class Response():
    def __init__(self, is_success, message, payload=None):
        self.is_success = is_success
        self.message = message
        self.payload = payload
