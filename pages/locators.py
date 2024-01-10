from selenium.webdriver.common.by import By


class MainPageLocators():
    pass
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    FORM_REGISTER = (By.ID, "register_form")
    EMAI_INPUT = (By.ID, "id_registration-email")
    PASSWORD_INPUT = (By.ID, "id_registration-password1")
    PASSWORD_AGAIN_INPUT = (By.ID, "id_registration-password2")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "#register_form > button")


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


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_LOOK_BASKET = (By.CSS_SELECTOR, 'span > a')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.hidden-xs > div > h2')
    MESSAGE_NO_PRODUCT = (By.CSS_SELECTOR, '#content_inner>p')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
