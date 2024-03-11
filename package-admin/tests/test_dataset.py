from pt_pump_up_admin.dataset import Dataset
from pt_pump_up_admin.link import Link
from pt_pump_up_admin.author import Author
from pt_pump_up_admin.resource_stats import ResourceStats
from pt_pump_up_admin.nlp_task import NLPTask
import pytest
from tests.lib.utils import fixture_load_admin_instance


@pytest.fixture
def fixture_create_dataset_link():
    link = Link()

    link.store(
        hugging_face_url="https://huggingface.co/datasets/liaad/Propbank-BR",
        papers_with_code_url="https://paperswithcode.com/paper/propbank-br-a-brazilian-treebank-annotated",
        website="http://143.107.183.175:21380/portlex/index.php/pt/projetos/propbankbr",
        paper_url="https://www.researchgate.net/profile/Sandra-Aluisio/publication/267227963_Propbank-Br_a_Brazilian_treebank_annotated_with_semantic_role_labels/links/54d388e60cf2b0c6146daa5a/Propbank-Br-a-Brazilian-treebank-annotated-with-semantic-role-labels.pdf",
    )

    return link


@pytest.fixture
def fixture_create_authors():
    link_author_1 = Link()
    link_author_2 = Link()
    link_author_3 = Link()

    link_author_1.store(
        email="ruben.f.almeida@inesctec.pt",
        website="https://www.inesctec.pt/pt/pessoas/ruben-filipe-seabra-almeida"
    )

    link_author_2.store(
        email="alipio.jorge@inesctec.pt",
        website="https://www.inesctec.pt/pt/pessoas/alipio-jorge"
    )

    link_author_3.store(
        email="sergio.nunes@inesctec.pt",
        website="https://www.inesctec.pt/pt/pessoas/sergio-nunes"
    )

    author_1 = Author()
    author_2 = Author()
    author_3 = Author()

    author_1.store(
        name="Ruben Almeida",
        institution="INESC TEC",
        link=link_author_1
    )

    author_2.store(
        name="Alipio Jorge",
        institution="INESC TEC",
        link=link_author_2
    )

    author_3.store(
        name="Sergio Nunes",
        institution="INESC TEC",
        link=link_author_3
    )

    return [author_1, author_2, author_3]


@pytest.fixture
def fixture_create_nlp_tasks():
    nlp_task_1 = NLPTask()
    nlp_task_2 = NLPTask()

    nlp_task_1.store(
        short_name="SRL",
        full_name="Semantic Role Labeling",
        description="Semantic Role Labeling is the task of identifying the predicate-argument structure of a sentence.",
        standard_format="BIO-Tagging",
        papers_with_code_ids=[1, 2, 3]
    )

    nlp_task_2.store(
        short_name="NER",
        full_name="Named Entity Recognition",
        description="Named Entity Recognition is the task of identifying named entities in a text.",
        standard_format="BIO-Tagging",
        papers_with_code_ids=[4, 5, 6]
    )

    return [nlp_task_1, nlp_task_2]


@pytest.fixture
def fixture_create_resource_stats():
    resource_stats = ResourceStats()

    resource_stats.store(
        standard_format=True,
        off_the_shelf=False,
        preservation_rating="high"
    )

    return resource_stats


def test_dataset_store(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    request = Dataset().store(
        short_name="Propbank-BR",
        description="Propbank-BR is a corpus of Brazilian Portuguese annotated with semantic roles.",
        year=2012,
        authors=fixture_create_authors,
        resource_stats=fixture_create_resource_stats,
        nlp_tasks=fixture_create_nlp_tasks,
        link=fixture_create_dataset_link,
    )

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
