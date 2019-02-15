
'''
重写：将函数重新定义写一遍
__str__():调用print打印对象时自动调用，是给用户用的，是一个描述对象的方法

__repr__()：给机器用的，再Python解释器里直接敲对象名再回车后调用的方法
注意：在没有str时，且有repr,str = repr

'''


class Person(object):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def __str__(self):
        return "%s-%d-%d-%d" % (self.name, self.age, self.height, self.weight)


per  = Person("hgsdh", 22, 342, 34)
#print(per.name, per.age, per.weight,per.height)
print(per)

#优点：当一个对象的属性有很多，并且都需要打印，重写了__str__方法后，简化了代码









