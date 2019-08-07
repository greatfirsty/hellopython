import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


class BaiDuTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)#页面元素的隐形等待时间30
        self.base_url = 'http://www.baidu.com/'
        self.verificationError = []
        self.accept_next_alert = True
        #进行初始化工作，定义浏览器启动器和url地址


    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url+'/')
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('美女')
        driver.find_element_by_id('su').click()
    def is_element_present(self,how,what):#检查查找页面元素是否存在
        #如果定位到元素，返回TRUE
        try:
            self.driver.find_element(by=how,value=what)
        except NoSuchElementException as e:
            return e
        return True
    #
    def is_alert_present(self):
        #检验是否出现警示框
        try:
            self.driver.switch_to.alert()

        except NoAlertPresentException as e:
            return e
        return True
    def close_alert_add_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text #返回警示信息
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()#忽略警示信息
            return alert_text
        finally:
            self.accept_next_alert = True
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationError)#最后清理工作空，定义了空数组
        #如果数组为空，表明没有出现异常
if __name__ == '__main__':
    unittest.main()





