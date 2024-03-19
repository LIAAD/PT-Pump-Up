
import json
import traceback
from pt_pump_up_admin.dataset import Dataset
from pt_pump_up_admin.author import Author
from pt_pump_up_admin.link import Link
from pt_pump_up_admin.nlp_task import NLPTask
from pt_pump_up_admin.resource_stats import ResourceStats
from pt_pump_up_admin.model import Model
from pt_pump_up_admin.result import Result
from tqdm import tqdm
from time import sleep


class Loader:
    def __init__(self, filepath):
        self.filepath = filepath

    def _load_nlp_tasks(self, data):
        return [
            NLPTask(
                short_name=nlp_task.get("short_name"),
                full_name=nlp_task.get("full_name"),
                standard_format=nlp_task.get("standard_format"),
                description=nlp_task.get("description"),
                papers_with_code_ids=nlp_task.get("papers_with_code_ids"),
            ) for nlp_task in data.get("nlp_tasks")
        ]

    def _load_datasets(self, data):
        cruds = []

        for dataset in data.get("datasets"):
            authors = [
                Author(
                    name=author.get("name"),
                    institution=author.get("institution"),
                    link=Link(
                        email=author.get("link").get("email"),
                        website=author.get("link").get("website"),
                    )
                ) for author in dataset.get("authors")
            ]

            cruds.extend(authors)

            nlp_tasks = [NLPTask(short_name=nlp_task_short_name)
                         for nlp_task_short_name in dataset.get("nlp_tasks")]

            link = Link(
                hugging_face_url=dataset.get("link").get("hugging_face_url"),
                papers_with_code_url=dataset.get(
                    "link").get("papers_with_code_url"),
                github_url=dataset.get("link").get("github_url"),
                website=dataset.get("link").get("website"),
                paper_url=dataset.get("link").get("paper_url"),
            )

            cruds.append(link)

            resource_stats = ResourceStats(
                standard_format=dataset.get(
                    "resource_stats").get("standard_format"),
                off_the_shelf=dataset.get(
                    "resource_stats").get("off_the_shelf"),
                preservation_rating=dataset.get(
                    "resource_stats").get("preservation_rating"),
            )

            cruds.append(resource_stats)

            dataset = Dataset(
                short_name=dataset.get("short_name"),
                description=dataset.get("description"),
                year=dataset.get("year"),
                authors=authors,
                resource_stats=resource_stats,
                nlp_tasks=nlp_tasks,
                link=link,
            )
            cruds.append(dataset)

        return cruds

    def _load_models(self, data):
        cruds = []

        for model in data.get("models"):
            authors = [
                Author(
                    name=author.get("name"),
                    institution=author.get("institution"),
                    link=Link(
                        email=author.get("link").get("email"),
                        website=author.get("link").get("website"),
                    )
                ) for author in model.get("authors")
            ]

            cruds.extend(authors)

            results = [
                Result(
                    metric=result.get("metric"),
                    value=result.get("value"),
                    train_dataset=Dataset(
                        short_name=result.get("train_dataset")),
                    validation_dataset=Dataset(
                        short_name=result.get("validation_dataset")),
                    test_dataset=Dataset(
                        short_name=result.get("test_dataset")),
                ) for result in model.get("results")
            ]

            nlp_tasks = [NLPTask(short_name=nlp_task_short_name)
                         for nlp_task_short_name in model.get("nlp_tasks")]

            link = Link(
                hugging_face_url=model.get("link").get("hugging_face_url"),
                papers_with_code_url=model.get(
                    "link").get("papers_with_code_url"),
                github_url=model.get("link").get("github_url"),
                website=model.get("link").get("website"),
                paper_url=model.get("link").get("paper_url"),
            )

            cruds.append(link)

            resource_stats = ResourceStats(
                standard_format=model.get(
                    "resource_stats").get("standard_format"),
                off_the_shelf=model.get("resource_stats").get("off_the_shelf"),
                preservation_rating=model.get(
                    "resource_stats").get("preservation_rating"),
            )

            cruds.append(resource_stats)

            model = Model(
                short_name=model.get("short_name"),
                description=model.get("description"),
                year=model.get("year"),
                authors=authors,
                resource_stats=resource_stats,
                nlp_tasks=nlp_tasks,
                link=link,
                results=results
            )

            cruds.append(model)

        return cruds

    def _erase_cruds(self, cruds):
        for crud in cruds:
            try:
                crud.destroy()
            except Exception as e:
                traceback.print_exc()
                print(f"Error deleting {crud}: {e}")

    def _submit(self, cruds):

        for crud in tqdm(cruds):
            response = crud.store()

            if response.status_code < 200 or response.status_code >= 300 and response.status_code != 409:
                print(f"Error submitting {crud}: {response.status_code}")
                # self._erase_cruds(cruds)
                return None
            elif response.status_code == 409:
                print(f"Already exists: {crud}")

            sleep(0.5)

        return True

    def parse(self, submit=False):
        data = json.loads(open(self.filepath, encoding="utf-8").read())

        nlp_tasks = self._load_nlp_tasks(data)

        if submit:
            self._submit(nlp_tasks)

        datasets = self._load_datasets(data)

        if submit:
            self._submit(datasets)

        models = self._load_models(data)

        if submit:
            self._submit(models)

        return nlp_tasks + datasets + models
