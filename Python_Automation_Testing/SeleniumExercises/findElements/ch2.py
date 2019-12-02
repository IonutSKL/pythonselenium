import time
from selenium import webdriver

driver = webdriver.Chrome('D:\chromedriver')  # Optional argument, if not specified will search path.
driver.get('file:///D:/LinkedIn%20Trainings/Python%20Testing%20Automation/Python_Automation_Testing/Exercise%20Files/CH02/html_code_02.html')

login_form = driver.find_element_by_id('loginForm')
print('login form is: ', login_form)

username = driver.find_element_by_name('username')
print('username is: ', username)

login_form_absolute = driver.find_element_by_xpath('/html/body/form[1]/input')
login_form_relative = driver.find_element_by_xpath('//form[1]/input')
login_form_id = driver.find_element_by_xpath("//input[@name='username']")
username.send_keys('scarlat')

content = driver.find_element_by_class_name('content')

print("content", content)
print("abs:", login_form_absolute)
print("relative:", login_form_relative)
print("id:", login_form_id)

time.sleep(5)
driver.close()