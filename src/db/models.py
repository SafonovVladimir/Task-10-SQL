from flask_sqlalchemy import SQLAlchemy
from src.app import app

db = SQLAlchemy(app)


class Group(db.Model):
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(5), unique=True)
    students = db.relationship('Student', backref='group', lazy=True)

    def __init__(self, name):
        self.name = name


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)

    def __init__(self, first_name, last_name, group_id):
        self.first_name = first_name
        self.last_name = last_name
        self.group_id = group_id


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    description = db.Column(db.String(250))

    def __init__(self, name, description):
        self.name = name
        self.description = description


class StudentsCourses(db.Model):
    __tablename__ = 'students_courses'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))

    def __init__(self, student_id, course_id):
        self.student_id = student_id
        self.course_id = course_id
