import tkinter as tk
import sqlite3

def update_lecturer():
    update_window = tk.Toplevel()  # Child window
    update_window.title("Update Lecturer")
    update_window.configure(bg="#003366")
    update_window.geometry("700x600")

    frame = tk.Frame(update_window, bg="#003366", width=600, height=400)
    frame.grid(row=0, column=0)

    # Label to inform user
    info_label = tk.Label(frame, text="Click a data entry to update:", bg="#003366", font=("Arial", 15), fg="white")
    info_label.grid(row=4, column=2, padx=15, pady=5)

    listLecturers = tk.Listbox(frame, width=40, height=20, font=("Arial", 13))
    listLecturers.grid(row=1, column=2, rowspan=19)

    def load_lecturers():
        listLecturers.delete(0, tk.END)  # Clear the Listbox before reloading
        conn = sqlite3.connect("SMS.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tblLecturers")
        rows = cursor.fetchall()
        if len(rows) == 0:
            listLecturers.insert(0,"No lecturers in database.")
        for row in rows:
            listLecturers.insert(tk.END, row)
        conn.close()

    load_lecturers()

    def on_select(event):
        selected_index = listLecturers.curselection()
        if selected_index:
            selected_lecturer = listLecturers.get(selected_index)

            # Clear all current and new entries before populating the current fields
            current_empid_entry.delete(0, tk.END)
            new_empid_entry.delete(0, tk.END)

            current_first_name_entry.delete(0, tk.END)
            new_first_name_entry.delete(0, tk.END)

            current_last_name_entry.delete(0, tk.END)
            new_last_name_entry.delete(0, tk.END)

            current_course_entry.delete(0, tk.END)
            new_course_entry.delete(0, tk.END)

            # Populate the current fields with selected lecturer data
            current_empid_entry.insert(0, selected_lecturer[0])
            current_first_name_entry.insert(0, selected_lecturer[1])
            current_last_name_entry.insert(0, selected_lecturer[2])
            current_course_entry.insert(0, selected_lecturer[3])

    listLecturers.bind("<<ListboxSelect>>", on_select)

    def confirm_update():
        current_id = current_empid_entry.get()
        new_id = new_empid_entry.get()

        current_fname = current_first_name_entry.get()
        new_fname = new_first_name_entry.get()

        current_lname = current_last_name_entry.get()
        new_lname = new_last_name_entry.get()

        current_course = current_course_entry.get()
        new_course = new_course_entry.get()

        if current_id:
            try:
                conn = sqlite3.connect("SMS.db")
                cursor = conn.cursor()

                # Update the lecturer's information in tblLecturers
                cursor.execute("""
                    UPDATE tblLecturers 
                    SET empid = ?, fname = ?, lname = ?, course = ? 
                    WHERE empid = ?
                """, (new_id or current_id, new_fname or current_fname, new_lname or current_lname,
                      new_course or current_course, current_id))
                conn.commit()

                if cursor.rowcount > 0:
                    result_label.config(text="Lecturer updated successfully.", fg="White")
                else:
                    result_label.config(text="Lecturer not found.", fg="White")

            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
                result_label.config(text="An error occurred while updating the Lecturer.", fg="red")
            finally:
                conn.close()

                load_lecturers()

        else:
            result_label.config(text="Please fill in the current Employee ID.", fg="red")

    # Label and entry for Current Employee ID
    current_empid_label = tk.Label(frame, text="Enter Current Employee ID:", bg="#003366", font=("Arial", 12), fg="white")
    current_empid_label.grid(row=2, column=1, padx=5, pady=5)

    current_empid_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    current_empid_entry.grid(row=3, column=1, padx=15)

    # Label and entry for New Employee ID
    new_empid_label = tk.Label(frame, text="Enter New Employee ID:", bg="#003366", font=("Arial", 12), fg="white")
    new_empid_label.grid(row=4, column=1, padx=5, pady=5)

    new_empid_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    new_empid_entry.grid(row=5, column=1, padx=5, pady=5)

    # Label and entry for First Name
    current_first_name_label = tk.Label(frame, text="Enter First Name:", bg="#003366", font=("Arial", 12), fg="white")
    current_first_name_label.grid(row=6, column=1, padx=5, pady=5)

    current_first_name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    current_first_name_entry.grid(row=7, column=1, padx=5, pady=5)

    new_first_name_label = tk.Label(frame, text="Enter New First Name:", bg="#003366", font=("Arial", 12), fg="white")
    new_first_name_label.grid(row=8, column=1, padx=5, pady=5)

    new_first_name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    new_first_name_entry.grid(row=9, column=1, padx=5, pady=5)

    # Label and entry for Last Name
    current_last_name_label = tk.Label(frame, text="Enter Last Name:", bg="#003366", font=("Arial", 12), fg="white")
    current_last_name_label.grid(row=10, column=1, padx=5, pady=5)

    current_last_name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    current_last_name_entry.grid(row=11, column=1, padx=5, pady=5)

    new_last_name_label = tk.Label(frame, text="Enter New Last Name:", bg="#003366", font=("Arial", 12), fg="white")
    new_last_name_label.grid(row=12, column=1, padx=5, pady=5)

    new_last_name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    new_last_name_entry.grid(row=13, column=1, padx=5, pady=5)

    # Label and entry for Course
    current_course_label = tk.Label(frame, text="Enter Course:", bg="#003366", font=("Arial", 12), fg="white")
    current_course_label.grid(row=14, column=1, padx=5, pady=5)

    current_course_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    current_course_entry.grid(row=15, column=1, padx=5, pady=5)

    new_course_label = tk.Label(frame, text="Enter New Course:", bg="#003366", font=("Arial", 12), fg="white")
    new_course_label.grid(row=16, column=1, padx=5, pady=5)

    new_course_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    new_course_entry.grid(row=17, column=1, padx=5, pady=5)

    # Update button
    update_button = tk.Button(frame, text="UPDATE Lecturer", command=confirm_update,  bg="#004080", fg="white", font=("Arial", 14), relief="flat", bd=0,activebackground="#0056b3", activeforeground="white")
    update_button.grid(row=18, column=1, padx=5, pady=5)

    # Result label to show success or failure
    result_label = tk.Label(frame, text="", bg="#003366", font=("Arial", 12))
    result_label.grid(row=19, column=1)
