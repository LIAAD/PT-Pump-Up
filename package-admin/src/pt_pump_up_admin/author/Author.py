from pt_pump_up_admin import CRUD


class Author(CRUD):
    def __init__(self, identifier: int = None) -> None:
        super().__init__("author", identifier)

    def store(self, name, institution, link):
        base_request = super().store()

        if link.identifier is None and link.json is None:
            raise ValueError("Link must be created before author")
        elif link.identifier is not None and link.json is not None:
            raise ValueError(
                "Link cannot have both identifier and json fields filled in. It must be one or the other.")

        base_request.json = {
            "name": name,
            "institution": institution,
            "link_id": link.identifier,
            "link": link.json
        }

        self.json = base_request.json

        return base_request
