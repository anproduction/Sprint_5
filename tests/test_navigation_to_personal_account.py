from data import EXISTING_USER
from helpers import wait_for_element
import locators as loc


def test_navigation_to_personal_account(driver, login_user):

    login_user(EXISTING_USER["email"], EXISTING_USER["password"])
    wait_for_element(driver, *loc.button_personal_account).click()
    profile_link = wait_for_element(driver, *loc.profile)
    assert profile_link.is_displayed()