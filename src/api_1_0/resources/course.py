import flask_restful
from flask import Blueprint, render_template, request
from flask_restful import abort, Resource

from db.models import Student, db, StudentsCourses, Course
from queries.queries_courses import get_course_id_by_name
from queries.queries_groups import get_group_id_by_name
from queries.queries_students import get_student, del_student_by_id

API_VERSION_V1 = 1

api_bp = Blueprint('api', import_name=__name__)
api_v1 = flask_restful.Api(api_bp)


# якщо course немає у базі
# def abort_if_course_id_doesnt_exist(course_id):
#     if course_id not in get_course_id():
#         abort(404, message=f"Course with ID-{course_id} doesn't exist")


@api_bp.route('/course/<course_id>', methods=['GET'])
def get(course_id):
    data = get_student(course_id)
    s_id = data[0][0]
    s_name = data[0][1]
    group = data[0][2]
    return render_template('course/edit_course.html', id=s_id, name=s_name, group=group)


@api_bp.route('/add_course/', methods=['POST'])
def post():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_group = request.form['student_group']
    group_id = get_group_id_by_name(student_group)

    student = Course(first_name, last_name, group_id)
    db.session.add(student)
    db.session.commit()
    return render_template('success/add_success.html')


@api_bp.route('/del_student/', methods=['POST'])
def delete():
    student_id = request.form['student_id']
    del_student_by_id(student_id)
    return render_template('success/del_success.html', id=student_id)


@api_bp.route('/change_course/', methods=['POST'])
def put():
    student_id = request.form['student_id']
    course_name = request.form['course']
    course_id = get_course_id_by_name(course_name)
    student = StudentsCourses(student_id, course_id)
    db.session.add(student)
    db.session.commit()
    return render_template('success/add_success.html')
