from contextlib import contextmanager
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

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
        query = "SELECT first_name, last_name, name AS course " \
                "FROM students_courses " \
                "JOIN students ON student_id = students.id " \
                "JOIN courses ON course_id = courses.id;"
        result = s.execute(text(query))
        for i in result:
            students_subjects_list.append(i)
    return students_subjects_list


def get_groups_name():
    with session_scope() as s:
        groups_name = []
        query = "SELECT * FROM groups ORDER BY id ASC "
        result = s.execute(text(query))
        for i in result:
            groups_name.append(i)
    return groups_name


def get_all_students_with_group_name():
    with session_scope() as s:
        students = []
        query = "SELECT first_name, last_name, name " \
                "FROM students " \
                "JOIN groups ON students.group_id = groups.id " \
                "ORDER BY students.last_name ASC"
        result = s.execute(text(query))
        for i in result:
            students.append(i)
    return students


# def get_group_students():
#     with session_scope() as s:
#         students = []
#         from src import Course
#         query = s.query(Course.name, Course.description).order_by(Course.name.asc())
#         result = s.execute(query)
#         for i in result:
#             students.append(i)
#     return students


#
# def get_group_inf(group_id):
#     with session_scope() as s:
#         students = []
#         query = s.query(Course.name, Course.description).order_by(Course.name.asc())
#         result = s.execute(query)
#         for i in result:
#             students.append(i)
#     return students

def get_courses():
    with session_scope() as s:
        courses = []
        query = "SELECT name, description FROM courses " \
                "ORDER BY name ASC "
        result = s.execute(text(query))
        for i in result:
            courses.append(i)
    return courses


# def get_course():
#     with session_scope() as s:
#         courses = []
#         query = s.query(Course.name, Course.description).order_by(Course.name.asc())
#         # result = s.execute(query)
#         for i in query:
#             courses.append(i)
#     return courses
