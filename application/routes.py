from application import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', index=True)


@app.route("/courses")
def courses():
    return render_template('courses.html', courses=True)


@app.route("/register")
def register():
    return render_template('register.html', register=True)


@app.route("/login")
def login():
    return render_template('login.html', login=True)



@app.route("/enrollment")
def enrollment():
    return render_template('enrollment.html', enrollment=True)