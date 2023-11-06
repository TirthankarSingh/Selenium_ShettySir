import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def setup(request):
    browser = request.config.getoption("browser_name")
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )