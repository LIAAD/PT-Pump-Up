from pt_pump_up_admin.dataset import Dataset
from pt_pump_up_admin.link import Link
from pt_pump_up_admin.author import Author
from pt_pump_up_admin.resource_stats import ResourceStats
from pt_pump_up_admin.nlp_task import NLPTask
import pytest
from tests.lib.utils import fixture_load_admin_instance


@pytest.fixture
def fixture_create_dataset_object(fixture_load_admin_instance):

    client = fixture_load_admin_instance

    authors = []

    for _ in range(3):
        author = Author()
        link = Link()

        link.store(
            email="ruben.f.almeida@inesctec.pt"
        )

        author.store(
            name="John Doe",
            institution="University of California",
            link=link
        )

        authors.append(author.json)

    link = Link()

    link.store(
        hugging_face_url="https://huggingface.co/datasets/propbank_br",
        paper_url="https://www.aclweb.org/anthology/W12-2713.pdf"
    )

    resource_stats = ResourceStats()
    resource_stats.store(
        standard_format=True,
        off_the_shelf=False,
        preservation_rating="high"
    )

    nlp_task = NLPTask()

    response = client.submit(nlp_task.store(
        short_name="Semantic Role Labeling",
        full_name="Semantic Role Labeling",
        description="Semantic Role Labeling is the task of identifying the predicate-argument structure of a sentence.",
        standard_format="BIO-Tagging",
        papers_with_code_ids=[1, 2, 3]
    ))

    nlp_task.identifier = response.json()["id"]

    request = Dataset().store(
        short_name="Propbank-BR",
        year=2012,
        authors=authors,
        resource_stats=resource_stats,
        nlp_tasks=[nlp_task],
        link=link,
        description="Propbank-BR is a corpus of Brazilian Portuguese annotated with semantic roles."
    )

    return request


def test_dataset_create_id(fixture_load_admin_instance, fixture_create_dataset_object):
    client = fixture_load_admin_instance
    request = fixture_create_dataset_object

    response = client.submit(request)

    assert response.status_code == 201
    assert response.json()["id"] is not None
    assert response.json()["short_name"] == "Propbank-BR"
    assert response.json()["year"] == 2012
    # assert response.json()["authors"] is not None
    assert response.json()["link_id"] is not None
    assert response.json()[
        "description"] == "Propbank-BR is a corpus of Brazilian Portuguese annotated with semantic roles."

    # assert response.json()["resource_stats"]["standard_format"] is True
    # assert response.json()["resource_stats"]["off_the_shelf"] is False
    # assert response.json()["resource_stats"]["preservation_rating"] == "high"
