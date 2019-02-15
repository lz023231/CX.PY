'''
概述：使用键值（Key-value），拥有极快的查找速度
注意：字典是无序的
Key的特性：
1.字典中的Key必须唯一
2。Key必须是不可变的对象
3.字符串、整数等都是不可变的，可以作为Key
4。list不能用Key



'''
dict1 = {"tom":60, "lilei":70}
#元素的访问
#获取：字典名[Key]
print(dict1["lilei"])
print(dict1.get("zunck"))#字典中没有“zunck”,会报错，前面加.get会打印None
#添加：
dict1["hanmeimei"] = 99
#因为一个Key对应一个value，所以，多次对一个value赋值，其实就是修改值
dict1["lilei"] = 80
print(dict1)
#删除
dict1.pop("tom")
print(dict1)
#遍历
for Key in dict1:
    print(Key)
    print(Key,dict1[Key])
for value in dict1.values():
    print(value)
for k,v in dict1.items():
    print(k, v)
for i, v2 in enumerate(dict1):
    print(i, v2)
#和list比较
#1、查找和插入的速度极快，不会随着Key-value的增加而变慢
#2、需要占用大量的内存，内存浪费多

#list
#1、查抄和插入的速度会随着数据量的增多变慢
#2、占用空间少，浪费内存少
'''
输入一个单词，查看其在字符串中出现的次数
'''
w = input()
d = {} # word:次数
str = "i am a good man ! i am a nice man! i am a handsome man! i am hand dome man "
l = str.split(" ")
for k in l:
    c = d.get(k)
    if c == None:
        d[k] = 1
    else:
        d[k] += 1
print(d)
'''
切割字符串
循环处理列表中的每个元素
以元素当做Key去一个字典中提取数据
如果没有提取到，就以钙元素当做Key，1作为value  存进字典
如果提取到，将对应的Key的value修改，值加1
根据输入的字符串当做Key再去字典提取


'''








































