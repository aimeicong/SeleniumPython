#coding=utf-8
import ddt
import unittest
import sys
sys.path.append('E:/PycharmProjects/seleniumPython')
from business.register_business import RegisterBusiness
from selenium import webdriver
import HTMLTestRunner
import os
from util.excel_util import ExcelUtil
import time

ex = ExcelUtil()
data = ex.get_data()
# 邮箱、 用户名 、密码 、验证码、错误信息定位元素、错误提示信息
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.rb = RegisterBusiness(self.driver)
        self.file_name = 'E:/PycharmProjects/seleniumPython/image/test001.png'

    def tearDown(self):
        time.sleep(2)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()
    '''
    @ddt.data(
        ['12', 'Mushishi01', '111111', 'E:/PycharmProjects/seleniumPython/image/test001.png', 'user_email_error', '请输入有效的电子邮件地址'],
        ['@qq.com', 'Mushishi01', '111111', 'E:/PycharmProjects/seleniumPython/image/test001.png', 'user_email_error', '请输入有效的电子邮件地址'],
        ['12@qq.com', 'Mushishi01', '111111', 'E:/PycharmProjects/seleniumPython/image/test001.png', 'user_email_error', '请输入有效的电子邮件地址']
    )
    @ddt.unpack
    '''
    @ddt.data(*data)
    def test_register_case(self, data):
        email, username, password, self.file_name, assertCode, assertText = data
        email_error = self.rb.register_function(email, username, password, self.file_name, assertCode, assertText)
        self.assertFalse(email_error,'测试失败')

if __name__ == '__main__':
    file_path = os.path.join(os.getcwd() + '/report/' + 'first_case1.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2,title='This is first report1',description='这是第一个测试报告1')
    runner.run(suite)

