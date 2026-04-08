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
        flash('Database created with sample data!', 'success')
    else:
        flash('Database creation failed!', 'error')
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
    snumber = request.form['snumber'].strip()
    
    conn = sqlite3.connect('SMS.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tblStudents WHERE snumber = ?", (snumber,))
    if cursor.fetchone():
        flash('Student number already exists!', 'warning')
        conn.close()
        return redirect(url_for('students'))
    
    cursor.execute("INSERT INTO tblStudents (fname, lname, snumber) VALUES (?, ?, ?)", (fname, lname, snumber))
    conn.commit()
    flash(f'Student "{fname} {lname}" ({snumber}) added!', 'success')
    conn.close()
    return redirect(url_for('students'))

@app.route('/add_lecturer', methods=['POST'])
def add_lecturer():
    fname = request.form['fname'].strip()
    lname = request.form['lname'].strip()
    course = request.form['course'].strip()
    
    conn = sqlite3.connect('SMS.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COALESCE(MAX(empid), 0) + 1 FROM tblLecturers")
    next_empid = cursor.fetchone()[0]
    
    cursor.execute("INSERT INTO tblLecturers (empid, fname, lname, course) VALUES (?, ?, ?, ?)", (next_empid, fname, lname, course))
    conn.commit()
    flash(f'Lecturer "{fname} {lname}" (EmpID: {next_empid}) added!', 'success')
    conn.close()
    return redirect(url_for('lecturers'))

@app.route('/update_student', methods=['POST'])
def update_student_route():
    try:
        student_id = int(request.form['id'])
        fname = request.form['fname'].strip()
        lname = request.form['lname'].strip()
        snumber = request.form['snumber'].strip()
        
        if update_student(student_id, fname, lname, snumber):
            flash(f'Student updated successfully! {fname} {lname}', 'success')
        else:
            flash('Update failed - student not found', 'danger')
    except ValueError as e:
        flash('Invalid input data', 'danger')
    except Exception as e:
        flash('Update error occurred', 'danger')
    return redirect(url_for('students'))

@app.route('/update_lecturer', methods=['POST'])
def update_lecturer_route():
    try:
        empid = int(request.form['empid'])
        fname = request.form['fname'].strip()
        lname = request.form['lname'].strip()
        course = request.form['course'].strip()
        
        if update_lecturer(empid, fname, lname, course):
            flash(f'Lecturer updated successfully! {fname} {lname}', 'success')
        else:
            flash('Update failed - lecturer not found', 'danger')
    except ValueError as e:
        flash('Invalid input data', 'danger')
    except Exception as e:
        flash('Update error occurred', 'danger')
    return redirect(url_for('lecturers'))

@app.route('/delete_student/<int:id>')
def delete_student_route(id):
    if delete_student(id):
        flash('Student deleted successfully!', 'success')
    else:
        flash('Error deleting student', 'danger')
    return redirect(url_for('students'))

@app.route('/delete_lecturer/<int:empid>')
def delete_lecturer_route(empid):
    if delete_lecturer(empid):
        flash('Lecturer deleted successfully!', 'success')
    else:
        flash('Error deleting lecturer', 'danger')
    return redirect(url_for('lecturers'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

