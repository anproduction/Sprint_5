import pytest
from data import TEST_USER, BASE_URL
import locators as loc
from helpers import wait_for_element


@pytest.fixture
def driver():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def register_new_user(driver):
    def _register(email, password):
        driver.get(BASE_URL + "/register")
        wait_for_element(driver, *loc.input_name).send_keys(TEST_USER["name"])
        wait_for_element(driver, *loc.input_email).send_keys(email)
        wait_for_element(driver, *loc.input_password).send_keys(password)
        wait_for_element(driver, *loc.button_submit).click()
        wait_for_element(driver, *loc.button_login)
    return _register


@pytest.fixture
def login_user(driver):
    def _login(email, password):
        driver.get(BASE_URL + "/login")
        wait_for_element(driver, *loc.input_email_auth).send_keys(email)
        wait_for_element(driver, *loc.input_password_auth).send_keys(password)
        wait_for_element(driver, *loc.button_login).click()
        wait_for_element(driver, *loc.button_personal_account)
    return _login