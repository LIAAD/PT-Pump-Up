from typing import Optional, List
from beanie import Document, Link
from pt_pump_up.orm.License import License
from pt_pump_up.orm.DatasetStats import DatasetStats
from pt_pump_up.orm.Author import Author
from pt_pump_up.orm.Conference import Conference
from pt_pump_up.orm.NLPTask import NLPTask
from pydantic import BaseModel


class Hrefs(BaseModel):
    link_source: str
    link_hf: Optional[str] = None
    doi: Optional[str] = None


class Status(BaseModel):
    broken_link: bool
    author_response: bool
    standard_format: bool
    backup: bool
    preservation_rating: int
    off_the_shelf: bool


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
    nlp_task: List[Link[NLPTask]]
