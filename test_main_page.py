import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage


link = "http://selenium1py.pythonanywhere.com"


@pytest.mark.login_guest
class TestLoginFromMainPage(object):

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_login_page(browser):
    page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
    page.open()
    page.should_be_login_page()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    page = CartPage(browser, link)
    page.open()
    page.go_to_cart()
    page.should_be_cart_empty()
    page.should_be_text_cart_empty()
