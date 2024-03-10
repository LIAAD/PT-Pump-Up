from pt_pump_up_admin.CRUD import CRUD


class Result(CRUD):
    def __init__(self, identifier: int = None) -> None:
        super().__init__("result", identifier)

    def store(self, metric, value,
              train_dataset_id,
              validation_dataset_id,
              test_dataset_id):

        base_request = super().store()

        base_request.json = {
            "metric": metric,
            "value": value,
            "train_dataset_id": train_dataset_id,
            "validation_dataset_id": validation_dataset_id,
            "test_dataset_id": test_dataset_id
        }

        self.json = base_request.json

        return base_request
