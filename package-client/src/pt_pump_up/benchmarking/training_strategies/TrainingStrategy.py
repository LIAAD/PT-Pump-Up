from abc import ABC, abstractmethod
from transformers import AutoTokenizer


class TrainingStrategy(ABC):
    def __init__(self, model_name, label_names, metric_for_best_model) -> None:
        self._model_name = model_name
        self._collator = None
        self._metric = None
        self._model = None
        self._tokenizer = AutoTokenizer.from_pretrained(
            model_name, add_prefix_space=True)
        self._label_names = label_names
        self._metric_for_best_model = metric_for_best_model

        if label_names is not None:
            self.id2label = {i: label for i, label in enumerate(label_names)}
            self.label2id = {v: k for k, v in self.id2label.items()}

    @abstractmethod
    def prepare_data(self, examples, **kwargs):
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

    @property
    def label_names(self):
        return self._label_names

    @label_names.setter
    def label_names(self, label_names):
        self._label_names = label_names

    @property
    def metric_for_best_model(self):
        return self._metric_for_best_model

    @metric_for_best_model.setter
    def metric_for_best_model(self, metric_for_best_model):
        self._metric_for_best_model = metric_for_best_model
