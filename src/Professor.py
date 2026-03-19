
from Student import Student

class Professor:
    def __init__(self,name,major):
        self.name= name
        self.major = major
        self.courses = []
    def add_course(self,course):
        self.courses.append(course)
    def set_grade(self,student,grade):
        student.add_grade(grade)        

prof = Professor("adam","computer Engineering")
student = Student("saif","11",[])
prof.set_grade(student,89)
print(student)
