import tkinter as tk
import sqlite3
#styling for the create database successful messagebox window label
label_style_success = {
    'bg': "#003366",
    'fg': "White",
    'font': ("Arial", 14),
    'width': 500,
    'relief': 'flat',
    'bd': 0,
    'activebackground': "#005780",
    'activeforeground': "White"
}

#Create database function
def on_btnCreate_click():
    create_window = tk.Toplevel()
    create_window.geometry('500x25')

    try:
        # Create the database and tables
        connection = sqlite3.connect("SMS.db")
        cursor = connection.cursor()
        # First delete tables if they do exist to ensure tabels are empty when created
        # To avoid having duplicate default data in the tables
        cursor.execute("DROP TABLE IF EXISTS tblStudents")
        cursor.execute("DROP TABLE IF EXISTS tblLecturers")
        # Create tblStudents
        cursor.execute("CREATE TABLE IF NOT EXISTS tblStudents (id INTEGER PRIMARY KEY,fname TEXT,lname TEXT,snumber INTEGER);")

        #Add default student data
        cursor.execute("INSERT INTO tblStudents (fname, lname, snumber) VALUES ('Hugo', 'du Preez', '600987');")
        cursor.execute("INSERT INTO tblStudents (fname, lname, snumber) VALUES ('John','Doe','000000');")


        # Create tblLecturers
        cursor.execute("CREATE TABLE IF NOT EXISTS tblLecturers (empid INTEGER PRIMARY KEY,fname TEXT,lname TEXT,course TEXT);")

        #Add default lecturer data
        cursor.execute("INSERT INTO tblLecturers (fname, lname, course) VALUES ('Wilma', 'Flintstone', 'PRG262');")
        cursor.execute("INSERT INTO tblLecturers (fname, lname, course) VALUES ('Barney','Rubbles','STA161');")
        cursor.execute("INSERT INTO tblLecturers (fname, lname, course) VALUES ('Fred', 'Flintstone', 'PRG161');")
        cursor.execute("INSERT INTO tblLecturers (fname, lname, course) VALUES ('Betty','Rubble','SSX361');")

        connection.commit()
        successDB = True
        successLbl = tk.Label(create_window,text="Successfully created database. Please close this window.",**label_style_success)
        successLbl.pack()


    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        successDB = False
    finally:
        connection.close()  # Close the database connection