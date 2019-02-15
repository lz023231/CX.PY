from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId  #用于id查询
#连接服务器
conn = MongoClient("localhost",27017)

#连接数据库
db = conn.myDb

#获取集合
collection = db.student

#查询文档

#查询部分文档
res = collection.find({"age":{"$gte":18}})
for row in res:
    print(row)

#查询所有文档

res = collection.find()
for row in res:
    print(row)

#统计查询

res = collection.find({"age":{"$gte":18}}).count()
print(res)
print(type(res))


#根据id查询
res = collection.find({"_id":ObjectId("5a991006754be868f1a8e8a6")})
print(res[0])

#排序
#res = collection.find().sort("age")  升序
#降序
res = collection.find().sort("age",pymongo.DESCENDING)
for row in res:
    print(row)

#分页
print("********")
res = collection.find().skip(3).limit(5)
for row in res:
    print(row)











#断开
conn.close()














