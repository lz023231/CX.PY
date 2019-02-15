import calendar
import time
#使用
#返回指定某年某月的日历
print(calendar.month(2017,7))

#返回指定年的日历
print(calendar.calendar(2017))

#判断是否是闰年
print(calendar.isleap(2000))

#返回某个月的第一天和所有天数
print(calendar.monthrange(2017,7))

#返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2017,7))








