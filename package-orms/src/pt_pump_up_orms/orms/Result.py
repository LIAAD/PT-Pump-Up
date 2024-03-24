from pt_pump_up_orms.ORM import ORM
from pt_pump_up_orms.orms import Dataset
from requests import Response


class Result(ORM):
    def __init__(self,
                 id: int = None,
                 metric: str = None,
                 value: float = None,
                 train_dataset: Dataset = None,
                 validation_dataset: Dataset = None,
                 test_dataset: Dataset = None,
                 ) -> None:

        super().__init__(id, "result")

        self.metric = metric
        self.value = value
        self.train_dataset = train_dataset
        self.validation_dataset = validation_dataset
        self.test_dataset = test_dataset

    def serialize(self) -> dict:
        return {
            "id": self._id,
            "metric": self.metric,
            "value": self.value,
            "train_dataset": self.train_dataset.serialize() if self.train_dataset else None,
            "validation_dataset": self.validation_dataset.serialize() if self.validation_dataset else None,
            "test_dataset": self.test_dataset.serialize() if self.test_dataset else None
        }

    def deserialize(self, response: Response):
        self._id = response.json().get("id")
        self.metric = response.json().get("metric")
        self.value = response.json().get("value")
        self.train_dataset = Dataset().deserialize(
            response.json().get("train_dataset"))
        self.validation_dataset = Dataset().deserialize(
            response.json().get("validation_dataset"))
        self.test_dataset = Dataset().deserialize(response.json().get("test_dataset"))
