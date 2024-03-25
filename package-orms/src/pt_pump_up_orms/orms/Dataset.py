from pt_pump_up_orms import ORM
from requests import Response


class Dataset(ORM):
    def __init__(self,
                 id: int = None,
                 short_name: str = None,
                 full_name: str = None,
                 description: str = None,
                 year: int = None,
                 link=None,
                 resource_stats=None,
                 authors: list = None,
                 nlp_tasks: list = None) -> None:

        super().__init__(id, "dataset")

        self.short_name = short_name
        self.full_name = full_name
        self.description = description
        self.year = year
        self.link = link
        self.resource_stats = resource_stats
        self.authors = authors
        self.nlp_tasks = nlp_tasks

    def serialize(self) -> dict:
        return {
            "id": self._id,
            "short_name": self.short_name,
            "full_name": self.full_name,
            "description": self.description,
            "year": self.year,
            "link": self.link.serialize() if self.link else None,
            "resource_stats": self.resource_stats.serialize() if self.resource_stats else None,
            "authors": [author.serialize() for author in self.authors] if self.authors else None,
            "nlp_tasks": [nlp_task.serialize() for nlp_task in self.nlp_tasks] if self.nlp_tasks else None
        }

    def deserialize(self, response: Response):
        self._id = response.json().get("id")
        self.short_name = response.json().get("short_name")
        self.full_name = response.json().get("full_name")
        self.description = response.json().get("description")
        self.year = response.json().get("year")
        
        self.link = self.link.deserialize(response.json().get("link"))

        self.resource_stats = [resource_stat.deserialize(
            resource_stat) for resource_stat in response.json().get("resource_stats")]

        self.authors = [author.deserialize(author)
                        for author in response.json().get("authors")]

        self.nlp_tasks = [nlp_task.deserialize(nlp_task)
                          for nlp_task in response.json().get("nlp_tasks")]

    """
    # TODO: Remove the Need for .index()
    @property
    def id(self):
        if self._id is None and self._json.get("short_name"):
            for dataset in self.index().json():
                if dataset.get("short_name") == self._json.get("short_name"):
                    self._id = dataset.get("id")
                    break

        return self._id
    """
