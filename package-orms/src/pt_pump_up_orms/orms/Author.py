from requests import Response
from pt_pump_up_orms import ORM
from pt_pump_up_orms.orms import Link


class Author(ORM):
    def __init__(self,
                 id: int = None,
                 name: str = None,
                 institution: str = None,
                 link: Link = None) -> None:

        super().__init__(id, "author")

        self.name = name
        self.institution = institution
        self.link = link

    def serialize(self) -> dict:
        return {
            "id": self._id,
            "name": self.name,
            "institution": self.institution,
            "link": self.link.serialize() if self.link else None
        }

    def deserialize(self, response: Response):
        self._id = response.json().get("id")
        self.name = response.json().get("name")
        self.institution = response.json().get("institution")
        self.link = Link().deserialize(response.json().get("link"))
