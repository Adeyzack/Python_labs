"""
This software application utilizes Python flask to create a basic website.
The website contains various routes and utilizes the render_template()
 function to display the HTML pages. The website also allow users to create account, login
 update password, record failed login attempts, test for weak passwords
 display various images, and table.
"""
from datetime import datetime
import logging
from flask import Flask, render_template, request, redirect, session
from passlib.hash import pbkdf2_sha256


app = Flask(__name__)
app.secret_key = 'abeBeBesoBela'

users = {}
common_passwords = set()

# Load common passwords from file
with open('CommonPassword.txt', 'r') as file:
    for line in file:
        common_passwords.add(line.strip())

# Configure logger
logging.basicConfig(filename='login_attempts.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Registration form, password requirement check.
    """
    if 'username' in session:
        return redirect('/calculator')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if is_password_common(password):
            return render_template('home.html',
                                   error_message='Password is too common. '
                                                 'Please choose a different password.')
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
    Function to check if the user already exists in the directory.
    If it exists, redirect to the calculator page.
    If not, display an error message.
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
        logging.info(f"Failed login attempt - Username: "
                     f"{username} - IP Address: {request.remote_addr}")
        return render_template('login.html', error_message=error_message)

    return render_template('login.html', error_message=None)


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    """
    This function performs calculations based on the form input.
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
    Logout function
    """
    session.pop('username', None)
    return redirect('/')


@app.route('/update_password', methods=['GET', 'POST'])
def update_password():
    """
    This function allows a user to update their password.
    """
    if 'username' not in session:
        return redirect('/login')

    username = session['username']

    if request.method == 'POST':
        old_password = request.form['old_password']
        new_password = request.form['new_password']

        # Check if the old password matches the one in the users dictionary
        if username in users:
            hashed_password = users[username]

            if pbkdf2_sha256.verify(old_password, hashed_password):
                # Read the common passwords from the file
                with open('CommonPassword.txt', 'r') as file:
                    common_passwords = [line.strip() for line in file]

                # Check if the new password is in the list of common passwords
                flag = False
                if is_password_common(new_password):
                    flag = True
                    return render_template('update_password.html'
                                           , error_message='Password is too common. Please '
                                                           'choose a different password.')

                # Perform password complexity check for the new password
                if not is_password_complex(new_password) and flag is False:
                    return render_template('update_password.html',
                                           error_message='Password must be at least 12 '
                                                         'characters long and contain at least'
                                                         ' 1 uppercase letter, '
                                                         '1 lowercase letter, 1 number, and '
                                                         '1 special character.')

                # Update the password in the users dictionary
                users[username] = pbkdf2_sha256.hash(new_password)

                # Redirect to the calculator page or home page
                return redirect('/calculator')

        # Display error message if the old password is incorrect
        error_message = 'Invalid old password.'
        return render_template('update_password.html', error_message=error_message)

    return render_template('update_password.html', username=username, error_message=None)


def is_password_complex(password):
    """
    Function to implement password complexity check logic.
    Returns True if the password is complex, False otherwise.
    """
    return len(password) >= 12 and any(char.isupper() for char in password) and any(
        char.islower() for char in password) and any(char.isdigit() for char in password) and any(
        not char.isalnum() for char in password)


def is_password_common(password):
    """
    Function to check if the password is common.
    Returns True if the password is common, False otherwise.
    """
    return password in common_passwords


def calculate_result(num1, num2, operator):
    """
    Function to implement calculation logic based on the operator (+, -, *, /).
    """
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        return num1 / num2


@app.context_processor
def inject_datetime():
    """
    Function to display the current date and time.
    """
    return {'now': datetime.now()}


if __name__ == '__main__':
    app.run(debug=True, port=5001)
