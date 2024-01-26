"""
This software application utilizes Python flask to create a basic website.
The website contains various routes and utilizes the render_template()
 function to display the HTML pages. The website also allow users to create account
 display various images, and table.
"""
from datetime import datetime
from flask import Flask, render_template, request, redirect, session
from passlib.hash import pbkdf2_sha256

global opp_output
app = Flask(__name__)
app.secret_key = 'abeBeBesoBela'

users = {}

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    registration form, password requirement check
    :return:
    """
    if 'username' in session:
        return redirect('/calculator')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Perform password complexity check
        if not is_password_complex(password):
            return render_template('home.html',
                                   error_message='Password must be at least\n'
                                                 '- 12 characters long and contain at least\n'
                                                 '- 1 uppercase letter\n'
                                                 '- 1 lowercase letter\n'
                                                 '- 1 number and 1 special character.')

        # Store the username and hashed password in the users dictionary
        users[username] = pbkdf2_sha256.hash(password)

        # Redirect to the login page
        return redirect('/login')

    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Function to check if user already exist in the directory.
    if it exists, redirect to the calculator page
    if not display error message
    :return:redirect to calculator page, render login.html
    """
    if 'username' in session:
        return redirect('/calculator')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username exists in the users dictionary
        if username in users:
            hashed_password = users[username]

            # Verify the password
            if pbkdf2_sha256.verify(password, hashed_password):
                session['username'] = username
                return redirect('/calculator')

        error_message = 'Invalid username or password.'
        return render_template('login.html', error_message=error_message)

    return render_template('login.html', error_message=None)


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    """
    This function performs calculation based on the form input
    :return: render calculator.html
    """
    if 'username' not in session:
        return redirect('/login')

    username = session['username']

    if request.method == 'POST':
        # Perform the calculation based on the form input
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operator = request.form['operator']
        result = calculate_result(num1, num2, operator)
        return render_template('calculator.html', username=username, result=result,
                               datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    return render_template('calculator.html', username=username)


@app.route('/logout')
def logout():
    """
    logout function
    :return: redirect to home page
    """
    session.pop('username', None)
    return redirect('/')


def is_password_complex(password):
    """
    function to Implement password complexity check logic
    and Return True if password is complex, False otherwise
    :param password:
    :return: bool
    """

    return len(password) >= 12 and any(char.isupper() for char in password) and any(
        char.islower() for char in password) and any(char.isdigit() for char in password) and any(
        not char.isalnum() for char in password)


def calculate_result(num1, num2, operator):
    """
    this function  Implement calculation logic based on operator (+, -, *, /)
    :param num1:
    :param num2:
    :param operator:
    :return: float
    """


    if operator == '+':
        opp_output = num1 + num2

    if operator == '-':
        opp_output = num1 - num2

    if operator == '*':
        opp_output = num1 * num2

    if operator == '/':
        opp_output = num1 / num2

    return opp_output

@app.context_processor
def inject_datetime():
    """
    display date and time
    :return:
    """
    return {'now': datetime.now()}

if __name__ == '__main__':
    app.run(debug=True)
