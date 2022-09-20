import random


class Student:
    def __init__(self,name,student_class):
        self.student_name=name
        self,student_class=student_class
        self,student_num =random.randint(9999,1000000)
    stu_courses=[]
    def add_course(self,courses):
      self.stu_courses.append(courses)