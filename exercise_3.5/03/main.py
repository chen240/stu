from menu import show_menu
from student_info import *


def main():
    docs=[]
    while True:
        show_menu()
        s=input("请输入选项>>")
        if s=='1':
            docs+=input_student()
        elif s=='2':
            output_student(docs)
        elif s=='3':
            modify_student(docs)
        elif s=='4':
            delete_student(docs)
        elif s=='5':
            score_student_desc(docs)
        elif s=='6':
            score_student_asc(docs)
        elif s=='7':
            age_student_desc(docs)
        elif s=='8':
            age_student_asc(docs)
        elif s=='9':
            save_to_file(docs)
        elif s=='10':
            docs=read_from_file()
        elif s=='q':
            return

main()  
