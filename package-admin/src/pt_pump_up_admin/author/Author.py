from pt_pump_up_admin import CRUD


class Author(CRUD):
    def __init__(self, identifier: int = None) -> None:
        super().__init__("author", identifier)

    def store(self, name, institution, link_id):
        base_request = super().store()

        base_request.json = {
            "name": name,
            "institution": institution,
            "link_id": link_id
        }

        self.json = base_request.json

        return base_request
