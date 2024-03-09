from pt_pump_up_admin.nlp_task import NLPTask
from tests.lib.utils import fixture_load_admin_instance
import pytest


def test_index_nlp_tasks(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    nlp_task = NLPTask()

    request = nlp_task.index()

    response = client.submit(request)

    assert response.status_code == 200

    data = response.json()['data']

    assert len(data) > 0

    assert data[0]['short_name'] == "NER"


def test_store_nlp_task_minimum_values(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    nlp_task = NLPTask()

    request = nlp_task.store(short_name="NER", papers_with_code_ids=[0, 100])

    assert request.json == {
        "short_name": "NER",
        "full_name": None,
        "description": None,
        "papers_with_code_ids": "[0, 100]"
    }

    response = client.submit(request)

    assert response.status_code == 201


def test_store_nlp_task_all_values(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    nlp_task = NLPTask()

    request = nlp_task.store(short_name="NER",
                             full_name="Named Entity Recognition",
                             description="Named Entity Recognition is a task in NLP that aims to identify named entities in a text.",
                             papers_with_code_ids=[0, 100])

    assert request.json == {
        "short_name": "NER",
        "full_name": "Named Entity Recognition",
        "description": "Named Entity Recognition is a task in NLP that aims to identify named entities in a text.",
        "papers_with_code_ids": "[0, 100]"
    }

    response = client.submit(request)

    assert response.status_code == 201


def test_delete_nlp_task(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    nlp_task = NLPTask()

    request = nlp_task.store(short_name="NER", papers_with_code_ids=[0, 100])

    response = client.submit(request)

    assert response.status_code == 201

    data = response.json()['data']

    assert 'id' in data

    identifier = data['id']

    request = nlp_task.delete(identifier)

    response = client.submit(request)

    assert response.status_code == 204


def test_show_nlp_task(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    nlp_task = NLPTask()

    request = nlp_task.store(short_name="NER", papers_with_code_ids=[0, 100])

    response = client.submit(request)

    assert response.status_code == 201

    data = response.json()['data']

    assert 'id' in data

    identifier = data['id']

    request = nlp_task.show(identifier)

    response = client.submit(request)

    assert response.status_code == 200

    data = response.json()['data']

    assert data['short_name'] == "NER"