import socket


udpServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpServer.bind(("192.168.1.102",8900))

while True:
    data,addr = udpServer.recvfrom(1024)
    print("客户端说：",data.decode("utf-8"))
    info = input("请输入数据：")
    udpServer.sendto(info.edcode("utf-8"),addr)