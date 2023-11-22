from beanie import Document
from typing import Optional

# TODO: Add reference to Platform Pytorch, Tensorflow, Sklearn, etc


class Architecture(Document):
    name: str
    year: Optional[int] = -1
    link_paper: Optional[str] = None
