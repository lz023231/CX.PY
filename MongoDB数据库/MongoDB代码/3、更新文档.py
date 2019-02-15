from pymongo import MongoClient

#连接服务器
conn = MongoClient("localhost",27017)

#连接数据库
db = conn.myDb

#获取集合
collection = db.student

#更新文档

collection.update({"name":"赵泽雷"},{"$set":{"age":22}})


#断开
conn.close()














