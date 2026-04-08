import sqlite3
import tkinter as tk
import tkinter
#import design

label_style = {
        'bg': "#003366",
        'fg': "White",
        'font': ("Arial", 14),
        'width': 30,
        'relief': 'flat',
        'bd': 0,
        'activebackground': "#005780",
        'activeforeground': "White"
    }

message_style={
    'bg': "#003366",
    'fg': "White",
    'font': ("Arial", 14),
    'width': 600,
    'relief': 'flat',
    'bd': 0,
    'activebackground': "#005780",
    'activeforeground': "White"
}
 
button_style = {
        'bg': "#005780",
        'fg': "White",
        'font': ("Arial", 14),
        'width': 25,
        'relief': 'flat',
        'bd': 0,
        'activebackground': "#005780",
        'activeforeground': "White"
    }
def show_lecturer_insert_window():
    LecInsertWindow = tkinter.Toplevel()
    LecInsertWindow.geometry('350x250')
    LecInsertWindow.title("Insert New Lecturer")
    LecInsertWindow.config(bg="#003366")
 
 
    # Lecturer first name label and entry
    LecFnameLabel = tkinter.Label(LecInsertWindow, text="Lecturer first name:", **label_style)
    LecFnameLabel.grid(column=0, row=1, padx= 5,pady= 5)
    lecFnameEntry = tkinter.Entry(LecInsertWindow)
    lecFnameEntry.grid(column=0, row=2, padx= 5,pady= 5)
 
    # Lecturer last name label and entry
    LecLnameLabel = tkinter.Label(LecInsertWindow, text="Lecturer last name:", **label_style)
    LecLnameLabel.grid(column=0, row=3,pady= 5)
    lecLnameEntry = tkinter.Entry(LecInsertWindow)
    lecLnameEntry.grid(column=0, row=4,pady= 5)
 
    # Lecturer course label and entry
    LecCourseLabel = tkinter.Label(LecInsertWindow, text="Lecturer course:", **label_style)
    LecCourseLabel.grid(column=0, row=5,pady= 5)
    lecCourseEntry = tkinter.Entry(LecInsertWindow)
    lecCourseEntry.grid(column=0, row=6,pady= 5)
 
    # Insert button with command
    LecInsertButton = tkinter.Button(LecInsertWindow, text="Insert",
                                     command=lambda: insert_lecturer(lecFnameEntry.get(), lecLnameEntry.get(),lecCourseEntry.get(),
                                                                     LecInsertWindow), **button_style)
    LecInsertButton.grid(column=0, row=7,padx=10,pady= 10)
 
 
 
def insert_lecturer(first_name, last_name, course, window):
    if first_name == "" or last_name == "" or course == "":
        incomplete_Message = tk.Toplevel()
        incomplete_Message.geometry('600x25')
        lbl_incomplete = tkinter.Label(incomplete_Message, text="Please enter the first name, last name and course.",**message_style)
        lbl_incomplete.pack()

    else:
        try:
            # Connect to the database
            connection = sqlite3.connect("SMS.db")
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