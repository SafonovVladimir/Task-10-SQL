from flask_restful import abort, Resource, reqparse
from src.db.models import db, Group
from src.queries.queries_groups import get_group_id_list, get_group, get_groups_name, del_group_by_id, update_group, \
    get_group_name_list

parser = reqparse.RequestParser()
parser.add_argument("name")


# якщо групи немає у базі
def abort_if_group_id_doesnt_exist(group_id):
    if group_id not in get_group_id_list():
        abort(404, message=f"Group with ID-{group_id} not found")


class Groups(Resource):

    def get(self, group_id):
        abort_if_group_id_doesnt_exist(group_id)
        data = get_group(group_id)
        output = {'name': data}
        return output, 200

    def post(self):
        params = parser.parse_args()
        name = params["name"]
        if name in get_groups_name():
            return f"Group with {name} already exists", 400
        group = Group(name)
        db.session.add(group)
        db.session.commit()
        return '', 204

    def delete(self, group_id):
        abort_if_group_id_doesnt_exist(group_id)
        del_group_by_id(group_id)
        return '', 204

    def put(self, group_id):
        abort_if_group_id_doesnt_exist(group_id)
        params = parser.parse_args()
        update_group(group_id, params["name"])
        return '', 204


class GroupsList(Resource):

    def get(self):
        output = {}
        data = get_group_name_list()
        count = 1
        for i in data:
            output[count] = {'group name': i}
            count += 1
        return output, 200
