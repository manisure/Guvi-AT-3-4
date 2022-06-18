from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Firefox()
action = ActionChains(driver)
driver.get('https://www.w3schools.com/')


login_button = driver.find_element(by=By.ID, value='w3loginbtn')

logo = driver.find_element(by=By.XPATH, value='/html/body/div[3]/a[1]/i')

action.context_click(logo)
time.sleep(10)
action.click(login_button)

action.perform()
