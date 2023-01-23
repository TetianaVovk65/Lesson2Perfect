import pytest


@pytest.fixture(scope='function', autouse=True)
def mod2_fixture_for_each_tests():
    print('mod2_fixture_for_each_tests Start')
    yield
    print('\nmod2_fixture_for_each_tests Finish')


@pytest.fixture
def input_value():
    input_val = 39
    return input_val
