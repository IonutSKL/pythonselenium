from Python_Automation_Testing import config
import time

config.driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

message = config.driver.find_element_by_xpath('//*[@id="user-message"]')
message.send_keys('test')

send_button = config.driver.find_element_by_xpath('//*[@id="get-input"]/button')
send_button.click()

time.sleep(5)
config.driver.close()