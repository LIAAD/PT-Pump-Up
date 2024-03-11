from abc import ABC
from requests import Request


class CRUD(ABC):

    def __init__(self, route, *args, **kwargs) -> None:
        if route is None:
            raise ValueError("route cannot be None")

        self.route = route.replace("/", "")
        self.json = dict()

        for arg in args:
            self.json.update(arg)

        for key, value in kwargs.items():
            self.json[key] = value

    def index(self) -> Request:
        return self, Request(
            method="GET",
            url=self.route,
        )

    def store(self) -> Request:
        return self, Request(
            method="POST",
            url=self.route,
            json=self.json
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
            url=f"{self.route}/{self.json.id}",
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
            url=f"{self.route}/{self.json.id}",
        )

    def destroy(self) -> Request:

        if self.json['id'] is None:
            raise ValueError("id cannot be None")

        return self, Request(
            method="DELETE",
            url=f"{self.route}/{self.json['id']}",
        )
