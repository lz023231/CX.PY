class Person(object):
    #这里的属性实际上属于类属性（用类名来调用）
    name = "person"
    def __init__(self, name):
        #对象属性
        self.name = name


print(Person.name)
per = Person("tom")
#对象属性的优先级高于类属性
print(per.name)
#动态的给对象添加对象属性
per.age = 18 #只针对于当前对象生效，对于类创建的其他对象没有意义
print(Person.name)
per2 = Person("jdhf")
#print(per2.age)  没有age属性


#删除对象中的name属性,再调用会使用同名的类属性
del per.name
print(per.name)

#以后千万不要将对象属性与类属性重名，对象属性会屏蔽掉类属性。但是当删除对象属性后，又能使用类属性了。




