from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gold Timber'}
    return render_template('index.html', title='Home', user=user)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title='Contacts')

@app.route('/information')
def information():
    return render_template('inform_page.html', title='Information')