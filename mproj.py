import random
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# -------- STORY DATA --------
characters = [
    "Aanya, a fearless explorer",
    "Rohan, a young scientist",
    "An old wizard",
    "A brave astronaut",
    "A clever detective",
    "A mysterious traveler"
]

places = [
    "inside an ancient underground city",
    "on a distant planet",
    "inside a magical forest",
    "near a hidden waterfall",
    "inside an abandoned laboratory",
    "at the edge of a frozen mountain"
]

problems = [
    "discovered a glowing door that had been locked for centuries",
    "found a strange map leading to a hidden treasure",
    "heard mysterious voices coming from underground",
    "accidentally activated an ancient machine",
    "met a creature asking for help",
    "found a secret portal to another world"
]

endings = [
    "In the end, they uncovered secrets that changed their life forever.",
    "After a long adventure, peace was finally restored.",
    "The mystery was solved, but many questions still remained.",
    "Their bravery became a legendary story for future generations.",
    "What started as a small discovery became the greatest adventure ever.",
    "From that day onward, nothing was ever the same again."
]

# -------- FUNCTIONS --------
def generate_story():
    story = (
        f"{random.choice(characters)} was traveling {random.choice(places)}. "
        f"One quiet evening, they unexpectedly {random.choice(problems)}. "
        f"At first, fear and confusion surrounded them, but curiosity pushed them forward. "
        f"They solved puzzles, faced dangers, and uncovered hidden secrets. "
        f"In the end, everything became clear. "
        f"{random.choice(endings)}"
    )

    story_box.config(state="normal")
    story_box.delete("1.0", tk.END)
    story_box.insert(tk.END, story)
    story_box.config(state="disabled")


def save_story():
    story = story_box.get("1.0", tk.END).strip()

    if not story:
        messagebox.showwarning("Warning", "Generate a story first!")
        return

    with open("saved_stories.txt", "a", encoding="utf-8") as file:
        file.write("\n" + "="*50 + "\n")
        file.write(f"Saved On: {datetime.now()}\n\n")
        file.write(story + "\n")

    messagebox.showinfo("Saved", "Story saved successfully!")


def exit_app():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()


# -------- GUI --------
root = tk.Tk()
root.title("Story Generator")
root.geometry("800x550")

tk.Label(root, text="Story Generator", font=("Arial", 20, "bold")).pack(pady=10)

# Buttons
frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Generate", command=generate_story, bg="green", fg="white").grid(row=0, column=0, padx=10)
tk.Button(frame, text="Save", command=save_story, bg="blue", fg="white").grid(row=0, column=1, padx=10)
tk.Button(frame, text="Exit", command=exit_app, bg="red", fg="white").grid(row=0, column=2, padx=10)

# Text Box
story_box = tk.Text(root, height=18, width=80)
story_box.pack(pady=20)
story_box.config(state="disabled")

root.mainloop()