
from pt_pump_up_admin.crud.Crud import Crud


class Dataset(Crud):
    def __init__(self, pt_pump_up) -> None:
        super().__init__(pt_pump_up, "api/datasets")

    def insert(self,
               english_name: str,
               description: str,
               year: int,
               link_source: str,
               broken_link: bool,
               author_response: bool,
               standard_format: bool,
               backup: bool,
               off_the_shelf: bool,
               authors: list,
               nlp_tasks: list,
               language_stats: list,
               **kwargs
               ):

        data = {
            "english_name": english_name,
            "full_portuguese_name": kwargs.get("full_portuguese_name", None),
            "description": description,
            "year": year,
            "hrefs": {
                "link_source": link_source,
                "link_papers_with_code": kwargs.get("link_papers_with_code", None),
                "link_hf": kwargs.get("link_hf", None),
                "doi": kwargs.get("doi", None),
            },
            "dataset_stats": {
                "broken_link": broken_link,
                "author_response": author_response,
                "standard_format": standard_format,
                "backup": backup,
                "off_the_shelf": off_the_shelf,
            },
            "authors": authors,
            "nlp_tasks": nlp_tasks,
            "language_stats": language_stats,
        }

        return self.send_post_request(data)

    def delete(self, id, **kwargs):
        pass

    def update(self, id, **kwargs):
        pass

    def get(self, id, **kwargs):
        pass
