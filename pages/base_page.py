from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage(object):

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_link_present(self):
        try:
            self.browser.current_url()
        except NoSuchElementException:
            return False
        return True

    def __init__(self, browser, url, timeout=10):
        self.browser: WebDriver = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
