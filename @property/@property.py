
class Person(object):
    def __init__(self, age):
        #属性直接对外暴露
        #self.age = age
        self.__age = age
    '''
    def getAge(self):
        return self.__age
    def setAge(self):
        if age < 0:
           age = 0
        self.__age = age
    '''
    #方法名为受限制的变量去掉双下划綫
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age < 0:
            age = 0
        self.__age = age


per = Person(18)

#属性直接对外暴露
#不安全，没有数据的过滤
#per.__age = -166
#print(per.__age)

per.age = 100  #相当于调用setAge
print(per.age)  #相当于调用getAge




#@property:可以让你对受限制访问的属性使用点语法




