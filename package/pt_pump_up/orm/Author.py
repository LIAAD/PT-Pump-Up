from beanie import Document
from typing import Optional
from pydantic import BaseModel


class Hrefs(BaseModel):
    email: str
    website: Optional[str] = None
    orcid: Optional[str] = None
    github: Optional[str] = None
    twitter: Optional[str] = None
    google_scholar: Optional[str] = None
    linkedin: Optional[str] = None


class Author(Document):
    name: str
    affiliation: str
    hrefs: Hrefs
