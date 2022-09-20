from course import Course
from student import Student
num = int (input("enter num of stu you wana enter"))
student_list=[]
student_course=[]
for i in range(num):
    stu = Student(input("enter stu name"), input("enter stu class"))
    stu1_course = Course(input("enter course name"), input("enter course class"))
    student_list.append(stu)
    student_course.append(stu1_course)
    stu.add_course(stu1_course)
    for i in student_list:
        print(i.get_student())
search =int(input("enter your num"))
for i in student_list:
    if  search in i["student_num"]:
        print("its exist")







