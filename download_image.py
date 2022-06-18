from selenium import webdriver
from selenium.webdriver.common.by import By

# Download an Image using Python Selenium
def Suman_Download_Image(url):
    driver = webdriver.Firefox()
    driver.get(url)
    with open('ALPHA_ROMEO.png', 'wb') as file:
        image_xpath = driver.find_element(by=By.XPATH, value='/html/body/img')
        file.write(image_xpath.screenshot_as_png)
    driver.quit()

url = 'http://127.0.0.1:5500/index.html'

Suman_Download_Image(url)
