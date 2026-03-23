class Course:
    def __init__(self, name, credit_hours):
        self.name = name
        self.credit_hours = credit_hours
        self.students = {}

    def enroll(self, student):
        self.students[student.get_id()] = {student, 0.0}

    def set_grade(self, student, grade):
        self.students[student.get_id()][1] = grade
        student.add_grade(grade)

    def get_students(self):
        return self.students

    def __iter__(self):
        for student in self.students:
            yield student
