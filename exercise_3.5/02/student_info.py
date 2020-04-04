#s==1
def input_student():
    L=[]
    while True:
        name=input("请输入学生名字:")
        if not name:
            break
        age=int(input("请输入学生年龄:"))
        score=int(input("请输入学生成绩:"))
        d={}
        d['name']=name
        d['age']=age
        d['score']=score
        L.append(d)
    return L
#s==2
def output_student(L):
    # 以表格形式再打印学生信息
    print('+------------+------+-------+')
    print('|   name     | age  | score |')
    print('+------------+------+-------+')
    for d in L:  # d绑定的是字典
        t = (d['name'].center(12),
             str(d['age']).center(6),
             str(d['score']).center(7))
        line = "|%s|%s|%s|" % t  # t是元组
        print(line)
    print('+------------+------+-------+')
# s==3
def modify_student(lst):
    name=input("请输入要修改的学生新名：")
    for d in lst:
        if d['name']==name:
            score=int(input('请输入新的学生成绩：'))
            d['score']=score
            age=int(input('请输入新的学生年龄：'))
            d['age']=age
            print("修改",name,"成绩为",score,"年龄为",age)
            return
        else:
            print("没有找到",name,"的信息")
#s==4
def delete_student(lst):
    name=input("请输入要删除的学生姓名：")
    for i in range(len(lst)):
        if lst[i]['name']==name:
            del lst[i]
            print("已经将",name,"的信息删除")
            return True
        else:
            print("没有找到",name,"的信息")

# s==5
def score_student_desc(lst):
    L=sorted(lst,key=lambda d:d['score'],reverse=True)
    output_student(L)

# s==6
def score_student_asc(lst):
    L=sorted(lst,key=lambda d:d['score'])
    output_student(L)
#s==7
def age_student_desc(lst):
    L=sorted(lst,key=lambda d:d['age'],reverse=True)
    output_student(L)

#s==8
def age_student_asc(lst):
    L=sorted(lst,key=lambda d:d['age'])
    output_student(L)