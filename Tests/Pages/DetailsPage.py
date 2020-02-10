from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Pages.Page import Page


class DetailsPage(Page):
    search_button = (By.CSS_SELECTOR, ".btn-primary")
    car_information_header = (By.CSS_SELECTOR, ".card-header")

    def check_proper_values(self):
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.car_information_header))
        assert self.browser.page_source.find("Toyota Aygo")
        assert self.browser.page_source.find("Location: Poland, Warsav")
        assert self.browser.page_source.find("Pickup date: 2020-01-03")
        assert self.browser.page_source.find("Dropoff date: 2020-01-10")

    def click_search_button1(self):
        self.browser.find_element(*self.search_button).click()