'''
self代表类的实例，而非类

哪个对象调用方法，那么该方法中的self就代表哪个对象

self.__class__  代表类名
'''

class Person(object):
    def run(self):
        print("run")
        print(self.__class__)
        p = self.__class__("efe", 324, 32, 34)
        print(p)
    def eat(self, food):
        print("eat" + food)
    def say(self):
        print("Hello!my name is %s,i am %d years old" % (self.name, self.age))
    #self不是关键字，换成其他的标识符也可以，但是帅的人都用self
    def play(a):
        print("play")
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

per1 = Person("tom", 24, 178, 67)
per1.say()
per1.play()
per1.run()











