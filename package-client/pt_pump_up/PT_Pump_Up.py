from pt_pump_up.utils import fetch_resources
from datasets import load_dataset as load_hf_dataset


class PTPumpUP:
    def __init__(self, url="http://pt-pump-up.inesctec.pt") -> None:
        self.url = url
        self.datasets = None
        self.models = None

    def all_datasets(self, nlp_task="all", use_cache=True):
        datasets = fetch_resources(
            url=self.url, endpoint="datasets", element=self.datasets, nlp_task=nlp_task, use_cache=use_cache)

        return datasets

    def all_models(self, nlp_task="all", use_cache=True):
        self.models = fetch_resources(
            url=self.url, endpoint="models", element=self.models, nlp_task=nlp_task, use_cache=use_cache)

        return self.models

    def load_dataset(self, dataset_name, use_cache=True):
        datasets = fetch_resources(
            url=self.url, endpoint="datasets", element=self.datasets, use_cache=use_cache)

        dataset = datasets.loc[dataset_name]

        if dataset is None:
            raise Exception("Dataset not found")

        if dataset['hrefs']['link_hf'] is None:
            raise Exception("Dataset not found in HuggingFace")

        dataset_name = dataset['hrefs']['link_hf'].split('/')[-1]

        return load_hf_dataset(dataset_name)
