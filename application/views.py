from flask import render_template
from application import app


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')
