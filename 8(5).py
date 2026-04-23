#5.Design a login and signup authentication system.
import tkinter as tk
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT,
    password TEXT
)
""")

def signup():
    u = entry_user.get()
    p = entry_pass.get()

    cursor.execute("INSERT INTO users VALUES (?, ?)", (u, p))
    conn.commit()
    label_msg.config(text="Signup Successful")

def login():
    u = entry_user.get()
    p = entry_pass.get()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p))
    result = cursor.fetchone()

    if result:
        label_msg.config(text="Login Successful")
    else:
        label_msg.config(text="Invalid Credentials")

root = tk.Tk()
root.title("Login System")

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Signup", command=signup).pack()
tk.Button(root, text="Login", command=login).pack()

label_msg = tk.Label(root, text="")
label_msg.pack()

root.mainloop()