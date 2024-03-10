from pt_pump_up_admin import CRUD


class NLPTask(CRUD):
    def __init__(self, identifier: int = None) -> None:
        super().__init__(route="nlp-task", identifier=identifier)

    def store(self,
              short_name: str,
              papers_with_code_ids: list,
              standard_format: str,
              full_name: str = None,
              description: str = None):
        base_request = super().store()

        base_request.json = {
            "short_name": short_name,
            "full_name": full_name,
            "standard_format": standard_format,
            "description": description,
            "papers_with_code_ids": papers_with_code_ids
        }

        return base_request

    def update(self, identifier):
        raise NotImplementedError(
            "Update method is not implemented for NLP Task")
