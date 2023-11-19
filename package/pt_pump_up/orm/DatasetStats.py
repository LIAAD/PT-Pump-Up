from beanie import Document
from typing import Optional
from pt_pump_up.orm.Language import Language
from beanie import Link


class DatasetStats(Document):
    language: Link[Language]
    number_documents: Optional[int] = 0
    number_tokens: Optional[int] = 0
    number_chars: Optional[int] = 0
