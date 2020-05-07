from datetime import date
from flask import render_template
from application import app


@app.route('/')
def index():
    today = date.today()  # getting today's date
    current_year = today.year  # obtaining the current year
    context = {'current_year': current_year}
    return render_template('index.html', **context)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')
