import flask_restful
from flask import Blueprint, render_template, request
from flask_restful import abort, Resource

from db.models import Student, db, StudentsCourses
from queries.queries_courses import get_course_id_by_name
from queries.queries_groups import get_group_id_by_name
from queries.queries_students import get_student, del_student_by_id, del_course_from_student

API_VERSION_V1 = 1

api_bp = Blueprint('api', import_name=__name__)
api_v1 = flask_restful.Api(api_bp)


# якщо студента немає у базі
# def abort_if_student_id_doesnt_exist(student_id):
#     if student_id not in get_student_id():
#         abort(404, message=f"Student with ID-{student_id} doesn't exist")


@api_bp.route('/student/', methods=['GET', 'POST'])
def get():
    stud_id = request.form['student_id']
    data = get_student(stud_id)
    return render_template('student/students.html', number=[1], id=[data[0][0]], name=[data[0][1]], group=[data[0][2]])


@api_bp.route('/add_student/', methods=['POST'])
def post():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_group = request.form['student_group']
    group_id = get_group_id_by_name(student_group)

    student = Student(first_name, last_name, group_id)
    db.session.add(student)
    db.session.commit()
    return render_template('success/add_success.html')


@api_bp.route('/del_student/', methods=['POST'])
def delete():
    student_id = request.form['stud_id']
    del_student_by_id(student_id)
    return render_template('success/del_success.html', id=student_id)


@api_bp.route('/change_student/', methods=['POST'])
def put():
    student_id = request.form['student_id']
    course_name = request.form['course']
    course_id = get_course_id_by_name(course_name)
    student = StudentsCourses(student_id, course_id)
    db.session.add(student)
    db.session.commit()
    # elif btn2:
    #     del_course_from_student(student_id, course_id)
    #     db.session.commit()
    return render_template('success/add_success.html')

# @api_bp.route('/change_student/', methods=['POST'])
# def put():
#     btn1 = request.form['btn1']
#     btn2 = request.form['btn2']
#     student_id = request.form['student_id']
#     course_name = request.form['course']
#     course_id = get_course_id_by_name(course_name)
#     if btn1:
#         student = StudentsCourses(student_id, course_id)
#         db.session.add(student)
#         db.session.commit()
#     elif btn2:
#         del_course_from_student(student_id, course_id)
#         db.session.commit()
#     return render_template('success/add_success.html')
