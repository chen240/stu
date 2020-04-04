 # 2.写一个读取'phone_book.txt'文件的程序
 #      把保存的信息以表格的形式打印出来
 #       +-----------------+-------------------+
 #       |    name         |     number        |
 #       +-----------------+-------------------+
 #       |  xiaozhang      | 13822222222       |
 #       +-----------------+-------------------+

 #从文件中读取数据，形成相应的数据结构，传递给显示的函数
def read_info_from(filename='phone_book.txt'):
    '''读取文件，形成元组组成的列表'''
    L=[]
    #读取文件信息，形成元组后放入列表Ｌ
    try:
        f=open(filename)
        #读取数据
        while True:
            s=f.readline()
            #去掉右侧的换行符'\n'
            if not s:
                break
            s=s.rstrip()
            name,number,age=s.split(',') #拆［＇姓名＇，＇电话＇］
            L.append((name,number,age))

        f.close()
    except OSError:
        print("打开文件失败！")



    return L

def print_infos(lst):
    print('+------------+-------------+-----------+')
    print('|    name    |   number    |   age     |')
    print('+------------+-------------+-----------+')
    for d in lst:
        name,number,age=d
        t=(name.center(12),number.center(13),
            age.center(11))
        line='|%s|%s|%s|' %t
        print(line)
    print('+------------+-------------+-----------+')

if __name__=='__main__':
    L=read_info_from()
    # print(L)
    print_infos(L)