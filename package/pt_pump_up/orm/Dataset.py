from typing import Optional, List
from beanie import Document, Link
from enum import Enum
from pydantic import BaseModel
from pt_pump_up.orm.License import License
from pt_pump_up.orm.DatasetStats import DatasetStats
from pt_pump_up.orm.Author import Author
from pt_pump_up.orm.Conference import Conference
from pt_pump_up.orm.NLPTask import NLPTask


class Status(Enum):
    BROKEN_LINK = 1
    READY = 2

# TODO: Change From BaseModel to Document


class Hrefs(BaseModel):
    link_source: str
    link_hf: Optional[str] = None
    doi: Optional[str] = None


class Dataset(Document):
    name: str
    language_stats: List[DatasetStats]
    conference: Optional[Link[Conference]] = None
    hrefs: Hrefs
    year: int
    # Status is an Enum
    status: Status
    overall_dataset_stats: Optional[DatasetStats] = None
    authors: List[Link[Author]]
    license: Optional[Link[License]] = None
    nlp_task: Link[NLPTask]
