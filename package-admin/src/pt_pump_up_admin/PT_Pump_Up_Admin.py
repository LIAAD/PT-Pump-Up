from requests import Request, Session
import json

class PTPumpUpAdmin:
    def __init__(self, bearer_token, url="https://pt-pump-up.inesctec.pt") -> None:
        self.bearer_token = bearer_token
        self.url = url
        self.session = Session()

    def submit(self, request: Request):
        request.headers["Authorization"] = f"Bearer {self.bearer_token}"
        request.headers["Content-Type"] = "application/json"
        request.headers["Accept"] = "application/json"

        request.url = f"{self.url}/api/{request.url}"
        
        print(request.url)

        return self.session.send(request.prepare())
