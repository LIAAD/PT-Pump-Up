from beanie import Document, Link
from typing import TypedDict, Optional
from utils.Conference import Conference
from Language import Language


class Hrefs(TypedDict):
    link_hf: Optional[str]
    link_source: str
    doi: Optional[str]


class Model(Document):
    name: str
    hrefs: Hrefs
    conference: Optional[Conference]
    year: int
    languages: list[Link[Language]]
