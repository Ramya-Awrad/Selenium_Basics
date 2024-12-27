import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/rawradx/Documents/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://www.linkedin.com/login')
driver.find_element(By.ID,'username').send_keys('Username')
driver.find_element(By.ID,'password').send_keys('password')
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(4)