from data import BASE_URL
from helpers import wait_for_element
import locators as loc


def test_buns_section(driver):
    driver.get(BASE_URL)
    wait_for_element(driver, *loc.sauces_block).click()
    wait_for_element(driver, *loc.buns_block).click()
    selected = wait_for_element(driver, *loc.selected_button)
    assert "Булки" in selected.text


def test_sauces_section(driver):
    driver.get(BASE_URL)
    wait_for_element(driver, *loc.sauces_block).click()
    selected = wait_for_element(driver, *loc.selected_button)
    assert "Соусы" in selected.text


def test_fillings_section(driver):
    driver.get(BASE_URL)
    wait_for_element(driver, *loc.fillings_block).click()
    selected = wait_for_element(driver, *loc.selected_button)
    assert "Начинки" in selected.text
