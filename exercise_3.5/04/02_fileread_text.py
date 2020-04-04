

#此示意以文本文件读取abc.txt的数据

try:
    f=open("abc.txt")
    print("文件打开成功！")

    s=f.readline()
    if s!='':
        print("读取成功，文字是：",s)
    else:
        print("文件内已经无数据可读了！")
    s=f.readline()
    print("第二行数据是:",s)
    s=f.readline()
    print("第三行数据是:",s)
    s=f.readline()
    if s=='':
        print("文件内已经没有数据可读取！")
    else:
        print("第四行数据是:",s)
    f.close()
except OSError:
    print("文件打开失败！")

