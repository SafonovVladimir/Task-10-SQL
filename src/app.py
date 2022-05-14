from flask import Flask, render_template
from config import config
from src.queries.queries import get_groups_name, get_all_students_with_group_name, get_courses

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
        res = get_all_students_with_group_name()
        count = 1
        for i in res:
            num.append(count)
            group_name.append(i[2])
            student_name = f'{i[0]} {i[1]}'
            student.append(student_name)
            count += 1
        return render_template('students.html', id=num, name=student, group=group_name)

    @app.route('/students')
    def students():
        num = []
        group_name = []
        student = []
        res = get_all_students_with_group_name()
        count = 1
        for i in res:
            num.append(count)
            group_name.append(i[2])
            student_name = f'{i[0]} {i[1]}'
            student.append(student_name)
            count += 1
        return render_template('students.html', id=num, name=student, group=group_name)

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
        get_courses()
        return render_template('courses.html', id=num, name=course_name, description=descrip)

    return app
