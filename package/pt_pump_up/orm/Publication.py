from beanie import Document
from typing import Optional


class Publication(Document):
    name: str
    doi: Optional[str] = None
    bibtex: Optional[str] = None
