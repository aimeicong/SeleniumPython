#coding=utf-8
import unittest


class FirstCase01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('所有case执行之前的前置')

    @classmethod
    def tearDownClass(cls):
        print('所有case执行之后的后置')

    def setUp(self):
        print('这个是case的前置条件')

    def tearDown(self):
        print('这个是case的后置条件')

    @unittest.skip('不执行第一条')
    def test01(self):
        print('这是第一条case')

    def test02(self):
        print('这是第二条case')

    def test03(self):
        print('这是第三条case')


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('test02'))
    suite.addTest(FirstCase01('test01'))
    suite.addTest(FirstCase01('test03'))
    unittest.TextTestRunner().run(suite)