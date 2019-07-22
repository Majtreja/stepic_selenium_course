from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM_ID = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_ID = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-lg.btn-primary.btn-add-to-basket")
