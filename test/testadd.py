import unittest

from count import Count


class Test_add(unittest.TestCase):
   def setUp(self):
       print('test start')
   def testadd(self):
       self.j = Count(2,3)
       self.add = self.j.add()
       return self.assertEqual(self.add,5)
   def testadd2(self):
       self.j = Count(45,13)
       self.add = self.j.add()
       return self.assertEqual(self.add,58)
   def tearDown(self):
        print('test end')
if __name__ == '__main__':
    unittest.main()


