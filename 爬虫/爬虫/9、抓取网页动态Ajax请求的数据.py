import urllib.request
import ssl
import json

def ajaxCrawler(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    }
    req = urllib.request.Request(url,headers=headers)
    #使用ssl创建未验证的上下文
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req,context=context)


    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)

    return jsonData
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20"
info = ajaxCrawler(url)

print(info)


for i in (1,11):
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="+str(i * 20) +" &limit=20"
    info = ajaxCrawler(url)
    print(info)






