from data import TEST_USER, BASE_URL, generate_unique_email, generate_random_password
from helpers import wait_for_element
import locators as loc


def register_new_user(driver, email, password):
    driver.get(BASE_URL + "/register")
    wait_for_element(driver, *loc.input_name).send_keys(TEST_USER["name"])
    wait_for_element(driver, *loc.input_email).send_keys(email)
    wait_for_element(driver, *loc.input_password).send_keys(password)
    wait_for_element(driver, *loc.button_submit).click()
    wait_for_element(driver, *loc.button_login)


def login_user(driver, email, password):
    wait_for_element(driver, *loc.input_email_auth).send_keys(email)
    wait_for_element(driver, *loc.input_password_auth).send_keys(password)
    wait_for_element(driver, *loc.button_login).click()
    wait_for_element(driver, *loc.button_personal_account)


def test_login_from_main_page_button(driver):
    email = generate_unique_email()
    password = generate_random_password()
    register_new_user(driver, email, password)

    driver.get(BASE_URL)
    wait_for_element(driver, *loc.button_login_in_main).click()
    login_user(driver, email, password)
    wait_for_element(driver, *loc.button_personal_account).click()
    logout_button = wait_for_element(driver, *loc.button_logout)
    assert logout_button.is_displayed()


def test_login_from_personal_account_button(driver):
    email = generate_unique_email()
    password = generate_random_password()
    register_new_user(driver, email, password)

    driver.get(BASE_URL)
    wait_for_element(driver, *loc.button_personal_account).click()
    login_user(driver, email, password)
    wait_for_element(driver, *loc.button_personal_account).click()
    logout_button = wait_for_element(driver, *loc.button_logout)
    assert logout_button.is_displayed()


def test_login_from_registration_form_button(driver):
    email = generate_unique_email()
    password = generate_random_password()
    register_new_user(driver, email, password)

    driver.get(BASE_URL + "/register")
    wait_for_element(driver, *loc.button_login_in_registration_form).click()
    login_user(driver, email, password)
    wait_for_element(driver, *loc.button_personal_account).click()
    logout_button = wait_for_element(driver, *loc.button_logout)
    assert logout_button.is_displayed()


def test_login_from_password_recovery_form_button(driver):
    email = generate_unique_email()
    password = generate_random_password()
    register_new_user(driver, email, password)

    driver.get(BASE_URL + "/forgot-password")
    wait_for_element(driver, *loc.button_login_passwd_recovery_form).click()
    login_user(driver, email, password)
    wait_for_element(driver, *loc.button_personal_account).click()
    logout_button = wait_for_element(driver, *loc.button_logout)
    assert logout_button.is_displayed()

