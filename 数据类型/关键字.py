import keyword
import random
print(keyword.kwlist )
print(random.randrange(1,655,2))
#生成[0,1)之间的随机数
print(random.random())
#将序列的所有元素随机排序
list = [1,2,3,4,5]
random.shuffle(list)
print(list)
num1 = 2
num2 = 2
if num1 == num2:
    num1 = 100
print("num1=",num1)