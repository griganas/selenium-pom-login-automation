import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    URL = "https://rahulshettyacademy.com/loginpagePractise/"
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(4)
    driver.maximize_window()

    driver.get(URL)

    yield driver
    driver.quit()
