from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage(object):

    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url):
        self.browser: WebDriver = browser
        self.url = url
