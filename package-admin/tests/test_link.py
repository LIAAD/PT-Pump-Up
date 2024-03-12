from tests.lib.utils import fixture_load_admin_instance
from pt_pump_up_admin.link import Link


def test_link_create(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    link = Link()

    request = link.store(
        email="ruben.f.almeida@inesctec.pt",
        website="https://www.inesctec.pt/pt/pessoas/ruben-filipe-seabra-almeida",
        hugging_face_url="https://huggingface.co/arubenruben",
        papers_with_code_url="https://paperswithcode.com/author/ruben-filipe-seabra-almeida",
        paper_url="https://www.researchgate.net/profile/Ruben-Almeida-2"
    )

    response = client.submit(request)

    assert response.status_code == 201

    assert response.json()["id"] is not None
    assert response.json()["email"] == "ruben.f.almeida@inesctec.pt"

    assert response.json()[
        "website"] == "https://www.inesctec.pt/pt/pessoas/ruben-filipe-seabra-almeida"

    assert response.json()[
        "hugging_face_url"] == "https://huggingface.co/arubenruben"

    assert response.json()[
        "papers_with_code_url"] == "https://paperswithcode.com/author/ruben-filipe-seabra-almeida"

    assert response.json()[
        "paper_url"] == "https://www.researchgate.net/profile/Ruben-Almeida-2"