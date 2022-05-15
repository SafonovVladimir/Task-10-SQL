from db.randomly_data import *
from src.db.models import *

# create database and the db tables
db.create_all()

# insert data
for _ in range(10):
    db.session.add(Group(get_groups()))
    db.session.commit()

for k, v in subject.items():
    db.session.add(Course(k, v))
    db.session.commit()

j = 1
for i in (get_random_digit_in_range(200, 10, 10, 30)):
    count = 1
    while count <= i:
        db.session.add(Student(get_random_student_first_name(), get_random_student_last_name(), j))
        db.session.commit()
        count += 1
    j += 1

for i in range(1, 201):
    for j in get_random_course_id():
        db.session.add(StudentsCourses(i, j))
        db.session.commit()
