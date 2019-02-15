import urllib.request
import re
def imageCrawler(url,topath):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    HtmlStr = response.read().decode("utf-8")
    #with open( r"E:\CX.PY\爬虫\file\yhd.html","wb")as f:
     #   f.write(HtmlStr)

   #pat = r"<"img" style="position: relative" defaultFlag="0" id="pdlink1_10502820097" parentId=0 pmId="0" isSnapProduct="0" isOverSea="0" isGrouponProv="0" grouponId="0" grouponType="0"(multiAreaStock="99" stockStatusMonitor="1" isOTCorRX="0" specialBusinessCate="0" isReserve="0"href="//item.yhd.com/1664645450.html" target="_blank" isSeiralCombine="0")|(multiAreaStock="0" stockStatusMonitor="0" isOTCorRX="0" specialBusinessCate="0" isReserve="0"href="//item.yhd.com/17970273482.html" target="_blank" isSeiralCombine="0")(.*?)target="_blank">"
   # re_image = re.compile(pat)
    #imageList = re_image.findall(HtmlStr)
    #print(imageList)
url = r"http://search.yhd.com/c0-0-1003302/"
topath = r"E:\CX.PY\爬虫\file"
imageCrawler(url,topath)

#正则有问题