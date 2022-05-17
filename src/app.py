from flask import render_template, request
from api_1_0 import API_VERSION_V1
from api_1_0.resources.student import api_bp, post, delete
from config import config, Config
from db.models import StudentsCourses
from queries.queries_courses import get_course_info, get_courses, get_course_id_by_name
from queries.queries_groups import get_group_inf, get_groups_name, get_groups_with_student_count, get_group_id_by_name
from queries.queries_students import get_student_courses, get_all_students_with_group_name, add_course_to_student, \
    del_course_from_student, del_student_by_id

app = Config.app
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['REST_URL_PREFIX'] = Config.REST_URL_PREFIX
conf = app.config['REST_URL_PREFIX']
ver = API_VERSION_V1


def create_app(config_name):
    app.config.from_object(config[config_name])
    app.register_blueprint(api_bp, url_prefix=f'{conf}/v{ver}')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/groups')
    def groups():
        num = []
        group_name = []
        rev = request.args.get('student_count')
        if rev:
            res = get_groups_with_student_count(rev)
        else:
            res = get_groups_name()
        count = 1
        for i in res:
            num.append(count)
            group_name.append(i[0])
            count += 1
        return render_template('groups/groups.html', id=num, name=group_name)

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
        return render_template('student/students.html', number=num, id=student_id, name=student, group=group_name)

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
        return render_template('student/students.html', number=num, id=student_id, name=student, group=group_name)

    @app.route('/student')
    def student():
        num = []
        subject = []
        description = []
        rev = request.args.get('student_id')
        res = get_student_courses(rev)
        count = 1
        for i in res:
            num.append(count)
            description.append(i[1])
            subject.append(i[0])
            count += 1
        return render_template('course/courses.html', id=num, name=subject, description=description)

    @app.route('/add_course', methods=['POST'])
    def add_course():
        student_id = request.form['s_id']
        course_name = request.form['courses']
        add_course_to_student(student_id, course_name)
        return render_template('success/add_success.html')

    @app.route('/del_course', methods=['POST'])
    def del_course():
        student_id = request.form['s_id_del']
        course_name = request.form['course_del']
        del_course_from_student(student_id, course_name)
        return render_template('success/del_success.html')

    @app.route('/add_student', methods=['POST'])
    def add_student():
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        student_group = request.form['student_group']
        group_id = get_group_id_by_name(student_group)
        output = {'first_name': first_name, 'last_name': last_name, 'group': group_id}
        post(output)
        return render_template('success/add_success.html')

    @app.route('/del_student', methods=['POST'])
    def del_student():
        student_id = request.form['stud_id']
        delete(student_id)
        return render_template('success/del_success.html', id=student_id)

    @app.route('/success')
    def success():
        return render_template('success/add_success.html')

    @app.route('/queries', methods=['GET'])
    def queries():
        return render_template('queries.html')

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
        return render_template('course/courses.html', id=num, name=course_name, description=description)

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
        return render_template('student/students.html', number=num, id=student_id, name=student, group=group_name)

    @app.route('/submit')
    def submit():
        num = []
        student_id = []
        group_name = []
        student = []
        rev = request.args.get('course')
        res = get_course_info(rev)
        count = 1
        for i in res:
            num.append(count)
            student_id.append(i[0])
            group_name.append(i[2])
            student.append(i[1])
            count += 1
        return render_template('student/students.html', number=num, id=student_id, name=student, group=group_name)

    return app
