import tkinter as tk
from tkinter import messagebox
import pyttsx3


def speak_text():
    text = entry.get()
    if text.strip() == "":
        messagebox.showwarning("Warning", "Please enter some text!")
        return

    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 180)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI window


root = tk.Tk()
root.title("Text To Speech")
root.geometry("400x200")
label = tk.Label(root, text="Enter Text:", font=("Arial", 14))
label.pack(pady=10)
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=5)
button = tk.Button(root, text="Speak", font=("Arial", 14), command=speak_text)
button.pack(pady=15)

root.mainloop()
