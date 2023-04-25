"""
Test `math` module.
"""
import pytest

from src.my_math import sqrt


@pytest.mark.parametrize("value", range(0, 100))
def test_sqrt(value: int) -> None:
    """
    Test `math.sqrt` function.
    """
    res = sqrt(value)
    assert res * res == pytest.approx(value)
