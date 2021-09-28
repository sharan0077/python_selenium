import time

from selenium import webdriver

driver = webdriver.Chrome("C:/Users/HP/PycharmProjects/seleniumProject/drivers/chromedriver.exe")

driver.set_page_load_timeout(10)

driver.get("https://www.google.com/")

time.sleep(5)

driver.quit()

