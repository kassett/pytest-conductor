"""Tests for basic calculator operations."""

import pytest
from calculator import Calculator


@pytest.mark.fast
@pytest.mark.unit
def test_addition(basic_calculator):
    """Test basic addition."""
    assert basic_calculator.add(2, 3) == 5
    assert basic_calculator.add(-1, 1) == 0
    assert basic_calculator.add(0, 0) == 0


@pytest.mark.fast
@pytest.mark.unit
def test_subtraction(basic_calculator):
    """Test basic subtraction."""
    assert basic_calculator.subtract(5, 3) == 2
    assert basic_calculator.subtract(1, 1) == 0
    assert basic_calculator.subtract(0, 5) == -5


@pytest.mark.fast
@pytest.mark.unit
def test_multiplication(basic_calculator):
    """Test basic multiplication."""
    assert basic_calculator.multiply(2, 3) == 6
    assert basic_calculator.multiply(-2, 3) == -6
    assert basic_calculator.multiply(0, 5) == 0


@pytest.mark.fast
@pytest.mark.unit
def test_division(basic_calculator):
    """Test basic division."""
    assert basic_calculator.divide(6, 2) == 3
    assert basic_calculator.divide(5, 2) == 2.5
    assert basic_calculator.divide(0, 5) == 0


@pytest.mark.fast
@pytest.mark.unit
def test_division_by_zero(basic_calculator):
    """Test division by zero raises error."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        basic_calculator.divide(5, 0)


@pytest.mark.fast
@pytest.mark.unit
def test_calculation_history(basic_calculator):
    """Test that calculations are recorded in history."""
    basic_calculator.add(1, 2)
    basic_calculator.multiply(3, 4)

    history = basic_calculator.get_history()
    assert len(history) == 2
    assert "1 + 2 = 3" in history
    assert "3 * 4 = 12" in history


@pytest.mark.fast
@pytest.mark.unit
def test_clear_history(basic_calculator):
    """Test clearing calculation history."""
    basic_calculator.add(1, 2)
    basic_calculator.clear_history()
    assert len(basic_calculator.get_history()) == 0
