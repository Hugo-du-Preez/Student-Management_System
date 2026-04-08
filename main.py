import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import design
from CRUD.Create import on_btnCreate_click
from CRUD.Delete import deleteLecturer, deleteStudent
from CRUD.Read import ReadAllStudents, ReadAllLecturers
from CRUD.Update import update_student, update_lecturer
#from Windows.InsertLecturer import show_lecturer_insert_window
from Windows.InsertLecturer2 import show_lecturer_insert_window
#from Windows.InsertStudent import show_student_insert_window
from Windows.InsertStudent2 import show_student_insert_window
import Windows.UpdateStudentWindow
import Windows.UpdateLecturerWindow
import os

def main():
    root = tk.Tk()
    root.title(design.window_title)
    # set the size of the root window
    root.geometry('400x680')

    # Load and resize logo image
    original_image = Image.open("images/BCLOGO.png")
    max_width = 380
    max_height = 180
    img_width, img_height = original_image.size
    scale = min(max_width/img_width, max_height/img_height)
    new_width = int(img_width * scale)
    new_height = int(img_height * scale)
    resized_image = original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    image = ImageTk.PhotoImage(resized_image)
    
    image_label = tk.Label(root, image=image, borderwidth=0)
    image_label.image = image  # Keep a reference
    image_label.pack()
    image_label.columnconfigure(2, weight= 2)
    # # Load and display the logo image

    # Display the main heading label
    lbl = tk.Label(root, bg=design.bg_colour_darker, width=20)
    lbl.pack()

    lbl_spacing2 = tk.Label(root, bg=design.bg_colour_darker)
    lbl_spacing2.pack()
    lbl.columnconfigure(1, weight=1, minsize=20)

    lbl.columnconfigure(0, weight=1)
    lbl_spacing2.columnconfigure(3, weight=1)


    button_style = {
        'bg': "#003366",
        'fg': "White",
        'font': ("Arial", 14),
        'width': 30,
        'relief': 'flat',
        'bd': 0,
        'activebackground': "#005780",
        'activeforeground': "White"
    }

    # First Column Buttons
    btnCreate = tk.Button(root, text="Create Database", command=on_btnCreate_click, **button_style)
    btnCreate.pack(pady=5)

    btnNewLecturer = tk.Button(root, text="New Lecturer", command=show_lecturer_insert_window, **button_style)
    btnNewLecturer.pack(pady=5)

    btnNewStudent = tk.Button(root, text="New Student", command=show_student_insert_window, **button_style)
    btnNewStudent.pack(pady=5)

    btnReadLecturers = tk.Button(root, text="Read All Lecturers", command=ReadAllLecturers, **button_style)
    btnReadLecturers.pack(pady=5)

    btnReadStudents = tk.Button(root, text="Read All Students", command=ReadAllStudents, **button_style)
    btnReadStudents.pack(pady=5)

    # Second Column Buttons
    btnUpdateStudent = tk.Button(root, text="Update Student",
                                 command=lambda: Windows.UpdateStudentWindow.update_student(), **button_style)
    btnUpdateStudent.pack(pady=5)

    btnUpdateLecturer = tk.Button(root, text="Update Lecturer", command=lambda: Windows.UpdateLecturerWindow.update_lecturer(), **button_style)
    btnUpdateLecturer.pack(pady=5)

    btnDeleteStudent = tk.Button(root, text="Delete Student", command=deleteStudent, **button_style)
    btnDeleteStudent.pack(pady=5)

    btnDeleteLecturer = tk.Button(root, text="Delete Lecturer", command=deleteLecturer, **button_style)
    btnDeleteLecturer.pack(pady=5)

    btnExit = tk.Button(root, text="Exit", command=root.destroy, **button_style)
    btnExit.pack(pady=5)

    # Centering all columns in the grid
    for i in range(2):
        root.grid_columnconfigure(i, weight=1)  # Allow columns to expand equally

    root.configure(bg=design.bg_colour_darker)  # Set the background color for the root
    root.mainloop()


if __name__ == "__main__":
    main()
