from pt_pump_up_admin.model import Model
from pt_pump_up_admin.link import Link
from pt_pump_up_admin.resource_stats import ResourceStats
from pt_pump_up_admin.nlp_task import NLPTask
from tests.lib.utils import fixture_load_admin_instance
import pytest


@pytest.fixture
def fixture_create_model(fixture_load_admin_instance):

    client = fixture_load_admin_instance

    model = Model()

    link = Link()

    nlp_tasks = []

    for i in range(1, 4):
        nlp_task = NLPTask(identifier=i)
        client.submit(nlp_task.store(
            short_name=f"nlp_task_{i}", papers_with_code_ids=[i, i+1, i+2, i+3, i+4]))

        nlp_tasks.append(nlp_task)

    resource_stats = ResourceStats()

    resource_stats.store(standard_format=True,
                         off_the_shelf=True, preservation_rating="High")

    link.store(website="http://143.107.183.175:21380/portlex/index.php/pt/projetos/propbankbr",
               hugging_face_url="https://huggingface.co/datasets/liaad/Propbank-BR",
               papers_with_code_url="https://paperswithcode.com/paper/propbank-br-a-brazilian-treebank-annotated",
               paper_url="https://www.researchgate.net/profile/Sandra-Aluisio/publication/267227963_Propbank-Br_a_Brazilian_treebank_annotated_with_semantic_role_labels/links/54d388e60cf2b0c6146daa5a/Propbank-Br-a-Brazilian-treebank-annotated-with-semantic-role-labels.pdf")

    request = model.store(short_name="Propbank-BR",
                          year=2012,
                          full_name="Propbank-Br: a Brazilian Treebank annotated with semantic role labels",
                          description="This paper reports the annotation of a Brazilian Portuguese Treebank with semantic role labels following Propbank guidelines. A different language and a different parser output impact the task and require some decisions on how to annotate the corpus. Therefore, a new annotation guide â€• called Propbank-Br - has been generated to deal with specific language phenomena and parser problems. In this phase of the project, the corpus was annotated by a unique linguist. The annotation task reported here is inserted in a larger projet for the Brazilian Portuguese language. This project aims to build Brazilian verbs frames files and a broader and distributed annotation of semantic role labels in Brazilian Portuguese, allowing inter-annotator agreement measures. The corpus, available in web, is already being used to build a semantic tagger for Portuguese language.",
                          link=link,
                          resource_stats=resource_stats,
                          nlp_tasks=nlp_tasks)

    return client, request, nlp_tasks


def test_model_store(fixture_create_model):
    client, request, nlp_tasks = fixture_create_model

    assert request.json['short_name'] == "Propbank-BR"
    assert request.json['full_name'] == "Propbank-Br: a Brazilian Treebank annotated with semantic role labels"
    assert request.json['description'] == "This paper reports the annotation of a Brazilian Portuguese Treebank with semantic role labels following Propbank guidelines. A different language and a different parser output impact the task and require some decisions on how to annotate the corpus. Therefore, a new annotation guide â€• called Propbank-Br - has been generated to deal with specific language phenomena and parser problems. In this phase of the project, the corpus was annotated by a unique linguist. The annotation task reported here is inserted in a larger projet for the Brazilian Portuguese language. This project aims to build Brazilian verbs frames files and a broader and distributed annotation of semantic role labels in Brazilian Portuguese, allowing inter-annotator agreement measures. The corpus, available in web, is already being used to build a semantic tagger for Portuguese language."
    assert request.json['year'] == 2012
    assert request.json['link']['website'] == "http://143.107.183.175:21380/portlex/index.php/pt/projetos/propbankbr"
    assert request.json['link']['hugging_face_url'] == "https://huggingface.co/datasets/liaad/Propbank-BR"
    assert request.json['link']['papers_with_code_url'] == "https://paperswithcode.com/paper/propbank-br-a-brazilian-treebank-annotated"
    assert request.json['link']['paper_url'] == "https://www.researchgate.net/profile/Sandra-Aluisio/publication/267227963_Propbank-Br_a_Brazilian_treebank_annotated_with_semantic_role_labels/links/54d388e60cf2b0c6146daa5a/Propbank-Br-a-Brazilian-treebank-annotated-with-semantic-role-labels.pdf"
    assert request.json['resource_stats']['standard_format'] == True
    assert request.json['resource_stats']['off_the_shelf'] == True
    assert request.json['resource_stats']['preservation_rating'] == "high"
    assert request.json['nlp_task_ids'] == [
        nlp_task.identifier for nlp_task in nlp_tasks]

    response = client.submit(request)

    assert response.status_code == 201


def test_model_delete(fixture_create_model):
    client, request, nlp_tasks = fixture_create_model

    response = client.submit(request)

    assert response.status_code == 201

    model = Model(identifier=response.json()['data']['id'])

    response = client.submit(model.delete())

    assert response.status_code == 204
