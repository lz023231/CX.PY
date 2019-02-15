'''
认识函数：在一个完整的项目中，某些功能会反复的使用。我们会
将这个功能封装城函数。
本质：函数就是对功能的封装

优点：1、简化代码结构 ，增加了函数的复用度
      2、如果想修改某些功能或者调试某个BUG，只需修改函数即可
'''
'''
定义函数：

格式：
def 函数名（参数列表）：
    语句
    return 表达式
    
def：函数代码块以def关机你开始
函数名：一般会遵循标识符规则
参数列表：（参数1， 参数2.....     ):任何传入函数的参数和变量
        必须放在圆括号之间，用逗号分隔。函数从函数调用者那里
        获得一些信息  
语句：函数封装的功能
return：一般用于结束函数，并返回信息给函数的调用者。
表达式：即为要返回给函数的调用者的信息
：注意：最后的return表达式可以不写，相当于return None 

'''
#定义了一个无参无返回值的函数
def myPrint():
    print("sunck is a good man!")
    print("sunck is a nice man!")
    print("sunck is a handsome man!")
'''
函数的调用
格式：函数名（参数列表）
参数列表：函数的调用者给函数传递的信息 ,如果没有参数，括号不能省略
函数调用的本质：实参给形参赋值的过程

'''
myPrint()

               # 函数的参数：
#需求：编写一个函数，给函数一个字符串和一个年龄，在函数内部打印出来
#形参：定义函数是小括号中的变量，本质是变量
#参数必须按顺序传递，个数目前来看要对应，否则将要报错，如下
#def myPrint(str,age，hoby):
    #print(str,age)

def myPrint(str,age):
    print(str,age)
#实参：调用函数时给函数传递的数据，本质是值
myPrint("sunck is a good man", 22)



#返回值
#编写函数，实现功能，给函数两个数，返回这两个数的和
def mySum(num1,num2):
    #将结果返回给函数的调用者，
    return num1 + num2
    #执行完return语句，该函数结束，return后面的代码不执行
    print("eewewewew")
res = mySum(1,2)
print(res)




'''
值传递：传递的是不可变类型，string、tuple、number
'''
def func1(num):
    num = 10

temp = 20
func1(temp)   #num = temp
print(temp)

'''
引用传递：传递的可变类型，list、dict、set

'''
def func2(lis):
    lis[0] = 100
li = [1, 2, 3, 4, 5]
func2(li)
print(li)







'''
关键字参数：允许函数调用时参数的顺序与定义时不一致

'''
def myPrint(str,age):
    print(str,age)

myPrint(age = 18, str = "sunck is a good man")

'''
默认参数：调用函数是，如果没有传递参数，则使用默认参数
'''
#要用默认参数，最好将默认参数放到最后
def myPrint(str = "sunck is a good man",age = 18):
    print(str,age)

myPrint()
myPrint("i am good", 22)


def myPrint(str ,age = 18):
    print(str,age)

myPrint("6")



'''
不定长参数：能处理比定义时更多的参数
'''
#加了星号的变量会存放所有未命名的变量参数，如果在函数指定时没有
#指定参数，他就是一个空元组
def func(name, *arr):
    print(name)
    for x in arr:
        print(x)
func("shgh", "dfhuew", "erg")


def lSum(*l):
    sum = 0
    for i in l:
        sum += i
    return sum
print(lSum(1,2,3,4))

#**代表键值对的参数字典，和*所代表的意义类似
def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))
func2(x=1, y=2,z=3)

#能传递所有类型的参数
def func3(*args,**kwargs):
    pass  #代表一个空语句

'''
匿名函数:不使用def这样的语句定义函数，使用lambda来创建匿名函数

特点：1、lambda只是一个表达式，函数体比def简单
      2、lambda主体是一个表达式，而不是代码块，仅仅只能在表达式中封装简单的逻辑
      3、lambda函数有自己的命名空间，且不能访问自由参数列表之外的或全局命名空间里的参数
      4、虽然lambda是一个表达式，而且看起来只能写一行，与c和c++的内联函数不同。
格式：lambda 参数1，参数2，……参数n：experssion
'''

sum = lambda num1,num2:num1 +num2
print(sum(1,2))



















