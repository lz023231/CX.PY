'''
客户端：创建TCP连接时，主动发起连接的叫客户端
服务端：接收客户端的连接
'''
import socket
# 1、创建一个socket
# 参数1：指定协议 AF_INET（IPv4） 或AF_INET6
# 参数2：socket.SOCK_STREAM指定使用面向流的TCP协议
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 2、建立连接
# 参数：是一个元组，第二个参数为端口号
sk.connect(('www.sina.com.cn', 80))


sk.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#等待接收数据
data = []
while True:
    #每次接收1k的数据
    tempData = sk.recv(1024)
    if tempData:
        data.append(tempData)
    else:
        break

dataStr = (b''.join(data)).decode("utf-8")

#断开连接
sk.close()
#print(dataStr)



headers, HTML = dataStr.split("\r\n\r\n", 1)
print(headers)
print(HTML)