from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_added(self):
        self.should_be_add_btn()
        self.add_to_cart()
        self.solve_quiz_and_get_code()
        self.write_product_added()
        self.price_true()

    def should_be_add_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add Button not found"

    def add_to_cart(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_btn.click()

    def write_product_added(self):
        text = self.browser.find_element_by_css_selector('#messages > div:nth-child(1) > div > strong').text
        text_example = "The shellcoder's handbook"
        assert text == text_example

    def price_true(self):
        price_msg = self.browser.find_element_by_css_selector('#messages > div:nth-child(3) >div > p > strong').text
        price_example = "£9.99"
        assert price_msg == price_example
