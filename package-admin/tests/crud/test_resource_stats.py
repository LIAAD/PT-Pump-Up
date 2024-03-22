import pytest
from pt_pump_up_orms import ResourceStats
from pt_pump_up_admin import CRUD


def test_store_resource_stats_full():

    resource_stats = ResourceStats(standard_format=True,
                                   off_the_shelf=True,
                                   preservation_rating="high")

    response = CRUD.store(resource_stats)

    assert response.status_code == 201


def test_store_resource_stats_id_expect_error():
    resource_stats = ResourceStats(id=1)

    with pytest.raises(ValueError, match="id cannot be set for POST request"):
        CRUD.store(resource_stats)
