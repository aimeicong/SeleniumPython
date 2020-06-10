#coding=utf-8
from selenium import webdriver
import time
import random
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
driver.maximize_window()
time.sleep(5)
print(EC.title_contains("注册"))
email_element = driver.find_element_by_id("register_email")
driver.save_screenshot('E:/Imooc/imooc2.png')
code_element = driver.find_element_by_id('getcode_num')
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open("E:/Imooc/imooc2.png")
img = im.crop((left, top, right, height))
img.save("E:/Imooc/imooc3.png")

r = ShowapiRequest("http://route.showapi.com/932-2","164135","7eb4c4b4448e4fe3a9dad2cd2c8e0e02")
r.addBodyPara("length", "5")
r.addBodyPara("specials", "false")
r.addBodyPara("secure", "false")
r.addBodyPara("image", r"E:/imooc1.png")
res = r.post()
print(res.text)
text = res.json()['showapi_res_body']['code']
print(text)
time.sleep(2)
driver.find_element_by_id('captcha_code').send_keys(text)

# for i in range(5):
#     user_email = ''.join(random.sample('1234567890abcdefg', 6))
#     print(user_email)

locator = (By.CLASS_NAME, "controls")
WebDriverWait(driver, 2).until(EC.visibility_of_element_located(locator))
print(email_element.get_attribute('placeholder'))
email_element.send_keys("test@163.com")
print(email_element.get_attribute('value'))
time.sleep(5)
driver.close()
