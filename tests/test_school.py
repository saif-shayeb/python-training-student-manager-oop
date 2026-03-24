import pytest

from src.school.Course import Course
from src.school.GraduateStudent import GraduateStudent
from src.school.Professor import Professor
from src.school.Student import Student


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


def test_student_eq_by_id():
    first = Student("alice", "42", [4])
    second = Student("bob", "42", [2])
    assert first == second


def test_student_eq_with_other_type():
    student = Student("alice", "42", [4])
    assert (student == "42") is False


def test_graduate_student_creation():
    grad = GraduateStudent("grad1", "77", [3.5], "Distributed Systems")
    assert grad.get_id() == "77"
    assert grad.get_name() == "grad1"


def test_course_enroll_set_grade_and_iterate_students():
    course = Course("Math", 3)
    student = Student("student1", "10", [])

    course.enroll(student)
    course.set_grade(student, 3.5)

    students = list(course)
    assert len(students) == 1
    assert students[0] == student
    assert course.get_students()[student.get_id()]["grade"] == 3.5


def test_course_set_grade_for_unenrolled_student_raises():
    course = Course("Math", 3)
    student = Student("student1", "10", [])

    with pytest.raises(KeyError):
        course.set_grade(student, 3.0)


def test_professor_add_course_and_set_grade():
    professor = Professor("Dr. Smith", "CS")
    course = Course("Algorithms", 4)
    student = Student("student1", "10", [])

    professor.add_course(course)
    course.enroll(student)
    professor.set_grade(student, 4.0, course)

    assert course in professor.courses
    assert course.get_students()[student.get_id()]["grade"] == 4.0
