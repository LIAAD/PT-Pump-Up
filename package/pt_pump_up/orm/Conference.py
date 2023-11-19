from beanie import Document
from typing import Optional


class Conference(Document):
    name: str
    year: int
    link: Optional[str] = None
