from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Suman:

    driver = webdriver.Firefox()

    # use the ID selector
    def ID_Usage(self, link_id, url):
        try:
            self.driver.get(url)
            link_id = self.driver.find_element(by=By.ID, value=link_id)
            if link_id:
                time.sleep(5)
                link_id.click()
        except:
            print('ERROR : ID not Found !')

    # use of the CLASS selector
    def Class_Usage(self,class_link,url):
        try:
            self.driver.get(url)
            class_link = self.driver.find_element(by=By.CLASS_NAME, value=class_link)
            if class_link:
                time.sleep(5)
                class_link.click()
        except:
            print('ERROR : CLASS not found !')

s = Suman()

url = "https://www.w3schools.com/"

id_1 = "w3loginbtn"

class_1 = "w3-hover-text-green"

s.Class_Usage(class_1,url)

# s.ID_Usage(id_1,url)
