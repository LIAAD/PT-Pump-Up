import pytest
from pt_pump_up_orms import NLPTask, Link
from pt_pump_up_admin import CRUD
from tests.lib.utils import fixture_erase_database


@pytest.fixture
def fixture_create_nlp_task():

    nlp_task = NLPTask(short_name="NER", papers_with_code_id=0,
                       standard_format="BIO-Tagging", link=Link(papers_with_code_url="https://paperswithcode.com/task/named-entity-recognition"))

    CRUD.store(nlp_task)

    return nlp_task


def test_index_nlp_tasks(fixture_erase_database, fixture_create_nlp_task):
    nlp_task_created = fixture_create_nlp_task

    response = CRUD.index(nlp_task_created)

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

    assert data[-1]['short_name'] == nlp_task_created.short_name
    assert data[-1]['id'] == nlp_task_created.id


def test_store_nlp_task_minimum_values():

    nlp_task = NLPTask(
        short_name="NER",
        papers_with_code_id=100,
        standard_format="BIO-Tagging",
        link=Link(papers_with_code_url="https://paperswithcode.com/task/named-entity-recognition"))

    response = CRUD.store(nlp_task)

    assert response.status_code == 201
    assert response.json().get('short_name') == "NER"
    assert response.json().get('full_name') is None
    assert response.json().get('standard_format') == "BIO-Tagging"
    assert response.json().get('description') is None
    assert response.json().get('papers_with_code_id') == 100


def test_store_nlp_task_all_values():

    nlp_task = NLPTask(short_name="NER",
                       full_name="Named Entity Recognition",
                       description="Named Entity Recognition is a task in NLP that aims to identify named entities in a text.",
                       standard_format="BIO-Tagging",
                       papers_with_code_id=500,
                       link=Link(papers_with_code_url="https://paperswithcode.com/task/named-entity-recognition"))

    response = CRUD.store(nlp_task)

    assert response.status_code == 201
    assert response.json()['short_name'] == "NER"
    assert response.json()['full_name'] == "Named Entity Recognition"
    assert response.json()['standard_format'] == "BIO-Tagging"
    assert response.json()[
        'description'] == "Named Entity Recognition is a task in NLP that aims to identify named entities in a text."
    # assert response.json()['papers_with_code_ids'] == [0, 100]


def test_delete_nlp_task(fixture_create_nlp_task):

    nlp_task = fixture_create_nlp_task

    response = CRUD.destroy(nlp_task)

    assert response.status_code == 204


def test_show_nlp_task():
    pass
