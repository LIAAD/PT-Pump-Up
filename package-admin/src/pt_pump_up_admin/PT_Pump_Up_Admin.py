from pt_pump_up_admin import CRUD
from requests import Request, Session


class PTPumpUpAdmin:
    def __init__(self, bearer_token, url="https://pt-pump-up.inesctec.pt") -> None:
        self.bearer_token = bearer_token
        self.url = url
        self.session = Session()

    def submit(self, request: Request):
        request.headers["Authorization"] = f"Bearer {self.bearer_token}"
        request.url = f"{self.url}/api/{request.url}"

        return self.session.send(request.prepare())
