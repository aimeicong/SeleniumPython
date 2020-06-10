#code=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest


driver = webdriver.Chrome()
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(5)

#获取element信息
def get_elemnt(id):
    element = driver.find_element_by_id(id)
    return element
#获取随机数
def get_range_user():
    user_info = ''.join(random.sample('1234567890abcdefg', 6))
    return user_info

#获取图片
def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_id('getcode_num')
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    im = Image.open(file_name)
    img = im.crop((left, top, right, height))
    img.save(file_name)

#解析图片，获取验证码
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/932-2", "164135", "7eb4c4b4448e4fe3a9dad2cd2c8e0e02")
    r.addBodyPara("length", "5")
    r.addBodyPara("specials", "false")
    r.addBodyPara("secure", "false")
    r.addBodyPara("image", file_name)
    res = r.post()
    print(res.text)
    text = res.json()['showapi_res_body']['code']
    return text

#运行主程序
def run_main():
    user_name_info = get_range_user()
    user_email = user_name_info+'@163.com'
    file_name = 'E:/PycharmProjects/seleniumPython/image/test02.png'
    driver_init()
    get_elemnt("register_email").send_keys(user_email)
    get_elemnt("register_nickname").send_keys(user_name_info)
    get_elemnt('register_password').send_keys('111111')
    get_code_image(file_name)
    text = code_online(file_name)
    get_elemnt('captcha_code').send_keys(text)
    get_elemnt('register-btn').click()
    driver.close()

run_main()
