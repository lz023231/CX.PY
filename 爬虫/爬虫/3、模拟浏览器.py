import urllib.request
import random
url = "http://www.baidu.com"
'''
#模拟请求头
headers = {
    "Accept"   : "application/json, text/javascript, */*;q=0.01"
    "X-Requested-With" :"XMLHttpRequest",
    "User-Agnet":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
    "Content-Type" :"application/x-www-from-urlencoded: charset=UTF-8"
}
#设置一个请求体
req = urllib.request.Request(url,headers=headers)
#发起请求
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)
'''

agnetList = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]
agentStr = random.choice(agnetList)
req = urllib.request.Request(url)
#向请求体里添加了User-Agent
req.add_header("User-Agent",agentStr)

response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))

