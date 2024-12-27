import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

service_obj = Service("C:/Users/rawradx/Downloads/edgedriver_win64/msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
driver.implicitly_wait(15)
driver.get('https://chatgpt.com/')
chatgpt = driver.find_element(By.CSS_SELECTOR,".placeholder")
chatgpt.send_keys("Explain about selenium")
chatgpt.send_keys(Keys.RETURN)
#driver.find_element(By.CSS_SELECTOR,".icon-2xl").click()
time.sleep(4)