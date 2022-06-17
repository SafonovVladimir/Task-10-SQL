from flask_restful import abort, Resource, reqparse
from db.models import db, Course
from queries.queries_courses import get_course_id_list, get_course, get_courses_name, del_course_by_id, update_course, \
    get_courses

parser = reqparse.RequestParser()
parser.add_argument("name")
parser.add_argument("description")


# якщо курса немає у базі
def abort_if_group_id_doesnt_exist(course_id):
    if course_id not in get_course_id_list():
        abort(404, message=f"Course with ID-{course_id} not found")


class Courses(Resource):

    def get(self, course_id):
        abort_if_group_id_doesnt_exist(course_id)
        data = get_course(course_id)
        output = {'name': data[0][0], 'description': data[0][1]}
        return output, 200

    def post(self):
        params = parser.parse_args()
        name = params["name"]
        description = params["description"]
        if name in get_courses_name():
            return f"Course with {name} already exists", 400
        group = Course(name, description)
        db.session.add(group)
        db.session.commit()
        return '', 204

    def delete(self, course_id):
        abort_if_group_id_doesnt_exist(course_id)
        del_course_by_id(course_id)
        return '', 204

    def put(self, course_id):
        abort_if_group_id_doesnt_exist(course_id)
        params = parser.parse_args()
        update_course(course_id, params["name"], params["description"])
        return '', 204


class CoursesList(Resource):

    def get(self):
        output = {}
        data = get_courses()
        count = 1
        for i in data:
            output[count] = {'name': i[0], 'description': i[1]}
            count += 1
        return output, 200
