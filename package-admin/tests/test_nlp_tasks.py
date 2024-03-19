from pt_pump_up_admin.nlp_task import NLPTask
import pytest


@pytest.fixture
def fixture_create_nlp_task():    

    nlp_task = NLPTask(short_name="NER", papers_with_code_ids=[
        0, 100], standard_format="BIO-Tagging")

    nlp_task.store()

    return nlp_task


def test_index_nlp_tasks(fixture_create_nlp_task ):    
    nlp_task_created = fixture_create_nlp_task

    nlp_task = NLPTask()

    response = nlp_task.index()

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

    assert data[-1]['short_name'] == nlp_task_created.json['short_name']
    assert data[-1]['id'] == nlp_task_created.json['id']


def test_store_nlp_task_minimum_values():    

    nlp_task = NLPTask(
        short_name="NER",
        papers_with_code_ids=[0, 100],
        standard_format="BIO-Tagging")

    response = nlp_task.store()

    assert response.status_code == 201
    assert response.json()['short_name'] == "NER"
    assert response.json()['full_name'] is None
    assert response.json()['standard_format'] == "BIO-Tagging"
    assert response.json()['description'] is None
    assert response.json()['papers_with_code_ids'] == [0, 100]


def test_store_nlp_task_all_values():    

    nlp_task = NLPTask(short_name="NER",
                       full_name="Named Entity Recognition",
                       description="Named Entity Recognition is a task in NLP that aims to identify named entities in a text.",
                       standard_format="BIO-Tagging",
                       papers_with_code_ids=[0, 100])

    response = nlp_task.store()

    assert response.status_code == 201
    assert response.json()['short_name'] == "NER"
    assert response.json()['full_name'] == "Named Entity Recognition"
    assert response.json()['standard_format'] == "BIO-Tagging"
    assert response.json()[
        'description'] == "Named Entity Recognition is a task in NLP that aims to identify named entities in a text."
    assert response.json()['papers_with_code_ids'] == [0, 100]


def test_delete_nlp_task(fixture_create_nlp_task):    

    nlp_task = fixture_create_nlp_task

    response = nlp_task.destroy()

    assert response.status_code == 204


def test_show_nlp_task():
    pass
