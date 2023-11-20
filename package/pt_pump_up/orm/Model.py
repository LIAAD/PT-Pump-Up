from beanie import Document, Link
from typing_extensions import TypedDict
from typing import Optional, List
from pt_pump_up.orm.Conference import Conference
from pt_pump_up.orm.Language import Language


class Hrefs(TypedDict):
    link_hf: Optional[str]
    link_source: str
    doi: Optional[str]


class Model(Document):
    name: str
    hrefs: Hrefs
    conference: Optional[Conference]
    year: int
    languages: List[Link[Language]]
