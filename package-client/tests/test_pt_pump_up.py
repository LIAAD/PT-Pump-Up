from pt_pump_up import PTPumpUpClient
import pytest


def test_all_nlp_tasks():
    client = PTPumpUpClient()
    nlp_tasks = client.all_nlp_tasks()
    assert nlp_tasks is not None


def test_all_datasets():
    pass


def test_all_models():
    pass


def test_load_dataset():
    pass

# TODO: Add transformers to the requirements


def test_load_model():
    pass
