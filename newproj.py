import random
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class StoryGeneratorApp:

    def __init__(self):

        self.characters = [
            "Aanya, a fearless explorer",
            "Rohan, a young scientist",
            "An old wizard",
            "A brave astronaut",
            "A clever detective",
            "A mysterious traveler"
        ]

        self.places = [
            "inside an ancient underground city",
            "on a distant planet",
            "inside a magical forest",
            "near a hidden waterfall",
            "inside an abandoned laboratory",
            "at the edge of a frozen mountain"
        ]

        self.problems = [
            "discovered a glowing door that had been locked for centuries",
            "found a strange map leading to a hidden treasure",
            "heard mysterious voices coming from underground",
            "accidentally activated an ancient machine",
            "met a creature asking for help",
            "found a secret portal to another world"
        ]

        self.endings = [
            "In the end, they uncovered secrets that changed their life forever.",
            "After a long adventure, peace was finally restored.",
            "The mystery was solved, but many questions still remained.",
            "Their bravery became a legendary story for future generations.",
            "What started as a small discovery became the greatest adventure ever.",
            "From that day onward, nothing was ever the same again."
        ]

        # ================= WINDOW =================

        self.root = tk.Tk()
        self.root.title("Creative Random Story Generator")
        self.root.geometry("850x600")
        self.root.configure(bg="#ECEFF1")

        # ================= HEADING =================

        heading = tk.Label(
            self.root,
            text="Creative Random Story Generator",
            font=("Helvetica", 24, "bold"),
            bg="#ECEFF1",
            fg="#222222"
        )

        heading.pack(pady=20)

        # ================= BUTTON FRAME =================

        button_frame = tk.Frame(self.root, bg="#ECEFF1")
        button_frame.pack(pady=10)

        # ================= GENERATE BUTTON =================

        generate_btn = tk.Button(
            button_frame,
            text="Generate Story",
            font=("Arial", 13, "bold"),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=10,
            command=self.generate_story
        )

        generate_btn.grid(row=0, column=0, padx=10)

        # ================= SAVE BUTTON =================

        save_btn = tk.Button(
            button_frame,
            text="Save Story",
            font=("Arial", 13, "bold"),
            bg="#2196F3",
            fg="white",
            padx=20,
            pady=10,
            command=self.save_story
        )

        save_btn.grid(row=0, column=1, padx=10)

        # ================= EXIT BUTTON =================

        exit_btn = tk.Button(
            button_frame,
            text="Exit",
            font=("Arial", 13, "bold"),
            bg="#f44336",
            fg="white",
            padx=20,
            pady=10,
            command=self.exit_app
        )

        exit_btn.grid(row=0, column=2, padx=10)

        # ================= STORY BOX =================

        self.story_box = tk.Text(
            self.root,
            height=18,
            width=90,
            font=("Arial", 13),
            wrap="word",
            bg="white",
            fg="#222222",
            padx=15,
            pady=15,
            relief="flat"
        )

        self.story_box.pack(pady=20)
        self.story_box.config(state="disabled")

        # ================= FOOTER =================

        footer = tk.Label(
            self.root,
            text="Built with Python & Tkinter",
            font=("Arial", 10),
            bg="#ECEFF1",
            fg="gray"
        )

        footer.pack(side="bottom", pady=10)

    # ================= GENERATE STORY =================

    def generate_story(self):

        character = random.choice(self.characters)
        place = random.choice(self.places)
        problem = random.choice(self.problems)
        ending = random.choice(self.endings)

        story = (
            f"{character} was traveling {place}. "
            f"One quiet evening, they unexpectedly {problem}. "
            f"At first, fear and confusion surrounded them, but curiosity slowly pushed them forward toward the unknown. "
            f"As they continued the journey, strange symbols began appearing on the walls around them, each one hiding an important clue. "
            f"Soon, dangerous obstacles started blocking their path, including collapsing bridges, mysterious sounds, and hidden traps waiting in the darkness. "
            f"Despite the fear, they carefully solved every puzzle using intelligence, courage, and determination. "
            f"During the adventure, they also discovered an ancient secret about the place that nobody had known for hundreds of years. "
            f"After facing countless challenges and uncovering the hidden truth, they finally reached the center of the mystery where everything became clear. "
            f"The experience completely changed the way they looked at the world and taught them the true meaning of bravery and hope. "
            f"{ending}"
        )

        self.story_box.config(state="normal")
        self.story_box.delete("1.0", tk.END)
        self.story_box.insert(tk.END, story)
        self.story_box.config(state="disabled")

    # ================= SAVE STORY =================

    def save_story(self):

        story = self.story_box.get("1.0", tk.END).strip()

        if story == "":
            messagebox.showwarning("Warning", "Generate a story first!")
            return

        with open("saved_stories.txt", "a", encoding="utf-8") as file:
            file.write("\n" + "=" * 80 + "\n")
            file.write(f"Saved On: {datetime.now()}\n\n")
            file.write(story + "\n")

        messagebox.showinfo("Saved", "Story saved successfully!")

    # ================= EXIT APP =================

    def exit_app(self):

        confirm = messagebox.askyesno("Exit", "Do you want to exit?")

        if confirm:
            self.root.destroy()


# ================= RUN APPLICATION =================

app = StoryGeneratorApp()
app.root.mainloop()