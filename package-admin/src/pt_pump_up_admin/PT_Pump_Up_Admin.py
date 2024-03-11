from requests import Session
import traceback
from environs import Env


class PTPumpUpAdmin:
    def __init__(self, bearer_token, url="https://pt-pump-up.inesctec.pt") -> None:
        self.bearer_token = bearer_token
        self.url = url
        self.session = Session()

    def submit(self, *args):
        crud, request = args[0]

        request.headers["Authorization"] = f"Bearer {self.bearer_token}"
        request.headers["Content-Type"] = "application/json"
        request.headers["Accept"] = "application/json"

        request.url = f"{self.url}/api/{request.url}"

        # Cannot send POST request with id in json body
        if request.method == "POST" and "id" in request.json and request.json['id'] is not None:
            raise ValueError("Cannot send POST request with id in json body")

        response = self.session.send(request.prepare())

        try:
            if request.method == "POST" and response.json()['id'] is not None:
                crud.json['id'] = response.json()['id']

            if request.method == "DELETE":
                crud.json = dict()
        except:
            traceback.print_exc()

        finally:
            return response


class PTPumpAdminFactory:
    @staticmethod
    def create():
        env = Env()
        env.read_env()
        return PTPumpUpAdmin(bearer_token=env.str("BEARER_TOKEN"), url=env.str("URL"))
