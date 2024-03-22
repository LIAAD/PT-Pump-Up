class HTTPException(Exception):
    def __init__(self, message, response):
        super().__init__(message)
        self.message = message
        self.response = response
