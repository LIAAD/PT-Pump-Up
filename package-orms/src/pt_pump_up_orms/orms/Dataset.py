from pt_pump_up_orms import ORM
from pt_pump_up_orms.orms import Link
from pt_pump_up_orms.orms import ResourceStats


class Dataset(ORM):
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
                         full_name=full_name if full_name else short_name,
                         description=description if description else short_name,
                         year=year,
                         link=link.json if link else None,
                         resource_stats=resource_stats.json if resource_stats else None,
                         author_emails=[
                             author.json['link']['email'] for author in authors] if authors else None,
                         nlp_tasks_short_names=[nlp_task.json['short_name'] for nlp_task in nlp_tasks] if nlp_tasks else None)
        self._link = link

    @property
    def link(self):
        if self._link is None:
            raise Exception("Link is not set")

        return self._link

    @link.setter
    def link(self, link):
        self._link = link

    # TODO: Remove the Need for .index()
    @property
    def id(self):
        if self._id is None and self._json.get("short_name"):
            for dataset in self.index().json():
                if dataset.get("short_name") == self._json.get("short_name"):
                    self._id = dataset.get("id")
                    break

        return self._id
