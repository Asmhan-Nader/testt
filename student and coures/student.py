import random

from course import Course


class Student:
    def __init__(self, name, student_class):
        self.student_name = name
        self.student_num = random.randint(0, 1000)  # get random stu number
        self.student_class = student_class

    stu_courses = []

    def add_course(self, courses):#courses is an obj so we will pass it as a parameter to function
        if self.student_class == courses.course_class:
            self.stu_courses.append(courses)  # that means I sort class in list

    def get_student(self):
        if len(self.stu_courses) == 0:
            print("there is not any courses enrolled")
        else:
            for i in range(len(self.stu_courses)):
                print(self.stu_courses[i].course_class)
        print(self.student_name)
        print(self.student_class)
        print(self.student_num)
