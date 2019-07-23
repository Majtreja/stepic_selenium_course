from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_cart_empty(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCT_IN_CART), "The cart is not empty"

    def should_be_text_cart_empty(self):
        text_empty = self.browser.find_element(*CartPageLocators.TEXT_CART_EMPTY).text
        assert text_empty == self.return_text_empty(), "Can't find text cart empty"

    def return_text_empty(self):
        text_empty = self.browser.find_element(*CartPageLocators.TEXT_CART_EMPTY).text
        return text_empty
