import random
num = int(input("请输入您的号码："))
res = random.choice(range(100))  + 1
print("中奖号码是:",res)
#判断是否中奖  num == res
if num == res:
    print("恭喜您中了500万")
else:
    print("对不起，您没有中奖")
