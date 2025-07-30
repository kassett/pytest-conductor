"""Tests for advanced calculator operations."""

import pytest
from calculator import AdvancedCalculator


@pytest.mark.slow
@pytest.mark.integration
def test_power_operation(advanced_calculator):
    """Test power operation."""
    assert advanced_calculator.power(2, 3) == 8
    assert advanced_calculator.power(5, 0) == 1
    assert advanced_calculator.power(2, -1) == 0.5


@pytest.mark.slow
@pytest.mark.integration
def test_square_root(advanced_calculator):
    """Test square root operation."""
    assert advanced_calculator.square_root(4) == 2
    assert advanced_calculator.square_root(9) == 3
    assert advanced_calculator.square_root(0) == 0


@pytest.mark.slow
@pytest.mark.integration
def test_square_root_negative_number(advanced_calculator):
    """Test square root of negative number raises error."""
    with pytest.raises(
        ValueError, match="Cannot calculate square root of negative number"
    ):
        advanced_calculator.square_root(-4)


@pytest.mark.slow
@pytest.mark.integration
def test_advanced_calculator_inheritance(advanced_calculator):
    """Test that advanced calculator inherits basic operations."""
    assert advanced_calculator.add(2, 3) == 5
    assert advanced_calculator.multiply(4, 5) == 20
    assert advanced_calculator.power(2, 3) == 8


@pytest.mark.slow
@pytest.mark.integration
def test_mixed_operations_history(advanced_calculator):
    """Test history with mixed basic and advanced operations."""
    advanced_calculator.add(1, 2)
    advanced_calculator.power(2, 3)
    advanced_calculator.square_root(16)

    history = advanced_calculator.get_history()
    assert len(history) == 3
    assert "1 + 2 = 3" in history
    assert "2 ^ 3 = 8" in history
    assert "√16 = 4.0" in history
