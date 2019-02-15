import time
'''
UTC(世界协调时间)：格林尼治时间，世界标准时间，在中国来说是UTC+8
DST（夏令时）：一种节约能源而人为规定时间制度，在夏季将时间调快一个小时

时间的表示形式：
1、时间戳：以整型或浮点型表示时间的一个以秒为单位的时间间隔，这个时间的基础指是从1970年一月一日凌晨开始算起
2、元组：一种python的数据结构表示，这个元组有9个整型内容
year
manth
day
hours
minutes
seconds
weekday
Julia day
flag(1或-1或0)
3、格式化字符串

'''
#返回当前时间的时间戳，浮点数形式，不需要参数
c = time.time()
print(c)

#将时间戳转为UTC时间元组
t = time.gmtime(c)
print(t)

#将时间戳转为本地时间元组
b = time.localtime(c)
print(b)

#将本地时间元组转为时间戳
m = time.mktime(b)
print(m)


#将时间元组转为字符串
s = time.asctime(b)
print(s)

#将时间戳转为字符串
p = time.ctime(c)
print(p)

#将时间元组转换成给定格式的字符串，参数2为时间元组，没有参数2，默认为当前时间
q = time.strftime("%Y-%m-%d %X",)
print(q)

#将时间字符串转为时间元组
t = time.strptime(q, "%Y-%m-%d %X")
print(t)


#延迟一个时间，整型或者浮点型
time.sleep()









