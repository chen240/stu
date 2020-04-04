

try:
    # f=open('/etc/passwd') #此时成功打开
    f=open('./abc.txt') #此时成功打开
    print("文件打开成功")

    f.close()
except OSError:
    print("文件打开失败！")