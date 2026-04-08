import tkinter as tk
import sqlite3

def update_student():
    update_window = tk.Toplevel()  # Child window
    update_window.title("Update Student")
    update_window.configure(bg="#003366")
    update_window.geometry("700x550")

    frame = tk.Frame(update_window, bg="#003366", width=600, height=400)
    frame.grid(row=0, column=0)

    # Label to inform user
    info_label = tk.Label(frame, text="Click a data entry to update:", bg="#003366", font=("Arial", 15), fg="white")
    info_label.grid(row=2, column=2, padx=15, pady=5)

    listStudents = tk.Listbox(frame, width=40, height=20, font=("Arial", 13))
    listStudents.grid(row=1, column=2, rowspan=19,padx=5)

    def load_students():
        listStudents.delete(0, tk.END)  # Clear the Listbox before reloading
        conn = sqlite3.connect("SMS.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tblStudents")
        rows = cursor.fetchall()
        if len(rows) == 0:
            listStudents.insert(0,"No students in database.")
        currRow = 0
        for row in rows:
            listStudents.insert(currRow, row)
            currRow += 1
        conn.close()

    load_students()

    def on_select(event):
        selected_index = listStudents.curselection()
        if selected_index:
            selected_student = listStudents.get(selected_index)

            # Clear all current and new entries before populating the current fields
            current_id_entry.delete(0, tk.END)
            new_id_entry.delete(0, tk.END)

            current_first_name_entry.delete(0, tk.END)
            new_first_name_entry.delete(0, tk.END)

            current_last_name_entry.delete(0, tk.END)
            new_last_name_entry.delete(0, tk.END)

            current_student_number_entry.delete(0, tk.END)
            new_student_number_entry.delete(0, tk.END)

            # Populate the current fields with selected student data
            current_id_entry.insert(0, selected_student[0])
            current_first_name_entry.insert(0, selected_student[1])
            current_last_name_entry.insert(0, selected_student[2])
            current_student_number_entry.insert(0, selected_student[3])

    listStudents.bind("<<ListboxSelect>>", on_select)

    def confirm_update():
        current_id = current_id_entry.get()
        new_id = new_id_entry.get()

        current_fname = current_first_name_entry.get()
        new_fname = new_first_name_entry.get()

        current_lname = current_last_name_entry.get()
        new_lname = new_last_name_entry.get()

        current_snumber = current_student_number_entry.get()
        new_snumber = new_student_number_entry.get()

        if current_id:
            try:
                conn = sqlite3.connect("SMS.db")
                cursor = conn.cursor()

                # Update the student's information
                cursor.execute("""
                    UPDATE tblStudents 
                    SET id = ?, fname = ?, lname = ?, snumber = ? 
                    WHERE id = ?
                """, (new_id or current_id, new_fname or current_fname, new_lname or current_lname,
                      new_snumber or current_snumber, current_id))
                conn.commit()

                if cursor.rowcount > 0:
                    result_label.config(text="Student updated successfully.", fg="White")
                else:
                    result_label.config(text="Student not found.", fg="red")

            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
                result_label.config(text="An error occurred while updating the student.", fg="red")
            finally:
                conn.close()

                load_students()

        else:
            result_label.config(text="Please fill in the current ID.", fg="red")

    # Label and entry for current ID
    current_id_label = tk.Label(frame, text="Enter Current ID:", font=("Arial", 12),fg= "White",bg="#003366")
    current_id_label.grid(row=2, column=1, padx= 5,pady= 5)

    current_id_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    current_id_entry.grid(row=3, column=1,padx=15)

    # Label and entry for new ID
    new_id_label = tk.Label(frame, text="Enter New ID:", font=("Arial", 12),fg= "White",bg="#003366")
    new_id_label.grid(row=4, column=1, padx= 5,pady= 5)

    new_id_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    new_id_entry.grid(row=5, column=1,padx=15)

    # Label and entry for first name
    current_first_name_label = tk.Label(frame, text="Enter First Name:", font=("Arial", 12),fg= "White",bg="#003366")
    current_first_name_label.grid(row=6, column=1, padx= 5,pady= 5)

    current_first_name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    current_first_name_entry.grid(row=7, column=1,padx=15)

    new_first_name_label = tk.Label(frame, text="Enter New First Name:", font=("Arial", 12),fg= "White",bg="#003366")
    new_first_name_label.grid(row=8, column=1, padx= 5,pady= 5)

    new_first_name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    new_first_name_entry.grid(row=9, column=1,padx=15)

    # Label and entry for last name
    current_last_name_label = tk.Label(frame, text="Enter Last Name:", font=("Arial", 12),fg= "White",bg="#003366")
    current_last_name_label.grid(row=10, column=1, padx= 5,pady= 5)

    current_last_name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    current_last_name_entry.grid(row=11, column=1,padx=15)

    new_last_name_label = tk.Label(frame, text="Enter New Last Name:", font=("Arial", 12),fg= "White",bg="#003366")
    new_last_name_label.grid(row=12, column=1, padx= 5,pady= 5)

    new_last_name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    new_last_name_entry.grid(row=13, column=1,padx=15)

    # Label and entry for student number
    current_student_number_label = tk.Label(frame, text="Enter Student Number:", font=("Arial", 12),fg= "White",bg="#003366")
    current_student_number_label.grid(row=14, column=1, padx= 5,pady= 5)

    current_student_number_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    current_student_number_entry.grid(row=15, column=1,padx=15)

    new_student_number_label = tk.Label(frame, text="Enter New Student Number:", font=("Arial", 12),fg= "White",bg="#003366")
    new_student_number_label.grid(row=16, column=1, padx= 5,pady= 5)

    new_student_number_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    new_student_number_entry.grid(row=17, column=1,padx=15,pady=5)



    # Update button
    update_button = tk.Button(frame, text="UPDATE Student", command=confirm_update,bg="#004080", fg="white", font=("Arial", 14),
                              relief="flat", bd=0, activebackground="#0056b3", activeforeground="white")
    update_button.grid(row=19, column=1, padx= 15,pady= 10)

    # Label to display the result of the update operation
    result_label = tk.Label(frame, text="",bg="#003366", font=("Arial", 12))
    result_label.grid(row=20, column=1, padx= 0,pady= 0)
