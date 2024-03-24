from pt_pump_up_orms import ORM
from requests import Response


class NLPTask(ORM):
    def __init__(self,
                 id: int = None,
                 short_name: str = None,
                 full_name: str = None,
                 standard_format: str = None,
                 description: str = None,
                 papers_with_code_ids: list = None) -> None:

        super().__init__(id, "nlp-task")

        self.short_name = short_name
        self.full_name = full_name
        self.standard_format = standard_format
        self.description = description
        self.papers_with_code_ids = papers_with_code_ids

    def serialize(self) -> dict:
        return {
            "id": self._id,
            "short_name": self.short_name,
            "full_name": self.full_name,
            "standard_format": self.standard_format,
            "description": self.description,
            "papers_with_code_ids": self.papers_with_code_ids
        }

    def deserialize(self, response: Response):
        self._id = response.json().get("id")
        self.short_name = response.json().get("short_name")
        self.full_name = response.json().get("full_name")
        self.standard_format = response.json().get("standard_format")
        self.description = response.json().get("description")
        self.papers_with_code_ids = response.json().get("papers_with_code_ids")
