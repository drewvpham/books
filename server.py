from flask import Flask, request, render_template, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app, 'email_validation')
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
    emails = mysql.query_db("select id, email, date from emails")


    return render_template('index.html', emails=emails)

@app.route('/register', methods=["POST"])
def register():

    errors={}
    if len(request.form['first_name']) > 2 or not request.form['first_name'].isalpha():
        errors['first_name']='First Name must be at least 3 characters in length and all alphabetic characters.'
        #flash("Email cannot be blank!")
    if len(request.form['last_name']) > 2 or not request.form['last_name'].isalpha():
        errors['last_name']='Last Name must be at least 3 characters in length and all alphabetic characters.'
    if len(request.form['email']) is 0:
        errors['email']'Email can not be empty'
    if not EMAIL_REGEX.MATCH(request.form['email']):
        errors['email']='Invalid email format.'
    if len(request.form['password']) < 8:
        errors['password']='Password must be at least 8 characters in length'
    if request.form['password'] is not request.form['password_confirmation']:
        errors['password']='Password and Password Confirmation do not match'

    if errors:
        flash(errors)



    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    else:
        flash("Success!")
        result = mysql.query_db(query, data)
    return redirect('/')




    print result


app.run(debug=True)
