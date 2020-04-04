

# try:
#     f=open('info.txt')
#     s=f.readline()
#     print("第一行文字",s)
#     s=f.readline()
#     print("第二行文字",s)
#     s=f.readline()
#     print("第三行文字",s)
# except OSError:
#     print("文件打开失败!")

def read_text_data():
    try:
        f=open('info.txt')
        #读取文件
        while True:
            s=f.readline()
            if not s:
                break
            if s[-1]=='\n':
                print('--->',s[:-1])
            else:
                print('--->',s)


        f.close()
    except OSError:
        print("打开失败")

if __name__=='__main__':
    read_text_data()