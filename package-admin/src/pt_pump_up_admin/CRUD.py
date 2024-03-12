from abc import ABC
from requests import Request
from pt_pump_up_admin import PTPumpAdminFactory


class CRUD(ABC):
    # id is a propriety of the class
    def __init__(self, route, **kwargs) -> None:
        if route is None:
            raise ValueError("route cannot be None")

        self.route = route.replace("/", "")
        self._id = None
        self._json = dict()

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif value is not None:
                self._json[key] = value

    @property
    def id(self):
        if self._id is None and self._json:
            self._id = self._json.get("id")

        if self._id is None:
            raise ValueError("Id is None")

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
        if not self._json and self._id is not None:
            client = PTPumpAdminFactory.create()

            print(f"JSON is empty for id: {self._id}, fetching from server")

            response = client.submit(self.show())
            self._json = response.json()

        return self._json

    def index(self) -> Request:
        return self, Request(
            method="GET",
            url=self.route,
        )

    def store(self) -> Request:
        return self, Request(
            method="POST",
            url=self.route,
            json=self._json
        )

    def show(self) -> Request:
        """
        if self.identifier is None and identifier is None:
            raise ValueError("identifier cannot be None")
        elif self.identifier is None and identifier is not None:
            self.identifier = identifier
        """

        return self, Request(
            method="GET",
            url=f"{self.route}/{self._id}",
        )

    def update(self) -> Request:
        """
        if self.identifier is None and identifier is None:
            raise ValueError("identifier cannot be None")
        elif self.identifier is None and identifier is not None:
            self.identifier = identifier
        """

        return self, Request(
            method="PUT",
            url=f"{self.route}/{self._id}",
        )

    def destroy(self) -> Request:

        if self._id is None:
            raise ValueError("id cannot be None")

        return self, Request(
            method="DELETE",
            url=f"{self.route}/{self._id}",
        )
