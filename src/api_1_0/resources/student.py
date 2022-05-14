from flask import request
from flask_restful import abort, Resource, reqparse
from xml.dom.minidom import parseString
from dicttoxml import dicttoxml

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('team')
parser.add_argument('lap')


# якщо пілота немає у базі
def abort_if_driver_id_doesnt_exist(driver_abb):
    if driver_abb not in query_driver_abb():
        abort(404, message=f"Driver {driver_abb} doesn't exist")


class StudentName(Resource):

    # інформація по пілоту
    def get(self, driver_abb):
        abort_if_driver_id_doesnt_exist(driver_abb)

        data = {driver_abb: {'name': name, 'team': team, 'lap': lap}}
        return data

    # видалення пілота
    def delete(self, driver_abb):
        abort_if_driver_id_doesnt_exist(driver_abb)
        query_driver_delete(driver_abb)
        return '', 204

    # додавання пілота
    def post(self, driver_abb):
        insert_driver_data(driver_abb, parser.parse_args())
        return query(), 201

    # зміна даних пілота
    def put(self, driver_abb):
        abort_if_driver_id_doesnt_exist(driver_abb)
        update_driver_data(driver_abb, parser.parse_args())
        # return query(), 201


class StudentsList(Resource):
    # отримання звіту по всім пілотам
    def get(self):
        f = request.args.get('format')
        if f == 'json':
            return query()
        elif f == 'xml':
            xml = dicttoxml(query(), attr_type=False)
            return parseString(xml).toprettyxml()
