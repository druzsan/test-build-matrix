"""
Test `dummy` module.
"""
import pytest

from src.dummy import echo


@pytest.mark.parametrize("value", [False, 10, 3.14, "foo"])
def test_echo(value: int) -> None:
    """
    Test `dummy.echo` function.
    """
    assert echo(value) == value
