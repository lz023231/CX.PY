
'''
析构函数：__del__()   释放对象时自动调用
'''


class Person(object):
    def run(self):
        print("run")
    def eat(self, food):
        print("eat" + food)
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def __del__(self):
        print("这里是析构函数")

per = Person("gsdg", 23, 234, 34)
#释放对象
del per


#对象释放以后就不能再访问了
#print(per.age)


#在函数里定义的对象，会在函数结束时自动释放，这样可以用来减少内存空间的浪费
def func():
    per2 = Person("er", 34,3,3)
func()

while 1:
    pass
























