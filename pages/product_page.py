from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_added(self):
        self.should_be_add_btn()
        self.add_to_cart()
        self.solve_quiz_and_get_code()
        self.write_product_added()
        self.price_true()

    def return_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def return_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def should_be_add_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add Button not found"

    def add_to_cart(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_btn.click()

    def write_product_added(self):
        text = self.browser.find_element(*ProductPageLocators.PROD_IN_CART).text
        assert text == self.return_product_name()

    def price_true(self):
        price_msg = self.browser.find_element(*ProductPageLocators.PRICE_IN_CART).text
        assert price_msg == self.return_product_price()
