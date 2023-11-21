from typing import Optional, List
from beanie import Document, Link
from pt_pump_up.orm.License import License
from pt_pump_up.orm.Author import Author
from pt_pump_up.orm.Conference import Conference
from pt_pump_up.orm.NLPTask import NLPTask
from pt_pump_up.orm.Hrefs import Hrefs
from pt_pump_up.orm.Status import Status
from pt_pump_up.orm.Language import Language

from pydantic import BaseModel


class DatasetStats(BaseModel):
    language: Link[Language]
    number_documents: Optional[int] = 0
    number_tokens: Optional[int] = 0
    number_chars: Optional[int] = 0


class Dataset(Document):
    name: str
    language_stats: List[DatasetStats]
    conference: Optional[Link[Conference]] = None
    hrefs: Hrefs
    year: int
    status: Status
    overall_dataset_stats: Optional[DatasetStats] = None
    authors: List[Link[Author]]
    license: Optional[Link[License]] = None
    nlp_task: List[Link[NLPTask]]
