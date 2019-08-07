import unittest

from count import Count


class Test_sub(unittest.TestCase):
   def setUp(self):
       print('test start')
   def testsub(self):
       self.j = Count(2,3)
       self.sub = self.j.sub()
       return self.assertEqual(self.sub,-1)
   def testsub2(self):
       self.j = Count(21,13)
       self.sub = self.j.sub()
       return self.assertEqual(self.sub,8)
   def tearDown(self):
        print('test end')
if __name__ == '__main__':
    unittest.main()