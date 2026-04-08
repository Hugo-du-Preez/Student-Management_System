import sqlite3

def delete_student(id):
    conn = sqlite3.connect("SMS.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tblStudents WHERE id = ?", (id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted

def delete_lecturer(empid):
    conn = sqlite3.connect("SMS.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tblLecturers WHERE empid = ?", (empid,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted
