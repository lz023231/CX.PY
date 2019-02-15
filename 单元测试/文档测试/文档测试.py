import doctest
#doctest这个模块可以提取注释中的代码执行
#doctest严格按照Python交互模式的输入提取


def mySum(x,y):
    '''

    :param x:
    :param y:
    :return:
    注意有>>>后有一个空格
    example:
    >>> print(mySum(1,2))
    3
    '''
    return x + y


print(mySum(1, 2))

#进行文档测试
doctest.testmod()

