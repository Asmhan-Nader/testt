from course import Course
from student import Student

print ("""           1-Add new student
           2-Remove student
           3-Edit student
           4-Display all sudent
           5-creat new course
           6-Add course to student
           0.exi""")
student_list=[]
student_course=[]
alpha=["A","B","C"]
while True:# in order not to stop the program
     num = int(input("enter the num of request you want"))
     if num == 1:
        stu_name = input("enter stu name")
        stu_class = input("enter stu class")
        while True:
          if stu_class in alpha:
            break
          stu_class = input("enter stu class A,B,C")
        stu = Student(stu_name, stu_class)
        student_list.append(stu)
        print("student saved successfully")

     if num==2:
        id=input("enter stu id")
        for i in student_list:
            if i.student_num==id:
                 student_list.pop(student_list.index(i))# هان بس بد اجيب اندكس ل عنصر المصفوفة
     if num == 3:
         stu_id = input("enter stu id")
         for i in student_list:
             if i.student_num == id:
                 i.student_num=input("enter new stu num")
                 i.student_class=input("enter new stu class")
                 break
             # هادي مشان لما الاقي الاسم يعدل عليه و يطلع بسرعة
             if student_list.index(i)== (len(student_list)-1):
                print("its not exist")

     if num==4:
         for i in student_list:
             i.get_student()
     if num==5:
        course_name = input("enter course name")
        course_class = input("enter course class")
        course_id = input("enter course id")
        while True:
           if course_class in alpha:
             break
           course_class = input("enter course class A,B,C")
        cours = Course(course_name, course_class,course_id)
        student_course.append(cours)
     if num ==6:
         stu_id = int(input("enter stu id"))
         for i in student_list:
             if i.student_num == stu_id:
                 a=student_list.index(i)
                 course_namee=input("enter course name")
                 for i in student_course:
                     if i.course_name==course_namee:
                         student_list[a].add_course(cours)
     if(num==0):
         exit






