from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome('D:\chromedriver')
#driver.get('http://jqueryui.com/droppable')
driver.maximize_window()
time.sleep(2)