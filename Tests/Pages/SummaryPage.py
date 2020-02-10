from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from Pages.Page import Page


class SummaryPage(Page):
    rent_form_locator = (By.ID, "rent_form")
    search_button = (By.CSS_SELECTOR, ".btn-primary")
    name_selector = (By.ID, "name")
    last_name_selector = (By.ID, "last_name")
    card_number_selector = (By.ID, "card_number")
    email_selector = (By.ID, "email")

    def check_all_values(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.rent_form_locator))
        assert self.browser.page_source.find("Location: Poland, Warsav")
        assert self.browser.page_source.find("Pickup date: 2020-01-03")
        assert self.browser.page_source.find("Dropoff date: 2020-01-10")

    def fill_all_fields(self):
        self.browser.find_element(*self.name_selector).send_keys("Test-name")
        self.browser.find_element(*self.last_name_selector).send_keys("Test-last-name")
        self.browser.find_element(*self.card_number_selector).send_keys("9999999999")
        self.browser.find_element(*self.email_selector).send_keys("test@test.pl")

    def click_search_button(self):
        self.browser.find_element(*self.search_button).click()
