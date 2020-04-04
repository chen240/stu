from socket import *

#１．创建套节字
sockfd=socket(AF_INET,SOCK_STREAM)

#2.绑定地址
sockfd.bind(('192.168.101.13',8888))

#3.设置监听
sockfd.listen(5)

while True:
    #4.等待接收连接
    print("Waiting for connect...")
    connfd,addr=sockfd.accept()
    print("Connect from",addr)

    while True:
        #5.收发消息
        data=connfd.recv(1024).decode()
        if not data:
            break
        print(data)  #utf-8
        n=connfd.send(b'Receive your message')
        print("发送了%d字节"%n)

    #6.关闭套节字
    connfd.close()  #客户端套节字关闭
sockfd.close()  #服务端套节字关闭


