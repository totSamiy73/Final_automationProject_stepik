from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):
    def add_to_basket(self):
        add = self.browser.find_element(*ProductPageLocator.BUTTON_BASKET)
        add.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocator.BUTTON_ADD_TO_BASKET), \
            "not button add to basket"

    def message_added_to_basket(self):
        assert self.is_element_present(*ProductPageLocator.GOOD_ADDED_MESSAGE), \
            "no message about adding to cart"

    def name_product_in_message(self):
        if (self.is_element_present(*ProductPageLocator.NAME_PRODUCT) and
                self.is_element_present(*ProductPageLocator.GOOD_NAME_IN_MESSAGE)):
            assert (self.browser.find_element(*ProductPageLocator.NAME_PRODUCT).text ==
                    self.browser.find_element(*ProductPageLocator.GOOD_NAME_IN_MESSAGE).text), \
                "Product name does not match the product added"
        else:
            raise Exception("No element or some other error in /def name_product_in_message/")

    def message_cart_cost(self):
        assert self.is_element_present(*ProductPageLocator.MESSAGE_CART_COST), "No message with cart value"

    def cart_price_same_as_the_product(self):
        if (self.is_element_present(*ProductPageLocator.PRICE_PRODUCT) and
                self.is_element_present(*ProductPageLocator.CART_PRICE)):
            assert (self.browser.find_element(*ProductPageLocator.NAME_PRODUCT).text ==
                    self.browser.find_element(*ProductPageLocator.GOOD_NAME_IN_MESSAGE).text), \
                "The price of the cart does not match the price of the product"
        else:
            raise Exception("No element or some other error in /def cart_price_same_as_the_product/")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocator.GOOD_ADDED_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocator.GOOD_ADDED_MESSAGE), \
            "Success message is presented, but should disappear"
