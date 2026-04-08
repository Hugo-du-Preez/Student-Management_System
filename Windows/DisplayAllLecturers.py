import tkinter as tk
from tkinter import *
import sqlite3

fontM = "TkMenuFont"
fontsizeBig = 18
fontsizeSmall = 14
def DisplayAllLecturersWindow():
    DALW = tk.Toplevel()
    DALW.geometry("550x600")
    #window title
    DALW.title("All Lecturers")

    conn = sqlite3.connect("SMS.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tblLecturers")
    rows = cursor.fetchall()

    textWidget1 = tk.Text(DALW, font=(fontM, fontsizeBig, "bold"))
    textWidget1.config(background="#003366", foreground="yellow" )
    textWidget1.grid(column=1,row=1)
    textWidget1.insert(END, "=======================================" + "\n")
    textWidget1.insert(END, "Lecturers in database:" + "\n")
    textWidget1.insert(END, "\n")
    textWidget1.insert(END, "Employee ID|First Name|Last Name|Course|  " + "\n")
    textWidget1.insert(END, "=======================================" + "\n")
    if len(rows) == 0:
        textWidget1.insert(END, "No lecturers available in database." + "\n")
    # Insert data into the Text widget
    for row in rows:
        # Format the row as a string
        formatted_row = " | ".join(map(str, row))
        # Insert each row
        textWidget1.insert(END, formatted_row + "\n")

    textWidget1.insert(END, "=======================================" + "\n")
    conn.close()


