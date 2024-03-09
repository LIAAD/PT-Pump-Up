from pt_pump_up_admin import CRUD


class Link(CRUD):
    def __init__(self, identifier: int = None) -> None:
        super().__init__("link", identifier)

    def store(self,
              email: str = None,
              website: str = None,
              github_url: str = None,
              hugging_face_url: str = None,
              papers_with_code_url: str = None,
              paper_url: str = None):

        base_request = super().store()

        base_request.json = {
            "email": email,
            "website": website,
            "github_url": github_url,
            "hugging_face_url": hugging_face_url,
            "papers_with_code_url": papers_with_code_url,
            "paper_url": paper_url
        }

        return base_request
