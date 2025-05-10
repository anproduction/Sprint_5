from data import TEST_USER, BASE_URL, generate_unique_email, generate_random_password
from helpers import wait_for_element
import locators as loc


def test_logout(driver):
    driver.get(BASE_URL)

    unique_email = generate_unique_email()
    random_password = generate_random_password()

    wait_for_element(driver, *loc.input_name).send_keys(TEST_USER["name"])
    wait_for_element(driver, *loc.input_email).send_keys(unique_email)
    wait_for_element(driver, *loc.input_password).send_keys(random_password)
    wait_for_element(driver, *loc.button_submit).click()
    wait_for_element(driver, *loc.button_personal_account).click()
    wait_for_element(driver, *loc.profile)
    wait_for_element(driver, *loc.button_logout).click()
    wait_for_element(driver, *loc.button_login_in_main)
    driver.quit()
