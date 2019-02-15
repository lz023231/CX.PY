'''
特点：把参数打包，单独传输

优点：数量大，安全

缺点：速度慢

'''

import urllib.request
import urllib.parse

url = "http://www.sunck.wang:8085/form"

#将要发送的数据合成一个字典，字典的键去网址里找，一般为input标签的name属性的值
data = {
    "username":"sunck",
    "passwd":"666"
}
#对要发送的数据进行打包,记住编码
postData = urllib.parse.urlencode(data).encode("utf-8")
#创建请求体
req = urllib.request.Request(url,postData)

#发起请求
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
















