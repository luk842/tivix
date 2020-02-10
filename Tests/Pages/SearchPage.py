from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Configs import config

from Pages.Page import Page


class SearchPage(Page):
    url = "/"

    country_locator = (By.CSS_SELECTOR, "#country > option:nth-child(3)")
    city_locator = (By.CSS_SELECTOR, "#city > option:nth-child(4)")
    car_model_locator = (By.ID, "model")
    pick_up_date_locator = (By.ID, "pickup")
    drop_off_date_locator = (By.ID, "dropoff")
    search_button = (By.CSS_SELECTOR, ".btn-primary")
    search_results = (By.CSS_SELECTOR, "tr:nth-child(1) td:nth-child(7) > a.btn.btn-success")

    def go_to_page1(self):
        self.browser.get(config.url_address)
        WebDriverWait(self.browser, 15).until(EC.url_changes)

    def fill_all_mandatory_fields(self):
        self.browser.find_element(*self.country_locator).click()
        self.browser.find_element(*self.city_locator).click()
        self.browser.find_element(*self.car_model_locator).send_keys("Toyota")
        self.browser.find_element(*self.pick_up_date_locator).send_keys("03.01.2020")
        self.browser.find_element(*self.drop_off_date_locator).send_keys("10.01.2020")
        self.browser.find_element(*self.search_button).click()

    def click_search_button(self):
        self.browser.find_element(*self.search_button).click()

    def check_search_results(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.search_results))
        assert self.browser.page_source.find("Toyota")

    def select_car_from_the_list(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.search_results))
        self.browser.find_element(*self.search_results).click()

