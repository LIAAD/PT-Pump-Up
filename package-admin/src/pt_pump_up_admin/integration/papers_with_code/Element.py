
from abc import ABC, abstractmethod
from pt_pump_up_admin.integration import PapersWithCode
from mechanize import Browser


class Element(ABC):
    def __init__(self, post_url: str, br: Browser = None) -> None:
        super().__init__()
        self._br = br if br else PapersWithCode.create()
        self._post_url = post_url

    @abstractmethod
    def insert(self):
        pass

    @property
    def br(self):
        if self._br is None:
            raise Exception('Browser not set')
        return self._br

    @property
    def post_url(self):
        if self._post_url is None:
            raise Exception('Post URL not set')
        return self._post_url
