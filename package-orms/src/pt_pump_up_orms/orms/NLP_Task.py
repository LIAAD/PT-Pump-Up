from pt_pump_up_orms import ORM

class NLPTask(ORM):
    def __init__(self,
                 id: int = None,
                 short_name: str = None,
                 full_name: str = None,
                 standard_format: str = None,
                 description: str = None,
                 papers_with_code_ids: list = None) -> None:

        super().__init__(route="nlp-task",
                         id=id,
                         short_name=short_name,
                         full_name=full_name,
                         standard_format=standard_format,
                         description=description,
                         papers_with_code_ids=papers_with_code_ids)