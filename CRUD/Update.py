import sqlite3

def update_student(id, fname, lname, snumber):
    conn = sqlite3.connect("SMS.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tblStudents SET fname = ?, lname = ?, snumber = ? WHERE id = ?", (fname, lname, snumber, id))
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated

def update_lecturer(empid, fname, lname, course):
    conn = sqlite3.connect("SMS.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tblLecturers SET fname = ?, lname = ?, course = ? WHERE empid = ?", (fname, lname, course, empid))
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated
