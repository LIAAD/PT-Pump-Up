from typing import Optional, TypedDict
from beanie import Document, Link
from License import License
from enum import Enum
from Language import Language
from utils.DatasetStats import DatasetStats
from Author import Author
from utils.Conference import Conference


class Status(Enum):
    BROKEN_LINK = 1
    READY = 2


class Hrefs(TypedDict):
    link_hf: Optional[str]
    link_source: str
    doi: Optional[str]


class Dataset(Document):
    name: str
    hrefs: Hrefs
    conference: Optional[Conference]
    year: Optional[int]
    license: Link[License]
    # Status is an Enum
    status: Status
    languages: list[Link[Language]]
    global_stats: DatasetStats
    authors: list[Link[Author]]
