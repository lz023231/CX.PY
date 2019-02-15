import redis

#连接
r = redis.StrictRedis(host='localhost',port=6379,password="zhaozelei110")


#方法1：根据数据类型的不同，调用相应的方法
#写
#r.set("o1","good")
#读
print(r.get("o1"))


#方法2：pipeline
#缓冲多条命令，然后依次执行，可以减少服务器-客户端之间的TCP数据包
pipe = r.pipeline()

pipe.set("o2","nice")
pipe.set("o3","nic")
pipe.set("o4","ok")
pipe.execute()








