
import urllib.request

urllib.request.urlretrieve("http://www.baidu.com",filename=r"E:\CX.PY\爬虫\file\file2.html")



#urlretrieve在执行的过程中，会产生一些缓存
#清楚缓存
urllib.request.urlcleanup()

