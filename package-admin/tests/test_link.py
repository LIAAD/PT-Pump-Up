from pt_pump_up_admin.link import Link
from tests.lib.utils import fixture_load_admin_instance


def test_link_store_full(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    link = Link()

    request = link.store(
        email="ruben.f.almeida@inesctec.pt",
        website="https://rubenalamida.me",
        github_url="https://github.com/LIAAD/PT-Pump-Up",
        hugging_face_url="https://huggingface.co/datasets/liaad/Propbank-BR",
        papers_with_code_url="https://paperswithcode.com/paper/propbank-br-a-brazilian-treebank-annotated",
        paper_url="https://www.researchgate.net/profile/Sandra-Aluisio/publication/267227963_Propbank-Br_a_Brazilian_treebank_annotated_with_semantic_role_labels/links/54d388e60cf2b0c6146daa5a/Propbank-Br-a-Brazilian-treebank-annotated-with-semantic-role-labels.pdf"
    )

    expected_dict = {
        "email": "ruben.f.almeida@inesctec.pt",
        "website": "https://rubenalamida.me",
        "github_url": "https://github.com/LIAAD/PT-Pump-Up",
        "hugging_face_url": "https://huggingface.co/datasets/liaad/Propbank-BR",
        "papers_with_code_url": "https://paperswithcode.com/paper/propbank-br-a-brazilian-treebank-annotated",
        "paper_url": "https://www.researchgate.net/profile/Sandra-Aluisio/publication/267227963_Propbank-Br_a_Brazilian_treebank_annotated_with_semantic_role_labels/links/54d388e60cf2b0c6146daa5a/Propbank-Br-a-Brazilian-treebank-annotated-with-semantic-role-labels.pdf"
    }

    assert request.json == expected_dict

    response = client.submit(request)

    assert response.status_code == 201

    body = response.json()['data']

    # Remove id from body_dict

    body.pop('id')

    assert body == expected_dict
