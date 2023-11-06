import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Pages.ConfirmPage import ConfirmPage
from Pages.HomePage import HomePage
from Pages.CheckoutPage import CheckOutPage
from Utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions


class TestOne(BaseClass):

    def test_e2e(self, setup):
        homePage = HomePage(self.driver)
        homePage.shopItem().click()
        checkoutPage = CheckOutPage(self.driver)
        products = checkoutPage.getProducts()
        i = -1
        for product in products:
            i+=1
            productName = product.text
        #     print(productName)
        #     productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                # product.checkoutPage.addCart().click()
                checkoutPage.getcardFooter()[i].click()

        checkoutPage.checkout().click()
        checkoutPage.checkout().click()
        confirm = ConfirmPage(self.driver)
        confirm.location().send_keys("ind")
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        # self.driver.find_element(By.LINK_TEXT, "India").click()
        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        # self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        # successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        # assert "Success! Thank you!" in successText
        # self.driver.close()
