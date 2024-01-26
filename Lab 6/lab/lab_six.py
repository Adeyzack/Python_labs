"""
"This software application utilizes Python flask to create a basic website.
The website contains various routes and utilizes the render_template()
 function to display the HTML pages."
"""
from datetime import datetime
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    """
    display home site
    :return: render index.html
    """
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def addition():
    """
    get two numbers from the form and
    perform the addition operation
    :return: renders output.htl, operation performed, the two numbers and the output
    """
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = num1 + num2
    return render_template('output.html', operation='Addition',
                           num1=num1, num2=num2, result=result)

@app.route('/subtract', methods=['POST'])
def subtract():
    """
    get two numbers from the form and
    perform the difference
    :return: renders output.htl, operation performed, the two numbers and the output
    """
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = num1 - num2
    return render_template('output.html', operation='Subtraction',
                           num1=num1, num2=num2, result=result)

@app.route('/divide', methods=['POST'])
def divide():
    """
    get two numbers from the form and
    perform division
    :return: renders output.htl, operation performed, the two numbers and the output
    """
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = num1 / num2
    return render_template('output.html', operation='Division',
                           num1=num1, num2=num2, result=result)

@app.route('/multiply', methods=['POST'])
def multiply():
    """
    get two numbers from the form and
    perform multiplication
    :return: renders output.htl, operation performed, the two numbers and the output
    """
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    result = num1 * num2
    return render_template('output.html', operation='Multiplication',
                           num1=num1, num2=num2, result=result)

@app.context_processor
def display_datetime():
    """
    display date and time
    :return: date and time
    """
    return {'now': datetime.now()}

if __name__ == '__main__':
    app.run()
