import tkinter as tk
from tkinter import *
import sqlite3
#design for DASW Text
fontM = "TkMenuFont"
fontsizeBig = 18
fontsizeSmall = 14
def DisplayAllStudentsWindow():
    DASW = tk.Toplevel()
    DASW.geometry("550x600")
    #window title
    DASW.title("All Students")

    conn = sqlite3.connect("SMS.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tblStudents")
    rows = cursor.fetchall()
    textWidget1 = tk.Text(DASW, font=(fontM,fontsizeBig, "bold"))
    textWidget1.config(background="#003366", foreground="yellow")
    textWidget1.grid(column=1,row=1)
    textWidget1.insert(END, "=======================================" + "\n")
    textWidget1.insert(END, "Students in database:" + "\n")
    textWidget1.insert(END, "\n")
    textWidget1.insert(END, "ID|First Name|Last Name|Student Number|  " + "\n")
    textWidget1.insert(END, "=======================================" + "\n")
    if len(rows) == 0:
        textWidget1.insert(END, "No students in database." + "\n")
    # Insert data into the Text widget
    for row in rows:
        # Format the row as a string
        formatted_row = " | ".join(map(str, row))
        # Insert each row
        textWidget1.insert(END, formatted_row + "\n")


    conn.close()
    textWidget1.insert(END, "=======================================" + "\n")

