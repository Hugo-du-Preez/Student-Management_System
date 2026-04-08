import sqlite3
import tkinter
import design


def show_student_insert_window():
    stuInsertWindow = tkinter.Toplevel()
    stuInsertWindow.geometry(design.window_size)
    stuInsertWindow.title("Insert New Student")

    # Student first name label and entry
    stuFnameLabel = tkinter.Label(stuInsertWindow, text="Student first name:")
    stuFnameLabel.grid(column=0, row=1)
    stuFnameEntry = tkinter.Entry(stuInsertWindow)
    stuFnameEntry.grid(column=1, row=1)

    # Student last name label and entry
    stuLnameLabel = tkinter.Label(stuInsertWindow, text="Student last name:")
    stuLnameLabel.grid(column=0, row=2)
    stuLnameEntry = tkinter.Entry(stuInsertWindow)
    stuLnameEntry.grid(column=1, row=2)

    # Student number label and entry
    stuNumberLabel = tkinter.Label(stuInsertWindow, text="Student number:")
    stuNumberLabel.grid(column=0, row=3)
    stuNumberEntry = tkinter.Entry(stuInsertWindow)
    stuNumberEntry.grid(column=1, row=3)

    # Insert button for student
    stuInsertButton = tkinter.Button(stuInsertWindow, text="Insert",
                                     command=lambda: insert_student(stuFnameEntry.get(), stuLnameEntry.get(),stuNumberEntry.get(),
                                                                     stuInsertWindow))
    stuInsertButton.grid(column=2, row=4)


def insert_student(first_name, last_name, student_number, window):
    try:
        # Connect to the database
        connection = sqlite3.connect("../SMS.db")
        cursor = connection.cursor()

        # Insert lecturer into tblLecturers
        command = "INSERT INTO tblStudents (fname, lname, snumber) VALUES (?, ?, ?);"
        print(f"Adding: {first_name} {last_name} {student_number}")
        cursor.execute(command, (first_name, last_name, student_number))

        connection.commit()
        print("Student added successfully.")

        # Close the insert window after insertion
        window.destroy()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        connection.close()

