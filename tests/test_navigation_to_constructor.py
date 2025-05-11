from data import EXISTING_USER
from helpers import wait_for_element
import locators as loc


class TestNavigationToConstructor:

    def test_navigation_to_constructor_from_account(self, driver, login_user):
        login_user(EXISTING_USER["email"], EXISTING_USER["password"])
        wait_for_element(driver, *loc.button_personal_account).click()
        wait_for_element(driver, *loc.header_of_page_constructor).click()
        assert wait_for_element(driver, *loc.button_make_the_order).is_displayed()


    def test_navigation_to_constructor_from_logo(self, driver, login_user):
        login_user(EXISTING_USER["email"], EXISTING_USER["password"])
        wait_for_element(driver, *loc.button_personal_account).click()
        wait_for_element(driver, *loc.logo).click()
        assert wait_for_element(driver, *loc.button_make_the_order).is_displayed()
