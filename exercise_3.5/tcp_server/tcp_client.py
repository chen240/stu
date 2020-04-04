#tcp_client.py
from socket import *

#创建套节字
sockfd=socket(AF_INET,SOCK_STREAM)

#发起连接
server_addr=('192.168.101.13',8888)
sockfd.connect(server_addr)

while True:
    data=input("发送>>")
    if not data:
        break
    sockfd.send(data.encode())  #以字节的方式发送bytes
    data=sockfd.recv(1024)
    print("接受到:",data.decode())

#关闭套节字
sockfd.close()


