from beanie import Document


class Conference(Document):
    name: str
    year: int
