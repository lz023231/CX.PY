'''
概念：是一种保存数据的格式
作用：可以保存本地的json文件，也可以将json串进行传输，通常将json称为轻量级的导入方式

json文件组成
{}   代表对象（）字典
[]   代表列表
:     代表键值对
,     分割两个部分

'''
import json
jsonStr = '{"name":"sunck凯","age":18,"hobby":["money","power","english"],"parames":{"a":1,"b":2}}'
#将json格式的字符串转为Python数据类型对象
jsonData = json.loads(jsonStr)
print(jsonData)
print(jsonData["hobby"])

#将Python数据类型对象转为json格式的字符串
jsonData2 = {"name":"sunck凯","age":18,"hobby":["money","power","english"],"parames":{"a":1,"b":2}}

jsonStr2 = json.dumps(jsonData2)
print(jsonStr2)
print(type(jsonStr2))


#读取本地的json文件

path1 = r"E:\CX.PY\爬虫\file\file3.json"
with open(path1,"rb") as f:
    data = json.load(f)
    print(data)

#写本地的json文件

path2 = r"E:\CX.PY\爬虫\file\file3.json"
jsonData3 = {"name":"sunck凯","age":18,"hobby":["money","power","english"],"parames":{"a":1,"b":2}}

with open(path2,"w") as f:
    json.dump(jsonData3,f)
















