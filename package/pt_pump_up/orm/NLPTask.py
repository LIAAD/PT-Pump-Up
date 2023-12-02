from beanie import Document
from typing import List


class NLPTask(Document):
    name: str
    acronym: str
    papers_with_code_ids: List[int]
