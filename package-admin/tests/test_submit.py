from requests import Request
from tests.lib.utils import fixture_load_admin_instance
from pt_pump_up_admin import CRUD


class TestSubmit(CRUD):
    def __init__(self) -> None:
        super().__init__("helloworld")

    def store(self, *args, **kwargs) -> Request:
        return super().store(*args, **kwargs)

    def update(self, *args, **kwargs) -> Request:
        return super().update(*args, **kwargs)


def test_submit(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    response = client.submit(TestSubmit().index())

    assert response.status_code == 200
    assert response.json()["message"] == "Hello World!"
