from data import TEST_USER, INVALID_USER, BASE_URL
from helpers import wait_for_element
import locators as loc
from data import generate_unique_email, generate_random_password


def test_successful_registration(driver):
    driver.get(BASE_URL + "/register")
    unique_email = generate_unique_email()
    random_password = generate_random_password()

    wait_for_element(driver, *loc.input_name).send_keys(TEST_USER["name"])
    wait_for_element(driver, *loc.input_email).send_keys(unique_email)
    wait_for_element(driver, *loc.input_password).send_keys(random_password)
    wait_for_element(driver, *loc.button_submit).click()
    email_input_auth = wait_for_element(driver, *loc.input_email_auth)
    assert email_input_auth. is_displayed()


def test_registration_with_invalid_password(driver):
    driver.get(BASE_URL + "/register")

    wait_for_element(driver, *loc.input_name).send_keys(INVALID_USER["name"])
    wait_for_element(driver, *loc.input_email).send_keys(INVALID_USER["email"])
    wait_for_element(driver, *loc.input_password).send_keys(INVALID_USER["password"])
    wait_for_element(driver, *loc.button_submit).click()
    error = wait_for_element(driver, *loc.notification_incorrect_password)
    assert error.is_displayed()
