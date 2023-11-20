from beanie import Document
from typing import Optional


class Hrefs(Document):
    website: Optional[str] = None
    orcid: Optional[str] = None
    github: Optional[str] = None
    twitter: Optional[str] = None
    google_scholar: Optional[str] = None
    linkedin: Optional[str]= None


class Author(Document):
    name: str
    affiliation: str
    email: str
    #hrefs: Optional[Hrefs] = None
