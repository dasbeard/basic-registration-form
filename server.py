from flask import Flask, render_template, redirect, request, session, flash
import re
app=Flask(__name__)
app.secret_key="SomeSecretKey"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
ALPHA_REGEX = re.compile(r'^[a-zA-Z]')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/validate', methods=['POST'])
def validate():

    validation = 'Success'

    if len(request.form['email'])<1:
        flash("Email cannot be blank!")
        validation = 'False'

    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid Email Address!')
        validation = 'False'
    if len(request.form['first_name'])<1 or not ALPHA_REGEX.match(request.form['first_name']):
            flash('Invalid First Name!')
            validation = 'False'
    if len(request.form['last_name'])<1 or not ALPHA_REGEX.match(request.form['last_name']):
            flash('Invalid Last Name!')
            validation = 'False'
    if len(request.form['password'])<=8:
        flash('Password must be longer than 8 characters!')
        validation = 'False'
    if request.form['password']!=request.form['conf_password']:
        flash('Password does not match!')
        validation = 'False'
    if validation == 'Success':
        flash ('Thanks for submitting your information')

    return redirect('/')







app.run(debug=True)
