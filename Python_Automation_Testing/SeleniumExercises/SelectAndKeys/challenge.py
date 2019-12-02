from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('D:\chromedriver')
driver.get('https://wiki.python.org/moin/FrontPage')
driver.maximize_window()

search_box = driver.find_element_by_id('searchinput')
search_box.send_keys('Beginner')
time.sleep(2)
search_box.send_keys(Keys.RETURN)

time.sleep(2)

action_menu = Select(driver.find_element_by_xpath("//select[@name='action']"))
time.sleep(2)
action_menu.select_by_value('raw')
time.sleep(2)

time.sleep(2)

driver.close()