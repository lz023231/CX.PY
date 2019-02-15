#定义空元组
tuple = ()
print(tuple)
tuple2 = (1,2,43,"gigig", True)
print(tuple2)
#定义只有一个元素的元组
tuple3 = (1, )
print(tuple3)
print(type(tuple3))
#元组的访问
#格式：元组名[下标]
#获取最后一个元素
print(tuple2[-1])
print(tuple2[-2])

#不能修改元组元素，如果元素是列表，则可以修改列表中的元素
#删除元组
tuple5 = (2,3,4)
del tuple5



#元组的操作
t7 = (1,2,3)
t8 = (4,5,6)
t9 = (t7 + t8)
#元组重复
t10 = (1,2,3)
print(t10 * 3)

#判断元素是否在元组中
t11 = (1,2,3)
print(1 in t11)

#元组的截取
#格式：元组值[开始下标：结束下标]
#从开始下标开始截取，截取到结束下标之前
t12 = (1,2,3,4,5,6,7,8,9)
print(t12[3:7])
print(t12[3:])
print(t12[:7])


#二维元组
t13 = ((1,2,3),(4,5,6),(7,8,9))
print(t13[1][1])


#元组的方法
t14 = (1,2,3,4,5)
#len()  max()  min()

#将列表转为元组
#list= [1,3,4]
#t15 = tuple(list)
#print(t15)

#元组的遍历
for i in (1,2,3,4,5):
    print(i)


















