'''
原型：filter（发你，lsd）
参数1为函数
参数2为序列

功能：用于过滤序列
白话文：把传入的函数依次作用于序列的每个元素，根据返回的是True还是False决定是否保留该元素
'''

list1 = [1,2,3,4,5,6,7,8,9]
#偶数保留，奇数剔除
def func(num):
    if num%2 == 0:
        return True
    return False
l = filter(func,list1)
print(list(l))

