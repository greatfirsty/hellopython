
import unittest

import time
from selenium import webdriver


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = 'http:// www.youdao.com'
    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url+'/')
        driver.find_element_by_id('query').clear()
        driver.find_element_by_id('query').send_keys('美女')
        driver.find_element_by_id('qb').click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title,'webdriver_有道搜索')
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
