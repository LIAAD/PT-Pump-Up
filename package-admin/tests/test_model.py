from pt_pump_up_admin.model import Model
from pt_pump_up_admin.link import Link
from pt_pump_up_admin.resource_stats import ResourceStats
from pt_pump_up_admin.nlp_task import NLPTask
from pt_pump_up_admin.result import Result
from pt_pump_up_admin.author import Author
from tests.lib.utils import fixture_load_admin_instance
import pytest


@pytest.fixture
def fixture_create_authors():
    author = Author()
    link = Link()

    link.store(
        email="ruben.f.almeida@inesctec.pt",
    )

    author.store(
        name="John Doe",
        institution="University of California",
        link=link
    )

    return [author]


@pytest.fixture
def fixture_create_nlp_tasks(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    nlp_tasks = []

    for i in range(1, 4):
        nlp_task = NLPTask(identifier=i)
        client.submit(nlp_task.store(
            short_name=f"nlp_task_{i}", papers_with_code_ids=[i, i+1, i+2, i+3, i+4], standard_format="BIO-Tagging"))

        nlp_tasks.append(nlp_task)

    return nlp_tasks


@pytest.fixture
def fixture_create_result():
    results = []

    for _ in range(0, 3):
        result = Result()
        result.store(metric="F1", value=0.9, train_dataset_id=1,
                     validation_dataset_id=2, test_dataset_id=3)
        results.append(result)

    return results


@pytest.fixture
def fixture_create_link():
    link = Link()

    link.store(website="http://143.107.183.175:21380/portlex/index.php/pt/projetos/propbankbr",
               hugging_face_url="https://huggingface.co/datasets/liaad/Propbank-BR",
               papers_with_code_url="https://paperswithcode.com/paper/propbank-br-a-brazilian-treebank-annotated",
               paper_url="https://www.researchgate.net/profile/Sandra-Aluisio/publication/267227963_Propbank-Br_a_Brazilian_treebank_annotated_with_semantic_role_labels/links/54d388e60cf2b0c6146daa5a/Propbank-Br-a-Brazilian-treebank-annotated-with-semantic-role-labels.pdf")

    return link


@pytest.fixture
def fixture_create_resource_stats(fixture_load_admin_instance):
    resource_stats = ResourceStats()

    resource_stats.store(standard_format=True,
                         off_the_shelf=True, preservation_rating="High")

    return resource_stats


@pytest.fixture
def fixture_create_model(fixture_load_admin_instance,
                         fixture_create_nlp_tasks,
                         fixture_create_resource_stats,
                         fixture_create_result,
                         fixture_create_link,
                         fixture_create_authors):

    client = fixture_load_admin_instance
    resource_stats = fixture_create_resource_stats
    nlp_tasks = fixture_create_nlp_tasks
    link = fixture_create_link
    results = fixture_create_result
    authors = fixture_create_authors

    model = Model()

    request = model.store(short_name="Propbank-BR",
                          year=2012,
                          full_name="Propbank-Br: a Brazilian Treebank annotated with semantic role labels",
                          description="This paper reports the annotation of a Brazilian Portuguese Treebank with semantic role labels following Propbank guidelines. A different language and a different parser output impact the task and require some decisions on how to annotate the corpus. Therefore, a new annotation guide â€• called Propbank-Br - has been generated to deal with specific language phenomena and parser problems. In this phase of the project, the corpus was annotated by a unique linguist. The annotation task reported here is inserted in a larger projet for the Brazilian Portuguese language. This project aims to build Brazilian verbs frames files and a broader and distributed annotation of semantic role labels in Brazilian Portuguese, allowing inter-annotator agreement measures. The corpus, available in web, is already being used to build a semantic tagger for Portuguese language.",
                          link=link,
                          resource_stats=resource_stats,
                          results=results,
                          authors=authors,
                          nlp_tasks=nlp_tasks)

    return client, request, nlp_tasks


def test_model_store(fixture_create_model):
    client, request, nlp_tasks = fixture_create_model

    assert request.json['nlp_task_ids'] == [
        nlp_task.identifier for nlp_task in nlp_tasks]

    response = client.submit(request)

    assert response.status_code == 201
    assert response.json()['id'] is not None
    assert response.json()['short_name'] == "Propbank-BR"
    assert response.json()[
        'full_name'] == "Propbank-Br: a Brazilian Treebank annotated with semantic role labels"
    assert response.json()['description'] == "This paper reports the annotation of a Brazilian Portuguese Treebank with semantic role labels following Propbank guidelines. A different language and a different parser output impact the task and require some decisions on how to annotate the corpus. Therefore, a new annotation guide â€• called Propbank-Br - has been generated to deal with specific language phenomena and parser problems. In this phase of the project, the corpus was annotated by a unique linguist. The annotation task reported here is inserted in a larger projet for the Brazilian Portuguese language. This project aims to build Brazilian verbs frames files and a broader and distributed annotation of semantic role labels in Brazilian Portuguese, allowing inter-annotator agreement measures. The corpus, available in web, is already being used to build a semantic tagger for Portuguese language."
    assert response.json()['year'] == 2012
    assert response.json()['link_id'] is not None


def test_model_delete(fixture_create_model):
    client, request, _ = fixture_create_model

    response = client.submit(request)

    assert response.status_code == 201

    model = Model(identifier=response.json()['id'])

    response = client.submit(model.delete())

    assert response.status_code == 204
