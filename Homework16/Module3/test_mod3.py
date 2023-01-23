import pytest


@pytest.mark.pack
@pytest.mark.joint
def test_girls(mod3_fixture_for_girls):
    print('\ngirls body module 3')
    pass


@pytest.mark.joint
@pytest.mark.pack
def test_boys(mod3_fixture_for_boys):
    print('\nboys body module 3')
    pass


@pytest.mark.rest
@pytest.mark.pack
def test_parents(mod3_fixture_for_parents):
    print('\nparents body module 3')
    pass
