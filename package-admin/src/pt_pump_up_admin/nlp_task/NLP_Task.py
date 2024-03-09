from pt_pump_up_admin import CRUD


class NLPTask(CRUD):
    def __init__(self, short_name: str, papers_with_code_ids: list, id: int = None, full_name: str = None, description: str = None) -> None:
        super().__init__(route="/nlp_task", id=id)
        self.short_name = short_name
        self.full_name = full_name
        self.description = description
        self.papers_with_code_ids = papers_with_code_ids

    def index(self):
        return super().index()

    def show(self):
        return super().show()

    def delete(self):
        return super().delete()

    def create(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass
