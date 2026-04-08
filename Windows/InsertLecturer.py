import sqlite3
import tkinter
import design


def show_lecturer_insert_window():
    LecInsertWindow = tkinter.Toplevel()
    LecInsertWindow.geometry(design.window_size)
    LecInsertWindow.title("Insert New Lecturer")

    # Lecturer first name label and entry
    LecFnameLabel = tkinter.Label(LecInsertWindow, text="Lecturer first name:")
    LecFnameLabel.grid(column=0, row=1)
    lecFnameEntry = tkinter.Entry(LecInsertWindow)
    lecFnameEntry.grid(column=1, row=1)

    # Lecturer last name label and entry
    LecLnameLabel = tkinter.Label(LecInsertWindow, text="Lecturer last name:")
    LecLnameLabel.grid(column=0, row=2)
    lecLnameEntry = tkinter.Entry(LecInsertWindow)
    lecLnameEntry.grid(column=1, row=2)

    # Lecturer course label and entry
    LecCourseLabel = tkinter.Label(LecInsertWindow, text="Lecturer course:")
    LecCourseLabel.grid(column=0, row=3)
    lecCourseEntry = tkinter.Entry(LecInsertWindow)
    lecCourseEntry.grid(column=1, row=3)

    # Insert button with command
    LecInsertButton = tkinter.Button(LecInsertWindow, text="Insert",
                                     command=lambda: insert_lecturer(lecFnameEntry.get(), lecLnameEntry.get(),lecCourseEntry.get(),
                                                                     LecInsertWindow))
    LecInsertButton.grid(column=2, row=3)


def insert_lecturer(first_name, last_name, course, window):
    try:
        # Connect to the database
        connection = sqlite3.connect("../SMS.db")
        cursor = connection.cursor()

        # Insert lecturer into tblLecturers
        command = "INSERT INTO tblLecturers (fname, lname, course) VALUES (?, ?, ?);"
        print(f"Adding: {first_name} {last_name} teaches {course}")
        cursor.execute(command, (first_name, last_name, course))

        connection.commit()
        print("Lecturer added successfully.")

        # Close the insert window after insertion
        window.destroy()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        connection.close()

