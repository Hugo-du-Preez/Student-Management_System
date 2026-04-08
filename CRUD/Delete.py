import tkinter as tk
import sqlite3

def deleteLecturer():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Lecturer")
    delete_window.configure(bg="#002855")

    lecturer_listbox = tk.Listbox(delete_window, width=70, height=10, font=("Arial", 12), bg="#1A1A1A", fg="white")
    lecturer_listbox.pack(padx=20, pady=20)

    # Information label to instruct the user
    instruction_label = tk.Label(
        delete_window,
        text="Click on a lecturer entry to delete it.",
        bg="#002855",
        fg="#FFFFFF",
        font=("Arial", 13, "italic")
    )
    instruction_label.pack(pady=(5, 20))

    # Load lecturers into the listbox
    def load_lecturers():
        try:
            connection = sqlite3.connect("SMS.db")
            cursor = connection.cursor()
            cursor.execute("SELECT empid, fname, lname, course FROM tblLecturers")
            lecturers = cursor.fetchall()

            lecturer_listbox.delete(0, tk.END)  # Clear existing entries
            for lecturer in lecturers:
                lecturer_listbox.insert(
                    tk.END, f"{lecturer[0]} - {lecturer[1]} {lecturer[2]} - Course: {lecturer[3]}"
                )
        except sqlite3.Error as e:
            print(f"An error occurred while loading lecturers: {e}")
        finally:
            connection.close()

    load_lecturers()  # Call function to load lecturers

    def on_select_lecturer(event):
        try:
            selected_item = lecturer_listbox.get(lecturer_listbox.curselection())
            empid = selected_item.split(' ')[0]  # Extract empid (first part of the string)
            empid_entry.delete(0, tk.END)
            empid_entry.insert(0, empid)
        except IndexError:
            pass  # Handle the case where no item is selected

    lecturer_listbox.bind("<<ListboxSelect>>", on_select_lecturer)

    def confirm_delete():
        empid = empid_entry.get()
        if empid:
            try:
                connection = sqlite3.connect("SMS.db")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM tblLecturers WHERE empid = ?", (empid,))
                connection.commit()

                if cursor.rowcount > 0:
                    result_label.config(text="Lecturer deleted successfully.", fg="green")
                    load_lecturers()  # Refresh the lecturer list after deletion
                else:
                    result_label.config(text="Lecturer not found.", fg="red")

            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
                result_label.config(text="An error occurred while deleting the lecturer.", fg="red")
            finally:
                connection.close()
        else:
            result_label.config(text="Please select a lecturer to delete.", fg="red")  # Validation message

    empid_label = tk.Label(delete_window, text="Enter Employee ID:", bg="#002855", fg="white", font=("Arial", 12))
    empid_label.pack(pady=5)

    empid_entry = tk.Entry(delete_window, font=("Arial", 12), width=30)
    empid_entry.pack(pady=5)

    delete_button = tk.Button(
        delete_window,
        text="Delete Lecturer",
        command=confirm_delete,
        bg="#004080",
        fg="white",
        font=("Arial", 14),
        relief="flat",
        bd=0,
        activebackground="#0056b3",
        activeforeground="white"
    )
    delete_button.pack(pady=10)

    result_label = tk.Label(delete_window, text="", bg="#002855", fg="white", font=("Arial", 12))
    result_label.pack(pady=5)

def deleteStudent():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Student")
    delete_window.configure(bg="#002855")

    student_listbox = tk.Listbox(delete_window, width=70, height=10, font=("Arial", 12), bg="#1A1A1A", fg="white")
    student_listbox.pack(padx=20, pady=20)

    # Information label to instruct the user
    instruction_label = tk.Label(
        delete_window,
        text="Click on a student entry to delete it.",
        bg="#002855",
        fg="#FFFFFF",
        font=("Arial", 13, "italic")
    )
    instruction_label.pack(pady=(5, 20))

    # Load students into the listbox
    def load_students():
        try:
            connection = sqlite3.connect("SMS.db")
            cursor = connection.cursor()
            cursor.execute("SELECT snumber, fname, lname FROM tblStudents")
            students = cursor.fetchall()

            student_listbox.delete(0, tk.END)  # Clear existing entries
            for student in students:
                student_listbox.insert(tk.END, f"{student[0]} - {student[1]} {student[2]}")
        except sqlite3.Error as e:
            print(f"An error occurred while loading students: {e}")
        finally:
            connection.close()

    load_students()  # Call function to load students

    def on_select_student(event):
        try:
            selected_item = student_listbox.get(student_listbox.curselection())
            snumber = selected_item.split(' ')[0]  # Extract snumber (first part of the string)
            snumber_entry.delete(0, tk.END)
            snumber_entry.insert(0, snumber)
        except IndexError:
            pass  # Handle the case where no item is selected

    student_listbox.bind("<<ListboxSelect>>", on_select_student)

    def confirm_delete():
        snumber = snumber_entry.get()
        if snumber:
            try:
                connection = sqlite3.connect("SMS.db")
                cursor = connection.cursor()
                cursor.execute("DELETE FROM tblStudents WHERE snumber = ?", (snumber,))
                connection.commit()

                if cursor.rowcount > 0:
                    result_label.config(text="Student deleted successfully.", fg="green")
                    load_students()  # Refresh the student list after deletion
                else:
                    result_label.config(text="Student not found.", fg="red")

            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
                result_label.config(text="An error occurred while deleting the student.", fg="red")
            finally:
                connection.close()
        else:
            result_label.config(text="Please select a student to delete.", fg="red")  # Validation message

    snumber_label = tk.Label(delete_window, text="Enter Student Number:", bg="#002855", fg="white", font=("Arial", 12))
    snumber_label.pack(pady=5)

    snumber_entry = tk.Entry(delete_window, font=("Arial", 12), width=30)
    snumber_entry.pack(pady=5)

    delete_button = tk.Button(
        delete_window,
        text="Delete Student",
        command=confirm_delete,
        bg="#004080",
        fg="white",
        font=("Arial", 14),
        relief="flat",
        bd=0,
        activebackground="#0056b3",
        activeforeground="white"
    )
    delete_button.pack(pady=10)

    result_label = tk.Label(delete_window, text="", bg="#002855", fg="white", font=("Arial", 12))
    result_label.pack(pady=5)
