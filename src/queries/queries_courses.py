from db.models import Course
from queries.queries_config import session_scope
from sqlalchemy import select


def get_courses():
    with session_scope() as s:
        courses = []
        query = select(Course.name, Course.description).order_by(Course.name.asc())
        result = s.execute(query)
        for i in result:
            courses.append(i)
    return courses


def get_course_info(course_name):
    with session_scope() as s:
        students = []
        query = f"SELECT students.id AS student_id, first_name, last_name, groups.name, courses.name " \
                f"FROM students_courses " \
                f"JOIN students ON student_id = students.id " \
                f"JOIN courses ON course_id = courses.id " \
                f"JOIN groups ON group_id = groups.id " \
                f"WHERE courses.name = '{course_name}' " \
                f"ORDER BY students.last_name ASC"
        result = s.execute(query)
        for i in result:
            students.append((i[0], f'{i[2]} {i[1]}', i[3]))
    return students


