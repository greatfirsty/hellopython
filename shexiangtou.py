import unittest

from right_click_action import Count


class Test(unittest.TestCase):
    def setUp(self,):
        print('test starting')

    def test_case(self):
        self.assertEqual(self.number,10,msg = 'you number is not 10!')
    def test_add(self):
        self.j =Count(2,3)
        self.add = self.j.add()
        self.assertEqual(self.add,5)
    def test_add2(self):
        self.j = Count(2.0,3.0)
        self.add = self.j.add()
        self.assertEqual(self.add,5.0)
    def test_add3(self):
        self.j = Count('hello','world')
        self.add = self.j.add()
        self.assertEqual(self.add,'hello world')
    def test_sub(self):
        self.j = Count(2.1,3)
        self.sub = self.j.sub()
        self.assertEqual(self.sub,-0.9)

    def tearDown(self):
        pass
class Test_Sub(unittest.TestCase):
    def setUp(self):
        print('test start')

    def test_sub(self):
        self.j =Count(2.3,3.0)
        self.sub = self.j.sub()
        self.assertEqual(self.sub,-0.7)
    def tearDown(self):
        pass
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Test('test_add'))
    suite.addTest(Test('test_add2'))
    suite.addTest(Test('test_add3'))
    suite.addTest(Test_Sub('test_sub'))
    runner = unittest.TextTestRunner()
    runner.run(suite)


