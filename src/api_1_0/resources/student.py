import flask_restful
from flask import Blueprint, jsonify, render_template
from flask_restful import abort, Resource

from queries.queries_students import get_student_id, get_student

API_VERSION_V1 = 1

api_bp = Blueprint('api', import_name=__name__)
api_v1 = flask_restful.Api(api_bp)


# якщо студента немає у базі
def abort_if_student_id_doesnt_exist(student_id):
    if student_id not in get_student_id():
        abort(404, message=f"Student with ID-{student_id} doesn't exist")


@api_bp.route('/student/<student_id>', methods=['GET'])
def get(student_id):
    data = get_student(student_id)
    s_id = data[0][0]
    s_name = data[0][1]
    group = data[0][2]
    return render_template('edit_student.html', id=s_id, name=s_name, group=group)


@api_bp.route('/student/<student_id>', methods=['POST'])
def post(student_id):
    numbers = []
    students_id = []
    students_name = []
    groups = []
    data = get_student(student_id)
    numbers.append(1)
    students_id.append(data[0][0])
    students_name.append(data[0][1])
    groups.append(data[0][2])
    return render_template('students.html', number=numbers, id=students_id, name=students_name, group=groups)


class StudentInfo(Resource):

    # Get student's info
    def get(self, student_id):
        abort_if_student_id_doesnt_exist(student_id)
        data = get_student(student_id)
        return data

    def delete(self, driver_abb):
        abort_if_student_id_doesnt_exist(driver_abb)
        # query_driver_delete(driver_abb)
        # return '', 204

    # def post(self, driver_abb):
    #     insert_driver_data(driver_abb, parser.parse_args())
    #     return query(), 201

    def put(self, driver_abb):
        abort_if_student_id_doesnt_exist(driver_abb)
        # update_driver_data(driver_abb, parser.parse_args())
        # return query(), 201
