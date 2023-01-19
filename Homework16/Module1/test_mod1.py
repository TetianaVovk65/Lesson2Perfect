import pytest


class TestPage:

    @pytest.mark.from_class
    def test_login(self):
        print('\nlogin')

    @pytest.mark.from_class
    def test_password(self):
        print('\npassword')

    @pytest.mark.from_class
    def test_avatar(self):
        print('\navatar')

    @pytest.mark.from_class
    def test_forgetpass(self):
        print('\nforget password')

    @pytest.mark.from_class
    def test_usernick(self):
        print('\nuser nick')
#pytest ./Homework16/Module1/test_mod1.py -m from_class