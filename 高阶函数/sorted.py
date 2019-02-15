#用来排序的：冒泡，选择，   快速，插入，计数器


#普通的排序
list1 = [3,45,1,8,45,232,23,43]
list2 = sorted(list1)#默认升序排序
print(list1)
print(list2)


#按绝对值大小排序

list3 = [3,45,1,43,-4,-6]
#key接受函数来实现自定义排序规则
list4 = sorted(list3,key=abs)
print(list3)
print(list4)


#降序

list5 = [3,45,1,8,45,232,23,43]
list6 = sorted(list5,reverse=True)
print(list5)
print(list6)

#函数可以自己写
def myLen(str):
    return len(str)

list7 = ["b33", "a11111111", "c22", "d5556"]
list8 = sorted(list7,key=myLen)
print(list7)
print(list8)


