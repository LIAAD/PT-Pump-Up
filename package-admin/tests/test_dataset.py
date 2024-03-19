from pt_pump_up_admin.dataset import Dataset
from pt_pump_up_admin.link import Link
import pytest
from tests.lib.resources import fixture_create_authors, fixture_create_resource_stats, fixture_create_nlp_tasks


@pytest.fixture
def fixture_create_dataset_link():

    link = Link(hugging_face_url="https://huggingface.co/datasets/liaad/Propbank-BR",
                papers_with_code_url="https://paperswithcode.com/paper/propbank-br-a-brazilian-treebank-annotated",
                website="http://143.107.183.175:21380/portlex/index.php/pt/projetos/propbankbr",
                paper_url="https://www.researchgate.net/profile/Sandra-Aluisio/publication/267227963_Propbank-Br_a_Brazilian_treebank_annotated_with_semantic_role_labels/links/54d388e60cf2b0c6146daa5a/Propbank-Br-a-Brazilian-treebank-annotated-with-semantic-role-labels.pdf")

    link.store()

    return link


def test_dataset_store(fixture_create_authors, fixture_create_resource_stats, fixture_create_nlp_tasks, fixture_create_dataset_link):

    dataset = Dataset(short_name="Propbank-BR",
                      description="Propbank-BR is a corpus of Brazilian Portuguese annotated with semantic roles.",
                      year=2012,
                      authors=fixture_create_authors,
                      resource_stats=fixture_create_resource_stats,
                      nlp_tasks=fixture_create_nlp_tasks,
                      link=fixture_create_dataset_link)

    response = dataset.store()

    assert response.status_code == 201
    assert response.json()["id"] == dataset.id
    assert response.json()["short_name"] == "Propbank-BR"
    assert response.json()["year"] == 2012
    assert response.json()["link_id"] is not None
    assert response.json()[
        "description"] == "Propbank-BR is a corpus of Brazilian Portuguese annotated with semantic roles."

    assert response.json()["authors"] is not None
    assert len(response.json()["authors"]) == 3
    assert response.json()["authors"][0]["name"] == "Rúben Almeida"
    assert response.json()["authors"][1]["name"] == "Alípio Jorge"
    assert response.json()["authors"][2]["name"] == "Sérgio Nunes"

    assert response.json()["resource_stats"]["standard_format"] is True
    assert response.json()["resource_stats"]["off_the_shelf"] is False
    assert response.json()["resource_stats"]["preservation_rating"] == "high"


def test_dataset_destroy(fixture_create_authors, fixture_create_resource_stats, fixture_create_nlp_tasks, fixture_create_dataset_link):

    dataset = Dataset(short_name="Propbank-BR",
                      description="Propbank-BR is a corpus of Brazilian Portuguese annotated with semantic roles.",
                      year=2012,
                      authors=fixture_create_authors,
                      resource_stats=fixture_create_resource_stats,
                      nlp_tasks=fixture_create_nlp_tasks,
                      link=fixture_create_dataset_link)

    response = dataset.store()

    assert response.status_code == 201
    assert response.json()["id"] is not None

    response = dataset.destroy()

    assert response.status_code == 204
