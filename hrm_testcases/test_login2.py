import pytest
from conftest import BASE_URL, USERNAME, PASS
from hrm_pages.LoginPage import LoginPage


@pytest.mark.usefixtures("browser_setup")
class Test_Login:
    def setup_class(self):
        self.driver.get(BASE_URL)
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        self.login_page.login(USERNAME, PASS)

    def teardown_class(self):
        self.driver.quit()