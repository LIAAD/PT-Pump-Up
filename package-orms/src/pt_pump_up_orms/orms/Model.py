from pt_pump_up_orms import ORM
from pt_pump_up_orms.orms import Link
from pt_pump_up_orms.orms import ResourceStats


class Model(ORM):
    def __init__(self,
                 id: int = None,
                 short_name: str = None,
                 full_name: str = None,
                 description: str = None,
                 year: int = None,
                 authors: list = None,
                 nlp_tasks: list = None,
                 link: Link = None,
                 resource_stats: ResourceStats = None,
                 results: list = None) -> None:

        super().__init__('machine-learning-model',
                         id=id,
                         short_name=short_name,
                         full_name=full_name,
                         description=description,
                         year=year,

                         author_emails=[author.json['link']['email']
                                        for author in authors] if authors else None,

                         nlp_tasks_short_names=[
                             nlp_task.json['short_name'] for nlp_task in nlp_tasks] if nlp_tasks else None,

                         link=link.json if link else None,
                         resource_stats=resource_stats.json if resource_stats else None,
                         results=[result.json for result in results] if results else None)
