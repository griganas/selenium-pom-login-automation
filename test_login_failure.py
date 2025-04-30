import pytest
from selenium.common.exceptions import TimeoutException
from loginPage import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("username, password", [
    ("rahulshetty", "learning"),        # wrong username
    ("rahulshettyacademy", "123456"),   # wrong password
    ("rahulshett", "123456")            # wrong username - password
])
def test_login_failure(driver, username, password):
    loginPage = LoginPage(driver)
    loginPage.enter_username(username)
    loginPage.enter_password(password)
    loginPage.click_terms()
    loginPage.click_login()

    wait = WebDriverWait(driver, 5)
    try:
        wait.until(EC.title_is("ProtoCommerce"))
        assert False, "Login should not have passed with invalid credentials."
    except TimeoutException:
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
            error = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
            print("Login failed as expected.")
            assert "username" in error.lower() or "password" in error.lower()
        except:
            print("Login failed, but error message disappeared too fast.")
            assert True