from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/rawradx/Documents/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://www.javatpoint.com/selenium-features')
#print("success")
driver.quit()

