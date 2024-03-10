from pt_pump_up_admin import CRUD
from requests import Request


class ResourceStats(CRUD):
    def __init__(self, identifier: int = None) -> None:
        super().__init__("resource-stats", identifier)

    def store(self, standard_format: bool, off_the_shelf: bool, preservation_rating: str = None) -> Request:
        base_request = super().store()

        base_request.json = {
            "standard_format": standard_format,
            "off_the_shelf": off_the_shelf,
            "preservation_rating": preservation_rating.lower()
        }

        self.json = base_request.json

        return base_request
