
import collections


queue = collections.deque()
print(queue)

#进队
queue.append("a")
print(queue)
queue.append("b")
print(queue)
queue.append("c")
print(queue)



#出队（取数据）
res1 = queue.popleft()
print("res1 = ", res1)
print(queue)
res2 = queue.popleft()
print("res2 = ", res2)
print(queue)
res3 = queue.popleft()
print("res3 = ", res3)
print(queue)


