from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from CRUD.Create import create_database
from CRUD.Read import get_all_students, get_all_lecturers
from CRUD.Delete import delete_student, delete_lecturer
from CRUD.Update import update_student, update_lecturer
import os

app = Flask(__name__)
app.secret_key = 'sms_key_dev'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_db')
def create_db():
    if create_database():
        flash('Database created successfully with sample data!')
    else:
        flash('Error creating database')
    return redirect(url_for('index'))

@app.route('/students')
def students():
    students = get_all_students()
    return render_template('students.html', students=students)

@app.route('/lecturers')
def lecturers():
    lecturers = get_all_lecturers()
    return render_template('lecturers.html', lecturers=lecturers)

@app.route('/add_student', methods=['POST'])
def add_student():
    fname = request.form['fname'].strip()
    lname = request.form['lname'].strip()
    snumber = str(request.form['snumber']).strip()
    
    try:
        conn = sqlite3.connect('SMS.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tblStudents (fname, lname, snumber) VALUES (?, ?, ?)", (fname, lname, snumber))
        conn.commit()
        flash(f'Student \"{fname} {lname}\" added successfully!')
        conn.close()
    except sqlite3.Error as e:
        flash(f'Error adding student: {str(e)}')
    return redirect(url_for('students'))

@app.route('/add_lecturer', methods=['POST'])
def add_lecturer():
    fname = request.form['fname'].strip()
    lname = request.form['lname'].strip()
    course = request.form['course'].strip()
    
    try:
        conn = sqlite3.connect('SMS.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tblLecturers (fname, lname, course) VALUES (?, ?, ?)", (fname, lname, course))
        conn.commit()
        flash(f'Lecturer \"{fname} {lname}\" added successfully!')
        conn.close()
    except sqlite3.Error as e:
        flash(f'Error adding lecturer: {str(e)}')
    return redirect(url_for('lecturers'))

@app.route('/delete_student/<int:id>')
def delete_student_route(id):
    if delete_student(id):
        flash('Student deleted successfully!')
    else:
        flash('Error deleting student')
    return redirect(url_for('students'))

@app.route('/delete_lecturer/<int:empid>')
def delete_lecturer_route(empid):
    if delete_lecturer(empid):
        flash('Lecturer deleted successfully!')
    else:
        flash('Error deleting lecturer')
    return redirect(url_for('lecturers'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
