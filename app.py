from flask import Flask, render_template, request
import mysql.connector
from database import db, cursor
# from database_config import db, cursor
import time

# from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():

    if request.method == 'POST':
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        email_address = request.form['email_address']
        age_group = request.form['age_group']
        dollars_spent = request.form['dollars_spent']
        on_time = request.form['on_time']
        correct_product = request.form['correct_product']
        expectation = request.form['expectation']
        photograph = request.form['photograph']
        description = request.form['description']
        recommend = request.form['recommend']
        use_again = request.form['use_again']
        loyalty = request.form['loyalty']
        comments = request.form['comments']
        created = time.strftime('%Y-%m-%d %H:%M:%S')
        # print(customer_first, customer_last, customer_email, age_group, dollars_spent, on_time, correct_product, expectation, photograph, description, recommend, use_again, loyalty, comments)
        if last_name == '' or last_name == '' or email_address == '':
            return render_template('index.html', message='Please enter required fields')
        if type(age_group) != int:
            return render_template('index.html', message='Please select an age group')
        if type(dollars_spent) != int:
            return render_template('index.html', message='Please select dollars spent')

        cursor.execute('INSERT INTO responses (last_name, first_name, email_address, age_group, dollars_spent, on_time, correct_product, expectation, photograph, description, recommend, use_again, loyalty, comments, created) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (last_name, first_name, email_address, age_group, dollars_spent, on_time, correct_product, expectation, photograph, description, recommend, use_again, loyalty, comments, created))

        db.commit()
        cursor.close()
        db.close()

        return render_template('success.html')


@app.route('/responses')
def get_responses():
    sql = ('SELECT * FROM reponses')
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)
    return render_template('responses.html', responses=result)


if __name__ == '__main__':
    app.debug = True
    app.run()
