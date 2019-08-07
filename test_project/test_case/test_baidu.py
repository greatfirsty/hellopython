import unittest

import time
from selenium import webdriver


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

    unittest.main()

