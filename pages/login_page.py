from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "what page are we on?)"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "no login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTER), "no registration form"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAI_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_AGAIN_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION).click()
