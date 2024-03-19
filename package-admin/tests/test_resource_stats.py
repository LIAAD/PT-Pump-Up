from pt_pump_up_admin.resource_stats import ResourceStats
import pytest


def test_store_resource_stats_full():

    resource_stats = ResourceStats(standard_format=True,
                                   off_the_shelf=True,
                                   preservation_rating="high")

    response = resource_stats.store()

    assert response.status_code == 201


def test_store_resource_stats_id_expect_error():
    resource_stats = ResourceStats(id=1)

    with pytest.raises(ValueError, match="id cannot be set for POST request"):
        resource_stats.store()
