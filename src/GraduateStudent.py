from Student import Student
class GraduateStudent(Student):
    def __init__(self,name,id,grades,thesis_title):
        super().__init__(name,id,grades)
        self._thesis_title = thesis_title

