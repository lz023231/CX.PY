from functools import reduce
#Python内置了map（）和reduce（）



#map()
#原型  map(fn,lsd)
#参数1是一个函数   参数2是一个序列
#功能：将传入的函数依次作用在序列中的每一个元素，并把结果作为一个新的Iterator返回
#将单个字符转成对应的自变量整数
def chr2int(chr):
    return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[chr]

list1 = ["7", "6", "4", "2"]
res = map(chr2int,list1)
print(res)
print(list(res))

#将整数元素的序列，转为字符型

l = map(str,[1,2,3,4])
print(list(l))


#reduce(fn,lsd)
#参数1是函数  参数2是列表
#功能： 一个函数作用在序列上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素累计运算
#reduce（f,[a,b,c,d]）
# f(f(f(a,b),c),d)


#求一个序列的和
list2 = [1,2,3,4,5]
def mySum(x,y):
    return x + y
r = reduce(mySum,list2)
print("r=",r)




#将字符串转成对应字面量数字

def str2int(str):
    def fc(x,y):
        return x * 10 +y
    def fs(chr):
        return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[chr]
    return reduce(fc,map(fs,list(str)))
print(str2int("123415"))








