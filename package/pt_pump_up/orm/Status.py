from pydantic import BaseModel

class Status(BaseModel):
    broken_link: bool
    author_response: bool
    standard_format: bool
    backup: bool
    preservation_rating: int
    off_the_shelf: bool