from animal import Animal
class Mouse(Animal):
    def __init__(self, name):
        #sele.name = name  等于下面的一行
        super(Mouse, self).__init__(name)
    #def eat(self):
        #print(self.name + "吃")