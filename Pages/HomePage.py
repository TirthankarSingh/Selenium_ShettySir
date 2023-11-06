from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[text()='Shop']")

    def shopItem(self):
        return self.driver.find_element(*HomePage.shop)
