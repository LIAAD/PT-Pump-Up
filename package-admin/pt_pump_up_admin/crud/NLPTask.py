from pt_pump_up_admin.crud.Crud import Crud


class NLPTask(Crud):
    def __init__(self, pt_pump_up) -> None:
        super().__init__(pt_pump_up, "api/nlp_tasks")

    def insert(self, name: str, acronym: str, papers_with_code_ids: list):

        data = {
            "name": name,
            "acronym": acronym,
            "papers_with_code_ids": papers_with_code_ids
        }

        return self.send_post_request(data)

    def delete(self, id, **kwargs):
        return self.send_delete_request({"id": id})

    def update(self, id, **kwargs):
        raise NotImplementedError

    def get(self, id, **kwargs):
        raise NotImplementedError
