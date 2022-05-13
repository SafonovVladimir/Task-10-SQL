from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates', static_folder='../static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/groups')
def groups():
    return render_template('groups.html')


@app.route('/students')
def students():
    return render_template('students.html')


@app.route('/courses')
def courses():
    return render_template('courses.html')
