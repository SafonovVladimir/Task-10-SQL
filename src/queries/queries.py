from contextlib import contextmanager
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from db.models import Course, Group, Student, StudentsCourses

engine = create_engine('postgresql://admin:admin@localhost:5432/uni')
conn = engine.connect()
Session = sessionmaker(bind=engine, expire_on_commit=False, )


@contextmanager
def session_scope():
    """Provides a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


def get_students_subjects_list():
    with session_scope() as s:
        students_subjects_list = []
        query = select(Student.first_name, Student.last_name, Course.name)
        result = s.execute(query)
        for i in result:
            students_subjects_list.append(i)
    return students_subjects_list


def get_groups_name():
    with session_scope() as s:
        groups_name = []
        query = select(Group.name).order_by(Group.name.asc())
        result = s.execute(query)
        for i in result:
            groups_name.append(i)
    return groups_name


def get_all_students_with_group_name():
    with session_scope() as s:
        students = []
        query = select(Student.id, Student.first_name, Student.last_name, Group.name).\
            join(Group).order_by(Student.last_name.asc())
        result = s.execute(query)
        for i in result:
            students.append((i[0], f'{i[2]} {i[1]}', i[3]))
    return students


def get_group_inf(group_name):
    with session_scope() as s:
        students = []
        query = select(Student.id, Student.first_name, Student.last_name, Group.name).\
            join(Group).where(Group.name == group_name).order_by(Student.last_name.asc())
        result = s.execute(query)
        for i in result:
            students.append((i[0], f'{i[2]} {i[1]}', i[3]))
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
