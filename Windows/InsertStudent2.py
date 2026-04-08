import sqlite3
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
def show_student_insert_window():
    stuInsertWindow = tkinter.Toplevel()
    stuInsertWindow.geometry('350x250')
    stuInsertWindow.title("Insert New Student")
    stuInsertWindow.config(bg="#003366")
 
    # Student first name label and entry
    stuFnameLabel = tkinter.Label(stuInsertWindow, text="Student first name:", **label_style)
    stuFnameLabel.grid(column=0, row=1, padx= 5,pady= 5)
    stuFnameEntry = tkinter.Entry(stuInsertWindow)
    stuFnameEntry.grid(column=0, row=2, padx= 5,pady= 5)
 
    # Student last name label and entry
    stuLnameLabel = tkinter.Label(stuInsertWindow, text="Student last name:", **label_style)
    stuLnameLabel.grid(column=0, row=3, padx= 5,pady= 5)
    stuLnameEntry = tkinter.Entry(stuInsertWindow)
    stuLnameEntry.grid(column=0, row=4, padx= 5,pady= 5)
 
    # Student number label and entry
    stuNumberLabel = tkinter.Label(stuInsertWindow, text="Student number:", **label_style)
    stuNumberLabel.grid(column=0, row=5, padx= 5,pady= 5)
    stuNumberEntry = tkinter.Entry(stuInsertWindow)
    stuNumberEntry.grid(column=0, row=6, padx= 5,pady= 5)
 
    # Insert button for student
    stuInsertButton = tkinter.Button(stuInsertWindow, text="Insert",
                                     command=lambda: insert_student(stuFnameEntry.get(), stuLnameEntry.get(),stuNumberEntry.get(),
                                                                     stuInsertWindow), **button_style)
    stuInsertButton.grid(column=0, row=7,padx=10,pady= 10)
 
 
def insert_student(first_name, last_name, student_number, window):
    if first_name == "" or last_name == "" or student_number == "":
        incomplete_message_s = tkinter.Toplevel()
        incomplete_message_lbl = tkinter.Label(incomplete_message_s, text="Please enter the first name, last name and student number.", **message_style)
        incomplete_message_lbl.pack()
    else:
        try:
            # Connect to the database
            connection = sqlite3.connect("SMS.db")
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