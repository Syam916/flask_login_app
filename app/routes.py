from flask import render_template, request, redirect, url_for, flash
from flask import current_app as app
from .models import User
from .forms import LoginForm
from . import db
from sqlalchemy import func


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print(f"Submitted Username: {username}, Password: {password}")  # Debugging

        # Query the database for the user
        user = User.query.filter_by(username=username).first()
        print(f"Query Result: {user}")  # Debugging

        if user:
            if user.password == password:
                print("Login successful!")  # Debugging
                return redirect(url_for('welcome', username=user.username))
            else:
                print("Password mismatch!")  # Debugging
                flash('Invalid password', 'danger')
        else:
            print("User not found!")  # Debugging
            flash('Invalid username', 'danger')
    return render_template('login.html', form=form)



@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)


@app.route('/test_user_query')
def test_user_query():
    try:
        user = User.query.filter_by(username='user1').first()
        if user:
            return f"User found: {user.username}, Password: {user.password}"
        else:
            return "User not found!"
    except Exception as e:
        return f"Query error: {e}"


@app.route('/dump_users')
def dump_users():
    try:
        users = User.query.all()
        if users:
            return "<br>".join([f"ID: {user.id}, Username: {user.username}, Password: {user.password}" for user in users])
        else:
            return "No users found in the database!"
    except Exception as e:
        return f"Error querying users: {e}"
