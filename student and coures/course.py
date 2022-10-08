class Course:
    def __init__(self,course_name,course_class,course_id):
        self.course_name=course_name
        self.course_class=course_class
        self.course_id=course_id


    def get_course_detail(self):
        print(str(self.course_id)+ "\t\t" + self.course_name+ self.course_class)
