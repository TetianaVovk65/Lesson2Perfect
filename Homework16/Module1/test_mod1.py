import pytest


class Test_Page:

    @pytest.mark.from_class
    def test_login(self):
        print('\nlogin')
        pass

    @pytest.mark.from_class
    def test_password(self):
        print('\npassword')
        pass

    @pytest.mark.from_class
    def test_avatar(self):
        print('\navatar')
        pass

    @pytest.mark.from_class
    def test_forgetpass(self):
        print('\nforget password')
        pass

    @pytest.mark.from_class
    def test_usernick(self):
        print('\nuser nick')
        pass
