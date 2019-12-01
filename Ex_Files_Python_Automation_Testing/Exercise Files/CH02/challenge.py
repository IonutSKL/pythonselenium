import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('D:\chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://selenium.dev/')

search_box = driver.find_element_by_xpath("//input[@id='gsc-i-id1']")
search_box.send_keys('Selenium')
search_box.send_keys(Keys.RETURN)
print("search_box element: ", search_box)

#element_id = driver.find_element_by_id('q')
#print(element_id)

#element_name = driver.find_element_by_name('q')
#print(element_name)

#heading = driver.find_element_by_xpath("//section[@class='hero homepage']/h1")
#print('header', heading)

#sub_header = driver.find_element_by_xpath("//h1[@class='sub-header']")
#print('sub-header', sub_header)

#element_classname = driver.find_element_by_class_name('selenium-sponsors')
#print('classname', element_classname)

time.sleep(5)
driver.close()