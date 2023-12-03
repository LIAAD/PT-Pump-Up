import pandas as pd
import requests
import logging
from datasets import load_dataset as load_hf_dataset

class PTPumpUp:
    def __init__(self):
        self.url = "http://pt-pump-up.inesctec.pt/"
        self.datasets = None
        self.models = None

    def all_datasets(self, use_cache=True):
        if self.datasets is not None and use_cache:
            logging.info("Using cached datasets")
            return self.datasets

        response = requests.get(f"{self.url}/api/datasets/")

        if response.status_code != 200:
            raise Exception("Error while fetching datasets")

        self.datasets = pd.DataFrame(data=response.json())

        self.datasets.set_index("id", inplace=True)

        return self.datasets

    def all_models(self, use_cache=True):

        if self.models is not None and use_cache:
            logging.info("Using cached models")
            return self.models

        response = requests.get(f"{self.url}/api/models/")

        if response.status_code != 200:
            raise Exception("Error while fetching models")

        self.models = pd.DataFrame(data=response.json())

        self.models.set_index("id", inplace=True)

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
