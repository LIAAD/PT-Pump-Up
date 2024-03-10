from pt_pump_up import PTPumpUpClient
import pytest


@pytest.fixture
def fixture_pt_pump_up_client():
    return PTPumpUpClient(url="http://localhost:8000")


def test_all_nlp_tasks(fixture_pt_pump_up_client):
    client = fixture_pt_pump_up_client

    nlp_tasks = client.all_nlp_tasks()

    assert nlp_tasks is not None

    assert len(nlp_tasks) > 0


def test_all_datasets(fixture_pt_pump_up_client):
    client = fixture_pt_pump_up_client

    datasets = client.all_datasets()

    assert datasets is not None

    assert len(datasets) > 0


def test_all_models(fixture_pt_pump_up_client):
    client = fixture_pt_pump_up_client

    models = client.all_models()

    assert models is not None

    assert len(models) > 0


def test_load_dataset(fixture_pt_pump_up_client):
    pass

# TODO: Add transformers to the requirements


def test_load_model():
    pass
