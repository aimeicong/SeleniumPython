#coding=utf-8
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
# image = image.open("E:/imooc1.png")
# text =pytesseract.image_to_string(image)
# print(text)
r = ShowapiRequest("http://route.showapi.com/932-2","164135","7eb4c4b4448e4fe3a9dad2cd2c8e0e02")
r.addBodyPara("length", "4")
r.addBodyPara("specials", "false")
r.addBodyPara("secure", "false")
r.addBodyPara("image", r"E:/imooc1.png")
res = r.post()
print(res.text)
text = res.json()['showapi_res_body']['code']
print(text) # 返回信息