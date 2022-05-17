import flask_restful
from flask import Blueprint, jsonify
from flask_restful import abort, reqparse

from db.models import Student, db
from queries.queries_students import get_student, del_student_by_id, update_student, get_student_id_list

API_VERSION_V1 = 1

api_bp = Blueprint('api', import_name=__name__)
api_v1 = flask_restful.Api(api_bp)

parser = reqparse.RequestParser()


# якщо студента немає у базі
def abort_if_student_id_doesnt_exist(student_id):
    if int(student_id) not in get_student_id_list():
        abort(404, message=f"Student with ID-{student_id} doesn't exist")


@api_bp.route('/student/<student_id>')
def get(student_id):
    abort_if_student_id_doesnt_exist(student_id)
    data = get_student(student_id)
    output = {'ID': data[0][0], 'student name': data[0][1], 'group': data[0][2]}
    return jsonify(output)


def post(arg=dict):
    first_name = arg['first_name']
    last_name = arg['last_name']
    student_group = arg['group']
    student = Student(first_name, last_name, student_group)
    db.session.add(student)
    db.session.commit()
    return '', 204


def delete(student_id):
    abort_if_student_id_doesnt_exist(student_id)
    del_student_by_id(student_id)
    return '', 204


def put(student_id, arg=dict):
    abort_if_student_id_doesnt_exist(student_id)
    first_name = arg['first_name']
    last_name = arg['last_name']
    student_group = arg['group']
    update_student(student_id, first_name, last_name, student_group)
    return '', 204
