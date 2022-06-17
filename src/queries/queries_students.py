from src.db.models import Student, Course, Group, StudentsCourses
from src.queries.queries_config import session_scope
from sqlalchemy import select, delete
from src.queries.queries_courses import get_course_id_by_name
from src.queries.queries_groups import get_group_id_by_name


def get_students_subjects_list():
    with session_scope() as s:
        students_subjects_list = []
        query = select(Student.first_name, Student.last_name, Course.name)
        result = s.execute(query)
        for i in result:
            students_subjects_list.append(i)
    return students_subjects_list


def get_all_students_with_group_name():
    with session_scope() as s:
        students = []
        query = select(Student.id, Student.first_name, Student.last_name, Group.name). \
            join(Group).order_by(Student.last_name.asc())
        result = s.execute(query)
        for i in result:
            students.append((i[0], f'{i[2]} {i[1]}', i[3]))
    return students


def get_student(student_id):
    with session_scope() as s:
        students = []
        query = select(Student.id, Student.last_name, Student.first_name, Group.name) \
            .join(Group).where(Student.id == student_id)
        result = s.execute(query)
        for i in result:
            students.append((i[0], f'{i[1]} {i[2]}', i[3]))
        return students


def get_student_courses(student_id):
    with session_scope() as s:
        students = []
        query = f"SELECT name AS course, description " \
                f"FROM students_courses " \
                f"JOIN students ON student_id = students.id " \
                f"JOIN courses ON course_id = courses.id " \
                f"WHERE students.id = '{student_id}' " \
                f"ORDER BY students.last_name ASC"
        result = s.execute(query)
        for i in result:
            students.append(i)
    return students


def get_student_id_list():
    with session_scope() as s:
        students_id = []
        query = select(Student.id)
        result = s.execute(query)
        for i in result:
            students_id.append(i[0])
    return students_id


def del_student_by_id(student_id):
    with session_scope() as s:
        query = delete(StudentsCourses).where(StudentsCourses.student_id == student_id)
        s.execute(query)
        query = delete(Student).where(Student.id == student_id)
        s.execute(query)


def del_course_from_student(student_id, course_name):
    with session_scope() as s:
        course_id = get_course_id_by_name(course_name)
        query = f"DELETE FROM students_courses " \
                f"WHERE student_id = '{student_id}' AND course_id = '{course_id}' "
        s.execute(query)


def add_course_to_student(student_id, course_name):
    with session_scope() as s:
        course_id = get_course_id_by_name(course_name)
        student = StudentsCourses(student_id, course_id)
        s.add(student)
        s.commit()


def update_student(student_id, first_name, last_name, group):
    with session_scope() as s:
        group_id = int(get_group_id_by_name(group))
        query1 = f"UPDATE students SET " \
                 f"first_name = '{first_name}' " \
                 f"WHERE students.id = '{student_id}' "
        query2 = f"UPDATE students SET " \
                 f"last_name = '{last_name}' " \
                 f"WHERE students.id = '{student_id}' "
        query3 = f"UPDATE students SET " \
                 f"group_id = '{group_id}' " \
                 f"WHERE students.id = '{student_id}' "
        s.execute(query1)
        s.execute(query2)
        s.execute(query3)
