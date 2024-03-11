from tests.lib.utils import fixture_load_admin_instance
from pt_pump_up_admin.author import Author
from pt_pump_up_admin.link import Link
import pytest


@pytest.fixture
def fixture_create_link_author(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    link = Link(email="ruben.f.almeida@inesctec.pt",
                website="https://www.inesctec.pt/pt/pessoas/ruben-filipe-seabra-almeida")

    client.submit(link.store())

    return link


def test_author_store(fixture_load_admin_instance, fixture_create_link_author):
    client = fixture_load_admin_instance
    link = fixture_create_link_author

    author = Author(name="Rúben Almeida",
                    institution="INESC TEC",
                    link=link)

    response = client.submit(author.store())

    assert response.status_code == 201
    assert response.json()["id"] is not None
    assert response.json()["name"] == author.json["name"]
    assert response.json()["institution"] == author.json["institution"]
    assert response.json()["link_id"] is not None

    assert response.json()["link"]["email"] == link.json["email"]
    assert response.json()["link"]["website"] == link.json["website"]
