from db.models import Student, Course, Group
from queries.queries_config import session_scope
from sqlalchemy import select


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


def get_student_info(student_id):
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


def get_student_id():
    with session_scope() as s:
        students_id = []
        query = select(Student.id)
        result = s.execute(query)
        for i in result:
            students_id.append(i[0])
    return students_id
