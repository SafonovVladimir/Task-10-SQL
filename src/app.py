from flask import Flask, render_template
from config import config

app = Flask(__name__, template_folder='../templates', static_folder='../static')

def create_app(config_name):
    # app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config[config_name])
    # config[config_name].init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/groups')
    def groups():
        # group = GroupName.
        return render_template('groups.html')

    @app.route('/students')
    def students():
        return render_template('students.html')

    @app.route('/courses')
    def courses():
        return render_template('courses.html')

    return app
