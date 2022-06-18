from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Suman:
    def Suman_Alert_Box(self, url):
        driver = webdriver.Firefox()
        driver.get(url)
        alert_button = driver.find_element(by=By.ID, value='btn1')
        alert_button.click()
        alert_box_object = driver.switch_to.alert
        print(alert_box_object.text)
        time.sleep(5)
        alert_box_object.accept()
        driver.close()

    def Suman_Confirm_Box(self,url):
        driver = webdriver.Firefox()
        driver.get(url)
        confirm_button = driver.find_element(by=By.ID, value='btn2')
        confirm_button.click()
        time.sleep(5)
        confirm_button_object = driver.switch_to.alert
        time.sleep(10)
        confirm_button_object.accept()

url = 'http://127.0.0.1:5500/index.html'
# Suman().Suman_Alert_Box(url)

Suman().Suman_Confirm_Box(url)
