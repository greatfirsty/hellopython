import unittest

import time
from HtmlTestRunner import HTMLTestRunner
test_dir = '../test_project/test_case'
discovery = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
if __name__ == '__main__':
    now = time.strftime('%Y_m_d %H_%M_%S')
    filename =test_dir+ './'+now + 'result.html'
    fp = open(filename,'w')
    runner = HTMLTestRunner(stream=fp,report_title='测试报告',descriptions='用例执行情况')
    runner.run(discovery)
    fp.close()
