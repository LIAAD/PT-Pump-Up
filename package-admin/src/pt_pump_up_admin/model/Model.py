from pt_pump_up_admin import CRUD
from requests import Request


class Model(CRUD):
    def __init__(self, identifier: int = None) -> None:
        super().__init__('machine-learning-model', identifier)

    def store(self, short_name: str,
              year: int,
              full_name: str = None,
              description: str = None,
              website_url: str = None,
              github_url: str = None,
              paper_url: str = None,
              huging_face_url: str = None,
              papers_with_code_url: str = None) -> Request:
        
        base_request = super().store()

        base_request.json = {
            "short_name": short_name,
            "full_name": full_name,
            "description": description,
            "year": year,
        }
