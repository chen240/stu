# 2.练习：
#     1.写一个程序，从键盘输入如下信息：
#       姓名 和 电话号码
#       如：
#         请输入姓名：xiaozhang
#     请输入电话：13888888
#     请输入姓名：小路
#     请输入电话：120000000
#     请输入姓名：<回车>
#     把从键盘读取的信息存入'phone_book.txt'文件中
#       然后用subline text 打开并查看写入的内容

def input_phone_number():

  L=[]
  while True:
    name=input("请输入名字：")
    if not name:
      break
    number=input("请输入电话：")
    age=input("请输入年龄:")

    L.append((name,number,age))  #形成元组


  return L

def write_to_file(lst,filename='phone_book.txt'):
  '''将lst列表内的数据放到文件filename中'''
  try:
    f=open(filename,'w')
    for name,number,age in lst:
      f.write(name)
      f.write(',')
      f.write(number)
      f.write(',')
      f.write(age)
      f.write('\n')



    f.close()
  except OSError:
    print("写入文件失败！！！")


if __name__=='__main__':
  L=input_phone_number()
  print(L)
  write_to_file(L)
