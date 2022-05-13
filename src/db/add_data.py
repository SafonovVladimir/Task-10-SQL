from db.create_random_data import get_groups, subject, get_random_student_first_name, get_random_student_last_name, \
    get_random_digit_in_range
from src.db.models import db
from src.db.models import Group, Student, Course

# create database and the db tables
# db.create_all()
#
# # insert data
# for _ in range(10):
#     db.session.add(Group(get_groups()))
#     db.session.commit()
#
#
# for k, v in subject.items():
#     db.session.add(Course(k, v))
#     db.session.commit()
#
j = 1
for i in (get_random_digit_in_range(200, 10, 10, 30)):
    count = 1
    while count <= i:
        db.session.add(Student(get_random_student_first_name(), get_random_student_last_name(), j))
        db.session.commit()
        count += 1
    j += 1
#
# # db.session.add(courses(ge))
#
# # commit the changes to db
# db.session.commit()
