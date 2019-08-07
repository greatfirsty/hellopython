import unittest

import testadd
import testsub

suite = unittest.TestSuite()
suite.addTest(testadd.Test_add('testadd'))
suite.addTest(testadd.Test_add('testadd2'))
suite.addTest(testsub.Test_sub('testsub'))
suite.addTest(testsub.Test_sub('testsub2'))
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)