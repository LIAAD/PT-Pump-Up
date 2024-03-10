from tests.lib.utils import fixture_load_admin_instance
from pt_pump_up_admin.author import Author
from pt_pump_up_admin.link import Link
import pytest


@pytest.fixture
def fixture_create_link():

    link = Link()

    link.store(
        email="ruben.f.almeida@inesctec.pt",
        website="https://www.inesctec.pt/pt/pessoas/ruben-filipe-seabra-almeida"
    )

    return link


def test_author_create_id(fixture_load_admin_instance, fixture_create_link):
    client = fixture_load_admin_instance
    link = fixture_create_link

    response = client.submit(link.store())
    identifier = response.json()["id"]

    request = Author().store(
        name="John Doe",
        institution="University of California",
        link=Link(identifier=response.json()["id"])
    )

    response = client.submit(request)

    assert response.status_code == 201

    assert response.json()["id"] is not None
    assert response.json()["name"] == "John Doe"
    assert response.json()["institution"] == "University of California"
    assert response.json()["link_id"] == identifier


def test_author_create_no_id(fixture_load_admin_instance, fixture_create_link):
    client = fixture_load_admin_instance
    link = fixture_create_link

    request = Author().store(
        name="John Doe",
        institution="University of California",
        link=link
    )

    response = client.submit(request)

    assert response.status_code == 201
    assert response.json()["id"] is not None
    assert response.json()["name"] == "John Doe"
    assert response.json()["institution"] == "University of California"
    assert response.json()["link_id"] is not None
