#coding=utf-8
import sys
sys.path.append('E:/PycharmProjects/seleniumPython')
from business.register_business import RegisterBusiness
from selenium import webdriver
from log.user_log import UserLog
import HTMLTestRunner 
import unittest
import os


class FirstCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.logger.info("this is the chrome")
        self.rb = RegisterBusiness(self.driver)
        self.file_name = 'E:/PycharmProjects/seleniumPython/image/test001.png'

    def tearDown(self):
        print('这是后置条件')
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd()+"/report/"+case_name+".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def test_login_email_error(self):
        email_error = self.rb.login_email_error('222@qq.com','user111','11111',self.file_name)
        self.assertFalse(email_error,'此条email的case执行了')


    def test_login_username_error(self):
        username_error = self.rb.login_name_error('222333@qq.com', 'sss', '11111', self.file_name)
        self.assertFalse(username_error)

    def test_login_password_error(self):
        password_error = self.rb.login_password_error('222333@qq.com', 'user11', '1111', self.file_name)
        self.assertTrue(password_error)

    def test_login_code_error(self):
        code_error = self.rb.login_code_error('222333@qq.com', 'user11', '11111', self.file_name)
        self.assertTrue(code_error)

    def test_login_success(self):
        success = self.rb.user_base('2222333@qq.com', 'user111', '11111', self.file_name)
        self.assertFalse(success)


if __name__ == '__main__':
    #file_path = os.path.join('../report/' + 'first_case.html')
    file_path = os.path.join(os.getcwd()+'/report/'+'first_case.html')
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_success'))
    suite.addTest(FirstCase('test_login_email_error'))
    #suite.addTest(FirstCase('test_login_username_error'))
    #suite.addTest(FirstCase('test_login_password_error'))
    #unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2,title='This is first report',description='这是第一个测试报告')
    runner.run(suite)





