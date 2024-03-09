from abc import ABC
from requests import Request


class CRUD(ABC):

    def __init__(self, route, identifier: int = None) -> None:
        if route is None:
            raise ValueError("route cannot be None")

        self.route = route.replace("/", "")
        self.identifier = identifier

    def index(self) -> Request:
        return Request(
            method="GET",
            url=self.route,
        )

    def store(self) -> Request:
        return Request(
            method="POST",
            url=self.route,
        )

    def show(self, identifier: int = None) -> Request:

        if self.identifier is None and identifier is None:
            raise ValueError("identifier cannot be None")
        elif self.identifier is None and identifier is not None:
            self.identifier = identifier
        return Request(
            method="GET",
            url=f"{self.route}/{self.identifier}",
        )

    def update(self, identifier: int = None) -> Request:

        if self.identifier is None and identifier is None:
            raise ValueError("identifier cannot be None")
        elif self.identifier is None and identifier is not None:
            self.identifier = identifier

        return Request(
            method="PUT",
            url=f"{self.route}/{self.identifier}",
        )

    def delete(self, identifier: int = None) -> Request:

        if self.identifier is None and identifier is None:
            raise ValueError("identifier cannot be None")
        elif self.identifier is None and identifier is not None:
            self.identifier = identifier

        return Request(
            method="DELETE",
            url=f"{self.route}/{self.identifier}",
        )
