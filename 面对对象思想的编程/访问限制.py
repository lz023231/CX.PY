class Person(object):
    def run(self):
        print("run")
        print(per.__money)
    def eat(self, food):
        print("eat" + food)
    def __init__(self, name, age, height, weight, money):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.__money = money  #_Person__money
    #通过内部的方法，去修改私有属性
    #通过自定义的方法实现对私有属性的赋值与修改
    def setMoney(self, money):
        #数据的过滤
        if money < 0:
            money = 0
        self.__money = money

    def getMoney(self):
        return self.__money

per = Person("heei", 22, 168, 53, 19999)



#如果要让内部的属性不被外部直接访问，在属性前加两个下划线（__）,在Python中，如果在属性前加两个下划线，那么这个属性就编程了私有属性
#print(per.__money)  #外部使用会报错

#per.run()#  内部可以使用
per.setMoney(10)
print(per.getMoney())

#不能直接访问per.__money是因为Python解释器把__money变成了_Person__money,仍然可以用_Person__money去访问，但是强烈建议不要这么干，不同的解释器可能存在解释的变量名不一致


#在Python中，__XXX__ 属于特殊变量，可以直接访问


#在Python中 _XXX 变量，这样的实例变量外部也是可以访问的，但是，按照约定的规则，当我们看到这样的变量时，意思是“虽然我可以被访问，但是请把我视为私有变量，不要直接访问我”