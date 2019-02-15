'''
for 语句
格式：
  for 变量名 in 集合：
    语句
逻辑： 按顺序取集合中的每个元素赋值给变量，再去执行语句，如此
往复，直到取完所有元素

'''
for i in [1, 2, 3, 4, 5]:
    print(i)
'''
 range()函数   列表生成器
 功能：生成列表       
'''
for x in range(10):
    print(x)
for y in range(2, 20, 2):   #2,20,2 分别为起点，终点，步长，起点默认为0，步长默认为1
    print(y)
for index, g in enumerate([1, 3, 4, 5, 6]): # index, g = 下标， 元素
    print(index, g)
#1到100求和
sum = 0
for n in range(1,101):
    sum += n
print(sum)









