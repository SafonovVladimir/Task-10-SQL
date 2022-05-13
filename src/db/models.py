from flask_sqlalchemy import SQLAlchemy
from src.app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/uni'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# courses = db.Table('courses',
#                    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
#                    db.Column('id', db.Integer, db.ForeignKey('course'), primary_key=True)
#                    )


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(5), unique=True)
    # students = db.relationship('Student', backref='group', lazy=True)

    def __init__(self, name):
        self.name = name


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    group_id = db.Column(db.Integer, nullable=True)
    # group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    # course_id = db.relationship('Course', secondary=courses, lazy='subquery',
    #                             backref=db.backref('students', nullable=False, lazy=True))

    def __init__(self, first_name, last_name, id_group):
        self.first_name = first_name
        self.last_name = last_name
        self.id_group = id_group


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    description = db.Column(db.String(250))


    def __init__(self, name, description):
        self.name = name
        self.description = description
