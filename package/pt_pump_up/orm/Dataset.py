from typing_extensions import TypedDict
from typing import Optional, List
from beanie import Document, Link, WriteRules
from enum import Enum
from pydantic import BaseModel
from pt_pump_up.orm.License import License
from pt_pump_up.orm.Language import Language
from pt_pump_up.orm.DatasetStats import DatasetStats
from pt_pump_up.orm.Author import Author
from pt_pump_up.orm.Conference import Conference


class Status(Enum):
    BROKEN_LINK = 1
    READY = 2


class Hrefs(BaseModel):
    link_source: str
    link_hf: Optional[str] = None
    doi: Optional[str] = None


class Dataset(Document):
    name: str
    languages: List[Link[Language]]
    conference: Optional[Link[Conference]] = None
    hrefs: Hrefs
    year: int
    # Status is an Enum
    status: Status
    overall_dataset_stats: Optional[DatasetStats] = None
    authors: List[Link[Author]]
    license: Optional[Link[License]] = []