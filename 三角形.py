import numpy as np
import random
class Vertex(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return ("x坐标：%s,y坐标：%s" % (self.x, self.y))
class Triangle(object):
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    def __str__(self):
        return ("A点：%s B点：%s C点：%s" % (self.A, self.B, self.C))
    def isTriangle(self):
        arr = np.array([[self.A.x, self.A.y, 1], [self.B.x, self.B.y, 1], [self.C.x, self.C.y, 1]])
        s = abs(0.5 * np.linalg.det(arr))
        return False if s == 0 else True
    def isInTriangle(self, D):
        arr1 = np.array([[self.A.x, self.A.y, 1], [self.B.x, self.B.y, 1], [self.C.x, self.C.y, 1]])
        sumAera = 0.5 * np.linalg.det(arr1)
        arr2 = np.array([[self.A.x, self.A.y, 1], [self.B.x, self.B.y, 1], [D.x, D.y, 1]])
        s1 = 0.5 * np.linalg.det(arr2)
        arr3 = np.array([[self.A.x, self.A.y, 1], [D.x, D.y, 1], [self.C.x, self.C.y, 1]])
        s2 = 0.5 * np.linalg.det(arr3)
        arr4 = np.array([[D.x, D.y, 1], [self.B.x, self.B.y, 1], [self.C.x, self.C.y, 1]])
        s3 = 0.5 * np.linalg.det(arr4)
        if s1 != 0 and s2 != 0 and s3 != 0 and abs(s1 + s2 + s3 - sumAera) < 0.000001:
            return True
        else:
            return False
if __name__ == '__main__':
    arrOfVertex = []
    for i in range(1000):
        tempx = random.randint(1, 100)
        tempy = random.randint(1, 100)
        tempVertex = Vertex(tempx, tempy)
        arrOfVertex.append(tempVertex)
    k, j, m = random.randint(0, 999), random.randint(0, 999), random.randint(0, 999)
    selectedTriangle = Triangle(arrOfVertex[k], arrOfVertex[j], arrOfVertex[m])
    while not selectedTriangle.isTriangle():
        k, j, m = random.randint(0, 999), random.randint(0, 999), random.randint(0, 999)
        selectedTriangle = Triangle(arrOfVertex[k], arrOfVertex[j], arrOfVertex[m])
    arrOfJudge = []
    sum = 0
    for i in range(1000):
        temp = selectedTriangle.isInTriangle(arrOfVertex[i])
        print(arrOfVertex[i], end=' ')
        if temp: sum += 1
        arrOfJudge.append(temp)
    print("选取的是否为三角形:%s" % selectedTriangle.isTriangle())
    print(arrOfJudge)

