'''
Using a python library like qrcode and pillow and converting url to qrcode
'''

import qrcode

url = input("Enter your url: ")
filename= input("By which filename you want to save it as: ")
if not(filename.endswith(".png")):
    filename = filename + ".png"

img = qrcode.make(url)
img.save(filename)



