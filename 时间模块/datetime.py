import datetime
#获取当前时间
d1 = datetime.datetime.now()
print(d1)

#获取指定时间
d2 = datetime.datetime(1999, 10, 1,10,28,34,123456)
print(d2)


#将时间转为字符串
d3 = d1.strftime("%Y-%m-%d %X")
print(d3)

#将格式化字符串转为datetime对象
#注意转换的个格式要与字符串一致
d4 = datetime.datetime.strptime(d3,"%Y-%m-%d %X")
print(d4)

d5 = datetime.datetime(1999, 10, 1,10,28,34,123456)
d6 = datetime.datetime.now()
d7 = d6 - d5
print(d7)

#提取到间隔的天数
print(d7.days)
#间隔天数除外的秒数
print(d7.seconds)











