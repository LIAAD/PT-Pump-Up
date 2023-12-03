from beanie import Document


# TODO: Integrate Python Library for ISO 639-1

class Language(Document):
    name: str
    iso_code: str
    papers_with_code_ids: int
