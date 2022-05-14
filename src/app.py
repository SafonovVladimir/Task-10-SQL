from flask import Flask, render_template, request
from config import config
from queries import get_groups_name, get_all_students_with_group_name, get_courses, get_group_inf, get_student_info, \
    get_course_info

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/uni'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def create_app(config_name):
    # app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config[config_name])

    # config[config_name].init_app(app)

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
            group_name.append(i[1])
            count += 1
        return render_template('groups.html', id=num, name=group_name)

    @app.route('/group')
    def group():
        num = []
        group_name = []
        student = []
        id = []
        rev = request.args.get('group_id')
        res = get_group_inf(rev)
        count = 1
        for i in res:
            num.append(count)
            id.append(i[0])
            group_name.append(i[2])
            student_name = i[1]
            student.append(student_name)
            count += 1
        return render_template('students.html', number=num, id=id, name=student, group=group_name)

    @app.route('/students')
    def students():
        num = []
        id = []
        group_name = []
        student = []
        res = get_all_students_with_group_name()
        count = 1
        for i in res:
            num.append(count)
            id.append(i[0])
            group_name.append(i[2])
            student.append(i[1])
            count += 1
        return render_template('students.html', number=num, id=id, name=student, group=group_name)

    @app.route('/student')
    def student():
        num = []
        subject = []
        descip = []
        rev = request.args.get('student_id')
        res = get_student_info(rev)
        count = 1
        for i in res:
            num.append(count)
            descip.append(i[1])
            subject.append(i[0])
            count += 1
        return render_template('courses.html', id=num, name=subject, description=descip)

    @app.route('/courses')
    def courses():
        num = []
        course_name = []
        descrip = []
        res = get_courses()
        count = 1
        for i in res:
            num.append(count)
            course_name.append(i[0])
            descrip.append(i[1])
            count += 1
        return render_template('courses.html', id=num, name=course_name, description=descrip)

    @app.route('/course')
    def course():
        num = []
        id = []
        group_name = []
        student = []
        rev = request.args.get('course_name')
        res = get_course_info(rev)
        count = 1
        for i in res:
            num.append(count)
            id.append(i[0])
            group_name.append(i[2])
            student.append(i[1])
            count += 1
        return render_template('students.html', number=num, id=id, name=student, group=group_name)

    return app
