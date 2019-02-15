
'''
Mac:无需安装
Linux:无需安装
windows:勾选了pip

'''
#安装三方模块，需要知道模块的名字
#Pillow   非常强大的处理图像的工具库
#引入了三方库
from PIL import Image

#打开图片
im = Image.open("313824.jpg")
#查看图片信息
print(im.format, im.size, im.mode)

#设置图片的大小
im.thumbnail((192, 108))
#保存成新图片
im.save("temp.jpg", "JPEG")

















