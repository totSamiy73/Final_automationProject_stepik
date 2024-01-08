from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    FORM_REGISTER = (By.ID, "register_form")

class ProductPageLocator:
    BUTTON_BASKET = (By.ID, "add_to_basket_form")
    BUTTON_ADD_TO_BASKET = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    GOOD_ADDED_MESSAGE = (By.CSS_SELECTOR,
                          "div[class='alert alert-safe alert-noicon alert-success  fade in']:nth-child(1)")
    GOOD_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, "div[class = 'col-sm-6 product_main']>h1")
    MESSAGE_CART_COST = (By.XPATH, '//*[@id="messages"]/div[3]')
    CART_PRICE = (By.CSS_SELECTOR, 'div.alert > div > p:nth-child(1) > strong')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main > p.price_color')
