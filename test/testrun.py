import unittest
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)
#自动根据测试目录匹配查找文件，并将查找到的测试用例组装到测试套装中，通过run方法进行测试