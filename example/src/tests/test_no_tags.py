"""Tests without any tags to demonstrate unmatched test handling."""


def test_simple_calculation():
    """A simple test without any tags or fixtures."""
    assert 2 + 2 == 4
    assert 3 * 4 == 12
    assert 10 / 2 == 5


def test_string_operations():
    """Another test without tags or fixtures."""
    text = "hello world"
    assert len(text) == 11
    assert "hello" in text
    assert "world" in text


def test_list_operations():
    """Test list operations without tags or fixtures."""
    numbers = [1, 2, 3, 4, 5]
    assert len(numbers) == 5
    assert sum(numbers) == 15
    assert max(numbers) == 5
