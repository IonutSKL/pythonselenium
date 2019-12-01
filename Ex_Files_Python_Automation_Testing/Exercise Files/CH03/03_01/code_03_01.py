from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('D:\chromedriver')
driver.get("http://python.org")

search = driver.find_element_by_name('q')
search.clear()
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.close()
