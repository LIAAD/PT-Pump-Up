from beanie import Document
from typing import Optional
from typing_extensions import TypedDict
from utils.DatasetStats import DatasetStats


# TODO: Integrate Python Library for ISO 639-1


class Language(Document):
    name: str
    iso_code: str
    percentage_of_dataset: Optional[float]
    language_stats: Optional[DatasetStats]
