import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/rawradx/Documents/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/')
print(driver.title)
driver.maximize_window()

time.sleep(2)