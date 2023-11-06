from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    CountrySelect = (By.LINK_TEXT, "India")
    locationSelect = (By.ID, "country")

    def country(self):
        return self.driver.find_element(*ConfirmPage.CountrySelect)

    def location(self):
        return self.driver.find_element(*ConfirmPage.locationSelect)

