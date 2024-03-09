from abc import ABC, abstractmethod
from requests import Request


class CRUD(ABC):

    def __init__(self, route, id: int = None) -> None:
        if route is None:
            raise ValueError("route cannot be None")

        self.route = route
        self.id = id

    def index(self) -> Request:
        return Request(
            method="GET",
            url=self.route,
        )

    @abstractmethod
    def create(self, *args, **kwargs) -> Request:
        raise NotImplementedError

    def show(self) -> Request:
        if self.id is None:
            raise ValueError("id cannot be None")

        return Request(
            method="GET",
            url=f"{self.route}/{self.id}",
        )

    @abstractmethod
    def update(self, *args, **kwargs) -> Request:
        raise NotImplementedError

    def delete(self) -> Request:
        if self.id is None:
            raise ValueError("id cannot be None")

        return Request(
            method="DELETE",
            url=f"{self.route}/{self.id}",
        )
