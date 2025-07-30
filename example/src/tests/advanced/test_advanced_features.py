"""Advanced tests that use local fixtures."""

import pytest


@pytest.mark.slow
@pytest.mark.integration
def test_local_advanced_fixture(local_advanced_fixture):
    """Test using the local advanced fixture."""
    assert local_advanced_fixture["type"] == "advanced"
    assert local_advanced_fixture["scope"] == "local"
    assert len(local_advanced_fixture["data"]) == 5
    assert sum(local_advanced_fixture["data"]) == 150


@pytest.mark.slow
@pytest.mark.integration
def test_specialized_config(specialized_config):
    """Test using the specialized configuration."""
    assert specialized_config["advanced_mode"] is True
    assert specialized_config["precision"] == "high"
    assert specialized_config["cache_size"] == 1000


@pytest.mark.slow
@pytest.mark.integration
def test_combined_local_fixtures(local_advanced_fixture, specialized_config):
    """Test using both local fixtures together."""
    data = local_advanced_fixture["data"]
    cache_size = specialized_config["cache_size"]

    # Simulate some advanced processing
    result = sum(data) * (cache_size / 1000)
    assert result == 150 * 1  # 150
