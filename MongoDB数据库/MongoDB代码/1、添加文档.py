from pymongo import MongoClient

#连接服务器
conn = MongoClient("localhost",27017)

#连接数据库
db = conn.myDb

#获取集合
collection = db.student

#添加文档
#collection.insert({"name":"李雷2","age":19,"gender":1,"address":"北京","isDelete":0})

collection.insert([{"name":"赵泽雷","age":19,"gender":1,"address":"北京","isDelete":1},{"name":"赵泽雷2","age":19,"gender":1,"address":"北京","isDelete":1}])

#断开
conn.close()














