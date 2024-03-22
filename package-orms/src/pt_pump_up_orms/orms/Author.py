from pt_pump_up_orms import ORM
from pt_pump_up_orms.orms import Link


class Author(ORM):
    def __init__(self,
                 id: int = None,
                 name: str = None,
                 institution: str = None,
                 link: Link = None) -> None:

        super().__init__("author",
                         id=id,
                         name=name,
                         institution=institution,
                         link=link.json if link else None)
