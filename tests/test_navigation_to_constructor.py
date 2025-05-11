from data import EXISTING_USER, BASE_URL
from helpers import wait_for_element
import locators as loc

def login(driver, email, password):
    driver.get(BASE_URL + "/login")
    wait_for_element(driver, *loc.input_email_auth).send_keys(email)
    wait_for_element(driver, *loc.input_password_auth).send_keys(password)
    wait_for_element(driver, *loc.button_login).click()


def test_navigation_to_constructor_from_account(driver):
    login(driver, EXISTING_USER["email"], EXISTING_USER["password"])
    wait_for_element(driver, *loc.button_personal_account).click()
    wait_for_element(driver, *loc.header_of_page_constructor).click()
    order_button = wait_for_element(driver, *loc.button_make_the_order)
    assert order_button.is_displayed()


def test_navigation_to_constructor_from_logo(driver):
    login(driver, EXISTING_USER["email"], EXISTING_USER["password"])
    wait_for_element(driver, *loc.button_personal_account).click()
    wait_for_element(driver, *loc.logo).click()
    order_button = wait_for_element(driver, *loc.button_make_the_order)
    assert order_button.is_displayed()
