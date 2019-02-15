from pymongo import MongoClient

#连接服务器
conn = MongoClient("localhost",27017)

#连接数据库
db = conn.myDb

#获取集合
collection = db.student

#删除

collection.remove({"name":"wer"})

#全部删除
collection.remove()

#断开
conn.close()
































