from pt_pump_up_admin.resource_stats import ResourceStats
from tests.lib.utils import fixture_load_admin_instance
import pytest


def test_store_resource_stats_full(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    resource_stats = ResourceStats(standard_format=True,
                                   off_the_shelf=True,
                                   preservation_rating="high")

    response = client.submit(resource_stats.store())

    assert response.status_code == 201


def test_store_resource_stats_id_expect_error(fixture_load_admin_instance):
    client = fixture_load_admin_instance

    resource_stats = ResourceStats(id=1)

    with pytest.raises(ValueError, match="Cannot send POST request with id in json body"):
        client.submit(resource_stats.store())
