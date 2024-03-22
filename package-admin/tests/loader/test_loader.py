import os
from pt_pump_up_admin.loader import Loader
from pt_pump_up_orms import Dataset
from pt_pump_up_orms import Author
from pt_pump_up_orms import Model
from pt_pump_up_orms import NLPTask

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def test_parse():
    loader = Loader(filepath=os.path.join(CURRENT_PATH, "data", "data.json"))

    assert len(loader.parse(submit=False)) > 10


def test_submit_with_all_info():
    loader = Loader(filepath=os.path.join(CURRENT_PATH, "data", "data.json"))

    loader.parse(submit=True)

    nlp_tasks = NLPTask().index().json()
    datasets = Dataset().index().json()
    models = Model().index().json()
    authors = Author().index().json()

    assert len(datasets) == 9
    assert len(models) == 6
    assert len(authors) == 17
    assert len(nlp_tasks) == 5


def test_submit_no_validation_dataset_results():
    loader = Loader(filepath=os.path.join(
        CURRENT_PATH, "data", "data-no-val.json"))

    loader.parse(submit=True)

    models = Model().index().json()

    assert len(models) == 6
