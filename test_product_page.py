from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.product_added()
