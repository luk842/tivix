
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Page import Page


class ThankYouPage(Page):
    url = "/"

    notification_locator = (By.ID, "notyfication")

    def check_confirmation(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.notification_locator))
        assert self.browser.page_source.find("Your rent a car!")