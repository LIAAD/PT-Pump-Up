from pt_pump_up_admin import CRUD
from requests import Request
from pt_pump_up_admin.link import Link
from pt_pump_up_admin.resource_stats import ResourceStats


class Model(CRUD):
    def __init__(self, identifier: int = None) -> None:
        super().__init__('machine-learning-model', identifier)

    def store(self, short_name: str,
              year: int,
              link: Link,
              resource_stats: ResourceStats,
              results: list = None,
              full_name: str = None,
              description: str = None,
              nlp_tasks: list = None) -> Request:

        base_request = super().store()

        base_request.json = {
            "short_name": short_name,
            "full_name": full_name,
            "description": description,
            "year": year,
            "link": link.json,
            "resource_stats": resource_stats.json,
            "results": [result.json for result in results] if results else [],
            "nlp_task_ids": [nlp_task.identifier for nlp_task in nlp_tasks]
        }

        return base_request
