class Student:
    def __init__(self, name, id, grades):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(id, str):
            raise TypeError("ID must be a string")
        if not isinstance(grades, list):
            raise TypeError("Grades must be a list")
        for grade in grades:
            if not isinstance(grade, (int, float)):
                raise TypeError("Grades must be a list of numbers")
            if grade < 0 or grade > 4:
                raise ValueError("Grades must be between 0 and 4")
        self.__name = name
        self.__id = id
        self.__grades = list(grades)
        self.gpa = self.get_average()

    def add_grade(self, grade):
        if not isinstance(grade, (int, float)):
            raise TypeError("Grade must be a number")
        if grade < 0 or grade > 4:
            raise ValueError("Grade must be between 0 and 4")
        self.__grades.append(grade)
        self.gpa = self.get_average()

    def get_average(self):
        return sum(self.__grades) / float(max([1, len(self.__grades)]))

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_grades(self):
        return list(self.__grades)

    def __str__(self):
        result = (
            f"student id: {self.__id} \n"
            f"student name:{self.__name}\n"
            f"student grades:{self.__grades}"
        )
        return result

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_id() == other.get_id()
