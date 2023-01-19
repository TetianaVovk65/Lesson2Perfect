import pytest


@pytest.fixture()
def mod3_fixture_for_girls():
    print('mod3_fixture_for_girls Start')
    yield
    print('mod3_fixture_for_girls Finish\n')


@pytest.fixture()
def mod3_fixture_for_boys():
    print('mod3_fixture_for_boys Start')
    yield
    print('mod3_fixture_for_boys Finish\n')


@pytest.fixture()
def mod3_fixture_for_parents():
    print('mod3_fixture_for_parents Start')
    yield
    print('mod3_fixture_for_parents Finish\n')