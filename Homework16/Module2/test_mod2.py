import pytest


@pytest.mark.param
@pytest.mark.parametrize("divitedby3", [3, 6, 9])
def test1(divitedby3):
    assert divitedby3 % 3 == 0


@pytest.mark.param
@pytest.mark.parametrize("color", 'Blue')
def test1(color):
    assert color == color


@pytest.mark.param
def test_divisible_by_3(input_value):
    assert input_value % 3 == 0
