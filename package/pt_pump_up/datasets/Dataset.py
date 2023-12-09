from abc import ABC, abstractmethod
from huggingface_hub import hf_hub_download
import os
import logging
from datasets import Dataset as HFDataset


class Dataset(ABC):
    def __init__(self, repo_id, filepath, filename, hf_token=None) -> None:

        if hf_token is None:
            logging.warning("No huggingface token provided.")

        self.hf_token = hf_token
        self.repo_id = repo_id
        self.filepath = filepath
        self.filename = filename

    def download(self):
        logging.info("Downloading dataset from HuggingFace Hub")

        path = hf_hub_download(
            repo_id=self.repo_id,
            subfolder=self.filepath,
            filename=self.filename,
            repo_type="dataset",
            revision="main",
        )

        logging.info(f"Dataset downloaded successfully | Path: {path}")

        return path

    @abstractmethod
    def standardize(self):
        pass

    def publish(self, dataset: HFDataset):
        logging.info("Publishing dataset to HuggingFace Hub")

        dataset.push_to_hub(repo_id=self.repo_id, token=self.hf_token)
