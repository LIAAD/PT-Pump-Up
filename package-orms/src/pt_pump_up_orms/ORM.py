from abc import ABC


class ORM(ABC):
    def __init__(self, route, **kwargs) -> None:
        super().__init__()

        self._id = None
        self._json = dict()
        self._route = route.replace("/", "")

        self.bootstrap(kwargs)

    def bootstrap(self, kwargs):
        for key, value in kwargs.items():
            if key == "id":
                self._id = value
            elif value is not None:
                self._json[key] = value

    # Getters and Setters

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
        if not self._json and self._id is not None:
            print(f"JSON is empty, fetching from server with id{self._id}")
            self.show()
        elif not self._json and self._id is None:
            raise ValueError(f"JSON is empty and id is None")

        return self._json

    @json.setter
    def json(self, value):
        self._json = value

    @property
    def route(self):
        if self._route is None:
            raise ValueError("Route is None")

        return self._route

    @route.setter
    def route(self, value):
        self._route = value
