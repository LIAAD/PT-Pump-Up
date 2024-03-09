from pt_pump_up_admin.nlp_task import NLPTask
from tests.lib.utils import fixture_load_admin_instance
import pytest


def test_create_nlp_task_minimum_values(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    nlp_task = NLPTask(short_name="NER",
                       papers_with_code_ids=[0, 100])

    response = client.submit(nlp_task.create())

    assert response.status_code == 201


def test_create_nlp_task_all_values(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    nlp_task = NLPTask(short_name="NER",
                       full_name="Named Entity Recognition",
                       description="Named Entity Recognition is a task in NLP that aims to identify named entities in a text.",
                       papers_with_code_ids=[0, 100])

    response = client.submit(nlp_task.create())

    assert response.status_code == 200
    assert response.json()["message"] == "Hello World!"
