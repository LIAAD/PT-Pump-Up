from beanie import Document
from typing import Optional, List
from pt_pump_up.orm.Author import Author
from pt_pump_up.orm.Conference import Conference
from beanie import Link


class Publication(Document):
    title: str
    abstract: str
    authors: List[Link[Author]]
    url_abstract: Optional[str] = None
    url_pdf: str
    published_date: str
    journal_or_conference: Optional[Link[Conference]] = None
    github_url: Optional[str] = None
    doi: Optional[str] = None
    bibtex: Optional[str] = None
