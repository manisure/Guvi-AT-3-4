from selenium import webdriver

class Suman:
    driver = webdriver.Firefox()

    # fetch the TITLE of any website using Python Selenium
    def get_title(self, url):
        self.driver.get(url)
        return self.driver.title

    # fetch the URL of any website
    def get_url(self,url):
        self.driver.get(url)
        return self.driver.current_url

    # fetch the entire webpage of any website
    def get_webpage(self,url):
        self.driver.get(url)
        return self.driver.page_source



url = "https://www.google.in"

s = Suman()

print(s.get_webpage(url))
