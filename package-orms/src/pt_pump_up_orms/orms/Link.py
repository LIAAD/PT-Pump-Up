from pt_pump_up_orms import ORM


class Link(ORM):
    def __init__(self,
                 id: int = None,
                 email: str = None,
                 website: str = None,
                 github_url: str = None,
                 hugging_face_url: str = None,
                 papers_with_code_url: str = None,
                 paper_url: str = None) -> None:

        super().__init__("link",
                         id=id,
                         email=email,
                         website=website,
                         github_url=github_url,
                         hugging_face_url=hugging_face_url,
                         papers_with_code_url=papers_with_code_url,
                         paper_url=paper_url)

        self._email = email
        self._website = website
        self._github_url = github_url
        self._hugging_face_url = hugging_face_url
        self._papers_with_code_url = papers_with_code_url
        self._paper_url = paper_url

    @property
    def papers_with_code_url(self):
        if self._papers_with_code_url is None:
            raise Exception("Papers with Code URL is not set")

        return self._papers_with_code_url

    @papers_with_code_url.setter
    def papers_with_code_url(self, papers_with_code_url):
        self._papers_with_code_url = papers_with_code_url
