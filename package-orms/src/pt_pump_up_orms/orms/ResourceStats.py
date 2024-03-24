from pt_pump_up_orms import ORM
from requests import Response


class ResourceStats(ORM):
    def __init__(self,
                 id: int = None,
                 standard_format: bool = None,
                 off_the_shelf: bool = None,
                 preservation_rating: str = None) -> None:

        super().__init__(id, "resource-stats")

        self.standard_format = standard_format
        self.off_the_shelf = off_the_shelf
        self.preservation_rating = preservation_rating.lower(
        ) if preservation_rating is not None else None

    def serialize(self) -> dict:
        return {
            "id": self._id,
            "standard_format": self.standard_format,
            "off_the_shelf": self.off_the_shelf,
            "preservation_rating": self.preservation_rating
        }

    def deserialize(self, response: Response):
        self._id = response.json().get("id")
        self.standard_format = response.json().get("standard_format")
        self.off_the_shelf = response.json().get("off_the_shelf")
        self.preservation_rating = response.json().get("preservation_rating")
