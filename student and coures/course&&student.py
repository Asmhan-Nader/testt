from course import Course
from student import Student
def search_fun(search):
    for i in student_course:
        if search == i.course_name:
            print("its exist")

def search_fun2(search):
    for i in student_list:
        if search == i.student_num :
            print("its exist")
num = int (input("enter num of stu you wana enter"))
student_list=[]
student_course=[]
alpha=["A","B","C"]

for i in range(num):
    stu_name= input("enter stu name")
    stu_class=input("enter stu class")
    while True:
        if stu_class in alpha:
            break
        stu_class = input("enter stu class A,B,C")
    stu = Student( stu_name, stu_class )
    student_list.append(stu)


    course_name = input("enter course name")
    course_class = input("enter course class")
    while True:
         if course_class in alpha:
            break
         course_class = input("enter stu class A,B,C")
    cours = Course(course_name,course_class)
    student_course.append(cours)
    stu.add_course(cours)
    for i in student_list:
        print(i.get_student())



search =int(input("enter your num"))
search_fun2(search)

search2 =input("enter course name")
search_fun(search2)






