from requests import Session
from environs import Env
from requests import Request
from pt_pump_up_admin.exceptions import HTTPException


class PTPumpAdminFactory:
    @staticmethod
    def create():
        env = Env()
        env.read_env()
        return PTPumpUpAdmin(bearer_token=env.str("BEARER_TOKEN"), url=env.str("URL"))


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

        response = self.session.send(request.prepare())

        if response.status_code < 200 or response.status_code >= 300:
            raise HTTPException(
                f"Error {response.status_code}: {response.text}", response)

        return response
