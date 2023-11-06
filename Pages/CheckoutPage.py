from selenium.webdriver.common.by import By


class CheckOutPage:
    productList = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOutButton = (By.XPATH, "//*[contains(text(),'Checkout')]")

    def __init__(self, driver):
        self.driver = driver

    def getProducts(self):
        return self.driver.find_elements(*CheckOutPage.productList)

    def getcardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkout(self):
        return self.driver.find_element(*CheckOutPage.checkOutButton)