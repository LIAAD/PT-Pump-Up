from pt_pump_up_admin import CRUD
from pt_pump_up_admin.link import Link
from pt_pump_up_admin.resource_stats import ResourceStats


class Dataset(CRUD):
    def __init__(self, identifier: int = None) -> None:
        super().__init__("dataset", identifier)

    def store(self,
              short_name: str,
              year: int,
              authors: list,
              link: Link,
              resource_stats: ResourceStats,
              description: str = None):

        base_request = super().store()

        base_request.json = {
            "short_name": short_name,
            "year": year,
            "authors": authors,
            "link_id": link.identifier,
            "resource_stats": resource_stats.json,
            "link": link.json,
            "description": description
        }

        return base_request
