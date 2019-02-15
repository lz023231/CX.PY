'''
装饰器：是一个闭包，把一个函数当做参数返回一个替代版的函数，本质上就是一个返回函数的函数

'''
#简单的装饰器
def func1():
    print("i am a good man!")

def outer(func):
    def inner():
        print("******************")
        func()
    return inner
#  f是函数func1的加强版本
f = outer(func1)
f()
print(type(f))




#复杂一点的装饰器

def say(age):
    print("i am %d years old" % (age))
say(-10)
#开始
def ter(func2):
    def ner(age):
        if age < 0:
            age = 0
        func2(age)
    return ner
@ter   # 相当于say = ter(say)
def say(age):
    print("i am %d years old" % (age))
#say = ter(say)
say(-10)



#通用装饰器
def our(func3):
    def nee(*args,**kwargs):#函数的参数理论上是无限制的，但最好不要超过6～７个
        #添加修改的功能
        func3(*args,**kwargs)
    return nee



















