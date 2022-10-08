from course import Course
from student import Student
def find_stu(student_list ,stu_id):
    index=0
    for i in student_list:
        if i.student_num == stu_id:
            return index
        index+=1
    return -1
def find_course(student_course ,course_name ):
    index=0
    for i in student_course:
        if i.course_name == course_name:
            return index
        index+=1
    return -1
def get_stu_detail(student_list) :
    for i in student_list:
        i.get_student

student_list = []
student_course = []
alpha = ["A", "B", "C"]

while True:  # in order not to stop the program
    num = int(input("""enter the num of request you want\n           1-Add new student
           2-Remove student
           3-Edit student
           4-Display all sudent
           5-creat new course
           6-Add course to student
           0.exi"""))
    if num == 1:
        stu_name = input("enter stu name")
        stu_class = input("enter stu class")
        stu_id=len(student_list)+1
        while True:
            if stu_class in alpha:
                break
            stu_class = input("enter stu class A,B,C")
        stu = Student(stu_name, stu_class,stu_id)
        student_list.append(stu)
        print("student saved successfully")

    if num == 2:
        id = int(input("enter stu id"))
        if find_stu(student_list,id)== -1:
            print("sorry we cant find what you want")
        else:
             student_list.pop(student_list.index(find_stu(student_list,id)))  # هان بس بد اجيب اندكس ل عنصر المصفوفة
    if num == 3:
        stu_id = input("enter stu id")
        if find_stu(student_list, id) == -1:
            print("sorry we cant find what you want")
        else:
             student_num = input("enter new stu num")
             student_class = input("enter new stu class")


    if num == 4:
        for i in student_list:
            i.get_student()
    if num == 5:
        course_name = input("enter course name")
        course_class = input("enter course class")
        course_id = len(student_course)+1
        while True:
            if course_class in alpha:
                break
            course_class = input("enter course class (A,B,C)")
        cours = Course(course_name, course_class, course_id)
        student_course.append(cours)
    if num == 6:
        stu_id = int(input("enter stu id"))
        a = find_stu(student_list, id)
        if a == -1:
            print("sorry we cant find what you want")
        else:
                course_namee = input("enter course name")
                if  find_course(student_course,course_namee)==-1:
                    print("sorry we cant do this process")
                else:
                        student_list[a].add_course(student_course[find_course(student_course,course_namee)])
    if (num == 0):
        exit







