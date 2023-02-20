import pytest


@pytest.mark.param
@pytest.mark.parametrize("divinity", [3, 6, 9])
def test1(divinity):
    assert divinity % 3 == 0


some_dict =
@pytest.mark.param
@pytest.mark.parametrize("color", 'Blue')
def test2(color):
    assert color == color


@pytest.mark.param
def test_divisible_by_3(input_value):
    assert input_value % 3 == 0
