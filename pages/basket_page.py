from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):

    def no_product_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCT_IN_BASKET), "product in basket"

    def message_product_not_in_basket(self):
        assert self.is_element_present(*BasePageLocators.MESSAGE_NO_PRODUCT), \
            'There is no text that the cart is empty!'
