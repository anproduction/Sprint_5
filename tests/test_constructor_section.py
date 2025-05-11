from data import BLOCKS
from helpers import wait_for_element
import locators as loc
from urls import BASE_URL

class TestConstructorSections:

    def test_buns_section(self, driver):
        driver.get(BASE_URL)
        wait_for_element(driver, *loc.sauces_block).click()
        wait_for_element(driver, *loc.buns_block).click()
        selected = wait_for_element(driver, *loc.selected_button)
        assert BLOCKS["buns"] in selected.text


    def test_sauces_section(self, driver):
        driver.get(BASE_URL)
        wait_for_element(driver, *loc.sauces_block).click()
        selected = wait_for_element(driver, *loc.selected_button)
        assert BLOCKS["sauces"] in selected.text


    def test_fillings_section(self, driver):
        driver.get(BASE_URL)
        wait_for_element(driver, *loc.fillings_block).click()
        selected = wait_for_element(driver, *loc.selected_button)
        assert BLOCKS["fillings"] in selected.text
