from Child import Child

def main():
    c = Child(300,100)
    print(c.money, c.faceValue)
    c.play()
    c.eat()
    #注意：父类中方法名相同，默认调用的是括号中排前面的方法中的父类
    c.func()

if __name__ == "__main__":
    main()





