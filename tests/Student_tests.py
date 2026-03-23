from src.school.Student import Student
import pytest


def test_create_student():
    student = Student("student1", "10", [4, 3.5, 3])
    assert student.get_id() == "10"
    assert student.get_name() == "student1"
    assert student.get_grades() == [4, 3.5, 3]


def test_get_average_with_grades():
    student = Student("student1", "10", [4, 3.5, 3])
    assert student.get_average() == 10.5 / 3.0


def test_get_average_without_grades():
    student = Student("student1", "10", [])
    assert student.get_average() == 0


def test_add_grade():
    student = Student("student1", "10", [4, 3.5])
    student.add_grade(3)
    assert student.get_grades() == [4, 3.5, 3]


def test_str_():
    student = Student("student1", "10", [4, 3.5, 3])
    assert student.__str__() == (
        f"student id: {student.get_id()} \n"
        f"student name:{student.get_name()}\n"
        f"student grades:{student.get_grades()}"
    )


def test_create_student_invalid_name():
    with pytest.raises(TypeError):
        Student(123, "10", [4, 3.5, 3])


def test_create_student_invalid_id():
    with pytest.raises(TypeError):
        Student("student1", 10, [4, 3.5, 3])


def test_create_student_invalid_grades_type():
    with pytest.raises(TypeError):
        Student("student1", "10", "not a list")


def test_create_student_invalid_grade_value():
    with pytest.raises(ValueError):
        Student("student1", "10", [4, 3.5, 5])


def test_add_invalid_grade():
    student = Student("student1", "10", [4, 3.5, 3])
    with pytest.raises(TypeError):
        student.add_grade("not a number")


def test_add_invalid_grade_value():
    student = Student("student1", "10", [4, 3.5, 3])
    with pytest.raises(ValueError):
        student.add_grade(5)
