from pt_pump_up_admin import CRUD
from pt_pump_up_admin.link import Link
from pt_pump_up_admin.resource_stats import ResourceStats


class Dataset(CRUD):
    def __init__(self,
                 id: int = None,
                 short_name: str = None,
                 full_name: str = None,
                 description: str = None,
                 year: int = None,
                 link: Link = None,
                 resource_stats: ResourceStats = None,
                 authors: list = None,
                 nlp_tasks: list = None) -> None:

        super().__init__("dataset",
                         id=id,
                         short_name=short_name,
                         full_name=full_name,
                         description=description,
                         year=year,
                         link=link.json if link else None,
                         resource_stats=resource_stats.json if resource_stats else None,
                         author_emails=[
                             author.json['link']['email'] for author in authors] if authors else None,
                         nlp_tasks_short_names=[nlp_task.json['short_name'] for nlp_task in nlp_tasks] if nlp_tasks else None)
