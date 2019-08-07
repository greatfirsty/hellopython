import unittest

import time
from selenium import webdriver
from HtmlTestRunner import HTMLTestRunner

class My_Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = 'http://www.baidu.com/'
    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url+'/')
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('美女')
        driver.find_element_by_id('su').click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title,'unittest_百度搜索')
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':

   testnit = unittest.TestSuite()
   testnit.addTest(My_Test('test_baidu'))
   fp = open('./result.html','wb')
   runner = HTMLTestRunner(stream=fp,
                           report_title='百度搜索用例报告',
                           descriptions='用例执行情况'
   )
   runner.run(testnit)
   fp.close()

#通过以上办法无法生成测试报告，最简单的办法看连接
#https://blog.csdn.net/weixin_38981172/article/details/82389416