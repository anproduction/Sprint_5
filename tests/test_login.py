from data import generate_unique_email, generate_random_password
from helpers import wait_for_element
import locators as loc
from urls import BASE_URL, REGISTER_URL, FORGOT_PASSWORD_URL


class TestLoginFromDifferentPlaces:

    def test_login_from_main_page_button(self, driver, register_new_user, login_user):
        email = generate_unique_email()
        password = generate_random_password()
        register_new_user(email, password)

        driver.get(BASE_URL)
        wait_for_element(driver, *loc.button_login_in_main).click()
        login_user(email, password)
        wait_for_element(driver, *loc.button_personal_account).click()
        assert wait_for_element(driver, *loc.button_logout).is_displayed()


    def test_login_from_personal_account_button(self, driver, register_new_user, login_user):
        email = generate_unique_email()
        password = generate_random_password()
        register_new_user(email, password)

        driver.get(BASE_URL)
        wait_for_element(driver, *loc.button_personal_account).click()
        login_user(email, password)
        wait_for_element(driver, *loc.button_personal_account).click()
        assert wait_for_element(driver, *loc.button_logout).is_displayed()


    def test_login_from_registration_form_button(self, driver, register_new_user, login_user):
        email = generate_unique_email()
        password = generate_random_password()
        register_new_user(email, password)

        driver.get(REGISTER_URL)
        wait_for_element(driver, *loc.button_login_in_registration_form).click()
        login_user(email, password)
        wait_for_element(driver, *loc.button_personal_account).click()
        assert wait_for_element(driver, *loc.button_logout).is_displayed()


    def test_login_from_password_recovery_form_button(self, driver, register_new_user, login_user):
        email = generate_unique_email()
        password = generate_random_password()
        register_new_user(email, password)

        driver.get(FORGOT_PASSWORD_URL)
        wait_for_element(driver, *loc.button_login_passwd_recovery_form).click()
        login_user(email, password)
        wait_for_element(driver, *loc.button_personal_account).click()
        assert wait_for_element(driver, *loc.button_logout).is_displayed()
