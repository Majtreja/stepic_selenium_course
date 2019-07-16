class BasePage(object):

    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
