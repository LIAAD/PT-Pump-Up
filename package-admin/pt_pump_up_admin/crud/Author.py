from pt_pump_up_admin.crud.Crud import Crud


class Author(Crud):
    def __init__(self, pt_pump_up) -> None:
        super().__init__(pt_pump_up, "api/authors")

    def insert(self, name: str, affiliation: str, email: str, **kwargs):
        data = {
            "name": name,
            "affiliation": affiliation,
            "hrefs": {
                "email": email,
                "website": kwargs.get("website", None),
                "orcid": kwargs.get("orcid", None),
                "github": kwargs.get("github", None),
                "twitter": kwargs.get("twitter", None),
                "googleScholar": kwargs.get("googleScholar", None),
                "linkedin": kwargs.get("linkedin", None)
            }
        }

        return self.send_post_request(data)

    def delete(self, id, **kwargs):
        raise NotImplementedError

    def update(self, id, **kwargs):
        raise NotImplementedError

    def get(self, id, **kwargs):
        raise NotImplementedError
