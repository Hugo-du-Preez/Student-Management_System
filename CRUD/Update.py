import tkinter as tk
import sqlite3

from Windows.DisplayAllStudents import DisplayAllStudentsWindow
from Windows.DisplayAllLecturers import DisplayAllLecturersWindow

def update_student():
    update_window = tk.Toplevel()  # Child window
    update_window.title("Update Student")
    update_window.configure(bg="#f0f0f0")
    update_window.geometry("800x650")

    frame = tk.Frame(update_window, bg="#f0f0f0")
    frame.grid(row=0, column=0)

def update_lecturer():
    update_window = tk.Toplevel()
    update_window.title("Update Lecturer")
    update_window.configure(bg="#f0f0f0")

    frame = tk.Frame(update_window, bg="#f0f0f0")
    frame.pack(padx=40, pady=40)

    def confirm_update():
        current_empid = current_empid_entry.get()
        new_empid = new_empid_entry.get()
        if current_empid and new_empid:
            try:
                conn = sqlite3.connect("SMS.db")
                cursor = conn.cursor()

                # Update lecturer's employee ID based on the current one
                cursor.execute("UPDATE tblLecturers SET empid = ? WHERE empid = ?", (new_empid, current_empid))
                conn.commit()

                if cursor.rowcount > 0:
                    result_label.config(text="Lecturer updated successfully.", fg="green")
                else:
                    result_label.config(text="Lecturer not found.", fg="red")

            except sqlite3.Error as e:
                print(f"An error occurred: {e}")
                result_label.config(text="An error occurred while updating the lecturer.", fg="red")
            finally:
                conn.close()

                current_course = current_course_entry.get()
                new_course = new_course_entry.get()
                try:
                    conn = sqlite3.connect("SMS.db")
                    cursor = conn.cursor()

                    # Update the student's ID
                    cursor.execute("UPDATE tblLecturers SET course = ? WHERE course = ?",(new_course, current_course))
                    conn.commit()

                    if cursor.rowcount > 0:
                        result_label.config(text="Lecturer updated successfully.", fg="blue")
                    else:
                        result_label.config(text="Lecturer not found.", fg="red")

                except sqlite3.Error as e:
                    print(f"An error occurred: {e}")
                    result_label.config(text="An error occurred while updating the student.", fg="red")
                finally:
                    conn.close()

                    current_fname = current_first_name_entry.get()
                    new_fname = new_first_name_entry.get()
                    try:
                        conn = sqlite3.connect("SMS.db")
                        cursor = conn.cursor()

                        # Update the student's ID
                        cursor.execute("UPDATE tblLecturers SET fname = ? WHERE fname = ?", (new_fname, current_fname))
                        conn.commit()

                        if cursor.rowcount > 0:
                            result_label.config(text="Lecturer updated successfully.", fg="blue")
                        else:
                            result_label.config(text="Lecturer not found.", fg="red")

                    except sqlite3.Error as e:
                        print(f"An error occurred: {e}")
                        result_label.config(text="An error occurred while updating the student.", fg="red")
                    finally:
                        conn.close()

                        current_lname = current_last_name_entry.get()
                        new_lname = new_last_name_entry.get()
                        try:
                            conn = sqlite3.connect("SMS.db")
                            cursor = conn.cursor()

                            # Update the student's ID
                            cursor.execute("UPDATE tblLecturers SET lname = ? WHERE lname = ?",
                                           (new_lname, current_lname))
                            conn.commit()

                            if cursor.rowcount > 0:
                                result_label.config(text="Lecturer updated successfully.", fg="blue")
                            else:
                                result_label.config(text="Lecturer not found.", fg="red")

                        except sqlite3.Error as e:
                            print(f"An error occurred: {e}")
                            result_label.config(text="An error occurred while updating the lecturer.", fg="red")
                        finally:
                            conn.close()
                            DisplayAllLecturersWindow()
        else:
            result_label.config(text="Please fill in both Employee ID fields.", fg="red")

    # Label and entry for last name
    current_last_name_label = tk.Label(frame, text="Enter Last Name:", bg="#f0f0f0", font=("Arial", 12))
    current_last_name_label.pack(pady=5)

    current_last_name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    current_last_name_entry.pack(pady=5)

    new_last_name_label = tk.Label(frame, text="Enter New Last Name :", bg="#f0f0f0", font=("Arial", 12))
    new_last_name_label.pack(pady=5)

    new_last_name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    new_last_name_entry.pack(pady=5)

    # Label and entry for first name
    current_first_name_label = tk.Label(frame, text="Enter First Name:", bg="#f0f0f0", font=("Arial", 12))
    current_first_name_label.pack(pady=5)

    current_first_name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    current_first_name_entry.pack(pady=5)

    new_first_name_label = tk.Label(frame, text="Enter New First Name :", bg="#f0f0f0", font=("Arial", 12))
    new_first_name_label.pack(pady=5)

    new_first_name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    new_first_name_entry.pack(pady=5)

    # Label and entry for Course
    current_course_label = tk.Label(frame, text="Enter Course:", bg="#f0f0f0", font=("Arial", 12))
    current_course_label.pack(pady=5)

    current_course_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    current_course_entry.pack(pady=5)

    new_course_label = tk.Label(frame, text="Enter New Course :", bg="#f0f0f0", font=("Arial", 12))
    new_course_label.pack(pady=5)

    new_course_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    new_course_entry.pack(pady=5)
    # Label and entry for Current Employee ID
    current_empid_label = tk.Label(frame, text="Enter Current Employee ID:", bg="#f0f0f0", font=("Arial", 12))
    current_empid_label.pack(pady=5)

    current_empid_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    current_empid_entry.pack(pady=5)

    # Label and entry for New Employee ID
    new_empid_label = tk.Label(frame, text="Enter New Employee ID:", bg="#f0f0f0", font=("Arial", 12))
    new_empid_label.pack(pady=5)

    new_empid_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    new_empid_entry.pack(pady=5)

    # Update button
    update_button = tk.Button(frame, text="UPDATE Lecturer", command=confirm_update, bg="#964caf", fg="white", font=("Arial", 12))
    update_button.pack(pady=10)

    # Result label to show success or failure
    result_label = tk.Label(frame, text="", bg="#f0f0f0", font=("Arial", 12))
    result_label.pack(pady=5)



