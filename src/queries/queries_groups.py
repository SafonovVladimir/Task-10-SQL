from db.models import Group, Student
from queries.queries_config import session_scope
from sqlalchemy import select, delete


def get_group(group_id):
    with session_scope() as s:
        groups_name = ''
        query = select(Group.name).where(Group.id == group_id)
        result = s.execute(query)
        for i in result:
            groups_name = i[0]
    return groups_name


def get_groups_name():
    with session_scope() as s:
        groups_name = []
        query = select(Group.name).order_by(Group.name.asc())
        result = s.execute(query)
        for i in result:
            groups_name.append(i[0])
    return groups_name


def get_group_id_list():
    with session_scope() as s:
        groups_id = []
        query = select(Group.id).order_by(Group.id.asc())
        result = s.execute(query)
        for i in result:
            groups_id.append(i[0])
        return groups_id


def get_group_name_list():
    with session_scope() as s:
        groups_name = []
        query = select(Group.name).order_by(Group.name.asc())
        result = s.execute(query)
        for i in result:
            groups_name.append(i[0])
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
            groups_name.append(i[0])
    return groups_name


def get_group_id_by_name(group_name):
    with session_scope() as s:
        try:
            query = select(Group.id).where(Group.name == group_name).order_by(Group.name.asc())
            result = s.execute(query)
        except TypeError as e:
            raise TypeError(f'Group {group_name} do not find in Group"s list!', e)
        for i in result:
            return i[0]


def del_group_by_id(group_id):
    with session_scope() as s:
        query = delete(Group).where(Group.id == group_id)
        s.execute(query)


def update_group(group_id, name):
    with session_scope() as s:
        query1 = f"UPDATE groups SET " \
                 f"name = '{name}' " \
                 f"WHERE groups.id = '{group_id}' "
        s.execute(query1)
