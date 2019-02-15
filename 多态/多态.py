from cat import Cat
from mouse import Mouse
from person import Person
'''
多态：一种事物的多种形态

最终目标：人可以喂任何一种动物
'''

tom = Cat("tom")
jerry = Mouse("jerry")
tom.eat()
jerry.eat()

#思考：在添加100种动物，每个动物都有name和eat方法
#定义了一个有name和eat方法的animal类，采用继承的方法



#定义一个人类，可以喂毛和老鼠吃东西
per = Person()
#per.feedCat(tom)
#per.feedMouse(jerry)

#思考：人要喂100种动物，难道要写100种feed方法吗？
per.feedAnimal(tom)
per.feedAnimal(jerry)
