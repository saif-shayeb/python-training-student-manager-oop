class Course:
    def __init__(self, name, credit_hours):
        self.name = name
        self.credit_hours = credit_hours
        self.students = {}

    def enroll(self, student):
        self.students[student.get_id()] = {
            "student": student,
            "grade": 0.0,
        }

    def set_grade(self, student, grade):
        student_id = student.get_id()
        if student_id not in self.students:
            raise KeyError("Student is not enrolled in this course")
        self.students[student_id]["grade"] = grade
        student.add_grade(grade)

    def get_students(self):
        return self.students

    def __iter__(self):
        for data in self.students.values():
            yield data["student"]
