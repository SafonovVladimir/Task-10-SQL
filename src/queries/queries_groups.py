from db.models import Group, Student
from queries.queries_config import session_scope
from sqlalchemy import select


def get_groups_name():
    with session_scope() as s:
        groups_name = []
        query = select(Group.name).order_by(Group.name.asc())
        result = s.execute(query)
        for i in result:
            groups_name.append(i)
    return groups_name


def get_group_inf(group_name):
    with session_scope() as s:
        students = []
        query = select(Student.id, Student.first_name, Student.last_name, Group.name). \
            join(Group).where(Group.name == group_name).order_by(Student.last_name.asc())
        result = s.execute(query)
        for i in result:
            students.append((i[0], f'{i[2]} {i[1]}', i[3]))
    return students


def get_groups_with_student_count(students_count):
    with session_scope() as s:
        groups_name = []
        query = f"SELECT groups.name " \
                f"FROM groups " \
                f"LEFT JOIN students ON group_id = groups.id " \
                f"GROUP BY groups.id " \
                f"HAVING COUNT (students.id) <= '{students_count}' " \
                f"ORDER BY groups.id"
        result = s.execute(query)
        for i in result:
            groups_name.append(i)
    return groups_name

print(get_groups_with_student_count(20))