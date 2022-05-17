from flask_restful import abort, Resource, reqparse
from db.models import Student, db
from queries.queries_groups import get_group_id_by_name
from queries.queries_students import get_student, del_student_by_id, update_student, get_student_id_list

parser = reqparse.RequestParser()
parser.add_argument("first_name")
parser.add_argument("last_name")
parser.add_argument("group")


# якщо студента немає у базі
def abort_if_student_id_doesnt_exist(student_id):
    if int(student_id) not in get_student_id_list():
        abort(404, message=f"Student with ID-{student_id} not found")


class Students(Resource):

    def get(self, student_id):
        abort_if_student_id_doesnt_exist(student_id)
        data = get_student(student_id)
        output = {'ID': data[0][0], 'student name': data[0][1], 'group': data[0][2]}
        return output, 200

    def post(self):
        params = parser.parse_args()
        group_id = get_group_id_by_name(params["group"])
        student = Student(params["first_name"], params["last_name"], group_id)
        db.session.add(student)
        db.session.commit()
        return '', 204

    def delete(self, student_id):
        abort_if_student_id_doesnt_exist(student_id)
        del_student_by_id(student_id)
        return '', 204

    def put(self, student_id):
        abort_if_student_id_doesnt_exist(student_id)
        params = parser.parse_args()
        update_student(student_id, params["first_name"], params["last_name"], params["group"])
        return '', 204
