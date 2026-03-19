from src.Student import Student


def test_create_student():
    student = Student("student1", "10", [95, 78, 85])
    assert student.id == "10"
    assert student.name == "student1"
    assert student.grades == [95, 78, 85]


def test_get_average_with_grades():
    student = Student("student1", "10", [94, 78, 85])
    assert student.get_average() == 257 / 3.0


def test_get_average_without_grades():
    student = Student("student1", "10", [])
    assert student.get_average() == 0


def test_add_grade():
    student = Student("student1", "10", [89, 75])
    student.add_grade(77)
    assert student.grades == [89, 75, 77]


def test_str_():
    student = Student("student1", "10", [77, 66, 93])
    assert (
        student.__str__()
        == f"student id: {student.id} \nstudent name:{student.name}\nstudent grades:{student.grades}"
    )
