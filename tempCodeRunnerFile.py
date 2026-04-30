#4.Create a GUI based task manager where users can add, edit and remove tasks. Use Tkinter (buttons, listbox), SQLite/MySQL (task storage).
import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

root = tk.Tk()
root.title("Task Manager")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Delete Task", command=delete_task).pack()

listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

root.mainloop()