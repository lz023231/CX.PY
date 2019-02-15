import itertools


myList = list(itertools.permutations([1,2,3,4],2))
print(myList)
print(len(myList))

'''
1，2，3,4
排列的可能性次数：n! / (n-m)！
'''

