from data import EXISTING_USER
from helpers import wait_for_element
import locators as loc


class TestLogout:

    def test_logout(self, driver, login_user):
        login_user(EXISTING_USER["email"], EXISTING_USER["password"])
        wait_for_element(driver, *loc.button_personal_account).click()
        wait_for_element(driver, *loc.profile)
        wait_for_element(driver, *loc.button_logout).click()
        assert wait_for_element(driver, *loc.button_login).is_displayed()
