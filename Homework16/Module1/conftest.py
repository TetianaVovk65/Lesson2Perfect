import pytest


@pytest.fixture(scope='class', autouse=True)
def mod1_fixture_for_each_tests():
    print('mod1_fixture_for_each_tests Start')
    yield
    print('mod1_fixture_for_each_tests Finish\n')