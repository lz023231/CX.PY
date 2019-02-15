'''
TCP是建立可靠的连接，并且通信双方都可以以流的形式发送数据
相对于TCP，UDP则是面向无连接的协议

使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以发送数据包，但是不保证到达

虽然UDP传输数据不可靠，但是优点是和TCP比，速度快，对于要求不高的数据，可以使用UDP
'''
str = ""
import socket
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.connect(("", ))



