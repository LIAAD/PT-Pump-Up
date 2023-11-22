from beanie import Document, Link
from typing import Optional, List
from pt_pump_up.orm.Conference import Conference
from pt_pump_up.orm.Language import Language
from pydantic import BaseModel
from pt_pump_up.orm.Hrefs import Hrefs
from pt_pump_up.orm.Status import Status
from pt_pump_up.orm.Author import Author
from pt_pump_up.orm.License import License
from pt_pump_up.orm.Architecture import Architecture
from pt_pump_up.orm.NLPTask import NLPTask
from pt_pump_up.orm.Dataset import Dataset
from pt_pump_up.orm.Metric import Metric

# Association table to Keep track of a finite set of metrics


class MetricResult(BaseModel):
    metric: Link[Metric]
    value: float


class Benchmark(BaseModel):
    train_dataset: Link[Dataset]
    test_dataset: Link[Dataset]
    scores: List[MetricResult]


class ModelStats(BaseModel):
    languages: List[Link[Language]]
    architecture: Link[Architecture]
    number_parameters: Optional[int] = 0
    size_MB: Optional[int] = 0


class Model(Document):
    name: str
    model_stats: ModelStats
    conference: Optional[Conference] = None
    hrefs: Hrefs
    year: int
    status: Status
    authors: List[Link[Author]]
    license: Optional[Link[License]] = None
    benchmarks: List[Benchmark]
    nlp_tasks: List[Link[NLPTask]]
