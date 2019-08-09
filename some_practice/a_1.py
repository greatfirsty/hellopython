import time
from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('美女')
driver.find_element_by_id('su').click()
driver.get_screenshot_as_file('./get_baidu.jpg',)
time.sleep(5)
driver.quit()

