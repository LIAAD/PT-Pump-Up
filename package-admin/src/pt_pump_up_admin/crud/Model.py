from pt_pump_up_admin.crud.Crud import Crud


class Model(Crud):
    def __init__(self, pt_pump_up) -> None:
        super().__init__(pt_pump_up, "api/models")
    
    def insert(self, 
               english_name, 
               description,
               year,
               architecture,
               authors,
               link_source,
               broken_link,
               author_response,
               standard_format,
               backup,
               off_the_shelf,
               nlp_tasks,
               benchmarks,
               **kwargs):
        
        data = {
            "english_name": english_name,
            "description": description,
            "full_portuguese_name": kwargs.get("full_portuguese_name", None),
            "year": year,
            "architecture": architecture,
            "authors": authors,
            "nlp_tasks": nlp_tasks,
            "hrefs": {
                "link_source": link_source,
                "link_papers_with_code": kwargs.get("link_papers_with_code", None),
                "link_hf": kwargs.get("link_hf", None),
                "doi": kwargs.get("doi", None),
            },
            "model_stats": {
                "broken_link": broken_link,
                "author_response": author_response,
                "standard_format": standard_format,
                "backup": backup,
                "off_the_shelf": off_the_shelf,
            },
            "benchmarks": benchmarks,
        }

        return self.send_post_request(data)

    def delete(self, id, **kwargs):
        raise NotImplementedError

    def update(self, id, **kwargs):
        raise NotImplementedError

    def get(self, id, **kwargs):
        raise NotImplementedError    
               