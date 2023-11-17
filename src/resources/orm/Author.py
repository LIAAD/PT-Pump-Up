from beanie import Document
from typing import TypedDict


class Hrefs(TypedDict):
    website: str
    orcid: str
    github: str
    twitter: str
    google_scholar: str
    linkedin: str


class Author(Document):
    name: str
    affiliation: str
    email: str
    hrefs: Hrefs
