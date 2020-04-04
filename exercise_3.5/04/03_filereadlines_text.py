#此示意Ｆ．readlines的用法

try:
    f=open('../04/info.txt')
    L=f.read()
    print(L)
    f.close()
except:
    print("打开文件失败")