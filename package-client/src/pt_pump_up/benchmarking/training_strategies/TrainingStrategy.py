from abc import ABC, abstractmethod
from transformers import AutoTokenizer


class TrainingStrategy(ABC):
    def __init__(self, model_name) -> None:
        self._model_name = model_name
        self._collator = None
        self._metric = None
        self._model = None
        self._tokenizer = AutoTokenizer.from_pretrained(model_name)

    @abstractmethod
    def prepare_data(self, examples):
        raise NotImplementedError

    @abstractmethod
    def compute_metrics(self, eval_pred):
        raise NotImplementedError

    # Getters and Setters
    @property
    def collator(self):
        if self._collator is None:
            raise Exception("Collator not set")

        return self._collator

    @collator.setter
    def collator(self, collator):
        self._collator = collator

    @property
    def metric(self):
        if self._metric is None:
            raise Exception("Metric not set")

        return self._metric

    @metric.setter
    def metric(self, metric):
        self._metric = metric

    @property
    def tokenizer(self):
        if self._tokenizer is None:
            raise Exception("Tokenizer not set")

        return self._tokenizer

    @tokenizer.setter
    def tokenizer(self, tokenizer):
        self._tokenizer = tokenizer

    @property
    def model(self):
        if self._model is None:
            raise Exception("Model not set")

        return self._model

    @model.setter
    def model(self, model):
        self._model = model
