from typing import Optional
from pydantic import BaseModel


class Hrefs(BaseModel):
    link_source: str
    link_hf: Optional[str] = None
    doi: Optional[str] = None