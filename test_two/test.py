import unittest

class My_test(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @unittest.skip('直接跳过测试')
    def test_skip(self):
        print('test skip!')
    @unittest.skipIf(3>2,'当条件为TRUE,跳过测试')
    def test_skip_if(self):
        print('the condition if ,test skip')
    @unittest.skipUnless(3>2,'当条件为TRUE，执行测试')
    def test_skip_unless(self):
        print('但条件为真时，执行测试')

if __name__ == '__main__':
    unittest.main()