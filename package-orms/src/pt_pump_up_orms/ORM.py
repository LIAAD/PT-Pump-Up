from abc import ABC, abstractmethod
from requests import Response

class ORM(ABC):
    def __init__(self, id, route) -> None:
        super().__init__()

        self._id = id
        self._route = route.replace("/", "")

    @abstractmethod
    def serialize(self):
        raise NotImplementedError

    @abstractmethod
    def deserialize(self, response: Response):
        raise NotImplementedError

    @property
    def id(self):
        if self._id is None:
            raise ValueError("ID is None")

        return self._id

    # Avoid numpy 64-bit integer that are not JSON serializable
    @id.setter
    def id(self, value):
        if value is not None:
            self._id = int(value)
        else:
            self._id = None

    @property
    def route(self):
        if self._route is None:
            raise ValueError("Route is None")

        return self._route

    @route.setter
    def route(self, value):
        self._route = value
