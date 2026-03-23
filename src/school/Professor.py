class Professor:
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def set_grade(self, student, grade, course):
        course.set_grade(student, grade)
