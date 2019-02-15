
'''

'''
#当程序遇到问题是不让程序结束，而略过错误继续向下执行

'''
try……except……else
格式：
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句1
……
except 错误码 as e:
    语句n
else:
    语句e
    
注意：else可有可无
作用：用来检测try语句块中的错误，从而让except补货错误信息并处理
逻辑：当程序执行到try～expect～else语句时
1、如果当try“语句t”出现错误，会匹配第一个错误码，如果匹配上就执行对应的语句
2、如果当try“语句t”出现错误，没有匹配的异常，那么我们的错误将会被提交到上一层的try语句，或者到程序的最上层
3、如果当try“语句t”没有出现错误，执行else下的“语句e”
（你得有）
'''

try:
    print(3 / 0)
except ZeroDivisionError as e:
    print("除数为零了")
print("*******")



#使用except而不使用任何的错误类型
try:
    print(4 / 0)
except:
    print("程序出现了异常")


#使用except带着多种异常
try:
    print(5 / 0)
except (NameError,ZeroDivisionError):
    print("出现了NameError或ZeroDivisionError")

#特殊的地方
#1、异常其实就是类，所有的异常都是承自BaseException,所有在捕获的时候，它捕获了该类型的错误，还把子类一网打尽
#2、跨越多层调用，也能捕获到异常




'''
try……except……finally
try:
    语句t
except 错误码 as e:
    语句1
except 错误码 as e:
    语句1
……
except 错误码 as e:
    语句n
finally:
    语句f

作用：无论语句f是否有异常都会执行最后的语句f

'''

'''
断言： 
'''

def func(num, div):
    assert (div != 0),"div不能为0"
    return num / div
print(func(10, 0))










