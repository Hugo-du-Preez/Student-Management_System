import sqlite3

def create_database():
    try:
        connection = sqlite3.connect("SMS.db")
        cursor = connection.cursor()
        # Drop existing tables
        cursor.execute("DROP TABLE IF EXISTS tblStudents")
        cursor.execute("DROP TABLE IF EXISTS tblLecturers")
        # Create tables
        cursor.execute("CREATE TABLE tblStudents (id INTEGER PRIMARY KEY AUTOINCREMENT, fname TEXT, lname TEXT, snumber TEXT)")
        cursor.execute("CREATE TABLE tblLecturers (empid INTEGER PRIMARY KEY AUTOINCREMENT, fname TEXT, lname TEXT, course TEXT)")
        # Sample students
        cursor.execute("INSERT INTO tblStudents (fname, lname, snumber) VALUES ('Hugo', 'du Preez', '600987')")
        cursor.execute("INSERT INTO tblStudents (fname, lname, snumber) VALUES ('John', 'Doe', '000000')")
        # Sample lecturers
        cursor.execute("INSERT INTO tblLecturers (fname, lname, course) VALUES ('Wilma', 'Flintstone', 'PRG262')")
        cursor.execute("INSERT INTO tblLecturers (fname, lname, course) VALUES ('Barney', 'Rubbles', 'STA161')")
        cursor.execute("INSERT INTO tblLecturers (fname, lname, course) VALUES ('Fred', 'Flintstone', 'PRG161')")
        cursor.execute("INSERT INTO tblLecturers (fname, lname, course) VALUES ('Betty', 'Rubble', 'SSX361')")
        connection.commit()
        connection.close()
        return True
    except sqlite3.Error as e:
        print(f'Database creation error: {e}')
        return False
