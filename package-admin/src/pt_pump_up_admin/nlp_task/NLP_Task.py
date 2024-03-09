from pt_pump_up_admin import CRUD
import requests
import json


class NLPTask(CRUD):
    def __init__(self, identifier: int = None) -> None:
        super().__init__(route="nlp-task", identifier=identifier)

    def index(self):
        return super().index()

    def show(self, identifier: int = None):
        return super().show(identifier=identifier)

    def delete(self, identifier: int = None):
        return super().delete(identifier=identifier)

    def store(self, short_name: str, papers_with_code_ids: list, identifier: int = None, full_name: str = None, description: str = None):
        base_request = super().store()

        base_request.json = {
            "short_name": short_name,
            "full_name": full_name,
            "description": description,
            "papers_with_code_ids": json.dumps(papers_with_code_ids)
        }

        return base_request

    def update(self, identifier):
        pass
