import pandas as pd
from abc import ABC, abstractmethod
from huggingface_hub import hf_hub_download
from huggingface_hub.utils import EntryNotFoundError
from huggingface_hub.hf_api import upload_file
import pickle
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import traceback


class PreservationRating(ABC):
    def __init__(self, hf_repo, hf_path, hf_token) -> None:
        self.hf_repo = hf_repo
        self.hf_token = hf_token
        self.hf_path = hf_path
        try:
            self._clf = self.load_clf()
        except EntryNotFoundError:
            traceback.print_exc()
            self._clf = self.create_clf()

    def create_clf(self) -> None:
        self.clf = DecisionTreeClassifier()

        self.save_clf(commit_msg="Initial commit")

        return self.clf

    def load_clf(self) -> None:

        downloaded_path = hf_hub_download(
            repo_id=self.hf_repo,
            filename=self.hf_path,
            token=self.hf_token
        )

        with open(downloaded_path, 'rb') as f:
            clf = pickle.load(f)

        return clf

    def train(self, data: pd.DataFrame) -> None:
        X, y = self.preprocess(data)

        self.clf.fit(X, y)

        self.save_clf()

    def predict(self, data: pd.DataFrame) -> str:
        X, _ = self.preprocess(data)

        output = self.clf.predict(X)

        return self.post_process(output)

    def save_clf(self, commit_msg: str = "Rating model update") -> None:
        return upload_file(
            path_or_fileobj=self.clf,
            path_in_repo=self.hf_path,
            repo_id=self.hf_repo,
            token=self.hf_token,
            commit_message=commit_msg
        )

    @abstractmethod
    def preprocess(self, data: pd.DataFrame) -> tuple:
        raise NotImplementedError

    @abstractmethod
    def postprocess(self, X: np.array) -> np.array:
        raise NotImplementedError

    # Getters and Setters
    @property
    def clf(self):
        if self._clf is None:
            raise Exception('Classifier not set')

        return self._clf
