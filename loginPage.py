from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.checkbox = (By.CSS_SELECTOR, "span.text-white.termsText")
        self.login_button = (By.ID, "signInBtn")
        self.error_message = (By.CSS_SELECTOR, ".alert-danger")

    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_terms(self):
        self.driver.find_element(*self.checkbox).click()

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text