from flask import request
from flask_restful import abort, Resource, reqparse
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml

from queries.queries import get_student
from src.api_1_0.resources import get_student_info

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('team')
parser.add_argument('lap')


# якщо студента немає у базі
def abort_if_student_id_doesnt_exist(student_id):
    for i in get_student():
        if student_id not in str(i[0]):
            abort(404, message=f"Student with ID-{student_id} doesn't exist")


class StudentInfo(Resource):

    # Get student's info
    def get(self, student_id):
        abort_if_student_id_doesnt_exist(student_id)
        data = get_student_info(student_id)
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
