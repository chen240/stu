

#此示例示意装饰器的用法

#定义一个装饰器函数解决上述问题－－－>直接改变了这个函数
def mydeco(fn):
    def fx():
        print('fx被调用')
    return fx


#定义函数的地方(可能是小张写的)
@mydeco  #myfunc=mydeco(myfunc)
def myfunc():
    # print('++++++++++++')
    print("myfunc被调用")
    # print('-------')

# myfunc=mydeco(myfunc)

#调用函数的地方可能是小李写的
myfunc()
myfunc()
#调用－－－小王写的
myfunc()