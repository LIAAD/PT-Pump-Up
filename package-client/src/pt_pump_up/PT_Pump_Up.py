from pt_pump_up.utils import fetch_resources
from datasets import load_dataset as load_hf_dataset
from transformers import AutoModel


class PTPumpUpClient:
    def __init__(self, url="https://pt-pump-up.inesctec.pt") -> None:
        self.url = url
        self.datasets = None
        self.models = None
        self.nlp_tasks = None

    # TODO: Add a method to fetch all NLP tasks
    def all_nlp_tasks(self, use_cache=True):
        nlp_tasks = fetch_resources(
            url=self.url, endpoint="nlp-task", element=self.nlp_tasks, use_cache=use_cache)

        return nlp_tasks

    def all_datasets(self, nlp_task="all", use_cache=True):
        datasets = fetch_resources(
            url=self.url, endpoint="dataset", element=self.datasets, nlp_task=nlp_task, use_cache=use_cache)

        return datasets

    def all_models(self, nlp_task="all", use_cache=True):
        self.models = fetch_resources(
            url=self.url, endpoint="machine-learning-model", element=self.models, nlp_task=nlp_task, use_cache=use_cache)

        return self.models

    def load_dataset(self, dataset_name, use_cache=True):
        datasets = fetch_resources(
            url=self.url, endpoint="dataset", element=self.datasets, use_cache=use_cache)

        datasets.set_index('short_name', inplace=True)

        dataset = datasets.loc[dataset_name]

        if dataset is None:
            raise Exception("Dataset not found")

        if dataset['link']['hugging_face_url'] is None:
            raise Exception("Dataset not found in HuggingFace")

        dataset_name = dataset['link']['hugging_face_url'].split(
            "datasets/")[1]

        return load_hf_dataset(dataset_name)

    def load_model(self, model_name, use_cache=True):
        models = fetch_resources(
            url=self.url, endpoint="machine-learning-model", element=self.models, use_cache=use_cache)

        models.set_index('short_name', inplace=True)

        model = models.loc[model_name]

        if model is None:
            raise Exception("Model not found")

        if model['link']['hugging_face_url'] is None:
            raise Exception("Model not found in HuggingFace")

        model_name = model['link']['hugging_face_url'].split(
            "huggingface.co/")[1]

        return AutoModel.from_pretrained(model_name)
