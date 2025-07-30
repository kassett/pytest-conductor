"""Tests for data processing functionality."""

import pytest


@pytest.mark.fast
@pytest.mark.unit
def test_numbers_processing(sample_data):
    """Test processing of numbers from sample data."""
    numbers = sample_data["numbers"]
    assert len(numbers) == 5
    assert sum(numbers) == 15
    assert max(numbers) == 5
    assert min(numbers) == 1


@pytest.mark.fast
@pytest.mark.unit
def test_strings_processing(sample_data):
    """Test processing of strings from sample data."""
    strings = sample_data["strings"]
    assert len(strings) == 3
    assert "hello" in strings
    assert "world" in strings
    assert "test" in strings


@pytest.mark.fast
@pytest.mark.unit
def test_mixed_data_processing(sample_data):
    """Test processing of mixed data types."""
    mixed = sample_data["mixed"]
    assert len(mixed) == 4
    assert 1 in mixed
    assert "two" in mixed
    assert 3.0 in mixed
    assert True in mixed


@pytest.mark.slow
@pytest.mark.integration
def test_config_usage(test_config):
    """Test using test configuration."""
    assert test_config["timeout"] == 30
    assert test_config["retries"] == 3
    assert test_config["debug"] is True


@pytest.mark.slow
@pytest.mark.integration
def test_data_and_config_combination(sample_data, test_config):
    """Test combining sample data with test configuration."""
    # Simulate some processing that uses both fixtures
    numbers = sample_data["numbers"]
    timeout = test_config["timeout"]

    # Simulate processing that takes time
    result = sum(numbers) * timeout
    assert result == 15 * 30  # 450
