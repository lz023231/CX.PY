import b.sunck
import a.sunck
import a.kaige
'''
不同的人编写的模块同名了怎么办？
为了解决模块命名的冲突，我们引入了按目录来组织模块的方法，我们称之为包
包：
特点：引入了包 以后，只要顶层的包不与其他人发生冲突，na那么模块都不会与别人的发生冲突

注意：目录只有包含一个叫做“__init__”的文件才被认作是包，主要是为了避免一些滥竽充数的名字，基本上目前这个文件中什么也不用写

'''

a.sunck.sayGood()
a.kaige.sayGood()
b.sunck.sayGood()









