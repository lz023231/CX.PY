import urllib.request
import urllib.response
import re
import ssl
def jokeCrawler(url):
    headers = {
        "User-Agnet": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)

    HTML = response.read().decode("utf-8")

    pat = r''
    re_joke = re.compile(pat,re.S)
    divsList=re_joke.findall(HTML)
    with open(r"E:\CX.PY\爬虫\file\file4.html","w") as f:
        f.write(HTML)
    for div in divsList:
        #提取用户名
        re_u = re.compile(r"")
        username = re_u.findall(div)

url = "https://www.qiushibaike.com/text/page/2/"
info = jokeCrawler(url)















