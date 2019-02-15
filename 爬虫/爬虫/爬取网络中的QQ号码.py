import urllib.request
import ssl
import re
import os
from collections import deque


def writeFlieBytes(htmlBytes,topath):
    with open(topath,"wb") as f:
        f.write(htmlBytes)
def writeFileStr(htmlBytes,topath):
    with open(topath,"w") as f:
        f.write(str(htmlBytes))

def  getHtmlBytes(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)
    return response.read()

def qqCrawler(url,topath):
    htmlBytes = getHtmlBytes(url)
    #writeFlieBytes(htmlBytes,r"E:\CX.PY\爬虫\file\qqFile1.html")
    #writeFileStr(htmlBytes,r"E:\CX.PY\爬虫\file\qqFile2.txt")
    htmlStr = str(htmlBytes)



    pat = r"(((http|ftp|https)://)(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?)"
    re_url = re.compile(pat)
    urlsList = re_url.findall(htmlStr)
    urlsList = list(set(urlsList))
    print(urlsList)
    print(len(urlsList))

    pat = r"[1-9]\d{4,9}"
    re_qq = re.compile(pat)
    qqsList = re_qq.findall(htmlStr)
    # 去重
    qqsList = list(set(qqsList))
    #print(qqsList)
    #print(len(qqsList))
    f = open(topath,"a")
    for qqStr in qqsList:
        f.write(qqStr+"\n")
    f.close()
    return urlsList

#qqCrawler(url,topath)


def center(url,topath):
    queue = deque()

    queue.append(url)
    while len(queue) != 0:
        targetUrl = queue.popleft()
        urlList = qqCrawler(targetUrl,topath)
        for item in urlList:
            tempUrl = item[0]
            queue.append(tempUrl)

url = r"https://www.douban.com/group/topic/17359302/"
topath = r"E:\CX.PY\爬虫\file\qqFile.txt"
center(url,topath)





