from pt_pump_up_admin.model import Model
from pt_pump_up_admin.link import Link
from pt_pump_up_admin.resource_stats import ResourceStats
from pt_pump_up_admin.nlp_task import NLPTask
from pt_pump_up_admin.result import Result
from pt_pump_up_admin.author import Author
from pt_pump_up_admin.dataset import Dataset
from tests.lib.utils import fixture_load_admin_instance
from tests.lib.resources import fixture_create_authors, fixture_create_resource_stats, fixture_create_nlp_tasks
import pytest


@pytest.fixture
def fixture_create_datasets_for_benchmarks(fixture_load_admin_instance):
    client = fixture_load_admin_instance
    link = Link(website="https://www.kaggle.com/c/nlp-getting-started/data",
                email="ruben.f.almeida@inesctec.pt")
    author = Author(name="John Doe",
                    institution="University of California", link=link)

    nlp_tasks = [NLPTask(short_name="nlp_task_1", papers_with_code_ids=[
                         1, 2, 3, 4, 5], standard_format="BIO-Tagging")]

    client.submit(author.store())
    client.submit(nlp_tasks[0].store())

    resource_stats = ResourceStats(
        off_the_shelf=True, standard_format=True, preservation_rating="High")

    dataset_1 = Dataset(
        short_name="train_dataset",
        link=link,
        year=2023,
        authors=[author],
        nlp_tasks=nlp_tasks,
        resource_stats=resource_stats,
        description="This is the train dataset for the benchmark"
    )

    dataset_2 = Dataset(
        short_name="validation_dataset",
        link=link,
        year=2023,
        authors=[author],
        nlp_tasks=nlp_tasks,
        resource_stats=resource_stats,
        description="This is the validation dataset for the benchmark"
    )

    dataset_3 = Dataset(
        short_name="test_dataset",
        link=link,
        year=2023,
        authors=[author],
        nlp_tasks=nlp_tasks,
        resource_stats=resource_stats,
        description="This is the test dataset for the benchmark"
    )

    r1 = client.submit(dataset_1.store())
    r2 = client.submit(dataset_2.store())
    r3 = client.submit(dataset_3.store())

    return [dataset_1.json['id'], dataset_2.json['id'], dataset_3.json['id']]


@pytest.fixture
def fixture_create_results(fixture_load_admin_instance, fixture_create_datasets_for_benchmarks):
    client = fixture_load_admin_instance

    results = [Result(
        metric="F1",
        value=0.9,
        train_dataset=Dataset(
            id=fixture_create_datasets_for_benchmarks[0]),  # train_dataset=,
        validation_dataset=Dataset(
            id=fixture_create_datasets_for_benchmarks[1]),  # validation_dataset=,
        test_dataset=Dataset(
            id=fixture_create_datasets_for_benchmarks[2])  # test_dataset=
    )]

    client.submit(results[0].store())

    results.append(results[0])

    return results


@pytest.fixture
def fixture_create_model_link(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    link = Link(
        hugging_face_url="https://huggingface.co/pucpr-br/postagger-bio-portuguese",)

    client.submit(link.store())

    return link


def test_model_store(fixture_load_admin_instance, fixture_create_authors, fixture_create_resource_stats, fixture_create_nlp_tasks, fixture_create_model_link, fixture_create_results):
    client = fixture_load_admin_instance

    authors = fixture_create_authors
    resource_stats = fixture_create_resource_stats
    nlp_tasks = fixture_create_nlp_tasks
    link = fixture_create_model_link
    results = fixture_create_results

    model = Model(
        short_name="POS-Tagger Bio Portuguese",
        year=2023,
        description="This is a POS-Tagger for Portuguese language",
        authors=authors,
        resource_stats=resource_stats,
        results=results,
        nlp_tasks=nlp_tasks,
        link=link,
    )

    response = client.submit(model.store())

    assert response.status_code == 201
    assert response.json()['id'] is not None
    assert response.json()['short_name'] == "POS-Tagger Bio Portuguese"
    assert response.json()['year'] == 2023
    assert response.json()[
        'description'] == "This is a POS-Tagger for Portuguese language"


def test_model_destroy(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    model = Model(id=1)

    response = client.submit(model.destroy())

    assert response.status_code == 204
