import tkinter as tk
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    course TEXT
)
""")

def save_data():
    name = entry_name.get()
    course = entry_course.get()

    cursor.execute("INSERT INTO students (name, course) VALUES (?, ?)", (name, course))
    conn.commit()

    entry_name.delete(0, tk.END)
    entry_course.delete(0, tk.END)

root = tk.Tk()
root.title("Student Registration")

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Course").pack()
entry_course = tk.Entry(root)
entry_course.pack()

tk.Button(root, text="Register", command=save_data).pack()

root.mainloop()