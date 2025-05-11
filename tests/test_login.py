from data import BASE_URL, generate_unique_email, generate_random_password
from helpers import wait_for_element
import locators as loc


def test_login_from_main_page_button(driver, register_new_user, login_user):
    email = generate_unique_email()
    password = generate_random_password()
    register_new_user(email, password)

    driver.get(BASE_URL)
    wait_for_element(driver, *loc.button_login_in_main).click()
    login_user(email, password)
    wait_for_element(driver, *loc.button_personal_account).click()
    logout_button = wait_for_element(driver, *loc.button_logout)
    assert logout_button.is_displayed()


def test_login_from_personal_account_button(driver, register_new_user, login_user):
    email = generate_unique_email()
    password = generate_random_password()
    register_new_user(email, password)

    driver.get(BASE_URL)
    wait_for_element(driver, *loc.button_personal_account).click()
    login_user(email, password)
    wait_for_element(driver, *loc.button_personal_account).click()
    logout_button = wait_for_element(driver, *loc.button_logout)
    assert logout_button.is_displayed()


def test_login_from_registration_form_button(driver, register_new_user, login_user):
    email = generate_unique_email()
    password = generate_random_password()
    register_new_user(email, password)

    driver.get(BASE_URL + "/register")
    wait_for_element(driver, *loc.button_login_in_registration_form).click()
    login_user(email, password)
    wait_for_element(driver, *loc.button_personal_account).click()
    logout_button = wait_for_element(driver, *loc.button_logout)
    assert logout_button.is_displayed()


def test_login_from_password_recovery_form_button(driver, register_new_user, login_user):
    email = generate_unique_email()
    password = generate_random_password()
    register_new_user(email, password)

    driver.get(BASE_URL + "/forgot-password")
    wait_for_element(driver, *loc.button_login_passwd_recovery_form).click()
    login_user(email, password)
    wait_for_element(driver, *loc.button_personal_account).click()
    logout_button = wait_for_element(driver, *loc.button_logout)
    assert logout_button.is_displayed()

