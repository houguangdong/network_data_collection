#-*- coding:utf8 -*-
'''
Created on 12/11/2016

@author: ghou
'''

'''
图像识别与文字处理
'''


from PIL import Image, ImageFilter

kitten = Image.open("kitten.jpg")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("kitten_blurred.jpg")
blurryKitten.show()
