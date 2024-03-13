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
    client = fixture_pt_pump_up_client

    dataset = client.load_dataset("Propbank-BR")

    assert dataset is not None


def test_load_model(fixture_pt_pump_up_client):
    client = fixture_pt_pump_up_client

    model = client.load_model("POS-Tagger Bio Portuguese")

    assert model is not None


def test_leaderboard(fixture_pt_pump_up_client):
    client = fixture_pt_pump_up_client

    leaderboard = client.leaderboard(nlp_task="NER")

    assert leaderboard is not None

    assert len(leaderboard) > 0
