# 2. 学生管理项目准备工作:
#    写一个程序，任意输入n个学生的信息,形成字典后存于列表中:
#      学生的信息包括:
#         姓名(字符串)
#         年龄(整数)
#         成绩(整数)
#    循环输入学生信息，直到输入学生姓名为空时结束输入,
#    最后形成字典列表如下:
#      L = [
#           {'name':'xiaozhang', 'age':20, 'score': 100},
#           {'name':'xiaoli', 'age':21, 'score': 98},
#           {'name':'xiaowang', 'age':19, 'score': 89},
#           ...
#      ]
#   2) 将以上列表显示为如下的表格:
#   +------------+------+-------+
#   |   name     | age  | score |
#   +------------+------+-------+
#   | xiaozhang  |  20  |  100  |
#   |  xiaoli    |  21  |   98  |
#   | xiaowang   |  19  |   89  |
#   +------------+------+-------+

#第一步，读取学生信息，形成字典后存入列表Ｌ中
L=[]
while True:
    name=input("请输入学生姓名：")
    if not name:
        break
    age=int(input("请输入学生年龄："))
    score=int(input("请输入学生成绩："))
    d={}   #字典的赋值？
    d['name']=name   #创建一个新的键值对
    d['age']=age
    d['score']=score
    L.append(d)  #列表尾部追加元素

print('+------------+-------+---------+')
print('|     name   |  age  |   score |')
print('+------------+-------+---------+')
for d in L:
    t=(d['name'].center(12),
        str(d['age']).center(7),
        str(d['score']).center(9))
    line="|%s|%s|%s|" %t　　#|||是什么意思
    print(line)
print('+------------+-------+---------+')