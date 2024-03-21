from pt_pump_up_admin.crud.CRUD import CRUD
from pt_pump_up_admin.dataset import Dataset


class Result(CRUD):
    def __init__(self,
                 id: int = None,
                 metric: str = None,
                 value: float = None,
                 train_dataset: Dataset = None,
                 validation_dataset: Dataset = None,
                 test_dataset: Dataset = None,
                 ) -> None:

        super().__init__("result",
                         id=id,
                         metric=metric,
                         value=value,
                         train_dataset_id=train_dataset.id if train_dataset else None,
                         validation_dataset_id=validation_dataset.id if validation_dataset else None,
                         test_dataset_id=test_dataset.id if test_dataset else None)
