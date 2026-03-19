from typing import Self


class Student:
    def __init__(self, name, id, grades):
        self.name = name
        self.id = id
        self.grades = []
        self.grades.extend(grades)

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / float(max([1, len(self.grades)]))


    def __str__(self):
        result = f"student id: {self.id} \nstudent name:{self.name}\nstudent grades:{self.grades}"
        return result


