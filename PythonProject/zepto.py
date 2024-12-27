import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/rawradx/Documents/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get('https://www.zeptonow.com/')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"input[id=':r2:--input']").send_keys("Chocolates")

#print("success")
driver.quit()

