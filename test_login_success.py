from conftest import driver
from loginPage import LoginPage
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_login_success(driver):
    loginPage = LoginPage(driver)
    loginPage.enter_username("rahulshettyacademy")
    loginPage.enter_password("learning")
    loginPage.click_terms()
    loginPage.click_login()

    wait = WebDriverWait(driver, 5)

    wait.until(EC.title_is("ProtoCommerce"))
    print("Login successful!")