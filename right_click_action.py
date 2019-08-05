from selenium import webdriver
from selenium.webdriver import ActionChains

dr = webdriver.Chrome()
dr.get('https://yunpan.360.cn/')
account = dr.find_element_by_name("account")
account.clear()
account.send_keys('183xxxx')

password = dr.find_element_by_name("password")
password.clear()
password.send_keys('hxxxxxxx')
left = dr.find_element_by_xpath("//input[@class='quc-submit quc-button quc-button-primary quc-button-sign-in']")
ActionChains(dr).context_click(left).perform()
#这里是鼠标右击操作，单击直接可以click
