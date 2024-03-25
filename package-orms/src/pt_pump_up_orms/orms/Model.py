from pt_pump_up_orms import ORM
from requests import Response


class Model(ORM):
    def __init__(self,
                 id: int = None,
                 short_name: str = None,
                 full_name: str = None,
                 description: str = None,
                 year: int = None,
                 authors: list = None,
                 nlp_tasks: list = None,
                 link=None,
                 resource_stats=None,
                 results: list = None) -> None:

        super().__init__(id, 'machine-learning-model')

        self.short_name = short_name
        self.full_name = full_name
        self.description = description
        self.year = year
        self.authors = authors
        self.nlp_tasks = nlp_tasks
        self.link = link
        self.resource_stats = resource_stats
        self.results = results

    def serialize(self) -> dict:
        return {
            "id": self._id,
            "short_name": self.short_name,
            "full_name": self.full_name,
            "description": self.description,
            "year": self.year,
            "authors": [author.serialize() for author in self.authors] if self.authors else None,
            "nlp_tasks": [nlp_task.serialize() for nlp_task in self.nlp_tasks] if self.nlp_tasks else None,
            "link": self.link.serialize() if self.link else None,
            "resource_stats": self.resource_stats.serialize() if self.resource_stats else None,
            "results": [result.serialize() for result in self.results] if self.results else None
        }

    def deserialize(self, response: Response):
        self._id = response.json().get("id")
        self.short_name = response.json().get("short_name")
        self.full_name = response.json().get("full_name")
        self.description = response.json().get("description")
        self.year = response.json().get("year")

        self.authors = [author.deserialize(author)
                        for author in response.json().get("authors")]

        self.nlp_tasks = [nlp_task.deserialize(nlp_task)
                          for nlp_task in response.json().get("nlp_tasks")]

        self.link = self.link.deserialize(response.json().get("link"))

        self.resource_stats = self.resource_stats.deserialize(
            response.json().get("resource_stats"))

        self.results = [result.deserialize(result)
                        for result in response.json().get("results")]
