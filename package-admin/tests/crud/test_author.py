import pytest
from pt_pump_up_orms import Author
from pt_pump_up_orms import Link
from pt_pump_up_admin import CRUD


@pytest.fixture
def fixture_create_link_author():
    link = Link(email="ruben.f.almeida@inesctec.pt",
                website="https://www.inesctec.pt/pt/pessoas/ruben-filipe-seabra-almeida")

    CRUD.store(link)

    return link


def test_author_store(fixture_create_link_author):
    link = fixture_create_link_author

    author = Author(name="Rúben Almeida",
                    institution="INESC TEC",
                    link=link)

    response = CRUD.store(author)

    assert response.status_code == 201
    assert response.json().get("id") == author.id
    assert response.json().get("name") == author.json.get("name")
    assert response.json().get("institution") == author.json.get("institution")
    assert response.json().get("link_id") is not None

    assert response.json().get("link")["email"] == link.json.get("email")
    assert response.json().get("link")["website"] == link.json.get("website")
