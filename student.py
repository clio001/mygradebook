class Student():
    name = ''
    course = []
    
    def add_student(self, name: str, course: str):
        self.course.append(name)
        print(course)

    def get_student(self, course):
        self.course=course
        print(course)
