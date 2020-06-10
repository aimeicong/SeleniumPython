#coding=utf-8
from PIL import Image
from ShowapiRequest import ShowapiRequest
import time
class GetCode:
    def __init__(self,driver):
        self.driver = driver

    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id('getcode_num')
        left = code_element.location['x']
        top = code_element.location['y']
        right = code_element.size['width'] + left
        height = code_element.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
        time.sleep(2)

    # 解析图片，获取验证码
    def code_online(self,file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/932-2", "164135", "7eb4c4b4448e4fe3a9dad2cd2c8e0e02")
        r.addBodyPara("length", "5")
        r.addBodyPara("specials", "false")
        r.addBodyPara("secure", "false")
        r.addFilePara("image", file_name)
        res = r.post()
        print(res.text)
        text = res.json()['showapi_res_body']['code']
        time.sleep(2)
        return text

