import pymysql
db = pymysql.connect("192.168.1.106","root","zhaozelei110","leige")
cursor = db.cursor()

#检查表是否存在，如果存在则删除
cursor.execute("drop table if exists bandcard")

#创建表
sql = 'create table bandcard(id int auto_increment primary key,money int not null)'
cursor.execute(sql)


cursor.close()
db.close()















