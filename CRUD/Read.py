import sqlite3

def get_all_students():
    conn = sqlite3.connect("SMS.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, fname, lname, snumber FROM tblStudents")
    students = cursor.fetchall()
    conn.close()
    return students

def get_all_lecturers():
    conn = sqlite3.connect("SMS.db")
    cursor = conn.cursor()
    cursor.execute("SELECT empid, fname, lname, course FROM tblLecturers")
    lecturers = cursor.fetchall()
    conn.close()
    return lecturers
