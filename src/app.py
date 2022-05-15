from flask import render_template, request
from api_1_0 import API_VERSION_V1, api_bp
from config import config, Config
from src.queries.queries import *
import src.api_1_0.routes

app = Config.app
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['REST_URL_PREFIX'] = Config.REST_URL_PREFIX
conf = app.config['REST_URL_PREFIX']

def create_app(config_name):
    app.config.from_object(config[config_name])

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/groups')
    def groups():
        num = []
        group_name = []
        res = get_groups_name()
        count = 1
        for i in res:
            num.append(count)
            group_name.append(i[0])
            count += 1
        return render_template('groups.html', id=num, name=group_name)

    @app.route('/group')
    def group():
        num = []
        group_name = []
        student = []
        student_id = []
        rev = request.args.get('group_id')
        res = get_group_inf(rev)
        count = 1
        for i in res:
            num.append(count)
            student_id.append(i[0])
            group_name.append(i[2])
            student_name = i[1]
            student.append(student_name)
            count += 1
        return render_template('students.html', number=num, id=student_id, name=student, group=group_name)

    @app.route('/students')
    def students():
        num = []
        student_id = []
        group_name = []
        student = []
        res = get_all_students_with_group_name()
        count = 1
        for i in res:
            num.append(count)
            student_id.append(i[0])
            group_name.append(i[2])
            student.append(i[1])
            count += 1
        return render_template('students.html', number=num, id=student_id, name=student, group=group_name)

    @app.route('/student')
    def student():
        num = []
        subject = []
        description = []
        rev = request.args.get('student_id')
        res = get_student_info(rev)
        count = 1
        for i in res:
            num.append(count)
            description.append(i[1])
            subject.append(i[0])
            count += 1
        return render_template('courses.html', id=num, name=subject, description=description)

    @app.route('/edit_student')
    def edit_student():
        return render_template('edit_student.html')

    @app.route('/delete_student')
    def delete_student():
        return render_template('edit_student.html')

    @app.route('/courses')
    def courses():
        num = []
        course_name = []
        description = []
        res = get_courses()
        count = 1
        for i in res:
            num.append(count)
            course_name.append(i[0])
            description.append(i[1])
            count += 1
        return render_template('courses.html', id=num, name=course_name, description=description)

    @app.route('/course')
    def course():
        num = []
        student_id = []
        group_name = []
        student = []
        rev = request.args.get('course_name')
        res = get_course_info(rev)
        count = 1
        for i in res:
            num.append(count)
            student_id.append(i[0])
            group_name.append(i[2])
            student.append(i[1])
            count += 1
        return render_template('students.html', number=num, id=student_id, name=student, group=group_name)

    ver = API_VERSION_V1
    app.register_blueprint(api_bp, url_prefix=f'{conf}/v{ver}', )

    return app
