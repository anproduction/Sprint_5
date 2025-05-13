from data import EXISTING_USER
from helpers import wait_for_element
import locators as loc


class TestNavigationToPersonalAccount:

    def test_navigation_to_personal_account(self, driver, login_user):

        login_user(EXISTING_USER["email"], EXISTING_USER["password"])
        wait_for_element(driver, *loc.button_personal_account).click()
        assert wait_for_element(driver, *loc.profile).is_displayed()
