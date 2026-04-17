import tkinter as tk

root = tk.Tk()
root.title("Simple Window")
root.geometry("400x300")   # Fixed size
root.resizable(False, False)

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=100)

root.mainloop()