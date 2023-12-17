from abc import ABC, abstractmethod
from conllu import parse as conllu_parse
import logging
from huggingface_hub import hf_hub_download
from datasets import Dataset as HF_Dataset
from tqdm import tqdm


class Dataset(ABC):
    def __init__(self, repo_id, hf_token=None) -> None:
        super().__init__()
        self.repo_id = repo_id
        self.hf_token = hf_token
        self.hf_dataset = None

    @abstractmethod
    def normalize(self, **kwargs):
        pass

    def download(self, subfolder, filename):
        logging.info(f"Downloading {filename} from {subfolder}")

        local_path = hf_hub_download(
            repo_id=self.repo_id,
            # HuggingFace is Linux based. It is necessary to Force using forward slash To run on Windows Locals
            subfolder=subfolder.replace("\\", "/"),
            filename=filename,
            repo_type="dataset",
            revision="main",
            token=self.hf_token,
        )

        logging.info(f"Downloaded {filename} to {local_path}")

        return local_path

    @abstractmethod
    def parse(self):
        pass

    def push_to_hub(self):
        self.hf_dataset.push_to_hub(
            repo_id=self.repo_id,
            token=self.hf_token,
        )
