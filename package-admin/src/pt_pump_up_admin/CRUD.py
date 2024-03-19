from abc import ABC
from requests import Request
from pt_pump_up_admin import PTPumpAdminFactory
import traceback
from pt_pump_up_admin.exceptions import HTTPException


class CRUD(ABC):
    # id is a propriety of the class
    def __init__(self, route, **kwargs) -> None:
        if route is None:
            raise ValueError("route cannot be None")

        self.route = route.replace("/", "")
        self._id = None
        self._json = dict()
        self.client = PTPumpAdminFactory.create()

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif value is not None:
                self._json[key] = value

    @property
    def id(self):
        return self._id

    # Avoid numpy 64-bit integer that are not JSON serializable
    @id.setter
    def id(self, value):
        if value is not None:
            self._id = int(value)
        else:
            self._id = None

    @property
    def json(self):
        if self._json is None:
            raise ValueError("JSON is empty")

        return self._json

    def index(self):
        try:
            response = self.client.submit(
                Request(method="GET", url=self.route))
        except HTTPException as e:
            traceback.print_exc()
            response = e.response
        finally:
            return response

    def store(self):
        if self._id is not None:
            raise ValueError("id cannot be set for POST request")

        if not self._json:
            raise ValueError("json cannot be empty for POST request")

        try:
            response = self.client.submit(
                Request(method="POST", url=self.route, json=self._json))

            self._id = response.json().get("id")
            self._json = response.json()

        except HTTPException as e:
            traceback.print_exc()
            response = e.response
            self.id = None
        finally:
            return response

    def show(self):
        if self._id is None:
            raise ValueError("id cannot be None")
        try:
            response = self.client.submit(
                Request(method="GET", url=f"{self.route}/{self._id}"))
            self._json = response.json()
        except HTTPException as e:
            traceback.print_exc()
            response = e.response
            self._json = dict()
        finally:
            return response

    def update(self):
        if self._id is None:
            raise ValueError("id cannot be None")

        if not self._json:
            raise ValueError("json cannot be empty for PUT request")

        try:
            response = self.client.submit(
                Request(method="PUT", url=f"{self.route}/{self._id}", json=self._json))
        except HTTPException as e:
            traceback.print_exc()
            response = e.response
        finally:
            return response

    def destroy(self):
        if self._id is None:
            raise ValueError("id cannot be None")

        try:
            response = self.client.submit(
                Request(method="DELETE", url=f"{self.route}/{self._id}"))
            self._json = dict()
            self._id = None
        except HTTPException as e:
            response = e.response
            traceback.print_exc()
        finally:
            return response
