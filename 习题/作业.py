'''
a = 100
while a <= 999:
#b = 1
    b = a // 100
    c = a - 100 * b
# d= 5
    d = c // 10
    e = c % 10
    if a == b**3 + d**3 + e**3:
        print(a)
    a += 1
'''




#else:
 #   print("不是水仙花数")
#打印出所有三位数中的水仙花数
#求五位数中有多少个回文数
#输入一个数，判断是否是质数
#输入一个数，分解质因数
#输入一个字符串，返回这个字符串中有多少个单词
#输入字符串，打印出这个字符串中所有的值的和
'''
list = [1, 2, 3, 3, 4, 5]
#print(list.pop(1))

list1 = list.count(list[2])
print(list1)
'''
str = input()
index = 0
while index < len(str):
    while str[index] != " ":
        index += 1
        if index == len(str):
            break
    count += 1
    if index == len(str):
        break
    while str[index] == " ":
        index += 1

'''
打印99乘法表
输入两个数，求最大公约数
输入一个字符串，将大写字母转换为小写字母，小写字母换为大写字母

'''











