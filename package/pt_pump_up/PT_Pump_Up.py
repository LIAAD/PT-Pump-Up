import pandas as pd
import requests
import logging
from datasets import load_dataset as load_hf_dataset


class PTPumpUp:
    def __init__(self):
        self.url = "http://pt-pump-up.inesctec.pt/"
        self.datasets = None
        self.models = None

    def fetch_data(self, endpoint, element, use_cache, nlp_task):
        if element is not None and use_cache:
            logging.info(f"Using cached")
            return element

        response = requests.get(f"{self.url}/api/{endpoint}/")

        if response.status_code != 200:
            raise Exception(f"Error while fetching")

        data = response.json()

        if nlp_task != "all":
            data = [elem for elem in data if any(
                task["name"] == nlp_task or task["acronym"] == nlp_task for task in elem["nlp_tasks"])]

        element = pd.DataFrame(data=data)
        element.set_index("id", inplace=True)

        return element

    def all_datasets(self, nlp_task="all", use_cache=True):
        self.datasets = self.fetch_data(
            "datasets", self.datasets, use_cache, nlp_task)
        return self.datasets

    def all_models(self, nlp_task="all", use_cache=True):
        self.models = self.fetch_data(
            "models", self.models, use_cache, nlp_task)
        return self.models

    def load_dataset(self, dataset_id, use_cache=True):
        if self.datasets is None or not use_cache:
            self.all_datasets()

        dataset = self.datasets.loc[dataset_id]

        if dataset is None:
            raise Exception("Dataset not found")

        if dataset['hrefs']['link_hf'] is None:
            raise Exception("Dataset not found in HuggingFace")

        dataset_name = dataset['hrefs']['link_hf'].split('/')[-1]

        return load_hf_dataset(dataset_name)
