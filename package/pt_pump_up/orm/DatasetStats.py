from beanie import Document
from typing import Optional


class DatasetStats(Document):
    number_documents: Optional[int] = None
    number_tokens: Optional[int] = None
    number_chars: Optional[int] = None
